#!/usr/bin/env python3
"""Validate OSINTAI machine-readable catalogs without external dependencies."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog"

ALLOWED_STATUS = {"verified", "verified-preprint", "candidate", "archival", "rejected"}
REQUIRED_TOOL_FIELDS = {
    "id", "name", "url", "category", "architecture", "protocols",
    "deployment", "local_first", "status", "verification", "last_reviewed",
}


def load(name: str) -> dict:
    path = CATALOG / name
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


def validate_unique(records: list[dict], key: str, prefix: str) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for index, record in enumerate(records):
        value = record.get(key)
        if not value:
            errors.append(f"{prefix}[{index}]: missing {key}")
        elif value in seen:
            errors.append(f"{prefix}[{index}]: duplicate {key} {value}")
        seen.add(value)
    return errors


def validate_tools(data: dict) -> list[str]:
    errors: list[str] = []
    records = data.get("tools", [])
    errors.extend(validate_unique(records, "id", "tools"))

    for index, tool in enumerate(records):
        prefix = f"tools[{index}]"
        missing = REQUIRED_TOOL_FIELDS - set(tool)
        if missing:
            errors.append(f"{prefix}: missing {sorted(missing)}")
            continue

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
    records = data.get("references", [])
    errors.extend(validate_unique(records, "id", "references"))

    for index, ref in enumerate(records):
        prefix = f"references[{index}]"
        for field in ("id", "title", "year", "type", "url", "topics"):
            if field not in ref:
                errors.append(f"{prefix}: missing {field}")
        if "url" in ref and not valid_url(ref["url"]):
            errors.append(f"{prefix}: invalid URL {ref['url']}")
        if "topics" in ref and not isinstance(ref["topics"], list):
            errors.append(f"{prefix}: topics must be a list")
        status = ref.get("verification_status")
        if status and status not in ALLOWED_STATUS:
            errors.append(f"{prefix}: invalid verification_status {status}")

    return errors


def validate_collections(data: dict) -> list[str]:
    errors: list[str] = []
    records = data.get("collections", [])
    errors.extend(validate_unique(records, "id", "collections"))

    for index, item in enumerate(records):
        prefix = f"collections[{index}]"
        for field in ("id", "name", "url", "status", "focus"):
            if field not in item:
                errors.append(f"{prefix}: missing {field}")
        if "url" in item and not valid_url(item["url"]):
            errors.append(f"{prefix}: invalid URL {item['url']}")
        if item.get("status") not in ALLOWED_STATUS:
            errors.append(f"{prefix}: invalid status {item.get('status')}")
        if "focus" in item and not isinstance(item["focus"], list):
            errors.append(f"{prefix}: focus must be a list")

    return errors


def validate_training(data: dict) -> list[str]:
    errors: list[str] = []
    records = data.get("resources", [])
    errors.extend(validate_unique(records, "id", "training"))

    for index, item in enumerate(records):
        prefix = f"training[{index}]"
        for field in ("id", "title", "provider", "url", "dates", "status", "topics"):
            if field not in item:
                errors.append(f"{prefix}: missing {field}")
        if "url" in item and not valid_url(item["url"]):
            errors.append(f"{prefix}: invalid URL {item['url']}")
        if item.get("status") not in ALLOWED_STATUS:
            errors.append(f"{prefix}: invalid status {item.get('status')}")
        if "topics" in item and not isinstance(item["topics"], list):
            errors.append(f"{prefix}: topics must be a list")

    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_tools(load("tools.json")))
    errors.extend(validate_research(load("research.json")))
    errors.extend(validate_collections(load("collections.json")))
    errors.extend(validate_training(load("training.json")))

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print("OSINTAI catalogs are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
