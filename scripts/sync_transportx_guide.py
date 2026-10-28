#!/usr/bin/env python3
"""Copy the canonical TransportX guide into the website, including asset deletions."""

import argparse
import hashlib
import re
import shutil
import tempfile
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("source", type=Path, help="Path to transportx-agent/docs/guide")
args = parser.parse_args()
source = args.source.resolve()
destination = Path(__file__).resolve().parents[1] / "static/application/transportx-agent/guide"

for filename in ("index.html", "styles.css", "guide.js"):
    if not (source / filename).is_file():
        parser.error(f"Missing guide file: {source / filename}")
if not (source / "assets").is_dir():
    parser.error(f"Missing guide assets: {source / 'assets'}")
if source == destination.resolve():
    parser.error("Source must be the canonical guide, not the website copy")

destination.parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(dir=destination.parent) as temporary:
    staged = Path(temporary) / "guide"
    shutil.copytree(source, staged)
    index_path = staged / "index.html"
    index = index_path.read_text(encoding="utf-8")
    for filename in ("styles.css", "guide.js"):
        asset = staged / filename
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:16]
        versioned = f"{asset.stem}.{digest}{asset.suffix}"
        shutil.copy2(asset, staged / versioned)
        index = re.sub(rf'(["\']){re.escape(filename)}(?:\?[^"\']*)?(["\'])',
                       lambda match: f"{match[1]}{versioned}{match[2]}", index)
    index_path.write_text(index, encoding="utf-8")
    # Cached HTML may still reference an earlier deployment's assets.
    if destination.exists():
        for pattern in ("styles.*.css", "guide.*.js"):
            for asset in destination.glob(pattern):
                if not (staged / asset.name).exists():
                    shutil.copy2(asset, staged / asset.name)
    if destination.exists():
        shutil.rmtree(destination)
    staged.rename(destination)

print(f"Synced {source} → {destination}")
