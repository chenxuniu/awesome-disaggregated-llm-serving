# A First Disaggregated Serving Experiment

This guide is a decision and verification workflow. Runtime commands and
compatibility are linked to official documentation checked **2026-10-13**;
the steps below have not been exercised on a GPU cluster in this repository.

## Pick the Experiment That Fits Your Resources

- **One GPU:** establish a colocated baseline with continuous batching and
  chunked prefill. Study interference and cache behavior first; this hardware
  cannot demonstrate separate GPU pools.
- **Two or more suitable GPUs:** start with one prefill and one decode worker,
  a small model that fits each worker, and a supported same-node transport.
  This tests phase handoff before introducing distributed-network effects.
- **Multiple nodes:** add RDMA/transport validation and topology reporting.
  Keep model and load identical while measuring the additional transfer cost.
- **AFD / large MoE:** plan repeated activation exchange, expert routing,
  attention-side KV ownership, and synchronization. StepMesh or DeepEP is a
  component choice; neither is sufficient to assemble a complete AFD service.
- **Multimodal:** account separately for encoder resources and transfers.
  Begin with [EPDServe or vLLM-Omni](systems.md), then compare to a matched
  encode+prefill colocated baseline.

## Choose One Supported Deployment Path

1. **vLLM:** follow the [disaggregated prefilling guide](https://docs.vllm.ai/en/latest/features/disagg_prefill/).
   Select a connector and use that release's paired-worker/proxy example.
2. **SGLang:** follow the [PD guide](https://docs.sglang.io/docs/advanced_features/pd_disaggregation).
   It documents worker roles, a router, and Mooncake/NIXL transport paths.
3. **Dynamo:** after the official installation/container setup, follow the
   [local disaggregated workflow](https://docs.nvidia.com/dynamo/v1.5.1/cli/disaggregated-serving/overview).
   Its preset uses two GPUs and starts frontend plus separate workers. Within a
   compatible Dynamo checkout/environment, the vLLM example entry point is:

   ```bash
   cd examples/backends/vllm
   bash launch/disagg.sh
   ```

4. **TensorRT-LLM:** use its [disaggregated serving guide](https://nvidia.github.io/TensorRT-LLM/features/disagg-serving.html)
   and supported model configurations.
5. **Kubernetes:** choose a tested [llm-d path](https://llm-d.ai/docs/well-lit-paths)
   or [Dynamo deployment guide](https://docs.nvidia.com/dynamo/dev/kubernetes/disaggregated-serving/overview).

Use a single coherent release across the engine, router, connector, and examples.
Record the resolved commits and container digests. Links to `latest`/`main` are
navigation aids, not pinned reproduction environments.

## Establish Correctness Before Throughput

Use identical model/tokenizer revisions and compatible KV layouts. Confirm
precision, block size, attention representation, and any supported differences
in tensor parallelism. A syntactically accepted configuration is insufficient
proof that KV handoff is correct.

Send a short deterministic request through the frontend. Replace the example
model with the served model name and adjust the local port to your deployment:

```bash
curl --no-buffer http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"YOUR_SERVED_MODEL","messages":[{"role":"user","content":"Compute 2 + 3."}],"temperature":0,"max_tokens":32,"stream":true}'
```

Compare the output with a colocated run using the same sampling settings, and
use the connector's official accuracy tests for more than this smoke test.
Inspect worker logs or tracing to confirm that the intended P/D handoff occurred
and that transfer did not silently fall back to another path.

## Measure a Decision, Not Just a Running Service

Use the [evaluation protocol](evaluation.md). Sweep offered load and prompt/output
lengths; include overload and bursts. Keep total GPUs fixed and tune the
colocated baseline as carefully as the split system.

A first report should show:

- TTFT and per-token latency distributions, not only their means.
- Completion/failure rates and requests satisfying the joint SLO.
- Prompt tokens, output tokens, and both phase utilizations.
- Exposed transfer time, transferred bytes, and observed bandwidth.
- Equal-GPU and, where relevant, equal-cost or equal-power comparisons.

The useful outcome is the workload/network regime where the split helps.
A successful KV transfer is an implementation milestone, not a performance conclusion.

## Diagnose the Bottleneck

- **TTFT rises while decode is idle:** separate prefill queueing from prefill
  compute and transfer; inspect the pool ratio and routing. Read
  [prefill deflection](catalog.md#prefill-deflection) and [FluidPD](catalog.md#fluidpd).
- **Time to the second token is large:** identify which worker emits the first
  token and whether KV transfer overlaps prefill/early output.
- **Decode tail latency rises:** inspect admission, batch size, in-flight
  memory, and any prefill offload competing with decode.
- **Throughput is high but SLO attainment is low:** compare goodput at the
  same TTFT and token-latency thresholds instead of peak tokens/s.
- **AFD workers are underutilized:** break down attention, expert skew,
  activation exchange, and synchronization; compare a temporal alternative
  such as [Helix](catalog.md#helix-parallelism) in its supported regime.
- **Cache hit rate looks strong but latency worsens:** measure lookup, storage
  read, transfer, and eviction costs; a hit is not necessarily cheaper than recomputation.
