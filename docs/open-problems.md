# Research Questions and Existing Progress

These are editorial questions for further investigation as of **2026-10-13**,
not claims of unexplored territory. A promising project must establish the gap
against the latest relevant paper and a tuned baseline.

## 1. Composing Multiple Split Decisions

[AFD provisioning](catalog.md#analytical-afd), [AFD-Ledger](catalog.md#afd-ledger),
and [How Far Can Disaggregation Go?](catalog.md#afd-design-space) provide
analytical/search/design-space anchors. [SQD](catalog.md#sqd) changes the split
boundary for subquadratic attention.

Question: how accurately can a model compare phase, operator, state, and temporal
splits under the same workload, hardware catalog, budget, and joint SLO?
Test prediction/architecture-selection accuracy on held-out live deployments;
separate simulator agreement from real-system validation.

## 2. Elasticity Across Time Scales

[LoongServe](catalog.md#loongserve), [Llumnix](catalog.md#llumnix),
[DynaServe](catalog.md#dynaserve), [prefill deflection](catalog.md#prefill-deflection),
and [FluidPD](catalog.md#fluidpd) already address forms of migration, load
balancing, offload, or role adaptation. Elastic PD is not an empty field.

Question: how should transient offload, sustained role changes, and resource
scaling interact with operator-level AFD and expert placement? Measure adaptation
latency, migration cost, oscillation, memory constraints, and decode-tail protection
under changing input/output ratios rather than only stationary throughput.

## 3. Placement with Fabric Congestion and Expert Skew

[MegaScale-Infer](catalog.md#megascale-infer), [AFD challenges](catalog.md#afd-challenges),
[StepMesh](catalog.md#stepmesh), and [NetKV](catalog.md#netkv) expose different
communication/placement concerns. NetKV's routing evidence is simulation-based;
PD network routing and repeated AFD activation exchange are distinct mechanisms.

Question: can topology-aware placement and routing preserve SLOs when expert skew,
contention, and stale telemetry occur together? Evaluate crossovers against a
tuned colocated/PD-only design on the target network.

## 4. Pipeline Robustness Under Jitter

[FinDEP](catalog.md#findep), [JANUS](catalog.md#janus-afd), and
[Helix](catalog.md#helix-parallelism) offer scheduling/overlap comparison points.

Question: which synchronization and overlap mechanisms tolerate kernel, CPU,
network, and expert-routing jitter without wasting attention-side or expert-side
capacity? Include deliberately disturbed and failure-recovery conditions, and
report per-token stalls rather than only average batch throughput.

## 5. Fair Architecture Comparisons

[Sarathi-Serve](catalog.md#sarathi-serve), [TaiChi](catalog.md#taichi),
[MuxWise](catalog.md#muxwise), [Nexus](catalog.md#nexus), and
[AFD-Ledger](catalog.md#afd-ledger) challenge simple split-versus-unsplit claims.

Question: how do winning regimes change when both architectures receive equal
tuning effort, compatible precision, cache policies, and hardware budgets?
Distinguish equal GPU count, equal purchase/cloud cost, and equal power.

## 6. State Ownership and Shared-Cache Isolation

[Mooncake](catalog.md#mooncake), [MemServe](catalog.md#memserve),
[LMCache](catalog.md#lmcache), and [Pensieve](catalog.md#pensieve) provide state
management anchors.

Question: what are the performance and correctness costs of tenant namespaces,
cache consistency, eviction, cancellation, and failure recovery in shared KV
pools? Investigate actual reuse/ownership semantics before asserting an isolation
gap or vulnerability in a named system.

## 7. Long-Context, Agentic, and Multimodal Units of Work

[Helix](catalog.md#helix-parallelism), [LoongServe](catalog.md#loongserve),
[vLLM-Omni](catalog.md#vllm-omni), [EPD](catalog.md#epd-disaggregation), and
[EAServe](catalog.md#easerve) expand the workload and stage design space.

Question: should scheduling and cache placement optimize requests, turns, or
whole application jobs? Publish dependencies, cache lifetime, encoder utilization,
and task-completion metrics so faster individual generations can be related to
actual application completion.

## 8. Heterogeneity and Phase-Specific Precision

[Splitwise](catalog.md#splitwise), [Mélange](catalog.md#melange),
[multi-vendor PD](catalog.md#multi-vendor-pd), [AFD-Ledger](catalog.md#afd-ledger),
and [disaggregated quantization](catalog.md#disaggregated-quantization) are anchors.

Question: when do role-specific hardware and precision gains survive compatible
state transfer, duplicate weights, pricing, and availability constraints? Compare
allocation policies independently of the precision/accuracy changes they enable.

## 9. Power-Aware Control Beyond Static Provisioning

[Energy implications](catalog.md#energy-disagg), [SQD](catalog.md#sqd), and
[power-aware PD provisioning](catalog.md#power-provisioning-pd) already study
energy or power-related decisions.

Question: can online power capping/DVFS and pool adaptation improve joules per
SLO-compliant completion under a fleet power limit? Include host/network/idle
energy where relevant, adaptation overhead, and tail latency. Analytical Pareto
fronts alone do not establish safe online control.

## 10. Reusable Evaluation with Explicit Evidence Boundaries

[BurstGPT](catalog.md#burstgpt), Mooncake's traces, [Vidur](catalog.md#vidur),
[Frontier](catalog.md#frontier), and [AIPerf](catalog.md#aiperf) supply parts of the
measurement stack.

Question: can one reproducible suite expose phase ratios, prefix reuse, expert
skew, congestion, failures, power, and application dependencies without conflating
measured, simulated, and analytical results? Start with [evaluation.md](evaluation.md)
and release raw timing plus the exact configuration used for every result.
