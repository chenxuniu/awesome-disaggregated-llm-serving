# Impact Ranking

This page is an editorial map, not an automated citation ranking. Citation
counts move slowly and can undercount new systems papers. The labels below
reflect reading roles and curator judgment, not measured adoption or scientific
quality. Recent preprints are not assigned influence from unverified citation
counts. The same work may serve more than one comparison role.

## Tier 1: Required Foundations

| Work | Role |
|---|---|
| Orca | Iteration-level scheduling and continuous batching foundation |
| vLLM / PagedAttention | Modern KV-cache memory management baseline |
| Splitwise | Early phase-splitting and heterogeneous-hardware case |
| DistServe | Canonical goodput-optimized PD disaggregation system |
| Mooncake | Production KV-centric disaggregation and open traces |
| MegaScale-Infer | Foundational AFD / DEP system |
| SARATHI / Sarathi-Serve | Strong co-located re-aggregation baseline |

## Tier 2: AFD-Specific Core

| Work | Role |
|---|---|
| Step-3 | AFD model-system co-design |
| StepMesh | AFD-specific low-latency communication substrate |
| JANUS | Newer attention/expert disaggregation design |
| FinDEP | Fine-grained scheduling for DEP |
| Analytical Provisioning for AFD | A/F provisioning theory |
| Revealing the Challenges of AFD | Boundary and dead-zone analysis |

## Tier 3: Counter-Baselines

| Work | Role |
|---|---|
| TaiChi | Unifies PD aggregation and disaggregation |
| MuxWise | Prefill-decode multiplexing as an alternative |
| Nexus | Intra-GPU PD disaggregation |
| Beyond the Buzz | Pragmatic skepticism about disaggregation wins |

## Tier 4: Substrate Papers

| Work | Role |
|---|---|
| DeepSeek-V3 / DeepEP | Production MoE and expert-parallel communication reference |
| Tutel | MoE execution substrate |
| DeepSpeed-MoE | Early large-scale MoE inference/training substrate |
| Lina | Distributed MoE communication optimization |
| FlowKV | Low-latency KV transfer |
| CacheGen | KV compression and streaming |
| LMCache | KV-cache layer for serving |
| CachedAttention / Pensieve | Stateful and multi-turn serving |

## How To Interpret Impact

For this field, impact has several forms:

- Conceptual impact: introduced a design vocabulary.
- Systems impact: shipped or influenced a runnable serving stack.
- Baseline impact: became a comparison every new paper must address.
- Boundary impact: clarified when a popular design does not work.
- Substrate impact: enabled later systems through communication, caching, or
  scheduling mechanisms.

AFD papers should be judged against all five forms, not citations alone.


## Recent Comparison Anchors

These additions matter for current coverage; this is not a claim that they have
accumulated the same influence as the earlier foundations.

- [Libra / DynaServe](catalog.md#dynaserve), [prefill deflection](catalog.md#prefill-deflection),
  and [FluidPD](catalog.md#fluidpd): compare elasticity and slack use before
  presenting adaptive PD as a new topic.
- [Helix](catalog.md#helix-parallelism): temporal attention/FFN sharding alternative
  for long-context interactive decode.
- [How Far Can Disaggregation Go?](catalog.md#afd-design-space) and
  [AFD-Ledger](catalog.md#afd-ledger): design-space and matched-budget provisioning anchors.
- [SQD](catalog.md#sqd) and [power-aware PD provisioning](catalog.md#power-provisioning-pd):
  architectural and power constraints on split decisions.
- [EPD](catalog.md#epd-disaggregation), [vLLM-Omni](catalog.md#vllm-omni), and
  [EAServe](catalog.md#easerve): multimodal stage comparisons.

Runnable components have a separate [systems directory](systems.md). Being
available as code is an implementation property, not evidence of research impact.
