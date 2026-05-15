#!/usr/bin/env python3
"""Validate required fields in papers.yaml.

This script uses only the Python standard library and parses the simple YAML
subset used by this repository.
"""

from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers.yaml"
REQUIRED = {
    "id",
    "title",
    "year",
    "venue",
    "category",
    "status",
    "tags",
    "why_it_matters",
    "limitation",
}


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


def main() -> None:
    papers = load_papers()
    ids: set[str] = set()
    errors: list[str] = []

    for index, paper in enumerate(papers, start=1):
        missing = sorted(REQUIRED - set(paper))
        if missing:
            errors.append(f"Entry {index} is missing: {', '.join(missing)}")

        paper_id = paper.get("id")
        if paper_id in ids:
            errors.append(f"Duplicate id: {paper_id}")
        ids.add(paper_id)

        if paper.get("arxiv") and not isinstance(paper["arxiv"], str):
            errors.append(f"{paper_id}: arxiv must be a string or null")

        if not isinstance(paper.get("tags"), list):
            errors.append(f"{paper_id}: tags must be a list")

    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)

    print(f"Validated {len(papers)} paper entries.")


if __name__ == "__main__":
    main()
