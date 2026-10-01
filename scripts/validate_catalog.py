#!/usr/bin/env python3
"""Validate OSINTAI machine-readable catalogs without external dependencies."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "catalog" / "tools.json"
RESEARCH = ROOT / "catalog" / "research.json"

ALLOWED_STATUS = {"verified", "candidate", "archival", "rejected"}
REQUIRED_TOOL_FIELDS = {
    "id",
    "name",
    "url",
    "category",
    "architecture",
    "protocols",
    "deployment",
    "local_first",
    "status",
    "verification",
    "last_reviewed",
}


def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def valid_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def validate_tools(data: dict) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()

    for index, tool in enumerate(data.get("tools", [])):
        prefix = f"tools[{index}]"
        missing = REQUIRED_TOOL_FIELDS - set(tool)
        if missing:
            errors.append(f"{prefix}: missing {sorted(missing)}")
            continue

        if tool["id"] in seen:
            errors.append(f"{prefix}: duplicate id {tool['id']}")
        seen.add(tool["id"])

        if tool["status"] not in ALLOWED_STATUS:
            errors.append(f"{prefix}: invalid status {tool['status']}")

        if not valid_url(tool["url"]):
            errors.append(f"{prefix}: invalid URL {tool['url']}")

        if not valid_date(tool["last_reviewed"]):
            errors.append(f"{prefix}: invalid last_reviewed date")

        for field in ("category", "architecture", "protocols", "deployment"):
            if not isinstance(tool[field], list):
                errors.append(f"{prefix}: {field} must be a list")

        if not isinstance(tool["local_first"], bool):
            errors.append(f"{prefix}: local_first must be boolean")

    return errors


def validate_research(data: dict) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()

    for index, ref in enumerate(data.get("references", [])):
        prefix = f"references[{index}]"
        for field in ("id", "title", "year", "type", "url", "topics"):
            if field not in ref:
                errors.append(f"{prefix}: missing {field}")

        if ref.get("id") in seen:
            errors.append(f"{prefix}: duplicate id {ref.get('id')}")
        seen.add(ref.get("id"))

        if "url" in ref and not valid_url(ref["url"]):
            errors.append(f"{prefix}: invalid URL {ref['url']}")

        if "topics" in ref and not isinstance(ref["topics"], list):
            errors.append(f"{prefix}: topics must be a list")

    return errors


def main() -> int:
    errors = []
    errors.extend(validate_tools(load(TOOLS)))
    errors.extend(validate_research(load(RESEARCH)))

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print("OSINTAI catalogs are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
