#!/usr/bin/env python3
"""Render the catalog-driven parts of README.md from catalog/*.json.

Stdlib only. Everything between `<!-- osintai:NAME:start -->` and
`<!-- osintai:NAME:end -->` is generated; edit the JSON, not the README.

    python scripts/render_readme.py          # rewrite README.md
    python scripts/render_readme.py --check  # exit 1 if README.md is stale
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog"
README = ROOT / "README.md"

STATUS = {
    "verified": "✅ verified",
    "verified-preprint": "📄 preprint",
    "candidate": "🧪 candidate",
    "archival": "🗄️ archival",
    "rejected": "⛔ rejected",
}

# Display groups for the tool catalog. Tools not listed fall into "Other".
GROUPS: list[tuple[str, str, list[str]]] = [
    ("🤖 Agentic & orchestration platforms",
     "Models plan, call bounded tools and iterate over evidence.",
     ["openosint", "argus-os", "argus-cotcollective", "fetih", "unburden", "the-big-brother"]),
    ("🔌 MCP servers & tool fabrics",
     "OSINT sources and utilities exposed to assistants through MCP.",
     ["osint-mcp-server", "osint-mcp-rjn32s", "mcp-dadosbr", "greynoise-mcp-server"]),
    ("🏠 Local-first & evidence pipelines",
     "Collection, extraction and correlation on analyst-controlled infrastructure.",
     ["osintai-gs-ai", "taranis-ai", "pano", "focal-harvest", "ail-framework", "intelhub-firefox"]),
    ("🎯 Specialized investigation domains",
     "Dark web, SOCMINT, GEOINT, search-based discovery, military and criminal intelligence.",
     ["robin-dark-web-osint", "owasp-social-osint-agent", "worldview-hunter5thompson",
      "banshee-ai", "theosight", "s2w-dri"]),
    ("🕸️ Decentralized & experimental",
     "Mesh / peer-to-peer intelligence networks and unaudited research claims.",
     ["shadowbroker-infonet", "novbase-vtx", "starcom"]),
]


def load(name: str) -> dict:
    with (CATALOG / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def badge(label: str, message: str, color: str) -> str:
    def esc(text: str) -> str:
        return quote(text.replace("-", "--").replace("_", "__"), safe="")
    return f"https://img.shields.io/badge/{esc(label)}-{esc(message)}-{color}?style=flat-square"


def cell(text: str) -> str:
    return text.replace("|", "\\|")


def tags(values: list[str], limit: int = 3) -> str:
    return " ".join(f"`{v}`" for v in values[:limit])


def render_badges(tools: list[dict], version: str, reviewed: str) -> str:
    verified = sum(t["status"] == "verified" for t in tools)
    items = [
        ("catalog", f"v{version}", "7C3AED"),
        ("tools", str(len(tools)), "0EA5E9"),
        ("verified", f"{verified}/{len(tools)}", "10B981"),
        ("last reviewed", reviewed, "475569"),
    ]
    imgs = "\n".join(f'  <img alt="{label}: {msg}" src="{badge(label, msg, color)}">'
                     for label, msg, color in items)
    workflow = ("https://github.com/Ridd1kulusC0d3r/OSINTAI/actions/workflows/validate-catalog.yml")
    return (f'<p align="center">\n'
            f'  <a href="{workflow}"><img alt="Catalog validation" src="{workflow}/badge.svg"></a>\n'
            f"{imgs}\n</p>")


def render_stats(data: dict[str, list[dict]]) -> str:
    tools = data["tools"]
    verified = sum(t["status"] == "verified" for t in tools)
    local = sum(t["local_first"] for t in tools)
    mcp = sum("MCP" in t["protocols"] for t in tools)
    cols = [
        (len(tools), "tools & platforms"),
        (verified, "verified"),
        (local, "local-first"),
        (mcp, "speak MCP"),
        (len(data["research"]), "research records"),
        (len(data["paradigms"]), "paradigms"),
        (len(data["training"]), "training resources"),
        (len(data["collections"]), "curated collections"),
    ]
    head = "| " + " | ".join(f"**{n}**" for n, _ in cols) + " |"
    sep = "|" + "|".join(":---:" for _ in cols) + "|"
    body = "| " + " | ".join(label for _, label in cols) + " |"
    return "\n".join([head, sep, body])


def tool_row(tool: dict) -> str:
    name = f"[{cell(tool['name'])}]({tool['url']})"
    local = "🏠" if tool["local_first"] else "—"
    proto = ", ".join(tool["protocols"]) or "—"
    return (f"| {name} | {tags(tool['category'])} | {tags(tool['architecture'], 2)} "
            f"| {local} | {proto} | {STATUS.get(tool['status'], tool['status'])} |")


def render_tools(tools: list[dict]) -> str:
    by_id = {t["id"]: t for t in tools}
    placed: set[str] = set()
    groups = []
    for title, blurb, ids in GROUPS:
        members = [by_id[i] for i in ids if i in by_id]
        placed.update(t["id"] for t in members)
        groups.append((title, blurb, members))
    rest = [t for t in tools if t["id"] not in placed]
    if rest:
        groups.append(("📦 Other", "Not yet assigned to a display group.", rest))

    header = ("| Project | Focus | Architecture | Local-first | Protocols | Status |\n"
              "|---|---|---|:---:|:---:|:---:|")
    out = []
    for title, blurb, members in groups:
        if not members:
            continue
        out.append(f"#### {title}\n\n{blurb}\n\n{header}")
        out.extend(tool_row(t) for t in members)
        out.append("")
    return "\n".join(out).rstrip()


def render_research(refs: list[dict]) -> str:
    rows = ["| Year | Reference | Type |", "|:---:|---|---|"]
    for ref in sorted(refs, key=lambda r: (-int(r["year"]), r["title"])):
        status = ref.get("verification_status")
        mark = f" {STATUS[status].split()[0]}" if status in STATUS and status != "verified" else ""
        rows.append(f"| {ref['year']} | [{cell(ref['title'])}]({ref['url']}){mark} | {cell(ref['type'].replace('-', ' '))} |")
    return "\n".join(rows)


def render_learning(collections: list[dict], training: list[dict]) -> str:
    rows = ["**Curated collections** — discovery feeds; high-value entries are re-verified before promotion.", ""]
    for c in collections:
        rows.append(f"- [{c['name']}]({c['url']}) — {tags(c['focus'], 4)}")
    rows += ["", "**Training** — verified courses on AI for intelligence and OSINT.", ""]
    for t in training:
        rows.append(f"- [{t['title']}]({t['url']}) — {t['provider']}")
    return "\n".join(rows)


def render(text: str) -> str:
    tools_doc = load("tools.json")
    data = {
        "tools": tools_doc["tools"],
        "research": load("research.json")["references"],
        "paradigms": load("paradigms.json")["paradigms"],
        "training": load("training.json")["resources"],
        "collections": load("collections.json")["collections"],
    }
    blocks = {
        "badges": render_badges(data["tools"], tools_doc["version"], tools_doc["last_reviewed"]),
        "stats": render_stats(data),
        "tools": render_tools(data["tools"]),
        "research": render_research(data["research"]),
        "learning": render_learning(data["collections"], data["training"]),
    }
    for name, content in blocks.items():
        pattern = re.compile(
            rf"(<!-- osintai:{name}:start -->\n)(?:.*?\n)?(<!-- osintai:{name}:end -->)", re.S)
        if not pattern.search(text):
            raise SystemExit(f"README.md is missing the osintai:{name} markers")
        text = pattern.sub(lambda m: m.group(1) + content + "\n" + m.group(2), text)
    return text


def main() -> int:
    current = README.read_text(encoding="utf-8")
    updated = render(current)
    if "--check" in sys.argv:
        if updated != current:
            print("README.md is out of date. Run: python scripts/render_readme.py")
            return 1
        print("README.md is in sync with the catalog.")
        return 0
    README.write_text(updated, encoding="utf-8")
    print("README.md updated from catalog.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
