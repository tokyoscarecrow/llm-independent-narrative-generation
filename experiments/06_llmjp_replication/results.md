# Experiment 06 — Final Results

## Model

- `llm-jp/llm-jp-4-8b-instruct`
- revision: `098f2b2cf33021eba19a6d3582aa3d071ccc0aff`
- FP16
- 3 seeds: 42 / 31415 / 27182
- Conditions:
  - C0 Baseline
  - C1 + Scene Boundary
  - C2 + Reveal Constraints
  - C3 + Scene Boundary + Reveal Constraints

## Score matrix

| Condition | Seed | Endpoint | Overrun | Reveal | Unsupported |
|---|---:|---:|---:|---:|---:|
| C0 | 42 | 0 | 3 | 1 | 3 |
| C0 | 31415 | 2 | 0 | 0 | 2 |
| C0 | 27182 | 0 | 1 | 2 | 3 |
| C1 | 42 | 0 | 2 | 0 | 3 |
| C1 | 31415 | 0 | 2 | 1 | 3 |
| C1 | 27182 | 0 | 1 | 2 | 3 |
| C2 | 42 | 0 | 3 | 2 | 3 |
| C2 | 31415 | 0 | 3 | 1 | 3 |
| C2 | 27182 | 0 | 3 | 1 | 3 |
| C3 | 42 | 0 | 2 | 2 | 3 |
| C3 | 31415 | 0 | 3 | 1 | 3 |
| C3 | 27182 | 0 | 3 | 1 | 3 |

## Hypothesis outcomes

### H1 — Scene Boundary

**Partially supported.**

Scene Boundary stabilized endpoint completion:
- C0: 0 / 2 / 0
- C1: 0 / 0 / 0
- C3: 0 / 0 / 0

But it did not reliably enforce stopping:
- C1 Overrun: 2 / 2 / 1
- C3 Overrun: 2 / 3 / 3

For this model, Scene Boundary behaves more like a soft endpoint attractor than a hard scene-range constraint.

### H2 — Reveal Constraints

**Not supported as a stable effect.**

- C0 Reveal: 1 / 0 / 2
- C2 Reveal: 2 / 1 / 1
- C3 Reveal: 2 / 1 / 1

The model may withhold the exact reason while still inventing new mystery material, relationship implications, or directly verbalizing the intended question.

### H3 — Combined constraints

**Not supported.**

C3 did not produce additive improvement.
Endpoint completion remained stable, but overrun and reveal problems persisted.

### H4 — Existing local layers

**Generally supported.**

Local character cues often survived:
- Mizuha's brightness
- Mizuha watching Shunta
- Shunta's short replies
- Sumiyoshi's cheerful energy

Global realization remained unstable:
- POV
- tense
- stop behavior
- output form
- naming consistency
- unsupported semantic additions

## Cross-model comparison with Experiment 05

Qwen3 responded more strongly to the same explicit constraints:

- Qwen3 B1 Overrun: 0 / 0 / 1
- LLM-jp C1 Overrun: 2 / 2 / 1

- Qwen3 B2 Reveal: 0 / 0 / 1
- LLM-jp C2 Reveal: 2 / 1 / 1

The direction of one effect partially generalizes:
explicit endpoint specification helps endpoint completion.

But the strength and reliability of the constraint representation do not generalize unchanged.

## Main conclusion

Experiment 06 provides evidence that a fixed Narrative IR encoding should not be assumed to transfer directly across model families.

A more realistic architecture is:

```text
Human Narrative Design
        ↓
Narrative IR
        ↓
Model Adapter / Constraint Compiler
        ↓
Target LLM
        ↓
Prose
```

This reframes the next research question:

> Which parts of Narrative IR can remain model-independent, and which parts require model-specific compilation?
