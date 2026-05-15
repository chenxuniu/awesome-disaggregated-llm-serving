# Contributing

Thanks for helping improve this map.

## What belongs here

Please add work that directly relates to at least one of:

- Attention-FFN Disaggregation (AFD)
- Disaggregated Expert Parallelism (DEP)
- Prefill-Decode (PD) disaggregation or aggregation
- KV-cache movement, pooling, compression, reuse, or migration
- MoE inference systems that affect AFD or DEP
- Hardware, interconnect, or energy limits of disaggregated serving
- Evaluation traces or simulators for disaggregated LLM serving

General LLM inference papers are welcome only if they clearly connect to one
of these themes.

## Paper entry format

Add a record to `papers.yaml`:

```yaml
- id: short-stable-id
  title: "Paper title"
  year: 2026
  venue: "arXiv"
  category: "afd"
  status: "foundational"
  arxiv: "2601.00000"
  code: "https://github.com/example/repo"
  tags: ["AFD", "MoE"]
  why_it_matters: "One sentence on contribution."
  limitation: "One sentence on limitation or scope."
```

Use one of these categories when possible:

- `pd-disaggregation`
- `afd`
- `afd-theory`
- `reaggregation`
- `kv-cache`
- `moe-serving`
- `serving-foundation`
- `hardware-energy`
- `evaluation`

Use one of these status labels when possible:

- `foundational`
- `production`
- `theory`
- `boundary`
- `counter-baseline`
- `substrate`
- `adjacent`

## Review rule

Each entry should answer two questions:

1. Why should an AFD or disaggregated-serving researcher read this?
2. What does this paper not solve?

That second question keeps the repo useful as a research map rather than a
link dump.

