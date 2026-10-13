# Evaluation: Workloads, Baselines, and Metrics

This is a proposed comparison protocol, not an established community standard.
Use it to make the assumptions behind a disaggregation result visible.

## Workload Sources

| Source | Direct entry point | What it can test | What it does not establish |
|---|---|---|---|
| Mooncake trace | [Official FAST25 trace](https://github.com/kvcache-ai/Mooncake/blob/main/FAST25-release/arxiv-trace/mooncake_trace.jsonl) | Request arrival/length and cache-related workload structure described by the release | Verify the schema and supplied cache identifiers; do not infer semantic prompt content or a production network |
| BurstGPT | [Official data and schema](https://github.com/HPMLL/BurstGPT) | Real request arrivals, input/output lengths, burstiness, and session metadata where present | Elapsed time is end-to-end time, not TTFT; original prompts are not provided |
| Synthetic workload | Your published generator and seeds | Controlled input/output ratio, load, bursts, prefix overlap, and expert-skew sensitivity | Realistic correlations and application quality need separate validation |
| Application replay | Publish the permitted trace/schema and replay method | Tool dependencies, multi-turn state, job-level completion, and modality-specific stages | Request-level throughput alone does not measure completion of an agent task |

For BurstGPT, record the release and whether the file includes failures. Explain
any exclusion of zero-output requests. [Official dataset description](https://github.com/HPMLL/BurstGPT).

Preserve the joint input/output length distribution and arrival timestamps when
possible. Scaling request rate, resampling lengths, or generating replacement
prompts changes the workload and must be described. A prefix-heavy test needs
actual reusable prefixes or a documented synthetic construction.

[AIPerf's BurstGPT replay](https://github.com/ai-dynamo/aiperf/blob/main/docs/tutorials/burst-gpt-trace.md)
synthesizes prompts from token counts. This is useful for load/length experiments,
but does not recreate the original semantic prefixes or conversation dependencies.

## Measurement Tools

- [vLLM benchmark CLI](https://docs.vllm.ai/en/latest/cli/bench/serve/): online
  serving benchmarking; use options supported by the installed release.
- [AIPerf](https://github.com/ai-dynamo/aiperf): client-side load generation,
  latency reporting, and trace replay.
- [Vidur](https://github.com/microsoft/vidur): calibrated operator-based simulation.
  Record profiles and supported model/device configurations; add and validate any
  AFD/network model rather than assuming it is already present.
- [Frontier](https://arxiv.org/abs/2508.03148): simulation research for future serving
  designs; treat simulator evidence separately from live deployment results.

Do not combine client queueing, server queueing, and GPU execution into a single
unexplained latency. Document the timestamp boundaries of each measurement.

## Minimum Baseline Set

1. **Tuned colocated serving:** continuous batching, chunked prefill, and an
   explicit cache policy using the same model, precision, and total GPUs.
2. **Static PD:** search several prefill/decode pool ratios; allow different
   supported parallelism choices and include transfer/router overhead.
3. **Adaptive or unified PD:** compare relevant mechanisms in
   [DynaServe](catalog.md#dynaserve), [TaiChi](catalog.md#taichi),
   [prefill deflection](catalog.md#prefill-deflection), and [FluidPD](catalog.md#fluidpd).
4. **For AFD:** compare a tuned colocated MoE deployment, PD-only deployment,
   and an AFD allocation search. In long-context low-latency regimes, evaluate
   [Helix](catalog.md#helix-parallelism) if the chosen platform supports it.
5. **For KV reuse/transfer:** hold cache semantics constant, then compare
   no reuse, local reuse, remote reuse, and transfer policies. Lossy methods
   also require task quality measurements.
6. **For EPD:** compare encode+prefill colocation with the stage split under
   identical modalities and encoder/decoder resource accounting.

Separate **equal resource** comparisons from **equal cost** comparisons. Count
routers, extra weight copies, idle reserved workers, and storage/network resources
where they affect the stated objective. AFD-Ledger provides a useful example of
[joint architecture provisioning](https://arxiv.org/abs/2608.04502).

## Metrics to Report Together

- **TTFT:** client-visible first token, including the stated admission/queueing boundary.
- **TPOT:** per-request mean token interval, typically `(last_token - first_token) / (output_tokens - 1)`.
  One-token outputs have no such interval; state how they are treated.
- **ITL / TBT:** individual token intervals and their tails. A mean TPOT threshold
  and a p99 ITL threshold are different SLOs.
- **End-to-end latency:** request completion; add job completion for multi-step applications.
- **Goodput:** define requests/s or output tokens/s satisfying the specified joint SLO.
  For request goodput, count qualifying requests over a declared measurement interval.
- **SLO attainment:** fraction of offered requests meeting the joint criterion;
  disclose timeouts, rejections, cancellations, and failed transfers in the denominator.
- **Throughput:** input tokens/s, output tokens/s, completed requests/s, and offered requests/s.
- **Communication:** bytes/request, exposed transfer time, bandwidth, congestion,
  and per-layer activation-exchange costs for AFD.
- **Resources:** per-pool utilization, active KV memory, allocation, and idle capacity.
- **Cost/energy:** cost per successful SLO-compliant unit; joules per completed
  request or output token, with GPU/host/network measurement boundaries stated.
- **Quality:** accuracy, perplexity, or task success when KV/weight precision,
  selective transfer, or speculative output behavior changes.

State percentiles per metric. Aggregate means or fleet-wide utilization can hide
an overloaded pool and long individual token stalls.

## Experiment Checklist

- [ ] Exact model/tokenizer revisions, attention architecture, precision, and output limits.
- [ ] Engine/router/connector commits, container digests, and all launch/config files.
- [ ] GPU count/type/memory, CPU/NUMA placement, topology, NICs, and measured transfer bandwidth.
- [ ] Same workload sample, seeds, prefixes, and offered arrival schedule for every baseline.
- [ ] Open-loop offered rate or closed-loop concurrency explicitly identified.
- [ ] Cold/warm cache policy, warm-up, measurement duration, drain behavior, and failures.
- [ ] Load sweep through overload; length-ratio, burstiness, and prefix-reuse sensitivity.
- [ ] Multiple runs with uncertainty and adaptation/migration overhead.
- [ ] Ablations for routing, pool ratio, cache policy, transfer overlap, and role switching.
- [ ] Simulator accuracy on held-out live configurations when simulation supports the conclusion.
- [ ] Raw per-request/per-token data and the script used to derive the figures.

A strong result explains both its winning regime and its crossover or failure regime.
