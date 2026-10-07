#!/usr/bin/env python3
"""Copy the canonical TransportX guide into the website, including asset deletions."""

import argparse
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
    if destination.exists():
        shutil.rmtree(destination)
    staged.rename(destination)

print(f"Synced {source} → {destination}")
