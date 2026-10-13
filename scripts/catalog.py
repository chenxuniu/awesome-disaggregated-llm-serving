"""Shared reader for a flat YAML subset with JSON scalars and arrays (Python 3.10+)."""
from __future__ import annotations
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / 'papers.yaml'
CATEGORIES = {
    'pd-disaggregation': 'Prefill–decode disaggregation and elasticity',
    'afd': 'Attention–FFN and expert disaggregation',
    'afd-theory': 'AFD provisioning and boundaries',
    'composite': 'Composite PD × attention–FFN serving',
    'reaggregation': 'Aggregation, multiplexing, and temporal alternatives',
    'kv-cache': 'KV-cache transfer, storage, and reuse',
    'moe-serving': 'MoE serving substrates',
    'serving-foundation': 'Serving foundations and engineering frameworks',
    'hardware-energy': 'Hardware, heterogeneity, quantization, and energy',
    'evaluation': 'Evaluation, traces, and simulators',
    'multimodal': 'Multimodal and encode–prefill–decode disaggregation',
}
STATUSES = {'foundational', 'production', 'theory', 'boundary', 'counter-baseline', 'substrate', 'adjacent'}
ARTIFACT_TYPES = {'paper', 'library', 'framework', 'benchmark'}
REQUIRED = {'id', 'title', 'year', 'venue', 'category', 'status', 'tags', 'why_it_matters',
            'limitation', 'source', 'verified', 'artifact_type'}
OPTIONAL = {'arxiv', 'code', 'aliases', 'related_sources', 'operator_subtype'}
OPERATOR_SUBTYPES = {'full-attention', 'core-attention', 'borrowed-attention', 'expert-service'}


def parse_value(raw: str):
    raw = raw.strip()
    if not raw:
        raise ValueError('empty value; use null explicitly')
    return json.loads(raw)


def load_papers(path: Path = PAPERS) -> list[dict]:
    papers, current = [], None
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if line.startswith('- '):
            current = {}
            papers.append(current)
            content = line[2:]
        elif line.startswith('  ') and not line.startswith('   ') and current is not None:
            content = line[2:]
        else:
            raise ValueError(f'Line {number}: expected a flat record or two-space field')
        key, sep, value = content.partition(':')
        if not sep or not re.fullmatch(r'[a-z_]+', key):
            raise ValueError(f'Line {number}: invalid field')
        if key in current:
            raise ValueError(f'Line {number}: duplicate key {key}')
        try:
            current[key] = parse_value(value)
        except (ValueError, TypeError) as exc:
            raise ValueError(f'Line {number}: invalid {key}: {exc}') from exc
    return papers


def valid_url(value) -> bool:
    if not isinstance(value, str) or any(char.isspace() for char in value):
        return False
    try:
        parsed = urlsplit(value)
        parsed.port  # Validate malformed and out-of-range ports as well as the hostname.
        return parsed.scheme == 'https' and bool(parsed.hostname) and not parsed.username
    except ValueError:
        return False


def validate(papers: list[dict]) -> list[str]:
    errors = []
    if not papers:
        errors.append('Catalog must contain at least one entry')
    ids, arxiv_ids = set(), set()
    for index, paper in enumerate(papers, 1):
        label = f"Entry {index} ({paper.get('id', '?')})"
        for key in sorted(REQUIRED - paper.keys()):
            errors.append(f'{label}: missing {key}')
        for key in sorted(paper.keys() - REQUIRED - OPTIONAL):
            errors.append(f'{label}: unknown field {key}')
        for key in ('id', 'title', 'venue', 'why_it_matters', 'limitation'):
            value = paper.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f'{label}: {key} must be a nonempty string')
        pid = paper.get('id')
        if isinstance(pid, str):
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', pid):
                errors.append(f'{label}: id must be a lowercase slug')
            if pid in ids:
                errors.append(f'{label}: duplicate id {pid}')
            ids.add(pid)
        year = paper.get('year')
        if type(year) is not int or not 2000 <= year <= date.today().year:
            errors.append(f'{label}: year must be an integer between 2000 and the current year')
        for key, choices in (('category', CATEGORIES), ('status', STATUSES), ('artifact_type', ARTIFACT_TYPES)):
            value = paper.get(key)
            if not isinstance(value, str) or value not in choices:
                errors.append(f'{label}: invalid {key}: {value!r}')
        aid = paper.get('arxiv')
        if aid is not None:
            if not isinstance(aid, str) or not re.fullmatch(r'\d{2}(?:0[1-9]|1[0-2])\.\d{4,5}', aid):
                errors.append(f'{label}: arxiv must be an unversioned identifier or null')
            elif aid in arxiv_ids:
                errors.append(f'{label}: duplicate arxiv {aid}')
            else:
                arxiv_ids.add(aid)
        if not valid_url(paper.get('source')):
            errors.append(f'{label}: source must be an HTTPS URL')
        if paper.get('code') is not None and not valid_url(paper['code']):
            errors.append(f'{label}: code must be an HTTPS URL or null')
        tags = paper.get('tags')
        if not isinstance(tags, list) or not tags or any(not isinstance(t, str) or not t.strip() for t in tags):
            errors.append(f'{label}: tags must be a nonempty list of nonempty strings')
        if 'aliases' in paper:
            aliases = paper['aliases']
            if not isinstance(aliases, list) or any(not isinstance(a, str) or not a.strip() for a in aliases):
                errors.append(f'{label}: aliases must be a list of nonempty strings')
        if 'related_sources' in paper:
            sources = paper['related_sources']
            if not isinstance(sources, list) or any(not valid_url(s) for s in sources):
                errors.append(f'{label}: related_sources must be a list of HTTPS URLs')
        if 'operator_subtype' in paper:
            subtype = paper['operator_subtype']
            if not isinstance(subtype, str) or subtype not in OPERATOR_SUBTYPES:
                errors.append(f'{label}: invalid operator_subtype')
        checked = paper.get('verified')
        try:
            if not isinstance(checked, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', checked):
                raise ValueError('expected YYYY-MM-DD')
            if date.fromisoformat(checked) > date.today():
                raise ValueError('future date')
        except (ValueError, TypeError):
            errors.append(f'{label}: verified must be a real, nonfuture YYYY-MM-DD date')
    return errors


def read_validated() -> list[dict]:
    papers = load_papers()
    errors = validate(papers)
    if errors:
        raise ValueError('\n'.join(errors))
    return papers


def link_for(paper: dict) -> str:
    return paper.get('source') or (f"https://arxiv.org/abs/{paper['arxiv']}" if paper.get('arxiv') else paper.get('code', ''))


def cell(value) -> str:
    return (str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('|', '&#124;').replace('[', '&#91;').replace(']', '&#93;')
            .replace('\n', ' ').replace('\r', ' '))


def markdown_url(value: str) -> str:
    return quote(value, safe=":/?#@!$&'*+,;=%~")
