#!/usr/bin/env python3
"""Generate Chinese page variants and normalize language-specific key fields."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT = REPO_ROOT / "content"

ROLE_ZH = {
    "Professor": "教授",
    "Ph.D. Student": "博士研究生",
    "Ph.D. Graduate": "博士毕业生",
    "Master's Student": "硕士研究生",
    "Master's Graduate": "硕士毕业生",
}
DEGREE_ZH = {"Professor": "教授", "Ph.D": "博士", "Master": "硕士"}
STATUS_ZH = {"Student": "在读", "Graduate": "已毕业"}


def split_page(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---"):
        raise ValueError("Expected YAML front matter")
    _, front_matter, body = text.split("---", 2)
    return yaml.safe_load(front_matter) or {}, body.lstrip("\n")


def render_page(data: dict[str, object], body: str) -> str:
    front_matter = yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).rstrip()
    suffix = f"\n\n{body.rstrip()}\n" if body.strip() else "\n"
    return f"---\n{front_matter}\n---{suffix}"


def generate_events() -> int:
    count = 0
    for event_dir in sorted((CONTENT / "event").glob("group-meeting-*")):
        english_path = event_dir / "index.md"
        chinese_path = event_dir / "index.zh.md"
        source_path = chinese_path if chinese_path.exists() else english_path
        source = source_path.read_text(encoding="utf-8")
        chinese_path.write_text(source, encoding="utf-8")

        data, _ = split_page(source)
        day = str(data.get("date", ""))[:10]
        reading_count = len(data.get("readings") or [])
        english = re.sub(
            r"(?m)^title: .+$",
            f'title: "Group Meeting | {day}"',
            source,
            count=1,
        )
        english = re.sub(
            r"(?m)^event: .+$",
            'event: "Group meeting"',
            english,
            count=1,
        )
        english = re.sub(
            r"(?m)^summary: .+$",
            f'summary: "{reading_count} papers were presented at this group meeting."',
            english,
            count=1,
        )
        english = english.replace('  - "组会"', '  - "Group meeting"', 1)
        english = english.replace('  - "文献分享"', '  - "Literature review"', 1)
        english_path.write_text(english, encoding="utf-8")
        count += 1
    return count


def generate_authors() -> int:
    count = 0
    for english_path in sorted((CONTENT / "authors").glob("*/_index.md")):
        data, body = split_page(english_path.read_text(encoding="utf-8"))
        chinese = dict(data)
        chinese["slug"] = english_path.parent.name.lower().replace(" ", "-")
        chinese_name = str(data.get("name_chinese") or "").strip()
        if chinese_name:
            chinese["title"] = chinese_name
        if data.get("role") in ROLE_ZH:
            chinese["role"] = ROLE_ZH[str(data["role"])]
        if data.get("academic_degree") in DEGREE_ZH:
            chinese["academic_degree"] = DEGREE_ZH[str(data["academic_degree"])]
        if data.get("academic_status") in STATUS_ZH:
            chinese["academic_status"] = STATUS_ZH[str(data["academic_status"])]
        if chinese.get("user_groups") == ["Faculty"]:
            chinese["user_groups"] = ["教师"]
        english_path.with_name("_index.zh.md").write_text(
            render_page(chinese, body),
            encoding="utf-8",
        )
        count += 1
    return count


def generate_publications() -> int:
    count = 0
    for english_path in sorted((CONTENT / "publication").glob("*/index.md")):
        chinese_path = english_path.with_name("index.zh.md")
        chinese_path.write_text(english_path.read_text(encoding="utf-8"), encoding="utf-8")
        count += 1
    return count


def main() -> None:
    events = generate_events()
    authors = generate_authors()
    publications = generate_publications()
    print(
        "Generated bilingual variants for "
        f"{events} events, {authors} authors, and {publications} publications"
    )


if __name__ == "__main__":
    main()
