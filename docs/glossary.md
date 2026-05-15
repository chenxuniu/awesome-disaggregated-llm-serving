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

Time To First Token. A latency metric dominated by prefill and queueing.

## TPOT

Time Per Output Token. A decode latency metric.

## Goodput

Throughput that satisfies an SLO, rather than raw throughput.

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

