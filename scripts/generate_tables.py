#!/usr/bin/env python3
"""Generate simple Markdown tables from papers.yaml.

Usage:
    python scripts/generate_tables.py

The script prints tables to stdout so maintainers can paste the output into
README.md or docs pages after editing papers.yaml.

It intentionally uses only the Python standard library. The parser below is a
small, repo-specific reader for the simple YAML subset used in papers.yaml.
"""

from __future__ import annotations

import ast
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers.yaml"


def parse_value(raw: str):
    raw = raw.strip()
    if raw == "null":
        return None
    if raw.startswith("[") and raw.endswith("]"):
        return ast.literal_eval(raw)
    if raw.startswith('"') and raw.endswith('"'):
        return raw[1:-1]
    return raw


def load_papers() -> list[dict]:
    papers: list[dict] = []
    current: dict | None = None

    for line in PAPERS.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("- "):
            if current is not None:
                papers.append(current)
            current = {}
            key, value = line[2:].split(":", 1)
            current[key.strip()] = parse_value(value)
            continue
        if line.startswith("  ") and current is not None:
            key, value = line.strip().split(":", 1)
            current[key.strip()] = parse_value(value)

    if current is not None:
        papers.append(current)

    return papers


def link_for(paper: dict) -> str:
    if paper.get("arxiv"):
        return f"https://arxiv.org/abs/{paper['arxiv']}"
    if paper.get("code"):
        return paper["code"]
    return ""


def main() -> None:
    papers = load_papers()
    by_category: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        by_category[paper.get("category", "uncategorized")].append(paper)

    for category in sorted(by_category):
        print(f"## {category}\n")
        print("| Year | Work | Status | Why it matters |")
        print("|---:|---|---|---|")
        for paper in sorted(by_category[category], key=lambda p: (p.get("year", 9999), p["title"])):
            url = link_for(paper)
            title = paper["title"]
            work = f"[{title}]({url})" if url else title
            print(
                f"| {paper.get('year', '')} | {work} | "
                f"{paper.get('status', '')} | {paper.get('why_it_matters', '')} |"
            )
        print()


if __name__ == "__main__":
    main()
