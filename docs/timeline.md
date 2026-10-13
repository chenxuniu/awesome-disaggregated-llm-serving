# Selective Timeline

Dates below distinguish preprint emergence from known publication milestones.
They are a reading aid rather than priority claims or an exhaustive history.
Use each [catalog entry](catalog.md) for its source and year convention.

## 2020–2022: Sparse Models and Serving Foundations

- [GShard](catalog.md#gshard): 2020 preprint, ICLR 2021 publication.
- [FastMoE](catalog.md#fastmoe): 2021 MoE training-system preprint.
- [Switch Transformers](catalog.md#switch-transformer): 2021 preprint, JMLR 2022.
- [Orca](catalog.md#orca): OSDI 2022 iteration-level serving scheduling.
- [DeepSpeed-MoE](catalog.md#deepspeed-moe): ICML 2022 MoE system substrate.

## 2023: Modern Memory and Scheduling Substrates

- [vLLM](catalog.md#vllm): SOSP 2023 PagedAttention.
- [SARATHI](catalog.md#sarathi): chunked-prefill preprint.
- [Splitwise](catalog.md#splitwise): phase-splitting preprint, later ISCA 2024.
- [Tutel](catalog.md#tutel) and [Lina](catalog.md#lina): 2023 publication milestones
  for MoE execution/communication, following earlier preprints.

## 2024: Phase Splitting and KV State

- [DistServe](catalog.md#distserve) and [Sarathi-Serve](catalog.md#sarathi-serve): OSDI 2024
  split-phase and colocated scheduling comparison points.
- [Mooncake](catalog.md#mooncake): 2024 preprint/trace release, FAST 2025 publication.
- [P/D-Serve](catalog.md#pdserve), [MemServe](catalog.md#memserve),
  [LoongServe](catalog.md#loongserve), [DejaVu](catalog.md#dejavu), and
  [Llumnix](catalog.md#llumnix): scale, state, context, streaming, and scheduling.
- [Vidur](catalog.md#vidur) and [Mélange](catalog.md#melange): simulation and
  heterogeneous allocation.
- [DeepSeek-V3](catalog.md#deepseek-v3): large-MoE technical report.

## 2025: Operator Splits, Alternatives, and Deployable Components

- [MegaScale-Infer](catalog.md#megascale-infer): SIGCOMM 2025 DEP/AFD system.
- [Adrenaline](catalog.md#adrenaline), [Step-3](catalog.md#step3),
  [JANUS](catalog.md#janus-afd), and [FinDEP](catalog.md#findep): operator/expert designs.
- [Libra / DynaServe](catalog.md#dynaserve), [TaiChi](catalog.md#taichi),
  [MuxWise](catalog.md#muxwise), [Nexus](catalog.md#nexus), and
  [Helix](catalog.md#helix-parallelism): adaptive, unified, logical, or temporal alternatives.
- [FlowKV](catalog.md#flowkv) and [LMCache](catalog.md#lmcache): transfer and reusable cache layers.
- [EPD](catalog.md#epd-disaggregation): ICML 2025 multimodal-stage publication;
  [BurstGPT](catalog.md#burstgpt): KDD 2025 dataset publication.

## January–May 2026: Provisioning and Broader Stages

- [Analytical AFD provisioning](catalog.md#analytical-afd) and
  [AFD challenges](catalog.md#afd-challenges): ratios and communication boundaries.
- [EPD-Serve on Ascend](catalog.md#epd-serve-ascend) and
  [vLLM-Omni](catalog.md#vllm-omni): multimodal stage disaggregation.
- [How Far Can Disaggregation Go?](catalog.md#afd-design-space): AFD design-space study.

## June–October 13, 2026: Networks, Elasticity, Power, and Co-Design

- [NetKV](catalog.md#netkv), [SpectrumKV](catalog.md#spectrumkv),
  [Lynx](catalog.md#lynx), and [SmartGen](catalog.md#smartgen): routing and KV handoff policies.
- [Prefill deflection](catalog.md#prefill-deflection) and [FluidPD](catalog.md#fluidpd):
  slack use and in-place P/D elasticity.
- [AFD-Ledger](catalog.md#afd-ledger): matched-budget deployment provisioning.
- [SQD](catalog.md#sqd), [power-aware PD provisioning](catalog.md#power-provisioning-pd),
  [disaggregated quantization](catalog.md#disaggregated-quantization), and
  [DynaCore](catalog.md#dynacore): split decisions conditioned on attention architecture,
  power, precision, and accelerator organization.
- [EAServe](catalog.md#easerve): encode-aware admission/provisioning for EPD.

Recent entries listed as `arXiv` are preprints in this catalog; no peer-review
acceptance is implied. See [source policy](sources.md) for the verification boundary.

## Additional 2026 Coverage and Canonical Revisions

- [Libra](catalog.md#dynaserve): NSDI 2026 canonical follow-up to DynaServe.
- [Extended Frontier](catalog.md#frontier): 2026 simulator version, retaining the earlier workshop link.
- [FastAFD](catalog.md#fastafd), [vLLM AFD Plugin](catalog.md#vllm-afd-plugin),
  [ASAP](catalog.md#asap), [KernelFlume](catalog.md#kernelflume), and
  [Tarragon](catalog.md#tarragon): open prototypes, prefill/core-attention splits, and resilience.
- [AFlex](catalog.md#aflex), [ExpertPlex](catalog.md#expertplex),
  [OpScale](catalog.md#opscale), and [OpWeave](catalog.md#opweave): composite and adaptable operator deployments.
- [ECO](catalog.md#eco) and [AFORE](catalog.md#afore): October 2026 energy-oriented
  configuration search and overlapped expert reconfiguration.
- [Crossflow](catalog.md#crossflow), [PPD](catalog.md#ppd), [DualPath](catalog.md#dualpath),
  and [PEARL](catalog.md#pearl): agentic state, elasticity, storage paths, and rollout execution.

Use [latest-updates.md](latest-updates.md) for renamed works and selected recent
mechanisms. The [discovery index](discovery.md) reflects the frozen survey search
window plus current metadata checks, not a new exhaustive search after its cutoff.
