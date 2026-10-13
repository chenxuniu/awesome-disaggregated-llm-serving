#!/usr/bin/env python3
"""Search by text, category, tag, year, or code availability."""
import argparse
import json
import sys
from catalog import CATEGORIES, read_validated, link_for
from discovery import CLASSES, load_discovery


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='', help='Case-insensitive substring in title, tags, and summaries')
    parser.add_argument('--category', choices=CATEGORIES)
    parser.add_argument('--tag', help='Exact case-insensitive tag')
    parser.add_argument('--year', type=int)
    parser.add_argument('--code', action='store_true', help='Only entries with a verified code/artifact link')
    parser.add_argument('--json', action='store_true', help='Return a JSON list')
    parser.add_argument('--collection', choices=['curated', 'discovery', 'all'], default='curated')
    parser.add_argument('--class', dest='boundary_class', choices=CLASSES, help='Survey discovery class; mapped curated matches are retained with --collection all')
    args = parser.parse_args()
    try:
        papers = read_validated()
        curated = {p['id']: p for p in papers}
        if args.boundary_class and args.collection == 'curated':
            parser.error('--class requires --collection discovery or all')
        if args.collection != 'curated':
            discovered = load_discovery({p['id'] for p in papers})
            if args.collection == 'discovery':
                papers = discovered
            else:
                papers += discovered
    except (ValueError, OSError) as exc:
        print(exc, file=sys.stderr)
        return 1
    rows = []
    seen = set()
    for p in papers:
        if args.boundary_class and p.get('class') != args.boundary_class:
            continue
        searchable = ' '.join([p['id'], p['title'], *p.get('aliases', []), *p['tags'], p['why_it_matters'], p['limitation']]).casefold()
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
        result = curated[p['main_id']] if args.collection == 'all' and p.get('main_id') else p
        if result['id'] not in seen:
            seen.add(result['id'])
            rows.append(result)
    rows.sort(key=lambda p: (-p['year'], p['id']))
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        print(f'{len(rows)} matches')
        for p in rows:
            print(f"\n{p['id']} ({p['year']}, {p['category']}): {p['title']}\n  {link_for(p)}")
            if p.get('code'):
                print(f"  Code: {p['code']}")
            if 'source_check' in p:
                print(f"  Source check: {p['source_check']}; checked: {p.get('checked') or 'unverified'}; class: {p['class']}/{p['subtype']}")
            print(f"  {p['why_it_matters']}\n  Scope: {p['limitation']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
