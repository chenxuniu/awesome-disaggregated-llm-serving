# Source and Verification Policy

## Review Snapshot

The 2026-10-13 update checked title/identifier metadata on official arXiv abstract
pages for all **44 existing arXiv entries** and **21 added papers**. It added an
official USENIX page for Orca, verified selected author-associated code links,
and consulted official runtime documentation and project READMEs.

This is a bibliographic and documentation review. It is not a reproduction of
reported speedups, a complete audit of every paper, or a GPU compatibility test.
Publication venues are recorded where supported; otherwise a new paper remains
`arXiv`. Titles on arXiv may change between revisions.

Primary sources are linked directly from every catalog record in `source`.
Runtime guides and workload schemas are linked where used in the engineering
and evaluation pages. Search results and other awesome lists are discovery aids,
not evidence for a contribution or artifact association.

## How to Interpret a Record

- `source`: primary page establishing the work's identity; a paper link is
  distinct from its implementation link.
- `arxiv`: unversioned modern identifier, or `null`. Sources without arXiv use
  their official publication/project page.
- `code`: verified author/project-associated artifact link, or `null`. It may
  be a library, research prototype, data release, or broader runtime; read the
  scope note before treating it as a full paper reproduction.
- `verified`: source identity/metadata check date, not a claim that all reported
  results or current dependencies have been validated.
- `year`: publication year when verified, otherwise first preprint year. For
  evolving software, use the cataloged artifact/snapshot year and describe it;
  do not infer a first release from this field.
- `venue`: verified conference/journal, `arXiv`, or `GitHub`. No acceptance is
  inferred from a project's maturity or a search result.
- `artifact_type`: `paper`, `library`, `framework`, or `benchmark`.
- `status`: editorial reading role, retained for compatibility with the initial
  map. `production` describes the original map's deployment-oriented role;
  it is not independent proof of production readiness or peer review.
- `why_it_matters`: source-grounded relevance to this repository's scope.
- `limitation`: an editorial scope/comparison note, not necessarily a limitation
  acknowledged by the authors. It should distinguish measured, simulated,
  analytical, model-specific, and hardware-specific evidence where relevant.

Missing code means an associated link was not verified during this pass; it does
not assert that code does not exist. A runtime's current `main` may no longer
match a historical paper. Pin commits when reproducing results.

## Corrections and Boundaries in This Update

- BurstGPT's author-maintained repository cites **KDD 2025**; its original 2024
  arXiv identifier is retained. [Dataset and citation](https://github.com/HPMLL/BurstGPT).
- The energy-implications paper is indexed with a 2026 arXiv ID, but its official
  page gives a 2025 submission date. The catalog uses **2025** under its stated
  first-preprint convention. [Primary source](https://arxiv.org/abs/2601.08833).
- DynaServe uses the title currently returned by the official abstract page,
  which differs from older search-index wording. [Paper](https://arxiv.org/abs/2504.09285).
- The ICML 2025 EPDServe artifact and the Ascend EPD-Serve preprint are separate
  entries with distinct sources. [ICML artifact](https://github.com/vbdi/epdserve),
  [Ascend preprint](https://arxiv.org/abs/2601.11590).
- Step-3's linked code is StepMesh, a communication library; it is not labeled
  as a full open implementation of the serving system.
- The author-linked Llumnix URL redirects to `llumnix-project/llumnix-ray`.
  The original association is preserved in the database, and the directory
  points to the resolved project. [Source](https://github.com/AlibabaPAI/llumnix).
- Frontier is conservatively listed as `arXiv` rather than an unspecified
  workshop; no named publication was verified in this pass.
- Analytical provisioning's description no longer claims to be the first
  framework; priority claims require a broader literature audit.
- Elastic PD, provisioning, and transfer optimization have existing work.
  The research-questions page now names those anchors before suggesting extensions.

## Maintenance Boundaries

Offline validation checks structure, syntax, nonempty fields, labels, date
format, and duplicate IDs/arXiv identifiers. It cannot establish bibliographic
truth, link availability, or correctness of scientific claims.

Generated Markdown and JSON are reproducible from `papers.yaml`. CI checks
freshness and command behavior without fetching external websites, avoiding
spurious failures from rate limits or temporarily unavailable sources.

Before adding an entry, read its primary source and verify title, year/venue,
artifact association, and at least the contribution/scope described in the
record. Before updating deployment commands, check the official guide for the
same software version. Prefer explicit source-linked corrections over an
unqualified claim that the catalog is exhaustive.

## Survey Integration Pass (2026-10-13)

The second pass used Chenxu Niu's author-supplied draft *Disaggregated LLM
Serving: A Survey and Taxonomy of Prefill–Decode and Attention–FFN Separation*
as a discovery and conceptual reference. Its frozen discovery layer contains
374 works with a 2026-10-07 search cutoff; its analytical set contains 46
source-located works. These are different layers and were not treated as
interchangeable evidence.

This repository now has **139 curated records** and **374 discovery records**,
with **117 mapped overlaps**. Those mapping rules yield **396 combined work
records**; this is a catalog count, not a count of distinct serving systems,
implementations, production deployments, or reproduced results.

The imported index contains:

- **257 metadata-verified records:** 250 official arXiv identities and seven
  identities recovered through the official Crossref DOI registry.
- **104 reachable records:** official proceedings/documentation/project links
  opened successfully. Reachability is not a full technical/status audit.
- **13 reference-only records:** primary links from the supplied bibliography
  remain, but access restrictions, timeouts, or registry rate limits prevented
  an independent identity check in this pass. They are visibly marked and have
  no successful-check date.

The extension preserves survey-reported venue and role as separate JSON fields.
Its descriptions and seven-class placements are attributed survey annotations.
Checking a title, DOI, or page does not independently validate its technical
classification, peer-review claim, state contract, or operational properties.
No system-property percentages were recomputed from the discovery layer.

ArXiv/current-title changes were applied to display titles, with historical
names retained for search. This includes LAPS/PLA-Serve, Tessera/FluidGPU,
DualScale/BiScale, and CHIME/L3. Libra's official NSDI 2026 page and the extended
Frontier paper became canonical while stable IDs and earlier source links remain.
ShuffleInfer's ACM TACO 2025 publication and Tropical's DAC 2025 publication
metadata were also checked against Crossref and made canonical. Their preprints
remain related sources. The TetriInfer/ShuffleInfer pair keeps both references
without claiming that the earlier technical extraction is identical to the
archival paper; Tropical's later arXiv posting is not a new 2026 publication.

Two supporting energy-evaluation references in the draft's later revision notes,
TokenPowerBench and TokenPowerSandbox, are curated separately from the frozen
374-work discovery set. Their scope notes explicitly avoid using measurement or
single-GPU calibration as proof of PD/AFD energy savings.

The boundary guide adapts the draft's structural/operational distinction and
four operator subtypes. It remains an editorial framework. The public repository
contains source-linked metadata and newly authored/adapted guides; it does not
contain the private Overleaf checkout, project access address, manuscript source,
or its full internal audit/coding logs.

## Discovery Maintenance

`data/discovery.json` is the source of truth for the extended layer. Run
`python3 scripts/generate_discovery.py --write` after changing it and use
`--check` in CI. The generator validates evidence-state dates, class/subtype
compatibility, duplicate JSON keys/IDs, source/metadata URLs, and mappings into
curated records. It does not call the network or upgrade source-check status.

Combined search matches either representation before returning a curated record
once for a mapped work. Accordingly, an inherited tag/category/year can match
while the returned curated record uses corrected metadata. Select the discovery
collection to inspect the exact matching historical classification.
