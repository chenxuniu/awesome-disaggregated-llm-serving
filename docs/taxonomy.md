# Taxonomy

Disaggregated LLM serving is best understood as a design space, not a single
architecture. This repo uses four axes.

The matrix is a coarse reading orientation. Deployment topology and adaptation
mechanisms are configuration-specific; use each source before treating an entry
as an implementation specification.

## Axis 1: What Is Split

| Split type | Meaning | Representative systems |
|---|---|---|
| Phase split | Prefill and decode run on separate resources | Splitwise, DistServe, Mooncake, P/D-Serve |
| Operator split | Attention and FFN or experts run on separate resources | MegaScale-Infer, Step-3, JANUS, FinDEP |
| State split | KV cache is stored, transferred, or pooled separately from compute | Mooncake, MemServe, LMCache, CacheGen |
| Expert split | MoE experts are sharded, replicated, or migrated independently | DeepEP, Tutel, DeepSpeed-MoE, Lina |
| Logical / temporal split | Chunking, multiplexing, or changing sharding on the same resources | SARATHI, TaiChi, MuxWise, Nexus, Helix |
| Multimodal stage split | Encode and other stages are independently placed | EPD, vLLM-Omni, EAServe |

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
| Static / offline provisioned | Ratio or placement is selected before serving | MegaScale-Infer, Splitwise, AFD-Ledger |
| Per request | Router chooses a pool by request features | Mooncake-style policy, adaptive serving designs |
| Per phase / pool role | Scheduling or running-worker roles adapt | P/D-Serve, TaiChi, DynaServe, FluidPD |
| Per expert | Expert placement or dispatch adapts by load | JANUS, FinDEP, DeepEP-related systems |
| Elastic | Membership, worker roles, or placement change during service | LoongServe, FluidPD |

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
| DeepSeek-V3 / DeepEP | Expert | Intra- and inter-node | Expert dispatch/combine | Runtime/configuration-specific |
| Helix | KV / temporal operator sharding | Supported GPU group | Attention KV parallelism, then FFN TP/EP | Per operator |
| FluidPD | Phase / worker role | Worker pools | Bounded prefill offload + role reassignment | Adaptive |
| vLLM-Omni | Multimodal stage graph | Independently placed engines | Stage connectors | Stage-specific |

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


## Distinctions That Prevent Misclassification

- **PD versus AFD:** PD moves prompt state at a phase boundary; AFD repeatedly
  exchanges activations between attention and FFN/expert sides. Their critical
  communication paths differ.
- **EP versus DEP/AFD:** sharding experts and using all-to-all communication does
  not by itself establish physically separate attention and expert pools.
- **Cache reuse versus state disaggregation:** local prefix reuse, remote reuse,
  CPU offload, and a distributed KV store are different placements/policies.
- **Spatial versus temporal separation:** Helix reuses GPUs with different
  attention/FFN sharding; do not label it as dedicated spatial AFD pools.
- **EPD versus text-only PD:** encoder computation, embeddings, modality mix, and
  stage graph dependencies require additional resource and latency accounting.
- **Runtime versus transport:** NIXL, Mooncake Transfer Engine, StepMesh, and
  DeepEP expose different communication/state primitives; a library alone does
  not specify routing, provisioning, or admission policy.

These are editorial classification rules grounded in the linked works. See the
[complete catalog](catalog.md), [systems directory](systems.md), and
[evaluation guide](evaluation.md) for sources and deployment boundaries.

## Boundary-First Extension from the Survey

The [boundary guide](boundary-guide.md) expands this map into capacity,
interface/state ownership, and independent control tests, plus five descriptive
planes. It separates structural qualification from progress, runtime role
scaling, and failure/recovery evidence. A missing report is distinct from an
explicitly absent property.

Operator subtypes now have explicit reading paths: full-attention, core-attention,
borrowed-attention, and expert-service. Composite PD × AFD systems form a separate
[category](catalog.md#composite). The survey-derived discovery layer uses seven
boundary/comparison classes and remains [separate from curated judgments](discovery.md).
