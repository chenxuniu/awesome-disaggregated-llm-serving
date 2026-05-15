# Reading Order

This page gives different paths depending on how much time you have.

## 30-Minute Route

Read abstracts and figures only.

1. DistServe
2. Mooncake
3. MegaScale-Infer
4. Analytical Provisioning for AFD
5. Revealing the Challenges of AFD
6. SARATHI or TaiChi

Outcome: you will understand the core conflict between disaggregation and
re-aggregation.

## One-Day Route

Read these in order:

1. Orca
2. vLLM / PagedAttention
3. Splitwise
4. DistServe
5. Mooncake
6. SARATHI / Sarathi-Serve
7. MegaScale-Infer
8. Step-3 / StepMesh
9. Analytical Provisioning for AFD
10. Revealing the Challenges of AFD

Outcome: you will understand the serving substrate, PD disaggregation, AFD,
and the main limitations.

## Writing Related Work

Use this ordering:

1. Serving foundations: Orca, vLLM, SGLang
2. PD disaggregation: Splitwise, DistServe, Mooncake, P/D-Serve
3. KV cache substrate: CacheGen, FlowKV, LMCache, MemServe
4. AFD and DEP: MegaScale-Infer, Step-3, JANUS, FinDEP, Adrenaline
5. Theory and limits: Analytical Provisioning, Revealing Challenges
6. Counter-baselines: SARATHI, TaiChi, MuxWise, Nexus
7. MoE substrate: DeepSeek-V3, DeepEP, Tutel, DeepSpeed-MoE, Lina

Outcome: your related work will avoid the common mistake of treating AFD,
PD disaggregation, and chunked prefill as unrelated islands.

## Building An AFD System

Start with:

1. MegaScale-Infer
2. Step-3
3. StepMesh
4. DeepSeek-V3 and DeepEP
5. SGLang and vLLM deployment docs
6. Analytical Provisioning for AFD
7. Revealing the Challenges of AFD
8. TaiChi / SARATHI as baselines

Outcome: you will see both the implementation path and the strongest attacks
against the design.

## Looking For A Research Problem

Read:

1. Analytical Provisioning for AFD
2. Revealing the Challenges of AFD
3. MegaScale-Infer
4. TaiChi
5. Mooncake
6. FlowKV
7. BurstGPT and Mooncake traces
8. docs/open-problems.md

Outcome: you will see where static provisioning, communication dead zones,
heterogeneity, and workload shift create publishable gaps.

