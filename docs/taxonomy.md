# Taxonomy

Disaggregated LLM serving is best understood as a design space, not a single
architecture. This repo uses four axes.

## Axis 1: What Is Split

| Split type | Meaning | Representative systems |
|---|---|---|
| Phase split | Prefill and decode run on separate resources | Splitwise, DistServe, Mooncake, P/D-Serve |
| Operator split | Attention and FFN or experts run on separate resources | MegaScale-Infer, Step-3, JANUS, FinDEP |
| State split | KV cache is stored, transferred, or pooled separately from compute | Mooncake, MemServe, LMCache, CacheGen |
| Expert split | MoE experts are sharded, replicated, or migrated independently | DeepEP, Tutel, DeepSpeed-MoE, Lina |
| Logical split | Work is interleaved without physical separation | SARATHI, TaiChi, MuxWise, Nexus |

## Axis 2: Where The Split Is Realized

| Location | Why it matters | Examples |
|---|---|---|
| Intra-GPU | Avoids network transfer but competes for device-local resources | Nexus |
| Intra-node | Uses NVLink/NVSwitch-class bandwidth and low latency | Some PD and MoE deployments |
| Inter-node | Requires RDMA, careful pipelining, and topology-aware placement | DistServe, Mooncake, MegaScale-Infer |
| Rack-scale | Makes fabric topology a first-order design variable | Step-3, NVL72-class deployments |

## Axis 3: How State Is Moved

| Mechanism | Description | Examples |
|---|---|---|
| Push | Producer sends state to consumer | Splitwise, DistServe |
| Pull | Consumer requests state when needed | Some KV-store designs |
| Layer-pipelined transfer | State is transferred progressively by layer or chunk | Splitwise optimized variant, TetriInfer |
| Pooled KV | KV cache lives in a distributed pool | Mooncake, MemServe, LMCache |
| Migration | Request or cache state moves between workers | Llumnix |
| Bipartite activation exchange | Attention-side and FFN-side workers exchange activations | StepMesh, MegaScale-Infer-style AFD |

## Axis 4: When The Split Is Decided

| Timing | Description | Examples |
|---|---|---|
| Static | Deployment-time ratio or placement | MegaScale-Infer, Splitwise |
| Per request | Router chooses a pool by request features | Mooncake-style policy, adaptive serving designs |
| Per phase | Prefill/decode role or scheduling changes by phase | P/D-Serve, TaiChi |
| Per expert | Expert placement or dispatch adapts by load | JANUS, FinDEP, DeepEP-related systems |
| Elastic | Membership and placement can change while service remains live | Elastic AFD proposals, LoongServe-style elasticity |

## Representative Matrix

| System | What | Where | How | When |
|---|---|---|---|---|
| Splitwise | Phase | Inter-node | Push / pipelined push | Static |
| DistServe | Phase | Inter-node | Push | Static |
| Mooncake | Phase + state | Inter-node | KV pool / transfer engine | Dynamic |
| MemServe | State | Inter-node | Elastic memory pool | Dynamic |
| LoongServe | Phase + sequence | Inter-node | Elastic sequence parallelism | Dynamic |
| Llumnix | Phase / request | Inter-node | Migration | Dynamic |
| Nexus | Phase | Intra-GPU | Logical partition | Dynamic |
| SARATHI | None physical | Co-located | Chunked prefill | Dynamic batching |
| TaiChi | Phase | Co-located or disaggregated | Unified aggregation/disaggregation | Dynamic |
| MegaScale-Infer | Operator + expert | Inter-node | Activation exchange | Static |
| Step-3 / StepMesh | Operator + expert | Inter-node | Bipartite RDMA communication | Static / system-specific |
| JANUS | Operator + expert | Inter-node | Activation and expert exchange | Dynamic components |
| FinDEP | Expert / operator | Inter-node | Fine-grained DEP scheduling | Dynamic components |
| DeepSeek-V3 / DeepEP | Expert | Intra- and inter-node | All-to-all expert communication | Static deployment |

## How To Read The Space

Three tensions show up repeatedly:

1. Disaggregation improves specialization but creates transfer cost.
2. Static provisioning is simple but fragile under mixed workloads.
3. Re-aggregation systems can match disaggregation when interference is low
   and workload shape is stable.

For AFD specifically, the central question is:

> When does separating attention-side state-heavy work from FFN/expert
> compute-heavy work beat a strong co-located or re-aggregated baseline?

That question requires both systems measurement and a theory of the hardware,
model, traffic, and fabric regime.

