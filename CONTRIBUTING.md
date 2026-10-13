# Contributing

Help readers decide what to read, implement, and compare. Every entry needs a
primary source, a concrete contribution, and an honest scope note.

## Scope

Include phase/operator/state/expert disaggregation, aggregation alternatives,
MoE substrates affecting those decisions, hardware/energy constraints,
multimodal stages, and evaluation tools/traces. General inference optimizations
need an explicit connection to this scope.

## Add or Correct an Entry

Edit `papers.yaml`, the source of truth. Do not edit `docs/catalog.md` or
`data/papers.json` directly. Use a flat record with **two-space indentation**
and JSON syntax for values: double-quoted strings, integer years, string arrays,
and `null`. Multiline YAML, single quotes, aliases, and inline comments are not
supported by the dependency-free reader.

```yaml
- id: "sample-work"
  title: "Exact title from the primary source"
  year: 2026
  venue: "arXiv"
  category: "pd-disaggregation"
  status: "adjacent"
  arxiv: null
  code: null
  tags: ["PD", "scheduling"]
  why_it_matters: "Explain the mechanism and its relevance to disaggregation."
  limitation: "Describe evaluation or scope boundaries without inventing a weakness."
  source: "https://example.org/official-paper-page"
  verified: "2026-10-13"
  artifact_type: "paper"
```

Replace the example identity/source and date with real verified values. Use an
arXiv identifier only after checking that its page contains the intended work.
The optional `arxiv` and `code` fields can be omitted or set to `null`.

## Labels and Conventions

Categories:

- `pd-disaggregation`: phase splitting, elasticity, placement.
- `afd`: attention/FFN or attention/expert systems.
- `afd-theory`: AFD provisioning and boundary studies.
- `reaggregation`: colocated, unified, multiplexed, or temporal alternatives.
- `kv-cache`: transfer, pooling, compression, storage, and reuse.
- `moe-serving`: expert routing/communication and sparse-model substrates.
- `serving-foundation`: runtime foundations and distributed frameworks.
- `hardware-energy`: hardware, heterogeneous allocation, precision, power, cost.
- `evaluation`: datasets, simulators, and benchmark tools.
- `multimodal`: encode/prefill/decode and other multimodal stage splits.

Use one primary category and multiple tags when work spans topics. Search tags
are exact and case-insensitive; reuse established spellings when applicable.

Reading-role labels (`status`): `foundational`, `production`, `theory`, `boundary`,
`counter-baseline`, `substrate`, `adjacent`. These are editorial roles, not
publication or readiness states. Preserve this distinction when revising old entries.

Artifact types: `paper`, `library`, `framework`, `benchmark`. Papers describing
traces or runtimes remain papers; project-only entries use the corresponding
artifact type. Software year identifies the cataloged artifact/snapshot; paper
year uses a verified publication year, otherwise first preprint year.

## Source Checks Before Submitting

1. Verify title and identity on arXiv, an official proceedings page, or the
   author-maintained project.
2. Verify publication/venue separately; use `arXiv` when acceptance is unconfirmed.
3. Use author/project-associated artifacts. Do not guess a GitHub URL from a title.
4. Explain whether linked code is the full system, a component, a data release,
   or a broader runtime; record that distinction in the scope note.
5. Distinguish simulation, analytical prediction, proxy hardware, and live-system
   evidence. Avoid transferring reported gains to a different setup.
6. Record the actual source-check date in `verified` and update relevant reading
   paths, taxonomy, or research questions when the entry changes their framing.

See [docs/sources.md](docs/sources.md) for the full interpretation policy.

## Regenerate and Check

From the repository root, using Python 3.10+ and the standard library:

```bash
python3 scripts/validate_papers.py
python3 scripts/generate_tables.py --write
python3 scripts/generate_tables.py --check
python3 -m unittest discover -s tests -v
```

Commit both generated files with the database change. The generator sorts within
categories by descending year and stable ID. `--check` never writes files.

Offline validation catches syntax/label errors and duplicate IDs/arXiv identifiers.
It does not prove that a link exists or that a scientific claim is true. Include
source evidence in your PR description and distinguish content checks from GPU testing.
