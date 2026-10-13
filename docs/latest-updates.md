# Recent Work and Canonical-Version Updates

Source snapshot: **2026-10-13**. This is a selected reading guide, not a total
ordering of importance. The [extended index](discovery.md) contains the complete
374-work discovery layer adapted from the survey's 2026-10-07 search snapshot.
Its technical classifications and publication labels are explicitly attributed
rather than silently promoted to independently audited evidence.

## October 2026: Configuration, Elasticity, and Expert Placement

- [ECO](catalog.md#eco): budgeted energy-oriented search across deployment
  structures and operating controls. Include search cost, held-out frozen outcomes,
  latency feasibility, and measurement boundaries in comparisons.
- [AFORE](catalog.md#afore): expert reconfiguration using upcoming microbatch
  demand and an overlap window. Compare placement adaptation with migration cost
  and skew, rather than assuming static expert placement is the only baseline.
- [FluidPD](catalog.md#fluidpd): transient prefill offload plus sustained role
  reassignment. Separate short-timescale slack use from resource scaling.
- [DynaCore](catalog.md#dynacore): phase-aware quantization and accelerator shape
  adaptation; its hardware evidence differs from a GPU runtime deployment.

These entries are preprints in the curated catalog unless a publication is
explicitly verified. “Recent” does not imply measured production readiness.

## Operator, Expert, and Composite Serving

- [FastAFD](catalog.md#fastafd) and [vLLM AFD Plugin](catalog.md#vllm-afd-plugin):
  runnable AFD starting points with distinct scope, backend, and measurement limits.
- [AFlex](catalog.md#aflex): joint phase/operator provisioning and operator DVFS;
  [ECO](catalog.md#eco): measurement-budgeted configuration optimization.
- [ExpertPlex](catalog.md#expertplex): shared experts across P/D with adaptive
  persistent kernels; [HexGen-3](catalog.md#hexgen-3): heterogeneous composite pools.
- [OpScale](catalog.md#opscale) and [OpWeave](catalog.md#opweave): operator-level
  scaling and flexible partitioning rather than only a fixed A/F cut.
- [CrossPool](catalog.md#crosspool): cold multi-model MoE memory organization.
- [KernelFlume](catalog.md#kernelflume): weightless core-attention elasticity;
  [Tarragon](catalog.md#tarragon): attention/expert failure-domain isolation.
- [ASAP](catalog.md#asap): asynchronous disaggregated MoE **prefill**, which must
  be evaluated separately from decode-focused claims.
- [EaaS](catalog.md#expert-as-a-service), [Remoe](catalog.md#remoe), and
  [FaaSMoE](catalog.md#faasmoe): expert-service and serverless cost models.

Use the [operator-boundary guide](boundary-guide.md) before transferring results
between full attention, core attention, borrowed capacity, and expert services.

## Agentic, Cache, and Elastic Phase Serving

- [Crossflow](catalog.md#crossflow): revocable leases for decode-side prefill slack.
- [PPD](catalog.md#ppd) and [AMPD](catalog.md#ampd): incremental multi-round prefill
  and cache locality; length-only independent request replay misses this behavior.
- [DualPath](catalog.md#dualpath): KV storage I/O through both sides' data paths.
- [TokenScale](catalog.md#tokenscale) and [HeteroScale](catalog.md#heteroscale):
  scaling signals, phase imbalance, heterogeneous placement, and topology.
- [semi-PD](catalog.md#semi-pd): unified storage and phase-wise computation.
- [RAPID-Serve](catalog.md#rapid-serve): intra-GPU P/D partitioning.
- [Libra](catalog.md#dynaserve) and [Tropical](catalog.md#tropical): flexible request
  partitioning and SLO-aware multiplexing are relevant alternatives to fixed pools.
- [PEARL](catalog.md#pearl): adaptive P/D execution and resource borrowing in
  agentic RL rollout; distinguish application completion from online-serving SLOs.

## Hardware, Power, and Multimodal Extensions

- [DualScale](catalog.md#dualscale), [PowerSlider](catalog.md#powerslider),
  [AFlex](catalog.md#aflex), and [power-aware PD provisioning](catalog.md#power-provisioning-pd)
  span phase/operator DVFS, moving power caps, and analytical sizing.
- [MIST](catalog.md#mist), [MemExplorer](catalog.md#memexplorer),
  [HeteroPanacea](catalog.md#heteropanacea), and [Tessera](catalog.md#tessera)
  widen the architecture/configuration comparison space.
- [KARAT](catalog.md#karat), [NELSSA](catalog.md#nelssa), and [CHIME](catalog.md#chime)
  connect attention representation with PNM/PIM assumptions.
- [ElasticMM](catalog.md#elasticmm), [TriInfer](catalog.md#triinfer),
  [Nova](catalog.md#nova), and [UnifiedServe](catalog.md#unifiedserve) supplement
  EPD with heterogeneous and shared-device stage organizations.

## Canonical Versions and Aliases

Stable catalog IDs remain valid when a name or canonical source changes.

| Search name(s) | Current treatment | Source/version note |
|---|---|---|
| Libra / DynaServe | One curated record, stable `dynaserve` ID | [NSDI 2026 Libra](https://www.usenix.org/conference/nsdi26/presentation/ruan-libra) is primary; earlier [DynaServe preprint](https://arxiv.org/abs/2504.09285) remains a related source |
| Frontier | One simulator version family | [Extended 2026 paper](https://arxiv.org/abs/2605.21312) replaces the [earlier workshop preprint](https://arxiv.org/abs/2508.03148) as primary |
| TetriInfer / ShuffleInfer | Stable `tetriinfer` ID and both aliases | [ACM TACO 2025 ShuffleInfer](https://doi.org/10.1145/3732941) is primary; [earlier preprint](https://arxiv.org/abs/2401.11181) remains linked; selected-version technical claims still need checking |
| Tropical | Verified publication year 2025 | [DAC 2025 publication](https://doi.org/10.1109/DAC63849.2025.11132617) is primary; the [2026 arXiv posting](https://arxiv.org/abs/2606.16264) remains related |
| DualScale / BiScale | One `dualscale` record | [Same arXiv identifier](https://arxiv.org/abs/2602.18755); different historical titles are not separate systems |
| LAPS / PLA-Serve | One `laps` record | [Current primary title](https://arxiv.org/abs/2601.11589) is LAPS |
| Tessera / FluidGPU | One `tessera` record | [Current primary title](https://arxiv.org/abs/2604.10180) is Tessera |
| CHIME / L3 | One `chime` record | [Current source](https://arxiv.org/abs/2504.17584) is CHIME; earlier-title provenance is retained |
| TriInfer / HydraInfer | One `triinfer` record | [MLSys 2026 proceedings](https://proceedings.mlsys.org/paper_files/paper/2026/hash/f068c65585985c25c17f221390774ec7-Abstract-Conference.html) is canonical |

Publication year and first-public year differ. The curated layer favors verified
publication year when available; the discovery snapshot records its own year
convention, corrected with official preprint metadata where available. Avoid
turning renamed or extended versions into a fabricated count of new systems.
