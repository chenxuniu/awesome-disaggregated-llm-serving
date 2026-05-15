# Timeline

This timeline is selective. It emphasizes papers that shape disaggregated LLM
serving rather than every efficient inference paper.

## Before 2022: Foundations

- GShard: conditional computation and automatic sharding.
- Switch Transformer: sparse expert routing at scale.

## 2022: Serving And MoE Systems Mature

- Orca: iteration-level scheduling and continuous batching.
- DeepSpeed-MoE: MoE inference and training system substrate.

## 2023: Modern LLM Serving Runtime

- vLLM: PagedAttention and KV-cache memory management.
- SARATHI: chunked prefill as a strong co-located baseline.
- Tutel, Lina, FastMoE: MoE system substrate.

## 2024: PD Disaggregation Becomes A Mainstream Systems Topic

- Splitwise: phase splitting and heterogeneous hardware motivation.
- DistServe: goodput-optimized PD disaggregation.
- Mooncake: KVCache-centric disaggregated serving and traces.
- Sarathi-Serve: production-style chunked prefill baseline.
- P/D-Serve, LoongServe, DejaVu, Llumnix: scaling, long-context, fault
  tolerance, and dynamic scheduling directions.
- DeepSeek-V3: production-scale MoE deployment reference.

## 2025: AFD And Re-Aggregation Both Accelerate

- MegaScale-Infer: foundational AFD/DEP system.
- Adrenaline: partial attention disaggregation.
- Step-3 and StepMesh: model-system AFD co-design and open communication
  library.
- JANUS and FinDEP: newer attention/expert and fine-grained DEP systems.
- TaiChi, MuxWise, Nexus: stronger re-aggregation and multiplexing baselines.
- FlowKV, LMCache, CacheBlend, Pensieve: KV transfer and reuse become a
  central serving layer.

## 2026: Theory And Boundaries

- Analytical Provisioning for AFD: closed-form A/F ratio under stochastic
  workloads.
- Revealing the Challenges of AFD: communication roofline, dead zone, and
  imbalance limits.
- Energy and hardware studies: disaggregation is increasingly evaluated by
  performance, TCO, and energy rather than throughput alone.

