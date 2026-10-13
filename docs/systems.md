# Systems and Artifacts You Can Use

Documentation/source snapshot checked **2026-10-13**. This directory identifies
integration starting points; no GPU deployment was reproduced during this review.
Pin a release or commit before using an example. Current software can differ
substantially from the implementation evaluated in its original paper.

## Serving Runtimes and Distributed Frameworks

| Project | Role | Official entry point | What to verify |
|---|---|---|---|
| [vLLM](https://github.com/vllm-project/vllm) | Engine and KV-connector interface for PD | [Disaggregated prefilling](https://docs.vllm.ai/en/latest/features/disagg_prefill/) | Experimental feature; check connector, model, KV layout, and parallelism compatibility |
| [SGLang](https://github.com/sgl-project/sglang) | Engine plus documented P/D roles and routing | [PD guide](https://docs.sglang.io/docs/advanced_features/pd_disaggregation) | Select a supported transfer backend; verify router and engine versions together |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | NVIDIA inference runtime with disaggregated serving | [Serving guide](https://nvidia.github.io/TensorRT-LLM/features/disagg-serving.html) | Supported model, GPU, precision, and feature combinations |
| [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo) | Distributed control/deployment layer over inference backends | [Local PD workflow](https://docs.nvidia.com/dynamo/v1.5.1/cli/disaggregated-serving/overview) | Frontend, independent workers, backend dependencies, NIXL, and GPU placement |
| [llm-d](https://github.com/llm-d/llm-d) | Kubernetes inference stack and routing/deployment recipes | [Well-lit paths](https://llm-d.ai/docs/well-lit-paths) | Kubernetes prerequisites, backend/transport versions, and the recipe's tested configuration |
| [vLLM-Omni](https://github.com/vllm-project/vllm-omni) | Multimodal stage graph and disaggregated execution | [Project and examples](https://github.com/vllm-project/vllm-omni) | Stage-specific resources, inter-stage connectors, and modality-specific metrics |

These are different layers. Dynamo and llm-d assemble distributed services;
vLLM, SGLang, and TensorRT-LLM execute models. Selecting a framework does not
remove the need to validate its engine and transfer backend.

## Cache and Communication Layers

| Project | Transfers or manages | Source | Boundary |
|---|---|---|---|
| [Mooncake](https://github.com/kvcache-ai/Mooncake) | KV cache, distributed storage, and inference data transfer | [Project documentation](https://github.com/kvcache-ai/Mooncake) | Transfer Engine and Store are components; an integration is needed for end-to-end scheduling |
| [NIXL](https://github.com/ai-dynamo/nixl) | Inference data across transport/storage plugins | [Build and backend guide](https://github.com/ai-dynamo/nixl) | Transfer layer, not a serving engine or cache-aware scheduler |
| [LMCache](https://github.com/LMCache/LMCache) | KV reuse and cache storage across serving integrations | [Documentation](https://docs.lmcache.ai/) | Check engine/connector compatibility; reuse/offload and physical PD are separate features |
| [StepMesh](https://github.com/stepfun-ai/StepMesh) | Attention/FFN-side communication | [Source and README](https://github.com/stepfun-ai/StepMesh) | AFD communication library, not the full Step-3 serving system |
| [DeepEP](https://github.com/deepseek-ai/DeepEP) | MoE expert dispatch/combine | [Requirements and examples](https://github.com/deepseek-ai/DeepEP) | EP communication alone does not imply attention/FFN worker separation |

**KV handoff and AFD activation exchange are different workloads.** PD generally
hands off prompt state at a phase boundary; AFD exchanges activations repeatedly
across transformer layers. A transfer benchmark for one cannot substitute for
end-to-end evaluation of the other.

For DeepEP in particular, distinguish the release used by a paper from current
main. The present README describes a revised API/backend and removed legacy V1
interfaces. Use the dependency requirements of the chosen release rather than
mixing old setup recipes with current APIs. [Primary source](https://github.com/deepseek-ai/DeepEP).

## Research Implementations and Evaluation Tools

- [DistServe](https://github.com/LLMServe/DistServe): foundational PD research
  implementation; begin with the paper's configuration and artifact instructions.
- [Llumnix](https://github.com/llumnix-project/llumnix-ray): multi-instance scheduling
  and migration. The author-linked AlibabaPAI URL redirects here; check the branch
  corresponding to the result you want to reproduce.
- [Sarathi-Serve](https://github.com/microsoft/sarathi-serve): chunked-prefill baseline
  with paper experiments. Its README calls it a research prototype with limited
  feature parity relative to vLLM.
- [LoongServe](https://github.com/LoongServe/LoongServe): long-context elastic sequence
  parallelism with an artifact evaluation guide.
- [DéjàVu](https://github.com/msr-fiddle/dejavu): streaming, prompt/token
  separation, and fault-tolerance artifact built on FasterTransformer.
- [EPDServe](https://github.com/vbdi/epdserve): ICML 2025 encode–prefill–decode artifact;
  distinguish it from the separate Ascend EPD-Serve preprint.
- [CacheGen](https://github.com/UChi-JCL/CacheGen): KV compression/streaming artifact;
  evaluate quality and compute overhead as well as transfer savings.
- [Vidur](https://github.com/microsoft/vidur): profiled serving simulator and
  configuration exploration. Extending to new models/hardware requires profiles;
  AFD support must be established explicitly.
- [AIPerf](https://github.com/ai-dynamo/aiperf): load generation and client metrics;
  its [BurstGPT tutorial](https://github.com/ai-dynamo/aiperf/blob/main/docs/tutorials/burst-gpt-trace.md)
  documents length-based trace replay.

For workload sources and a comparison protocol, continue to [evaluation.md](evaluation.md).
