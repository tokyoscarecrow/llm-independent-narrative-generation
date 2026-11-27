# Experiment 06 — LLM-jp Cross-Model Replication

## 目的

Experiment 05では、Qwen3-8Bを用いて高次ナラティブ制約を局所的・検査可能なconstraintへ分解し、

- Scene Boundary
- Reveal Constraints

の効果を検証した。

Experiment 06では、同じBenchmark・同じconstraint構造を別系統の日本語LLMへ適用し、

> Experiment 05で観測したconstraint response patternがQwen3固有なのか、モデルをまたいで再現するのか

を検証する。

単純な文章品質ランキングではなく、

> Narrative IRの各constraint layerに対するモデルの反応パターン

を比較対象とする。

---

## Model

- Model: `llm-jp/llm-jp-4-8b-instruct`
- Dense model
- Instruct / SFT-only variant
- Thinking modelは使用しない

Qwen3-8Bでは `enable_thinking=False` を使用していたため、reasoning方式差を極力混入させない目的で、LLM-jp側もThinking variantではなくInstruct variantを採用する。

---

## Benchmark

Experiment 05と同じ。

- Benchmark: `benchmark/v1.0`
- Scene: `EP01_SC02`

Baseline inputs:

```text
Scene Card
+ Character Context
+ Addressing Rules
+ Style Guide
```

Benchmark入力は変更しない。

---

## Conditions

Experiment 05のB0〜B3をそのまま再現する。

### C0 — Baseline

追加constraintなし。

### C1 — + Scene Boundary

C0 + `constraints/scene_boundary.yaml`

### C2 — + Reveal Constraints

C0 + `constraints/reveal_constraints.yaml`

### C3 — + Scene Boundary + Reveal Constraints

両方を追加。

---

## Seeds

Experiment 05と同じ。

- 42
- 31415
- 27182

合計12 run。

---

## Research Questions

### RQ1

Scene Boundary constraintによるScene Range制御はLLM-jpでも再現するか。

### RQ2

Reveal Constraintsによる「具体的な答えを出さない」制御はLLM-jpでも再現するか。

### RQ3

State / Range ConstraintsとRealization Constraintsの難易度差はLLM-jpでも観測されるか。

### RQ4

Qwen3とLLM-jpで、同じNarrative IR layerに対する反応パターンはどこまで共通するか。

---

## Hypotheses

### H1

C1/C3ではC0/C2よりScene Range controlが安定する。

### H2

C2/C3ではC0/C1より具体的Revealが減る。

### H3

Scene Questionの暗示化、Meta-language抑制などRealization-level controlは、State / Range controlより不安定である。

### H4

constraint追加によってCharacter / Addressingなど既存の局所レイヤーは大きく悪化しない。

---

## Experimental Stages

### Stage 0 — Design Freeze

- Model
- Benchmark
- Conditions
- Seeds
- Evaluation criteria

を固定する。

### Stage 1 — Runtime Compatibility

Narrative Benchmarkを使わず、短い日本語Smoke Testだけを実行する。

確認項目：

- model load
- tokenizer
- chat template
- Japanese generation
- special-token anomaly
- repetition anomaly
- dtype
- device_map
- GPU memory
- library versions

Runtime failureはNarrative Qualityと分離して記録する。

### Stage 2 — Generation Parameter Freeze

Smoke Test成功後、LLM-jp向けgeneration parametersを一度だけ確定する。

その後C0〜C3では変更しない。

### Stage 3 — C0

3 Seedを生成し、LLM-jp固有Baselineを評価する。

### Stage 4 — C1 / C2 / C3

各条件を3 Seedずつ生成する。

### Stage 5 — Within-model Evaluation

まずLLM-jp内部でC0→C1/C2/C3の効果を評価する。

### Stage 6 — Cross-model Evaluation

最後にExperiment 05 Qwen3 B0〜B3と比較する。

---

## Comparison Policy

### Within Experiment 06

Strict variable control:

- model fixed
- runtime fixed
- generation parameters fixed
- benchmark fixed
- seeds fixed
- only additional constraints differ

### Qwen3 vs LLM-jp

Practical cross-model comparison:

- Narrative Specificationは同一
- Seedsは同一
- decodingは各モデルで安定した推奨条件を使用してよい
- 比較対象は文章品質そのものではなくconstraint response pattern

---

## Important Rule

Experiment 05で使用したScene Boundary / Reveal Constraintsの内容は変更しない。

Experiment 06中に新たな問題が見つかっても、その場でconstraintを修正しない。
修正案は次Experimentの研究課題として扱う。
