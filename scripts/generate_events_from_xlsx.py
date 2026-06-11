#!/usr/bin/env python3
"""Generate Hugo event pages from data-input/events/events.xlsx."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import date, datetime, time
from pathlib import Path

from openpyxl import load_workbook


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = REPO_ROOT / "data-input" / "events" / "events.xlsx"
DEFAULT_PICTURES = REPO_ROOT / "data-input" / "events" / "pictures"
DEFAULT_OUTPUT = REPO_ROOT / "content" / "event"


def text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def yaml_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "''"
    return json.dumps(str(value), ensure_ascii=False)


def split_list(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[,，;；]", value) if part.strip()]


def parse_bool(value: object, default: bool = False) -> bool:
    raw = text(value).lower()
    if not raw:
        return default
    return raw in {"1", "true", "yes", "y", "是", "发布"}


def parse_datetime(value: object) -> datetime | None:
    if value in (None, ""):
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime.combine(value, time.min)
    raw = text(value)
    for fmt in ("%Y-%m-%d %H:%M", "%Y/%m/%d %H:%M", "%Y-%m-%d", "%Y/%m/%d"):
        try:
            parsed = datetime.strptime(raw, fmt)
            if "%H" not in fmt:
                parsed = datetime.combine(parsed.date(), time.min)
            return parsed
        except ValueError:
            pass
    try:
        return datetime.fromisoformat(raw)
    except ValueError as exc:
        raise ValueError(f"Invalid datetime value: {raw}") from exc


def format_datetime(value: datetime | None) -> str:
    if value is None:
        return ""
    return value.strftime("%Y-%m-%dT%H:%M:%S+08:00")


def slugify(value: str, fallback: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", value).strip("-").lower()
    return slug or fallback


def read_rows(path: Path) -> list[dict[str, object]]:
    workbook = load_workbook(path, data_only=True)
    sheet = workbook[workbook.sheetnames[0]]
    rows = list(sheet.iter_rows(values_only=True))
    if not rows:
        return []
    headers = [text(cell) for cell in rows[0]]
    if "title" not in headers or "date" not in headers:
        raise ValueError("events.xlsx must include at least title and date columns")
    return [dict(zip(headers, row)) for row in rows[1:]]


def copy_picture(row: dict[str, object], event_dir: Path, pictures_dir: Path) -> None:
    picture = text(row.get("picture"))
    if not picture:
        return
    source = pictures_dir / picture
    if not source.is_file():
        print(f"WARNING: missing event picture: {source}")
        return
    shutil.copyfile(source, event_dir / f"featured{source.suffix.lower()}")


def render_event(row: dict[str, object]) -> tuple[str, str] | None:
    if "publish" in row and not parse_bool(row.get("publish")):
        return None

    title = text(row.get("title"))
    if not title:
        return None
    start = parse_datetime(row.get("date"))
    if start is None:
        raise ValueError(f"Missing date for event: {title}")
    end = parse_datetime(row.get("date_end"))
    day = start.strftime("%Y-%m-%d")
    folder = slugify(text(row.get("slug")) or f"{day}-{title}", f"event-{start.strftime('%Y%m%d')}")

    lines = [
        "---",
        f"title: {yaml_scalar(title)}",
        f"event: {yaml_scalar(text(row.get('event')))}",
        f"location: {yaml_scalar(text(row.get('location')))}",
        f"summary: {yaml_scalar(text(row.get('summary')))}",
        f"abstract: {yaml_scalar(text(row.get('abstract')))}",
        f"date: {yaml_scalar(format_datetime(start))}",
    ]
    if end:
        lines.append(f"date_end: {yaml_scalar(format_datetime(end))}")
    lines.extend(
        [
            f"all_day: {yaml_scalar(parse_bool(row.get('all_day')))}",
            f"publishDate: {yaml_scalar(day + 'T00:00:00+08:00')}",
        ]
    )
    authors = split_list(text(row.get("authors")))
    if authors:
        lines.append("authors:")
        lines.extend(f"  - {yaml_scalar(author)}" for author in authors)
    else:
        lines.append("authors: []")
    tags = split_list(text(row.get("tags")))
    if tags:
        lines.append("tags:")
        lines.extend(f"  - {yaml_scalar(tag)}" for tag in tags)
    else:
        lines.append("tags: []")
    lines.extend(
        [
            f"featured: {yaml_scalar(parse_bool(row.get('featured')))}",
            "image:",
            f"  caption: {yaml_scalar(text(row.get('caption')))}",
            "  focal_point: Center",
            "url_code: ''",
            "url_pdf: ''",
            "url_slides: ''",
            "url_video: ''",
            "slides: ''",
            "projects: []",
            "---",
            "",
        ]
    )
    body = text(row.get("body"))
    if body:
        lines.extend([body, ""])
    return folder, "\n".join(lines)


def generate(input_path: Path, output_dir: Path, pictures_dir: Path) -> int:
    rows = read_rows(input_path)
    count = 0
    for row in rows:
        rendered = render_event(row)
        if rendered is None:
            continue
        folder, content = rendered
        event_dir = output_dir / folder
        event_dir.mkdir(parents=True, exist_ok=True)
        (event_dir / "index.md").write_text(content, encoding="utf-8")
        copy_picture(row, event_dir, pictures_dir)
        count += 1
    print(f"Generated {count} event pages in {output_dir}")
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--pictures", type=Path, default=DEFAULT_PICTURES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    generate(args.input, args.output, args.pictures)


if __name__ == "__main__":
    main()
