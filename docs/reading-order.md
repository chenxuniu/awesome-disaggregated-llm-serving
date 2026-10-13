# Reading Paths

All entries link to [the catalog](catalog.md), which contains the primary source,
associated artifact, contribution, and scope. These paths are editorial choices.

## 30 Minutes: Understand the Main Tradeoff

Read abstracts and system diagrams rather than complete papers.

1. [DistServe](catalog.md#distserve): separate phases and optimize SLO-constrained goodput.
2. [Mooncake](catalog.md#mooncake): make KV state and reuse central to placement.
3. [MegaScale-Infer](catalog.md#megascale-infer): separate attention and expert computation.
4. [AFD challenges](catalog.md#afd-challenges): inspect communication and imbalance limits.
5. [Sarathi-Serve](catalog.md#sarathi-serve) or [TaiChi](catalog.md#taichi): understand a strong alternative.

The question to retain is when specialization and interference reduction repay
transfer, synchronization, and reserved-capacity costs.

## One Day: Foundations and Comparisons

1. [Orca](catalog.md#orca) and [vLLM](catalog.md#vllm): scheduling and KV memory.
2. [Splitwise](catalog.md#splitwise) and [DistServe](catalog.md#distserve): phase splitting.
3. [Mooncake](catalog.md#mooncake): cache-centric architecture.
4. [Sarathi-Serve](catalog.md#sarathi-serve): tune the colocated baseline.
5. [MegaScale-Infer](catalog.md#megascale-infer) and [Step-3](catalog.md#step3): operator/expert separation.
6. [AFD provisioning](catalog.md#analytical-afd) and [AFD challenges](catalog.md#afd-challenges): ratios and limits.
7. [AFD-Ledger](catalog.md#afd-ledger): compare independently provisioned architectures.

Skim methods and evaluation assumptions before reading all implementation details.

## Write Related Work

- **Foundations:** [Orca](catalog.md#orca), [vLLM](catalog.md#vllm), [SGLang](catalog.md#sglang).
- **PD:** [Splitwise](catalog.md#splitwise), [DistServe](catalog.md#distserve),
  [P/D-Serve](catalog.md#pdserve), [Libra / DynaServe](catalog.md#dynaserve), [FluidPD](catalog.md#fluidpd).
- **State:** [Mooncake](catalog.md#mooncake), [MemServe](catalog.md#memserve),
  [CacheGen](catalog.md#cachegen), [LMCache](catalog.md#lmcache), [FlowKV](catalog.md#flowkv).
- **AFD/DEP:** [MegaScale-Infer](catalog.md#megascale-infer), [Step-3](catalog.md#step3),
  [JANUS](catalog.md#janus-afd), [FinDEP](catalog.md#findep), [Adrenaline](catalog.md#adrenaline).
- **Boundaries/provisioning:** [AFD challenges](catalog.md#afd-challenges),
  [How Far Can Disaggregation Go?](catalog.md#afd-design-space), [AFD-Ledger](catalog.md#afd-ledger).
- **Alternatives:** [Sarathi-Serve](catalog.md#sarathi-serve), [TaiChi](catalog.md#taichi),
  [MuxWise](catalog.md#muxwise), [Nexus](catalog.md#nexus), [Helix](catalog.md#helix-parallelism).
- **Multimodal:** [EPD](catalog.md#epd-disaggregation), [vLLM-Omni](catalog.md#vllm-omni),
  [EAServe](catalog.md#easerve).
- **Hardware/power:** [Mélange](catalog.md#melange), [SQD](catalog.md#sqd),
  [power-aware provisioning](catalog.md#power-provisioning-pd), [DQ](catalog.md#disaggregated-quantization).

Select work that addresses your actual split and objective. A transfer library,
a deployed runtime, and a paper are different kinds of evidence.

## Build or Evaluate a PD Service

1. [Practical guide](practical-guide.md) and [systems directory](systems.md).
2. The official engine/connector/router guide for a pinned release.
3. [DistServe](catalog.md#distserve), [Mooncake](catalog.md#mooncake), and [Sarathi-Serve](catalog.md#sarathi-serve).
4. [Libra / DynaServe](catalog.md#dynaserve), [prefill deflection](catalog.md#prefill-deflection), and [FluidPD](catalog.md#fluidpd).
5. [Evaluation protocol](evaluation.md) and [BurstGPT](catalog.md#burstgpt).

## Build or Evaluate AFD

1. [MegaScale-Infer](catalog.md#megascale-infer) and [Step-3](catalog.md#step3).
2. [StepMesh](catalog.md#stepmesh) and [DeepEP](catalog.md#deepep), checking their distinct roles.
3. [AFD provisioning](catalog.md#analytical-afd), [AFD challenges](catalog.md#afd-challenges), and [AFD-Ledger](catalog.md#afd-ledger).
4. [Helix](catalog.md#helix-parallelism) for the long-context temporal alternative.
5. [Evaluation protocol](evaluation.md), especially equal-budget provisioning and communication accounting.

## Choose a Research Question

Use [research questions](open-problems.md) after identifying an existing mechanism
and its evaluation boundaries. Read the nearest recent work before calling a
direction unexplored. The [timeline](timeline.md) helps locate newer anchors.

## Recent-Mechanism Update Route

1. [Canonical versions](latest-updates.md): Libra, extended Frontier, and historical aliases.
2. [Boundary guide](boundary-guide.md): four operator subtypes and separate operational evidence.
3. [FastAFD](catalog.md#fastafd) and [vLLM AFD Plugin](catalog.md#vllm-afd-plugin): implementation paths.
4. [OpScale](catalog.md#opscale), [OpWeave](catalog.md#opweave), and [AFORE](catalog.md#afore): adaptable operator/expert placement.
5. [AFlex](catalog.md#aflex), [ECO](catalog.md#eco), and [PowerSlider](catalog.md#powerslider): energy/power decisions.
6. [Research map](research-map.md): match the proposed mechanism to current baselines.
