# Awesome AFD and Disaggregated LLM Serving

A curated map of papers, systems, datasets, and open problems around
disaggregated large language model serving.

This repository focuses on:

- Attention-FFN Disaggregation (AFD) and Disaggregated Expert Parallelism (DEP)
- Prefill-Decode (PD) disaggregation
- KV-cache transfer, storage, and reuse
- Mixture-of-Experts (MoE) serving substrates
- Re-aggregation baselines such as chunked prefill and PD multiplexing
- Hardware, interconnect, and energy implications

The goal is not to collect every LLM inference paper. The goal is to help
readers understand where each paper sits in the disaggregated serving design
space, what problem it solves, and what it leaves open.

## Start Here

| Topic | Best first paper | Why it matters |
|---|---|---|
| PD disaggregation | DistServe | Canonical prefill/decode split with goodput/SLO framing |
| Phase splitting | Splitwise | Early cost and heterogeneous-hardware argument |
| KV-centric disaggregation | Mooncake | Production-scale KV-cache pool and open traces |
| AFD / DEP | MegaScale-Infer | Foundational attention/FFN and expert disaggregation system |
| AFD model-system co-design | Step-3 | Production-oriented AFD design with communication library |
| AFD provisioning theory | Analytical Provisioning for AFD | Gives a tractable A/F ratio model |
| AFD limits | Revealing the Challenges of AFD | Explains when AFD hits communication and imbalance limits |
| Re-aggregation baseline | SARATHI / TaiChi | Main counter-argument to physical disaggregation |

## Repository Map

| File | Purpose |
|---|---|
| [papers.yaml](papers.yaml) | Structured paper database |
| [docs/taxonomy.md](docs/taxonomy.md) | Four-axis taxonomy of disaggregated serving |
| [docs/reading-order.md](docs/reading-order.md) | Reading paths for different goals |
| [docs/open-problems.md](docs/open-problems.md) | Research problems that remain open |
| [docs/impact-ranking.md](docs/impact-ranking.md) | Influence map by role, not just citation count |
| [docs/timeline.md](docs/timeline.md) | Chronological map of the field |
| [docs/glossary.md](docs/glossary.md) | Short definitions of terms |
| [scripts/generate_tables.py](scripts/generate_tables.py) | Generates Markdown tables from `papers.yaml` |

## Taxonomy Snapshot

We organize disaggregated LLM serving along four axes:

| Axis | Choices | Examples |
|---|---|---|
| What is split? | Phase, operator, state, model/expert | Splitwise, MegaScale-Infer, Mooncake, DeepEP |
| Where is it split? | Intra-GPU, intra-node, inter-node, rack-scale | Nexus, DistServe, StepMesh, NVL72-class fabrics |
| How is state moved? | Push, pull, pipelined transfer, pooled KV, migration | DistServe, Mooncake, MemServe, Llumnix |
| When is the split decided? | Static, per request, per phase, elastic | MegaScale-Infer, P/D-Serve, JANUS, elastic AFD |

See [docs/taxonomy.md](docs/taxonomy.md) for the full matrix.

## Main Paper Groups

### 1. Prefill-Decode Disaggregation

These systems split compute-heavy prefill from memory-bound decode.

- Splitwise
- DistServe
- Mooncake
- P/D-Serve
- TetriInfer
- MemServe
- LoongServe
- DejaVu
- Llumnix

### 2. Attention-FFN / Expert Disaggregation

These systems push disaggregation inside the transformer layer, separating
attention/KV work from FFN or expert computation.

- MegaScale-Infer
- Step-3
- JANUS
- FinDEP
- Adrenaline
- Analytical Provisioning for AFD
- Revealing the Challenges of AFD
- DeepSeek-V3 / DeepEP

### 3. Re-aggregation and Counter-Baselines

These papers argue that physical disaggregation is not always necessary.
They are essential baselines for any AFD or PD-disaggregation paper.

- SARATHI
- Sarathi-Serve
- TaiChi
- MuxWise
- Nexus

### 4. KV Cache Transfer, Storage, and Reuse

These papers provide the state-management layer that makes disaggregation
practical.

- Mooncake Transfer Engine and Mooncake Store
- CacheGen
- FlowKV
- LMCache
- CachedAttention / AttentionStore
- CacheBlend
- Pensieve
- RAGCache
- Infinite-LLM / DistAttention

### 5. MoE Serving Substrate

AFD depends heavily on expert parallelism, all-to-all communication, and
large-MoE deployment practice.

- DeepSeek-V3
- DeepEP
- Tutel
- DeepSpeed-MoE
- GShard
- Switch Transformer
- FastMoE
- Lina

## How To Use This Repo

- New to the area: read [docs/reading-order.md](docs/reading-order.md).
- Writing related work: start with [papers.yaml](papers.yaml) and
  [docs/taxonomy.md](docs/taxonomy.md).
- Looking for research ideas: read [docs/open-problems.md](docs/open-problems.md).
- Comparing paper impact: read [docs/impact-ranking.md](docs/impact-ranking.md).

## Inclusion Criteria

A paper or system belongs here if it directly studies at least one of:

- LLM serving disaggregation
- Attention/FFN or expert disaggregation
- Prefill/decode split, aggregation, or multiplexing
- KV-cache movement, pooling, migration, compression, or reuse
- MoE inference systems that affect AFD/DEP design
- Hardware, interconnect, or energy constraints for disaggregated serving

General quantization, speculative decoding, or model-compression papers are
included only when they interact with disaggregated serving.

## Related Repositories

- [Awesome LLM Inference](https://github.com/xlite-dev/Awesome-LLM-Inference)
- [Awesome LLM Inference Serving](https://github.com/zenrran4nlp/Awesome-LLM-Inference-Serving)
- [Awesome KV Cache Optimization](https://github.com/jjiantong/Awesome-KV-Cache-Optimization)
- [Awesome MoE Inference](https://github.com/MoE-Inf/awesome-moe-inference)
- [Awesome Mixture of Experts Papers](https://github.com/codecaution/Awesome-Mixture-of-Experts-Papers)

## Contributing

Pull requests are welcome. Please include:

- Paper title, year, venue or preprint status
- Paper link, code link if available, and arXiv ID if available
- One sentence on why the paper matters
- One sentence on its main limitation or relationship to prior work

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full format.

## Citation

If this repository helps your research, please cite the repository using
[CITATION.cff](CITATION.cff).

