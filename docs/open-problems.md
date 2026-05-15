# Open Problems

This page records research gaps that appear repeatedly across AFD, PD
disaggregation, KV-cache systems, and MoE serving.

## 1. Unified Theory Of Disaggregation

We do not yet have a portable model that takes model, traffic, hardware,
fabric, and SLOs as input and predicts:

- whether to disaggregate
- which axis to split
- where to place the split
- how to move state
- when to adapt

The AFD provisioning papers are a strong start, but a full theory must compose
phase, operator, expert, and state splits.

## 2. Dynamic A/F Ratio Scheduling

Most AFD systems use a static attention-to-FFN provisioning ratio. Real traffic
mixes short prompts, long-context sessions, tool calls, and bursty agentic
workloads. A static ratio can be badly wrong.

Open question: can a serving system route or resize AFD configurations fast
enough to preserve SLOs while improving goodput?

## 3. Communication-Aware AFD Placement

AFD is only attractive when activation transfer and expert communication are
cheap enough. On standard clusters, network and synchronization overhead can
erase the benefit.

Open question: can we design topology-aware placement and communication
schedules that avoid the AFD dead zone on non-superpod clusters?

## 4. Robust Synchronization Under Jitter

AFD pipelines rely on tight coordination between attention-side and FFN-side
workers. Jitter from kernels, networking, CPU scheduling, and expert skew can
collapse overlap.

Open question: what is the right jitter-tolerant pipeline protocol for AFD?

## 5. Re-Aggregation Baselines

SARATHI, TaiChi, MuxWise, and Nexus show that smart co-location can recover
much of the benefit without paying full disaggregation cost.

Open question: in which regimes does AFD strictly beat the best re-aggregated
baseline, and by how much?

## 6. KV-Cache Pool Isolation

KV-cache pooling improves reuse and elasticity, but it creates multi-tenant
isolation and security questions. Prefix sharing can leak information if the
cache is not tenant-aware.

Open question: what isolation model should a shared KV pool implement, and
what is the tail-latency cost?

## 7. Long-Context And Agentic Workloads

Agentic systems break simple request-level assumptions. A single user task can
create many internal generations, tool calls, and long-lived cache state.

Open question: should the unit of disaggregation be a request, a turn, a
conversation, a tool call, or an agent?

## 8. Heterogeneous Fleet Provisioning

Disaggregation is attractive because different stages want different resources.
But modern GPU lineups do not always provide cleanly separated memory-heavy
and compute-heavy price-performance points.

Open question: can heterogeneous AFD deliver stable cost/performance gains
under real cloud pricing and availability?

## 9. Energy-Proportional Disaggregated Serving

Separate pools create new DVFS and power-capping opportunities. But saving
energy can hurt tail latency if one side becomes the bottleneck.

Open question: can a disaggregated cluster become energy-proportional without
destroying TTFT or TPOT SLOs?

## 10. Shared Evaluation Methodology

The field lacks a standard benchmark suite for disaggregated LLM serving.
Papers use different traces, models, hardware, SLOs, and reporting metrics.

Open question: what is the MLPerf-like benchmark for PD, AFD, KV-pool, and
re-aggregation systems?

