# C: Composite PD × AFD

<!-- Generated; edit data/discovery.json instead. -->

4 discovery records. [Index and evidence policy](../discovery.md).

Subtypes and descriptions below are inherited survey classifications; source metadata checks do not validate the technical classification.

| Year / subtype | Work and sources | Source check | Boundary or comparison note |
|---|---|---|---|
| 2026 / C1 | <a name="survey-hu2026aflex"></a>[Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling](https://arxiv.org/abs/2608.01891)<br>Also indexed as: AFlex, Energy-Efficient LLM Serving via Disaggregated Attention-FFN and Flexible Frequency Scaling<br>[Curated entry](../catalog.md#aflex) | metadata-verified | Four pools (prefill/decode x attention/FFN) with per-pool frequency; hidden states cross A/F, KV crosses P to D. |
| 2026 / C1 | <a name="survey-wu2026expertplex"></a>[ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](https://arxiv.org/abs/2607.18002)<br>Also indexed as: ExpertPlex, ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels<br>[Curated entry](../catalog.md#expertplex) | metadata-verified | Prefill-attention and decode-attention servers share MoE servers; routed activations cross via persistent-kernel buffers. |
| 2026 / C1 | <a name="survey-jiang2026hexgen3"></a>[HexGen-3: A Fully Disaggregated LLM Serving Framework with Fine-Grained Heterogeneous Resource Autoscaling](https://proceedings.mlr.press/v306/jiang26z.html)<br>Also indexed as: HexGen-3, HexGen-3: A Fully Disaggregated LLM Serving Framework with Fine-Grained Heterogeneous Resource Autoscaling<br>[Curated entry](../catalog.md#hexgen-3) | reachable | Separate prefill, attention and FFN pools on heterogeneous GPUs; KV crosses P to A, activations cross A to F. |
| 2025 / C1 | <a name="survey-xiao2025xdeepserve"></a>[Huawei Cloud Model-as-a-Service on the CloudMatrix384 SuperPod](https://arxiv.org/abs/2508.02520)<br>Also indexed as: xDeepServe, Huawei Cloud Model-as-a-Service on the CloudMatrix384 SuperPod<br>[Curated entry](../catalog.md#xdeepserve) | metadata-verified | Production PD with attention-FFN disaggregated decode on CloudMatrix384; KV and activations cross. |
