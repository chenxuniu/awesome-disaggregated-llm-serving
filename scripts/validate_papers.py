#!/usr/bin/env python3
"""Validate catalog structure and metadata syntax offline."""
import sys
from catalog import read_validated


def main() -> int:
    try:
        papers = read_validated()
    except (ValueError, OSError) as exc:
        print(exc, file=sys.stderr)
        return 1
    print(f'Validated {len(papers)} catalog entries.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
