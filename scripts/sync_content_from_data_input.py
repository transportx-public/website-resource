#!/usr/bin/env python3
"""Sync Hugo content from the editable files under data-input."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = {
    "people": REPO_ROOT / "scripts" / "generate_authors_from_people.py",
    "posts": REPO_ROOT / "scripts" / "generate_posts_from_xlsx.py",
    "events": REPO_ROOT / "scripts" / "generate_events_from_xlsx.py",
    "publications": REPO_ROOT / "scripts" / "generate_publications_from_xlsx.py",
}
LANGUAGE_VARIANTS = REPO_ROOT / "scripts" / "generate_language_variants.py"


def run_module(name: str) -> None:
    script = SCRIPTS[name]
    subprocess.run([sys.executable, str(script)], cwd=REPO_ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "modules",
        nargs="*",
        help=f"Content modules to sync: {', '.join(sorted(SCRIPTS))}. Leave empty to sync all modules.",
    )
    args = parser.parse_args()

    unknown = sorted(set(args.modules).difference(SCRIPTS))
    if unknown:
        parser.error(f"unknown module(s): {', '.join(unknown)}")

    modules = args.modules or ["people", "posts", "events", "publications"]
    for module in modules:
        print(f"==> Syncing {module}", flush=True)
        run_module(module)
    subprocess.run([sys.executable, str(LANGUAGE_VARIANTS)], cwd=REPO_ROOT, check=True)


if __name__ == "__main__":
    main()
