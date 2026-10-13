# Find the Nearest Mechanism Before Claiming a Gap

This page turns the survey-derived coverage into comparison questions. It does
not assert that a listed direction is unexplored. The [boundary guide](boundary-guide.md)
explains why phase, core-attention, full-attention, and expert-service results
need different baselines.

| Decision or proposed contribution | Existing anchors | A comparison that would make the contribution concrete |
|---|---|---|
| Dynamically resize P/D resources | [FluidPD](catalog.md#fluidpd), [HeteroScale](catalog.md#heteroscale), [TokenScale](catalog.md#tokenscale), [Libra](catalog.md#dynaserve) | Separate worker startup, fast offload, role flips, and steady capacity changes; test both burst and sustained ratio shifts |
| Execute some prefill on decode slack | [Prefill deflection](catalog.md#prefill-deflection), [Crossflow](catalog.md#crossflow), [PPD](catalog.md#ppd), [Tropical](catalog.md#tropical) | Protect the same decode-tail SLO, preserve multi-turn cache semantics, and measure avoided versus newly created state movement |
| Independently scale attention and experts | [MegaScale-Infer](catalog.md#megascale-infer), [OpScale](catalog.md#opscale), [AFORE](catalog.md#afore), [KernelFlume](catalog.md#kernelflume) | State the operator subtype; isolate KV-capacity scaling, expert placement, replica counts, and weight/resharding overhead |
| Use AFD to improve energy | [AFlex](catalog.md#aflex), [ECO](catalog.md#eco), [DualScale](catalog.md#dualscale), [energy reevaluation](catalog.md#energy-disagg) | Compare matched resource allocation and metric definitions; ablate the cut, DVFS, layout, batching, and configuration-search budget |
| Predict which architecture/configuration wins | [AFD-Ledger](catalog.md#afd-ledger), [BestServe](catalog.md#bestserve), [AIConfigurator](catalog.md#aiconfigurator), [Frontier](catalog.md#frontier) | Evaluate held-out architecture choices and feasible-plan ranking, including configurations where a predictor should abstain |
| Improve activation/KV communication | [KVDirect](catalog.md#kvdirect), [StepMesh](catalog.md#stepmesh), [FastAFD](catalog.md#fastafd), [DualPath](catalog.md#dualpath) | Price the actual directional bytes, cadence, registration/control overhead, queueing, and achieved bandwidth on each resource |
| Separate experts as a resilient service | [Tarragon](catalog.md#tarragon), [EaaS](catalog.md#expert-as-a-service), [Remoe](catalog.md#remoe), [FaaSMoE](catalog.md#faasmoe) | Inject failures and account for checkpoint/replica memory, failure-free overhead, restored request state, and healthy-peer progress |
| Optimize agentic or multimodal serving | [PPD](catalog.md#ppd), [KernelFlume](catalog.md#kernelflume), [PEARL](catalog.md#pearl), [TriInfer](catalog.md#triinfer), [EAServe](catalog.md#easerve) | Preserve job/turn dependencies, cache lifetimes, encode cost, and task correctness; report application completion as well as request latency |

## Count Traffic on the Resource That Actually Carries It

For a communication or storage resource `e`, a useful capacity check is
`rho_e = handoffs_per_second_e × mean_bytes_per_handoff_e / achieved_bytes_per_second_e`.
Routing, cache hits, pooling, batching, and placement change both the traffic
rate and the bytes. One nominal fabric-bandwidth figure cannot characterize all
NICs, links, storage servers, or shared paths.

For direct PD, separate initial transfer/setup from overlap with prefill or the
first generated token. For operator splits, include both directions and repeated
layer/step cadence. A shared-state view instead needs visibility, remote-access,
and ownership accounting. Full-duplex paths and a single shared half-duplex
resource imply different pipeline bounds.

The expression is a capacity diagnostic, not a tail-latency predictor. Include
queueing, contention, synchronization, and uncertainty before claiming an SLO.

## Keep Search Cost and Serving Cost Separate

A configuration search can spend GPU time, energy, and failed trials before it
returns a plan. Report that budget separately from the serving cost of the
selected frozen configuration. Compare predictors/search policies under the
same measurement budget and validate feasibility on disjoint requests.

[TokenPowerSandbox](catalog.md#tokenpowersandbox) is a scoped methodological
reference for metric-specific verification/abstention; its single-GPU validation
does not establish multi-GPU transfer or architecture crossover accuracy.
[TokenPowerBench](catalog.md#tokenpowerbench) supplies measurement context rather
than proof of a disaggregation benefit.

Use [evaluation.md](evaluation.md) for the reporting checklist and
[open-problems.md](open-problems.md) for broader questions.
