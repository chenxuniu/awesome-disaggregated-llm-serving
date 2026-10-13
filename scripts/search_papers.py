#!/usr/bin/env python3
"""Search by text, category, tag, year, or code availability."""
import argparse
import json
import sys
from catalog import CATEGORIES, read_validated, link_for


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='', help='Case-insensitive substring in title, tags, and summaries')
    parser.add_argument('--category', choices=CATEGORIES)
    parser.add_argument('--tag', help='Exact case-insensitive tag')
    parser.add_argument('--year', type=int)
    parser.add_argument('--code', action='store_true', help='Only entries with a verified code/artifact link')
    parser.add_argument('--json', action='store_true', help='Return a JSON list')
    args = parser.parse_args()
    try:
        papers = read_validated()
    except (ValueError, OSError) as exc:
        print(exc, file=sys.stderr)
        return 1
    rows = []
    for p in papers:
        searchable = ' '.join([p['id'], p['title'], *p['tags'], p['why_it_matters'], p['limitation']]).casefold()
        if args.query.casefold() not in searchable:
            continue
        if args.category and p['category'] != args.category:
            continue
        if args.tag and args.tag.casefold() not in [t.casefold() for t in p['tags']]:
            continue
        if args.year is not None and p['year'] != args.year:
            continue
        if args.code and not p.get('code'):
            continue
        rows.append(p)
    rows.sort(key=lambda p: (-p['year'], p['id']))
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        print(f'{len(rows)} matches')
        for p in rows:
            print(f"\n{p['id']} ({p['year']}, {p['category']}): {p['title']}\n  {link_for(p)}")
            if p.get('code'):
                print(f"  Code: {p['code']}")
            print(f"  {p['why_it_matters']}\n  Scope: {p['limitation']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
