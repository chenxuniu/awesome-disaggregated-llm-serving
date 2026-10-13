"""Load the source-linked survey discovery layer without upgrading its evidence."""

from datetime import date
import json
from pathlib import Path
import re

from catalog import CATEGORIES, ROOT, valid_url

DISCOVERY = ROOT / 'data' / 'discovery.json'
CLASSES = {
    'P': ('phase', 'Fixed phase separation'),
    'A': ('adaptive', 'Adaptive phase execution'),
    'O': ('operator', 'Operator and expert-service separation'),
    'C': ('composite', 'Composite PD × AFD'),
    'S': ('stage', 'Multimodal and other stage boundaries'),
    'D': ('comparative', 'Direct comparative and provisioning work'),
    'E': ('enabling', 'Enabling mechanisms and adjacent baselines'),
}
SUBTYPES = {
    'P': {'P1', 'P2', 'P3'}, 'A': {'A1', 'A2'}, 'O': {'O1', 'O2', 'O3', 'O4'},
    'C': {'C1'}, 'S': {'S1', 'S2'}, 'D': {'D1', 'D2', 'D3'}, 'E': {'E1', 'E2', 'E3', 'E4'},
}
CHECKS = {'metadata-verified', 'reachable', 'reference-only'}


def unique_object(pairs: list[tuple]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Discovery JSON: duplicate key {key}')
        result[key] = value
    return result


def load_discovery(main_ids: set[str], path: Path = DISCOVERY) -> list[dict]:
    rows = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
    if not isinstance(rows, list) or not rows:
        raise ValueError('Discovery must be a nonempty JSON list')
    ids = set()
    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            raise ValueError(f'Discovery row {index}: expected a record')
        label = f'Discovery row {index}'
        pid = row.get('id')
        if not isinstance(pid, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', pid) or pid in ids or pid in main_ids:
            raise ValueError(f'{label}: invalid, duplicate, or curated-colliding id')
        ids.add(pid)
        for key in ('title', 'survey_key', 'why_it_matters', 'limitation'):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError(f'{label}: missing/invalid {key}')
        year = row.get('year')
        if type(year) is not int or not 2000 <= year <= date.today().year:
            raise ValueError(f'{label}: invalid year')
        if not isinstance(row.get('category'), str) or row['category'] not in CATEGORIES:
            raise ValueError(f'{label}: invalid category')
        cls, sub = row.get('class'), row.get('subtype')
        if not isinstance(cls, str) or cls not in CLASSES or not isinstance(sub, str) or sub not in SUBTYPES[cls]:
            raise ValueError(f'{label}: class/subtype mismatch')
        if not isinstance(row.get('tags'), list) or any(not isinstance(t, str) or not t.strip() for t in row['tags']):
            raise ValueError(f'{label}: invalid tags')
        if not isinstance(row.get('aliases', []), list) or any(not isinstance(t, str) for t in row.get('aliases', [])):
            raise ValueError(f'{label}: invalid aliases')
        state = row.get('source_check')
        if not isinstance(state, str) or state not in CHECKS:
            raise ValueError(f'{label}: invalid source_check')
        if not valid_url(row.get('source')):
            raise ValueError(f'{label}: source must be an HTTPS URL')
        if row.get('code') is not None and not valid_url(row['code']):
            raise ValueError(f'{label}: invalid code URL')
        aid = row.get('arxiv')
        if aid is not None and (not isinstance(aid, str) or not re.fullmatch(r'\d{2}(?:0[1-9]|1[0-2])\.\d{4,5}', aid)):
            raise ValueError(f'{label}: invalid arxiv')
        if row.get('metadata_source') is not None and not valid_url(row['metadata_source']):
            raise ValueError(f'{label}: invalid metadata_source URL')
        checked = row.get('checked')
        if state == 'reference-only':
            if checked is not None:
                raise ValueError(f'{label}: reference-only checked must be null')
        else:
            try:
                if not isinstance(checked, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', checked) or date.fromisoformat(checked) > date.today():
                    raise ValueError('invalid date')
            except (TypeError, ValueError) as exc:
                raise ValueError(f'{label}: invalid checked date') from exc
        main_id = row.get('main_id')
        if main_id is not None and (not isinstance(main_id, str) or main_id not in main_ids):
            raise ValueError(f'{label}: unknown main_id {main_id!r}')
    return rows
