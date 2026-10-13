# Glossary

## AFD

Attention-FFN Disaggregation. A serving architecture that separates attention
work, which is state-heavy and KV-cache-bound, from FFN or expert work, which
is often compute-heavy and stateless across decode steps.

## DEP

Disaggregated Expert Parallelism. A related term used for MoE systems where
expert computation is separated and scheduled independently from other parts
of the model.

## PD Disaggregation

Prefill-Decode Disaggregation. A serving architecture that runs compute-heavy
prefill and memory-bound decode on separate resources.

## Prefill

The phase where the model processes the input prompt and builds the initial
KV cache. Prefill is usually more compute intensive and parallelizable than
decode.

## Decode

The autoregressive phase where the model generates tokens one by one. Decode
is often memory-bandwidth-bound because it repeatedly reads KV cache.

## KV Cache

Stored keys and values from previous tokens. KV cache avoids recomputing
attention history but grows with sequence length and concurrency.

## TTFT

Time To First Token. State the client/server timestamp boundary. It can include
admission, queueing, encode, prefill, and exposed transfer time. If the prefill
worker emits the first token, handoff can instead appear in the next interval.

## TPOT

Time Per Output Token. Usually the mean interval per request after its first
token: `(last_token - first_token) / (output_tokens - 1)`. One-token requests
have no interval. State whether an implementation uses a different definition.

## Goodput

Throughput of work satisfying a declared SLO. Specify whether the unit is
requests or output tokens and whether TTFT and token-latency conditions must
hold jointly. Failed/rejected requests must be accounted for when reporting
SLO attainment.

## MoE

Mixture of Experts. A model architecture where tokens are routed to a subset
of expert FFN modules.

## Expert Parallelism

Parallel execution strategy that shards or replicates MoE experts across
devices and routes tokens to the right expert workers.

## Re-Aggregation

The counter-camp to physical disaggregation. These systems keep work
co-located but use chunking, multiplexing, or unified scheduling to reduce
interference.

## A/F Ratio

The provisioning ratio between attention-side workers and FFN-side workers in
an AFD system.

## Dead Zone

A regime where adding FFN or expert workers fails to improve utilization
because communication, synchronization, or scale-out bandwidth becomes the
bottleneck.


## ITL / TBT

Inter-Token Latency / Time Between Tokens. Individual streaming token intervals.
A tail ITL metric can reveal stalls hidden by a per-request mean TPOT.

## EPD

Encode-Prefill-Decode disaggregation. Separates multimodal input encoding from
language-model prompt processing and generation.

## GQA / MQA / MLA

Grouped-Query Attention, Multi-Query Attention, and Multi-head Latent Attention.
Different attention representations change KV size, sharding, and transfer
compatibility. A conventional full K/V-head size estimate need not apply to MLA.

## Exposed Transfer Time

Communication time remaining on the request's critical path after overlap with
computation. Total transfer duration and exposed duration are different metrics.

## Open-Loop / Closed-Loop Load

Open-loop load schedules arrivals independently of completions. Closed-loop
load limits concurrent outstanding requests and submits new work as requests
finish. They produce different queueing behavior; identify the load model.

## Prefix Locality

A placement opportunity from reusable prompt prefixes. Routing for locality can
conflict with queue load, transfer cost, or tenant isolation. Token-length-only
replay does not recreate semantic prefix sharing.

## Temporal Attention/FFN Sharding

Reconfigure the same GPU group between attention and FFN/expert computation,
as in Helix. This differs from assigning dedicated spatial A/F worker pools.

See [evaluation.md](evaluation.md) for a consistent measurement protocol and
[the catalog](catalog.md) for sources of the named mechanisms.
