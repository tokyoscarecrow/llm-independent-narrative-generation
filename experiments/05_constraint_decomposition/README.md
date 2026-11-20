# Experiment 05 — High-level Constraint Decomposition

## 目的

Experiment 04で、LLMは

- 呼称
- 括弧
- 短文傾向

のような局所的・明示的な制約には比較的強い一方、

- Scene境界
- Reveal Policy
- 「説明しすぎない」
- 「伏線を明かさない」

のような高次制約には弱いことが確認されました。

Experiment 05では、

> 高次のナラティブ意図を、より局所的・明示的・検査可能な制約へ分解すると、制御性能が改善するか

を検証します。

これは単なるプロンプト改善ではなく、Narrative IRを成立させるために、

> 高次の意図をどのような情報単位へ変換すべきか

を調べる最初の実験です。

---

## Model

- Model: `Qwen/Qwen3-8B`
- `enable_thinking=False`

## Benchmark

- Benchmark: `benchmark/v1.0`
- Scene: `EP01_SC02`

BaselineはExperiment 04のA3と同一です。

```text
Scene Card
+ Character Context
+ Addressing Rules
+ Style Guide
```

---

## 実験条件

### B0 — Baseline

Experiment 04 A3と同じ入力。

### B1 — + Scene Boundary

B0に `constraints/scene_boundary.yaml` を追加。

目的：

> 「Sceneを越えるな」という抽象制約を、開始位置・終了条件・禁止される後続イベントへ分解すると、Scene境界逸脱が減るか。

### B2 — + Reveal Constraints

B0に `constraints/reveal_constraints.yaml` を追加。

目的：

> 「伏線のみ」「理由を明かさない」という抽象制約を、明示してよい情報・禁止情報へ分解すると、Reveal Policy違反が減るか。

### B3 — + Scene Boundary + Reveal Constraints

B0に両方を追加。

目的：

> 2種類の高次制約を同時に与えても、それぞれの効果を維持できるか。

---

## Seeds

Experiment 04と同じ3 Seedを使用します。

- 42
- 31415
- 27182

これにより、B0についてはExperiment 04 A3を比較基準として利用できます。

---

## 主評価項目

### Primary

- Scene Boundary
- Reveal Policy

### Secondary

- Unsupported Additions Level 2–3
- Scene Question
- Meta-information Leakage
- Local Coherence
- Style Compliance

---

## 仮説

### H1

Scene Boundaryを明示的な開始・終了・禁止イベントに分解すると、Scene境界逸脱が減少する。

### H2

Reveal Policyをallowed / forbidden informationへ分解すると、伏線の過剰説明やScene Questionへの直接回答が減少する。

### H3

B3では、Scene BoundaryとReveal Constraintsの両方の改善が同時に維持される。

### H4

局所化した制約を追加しても、文体やCharacter Contextなど既存レイヤーの遵守率は大きく悪化しない。

---

## 因果関係を守るためのルール

- Modelは固定
- Benchmarkは固定
- generation parametersは固定
- Seedは固定
- B0〜B3で変更するのは追加constraintだけ
- 出力後の対話修正は行わない
- Raw Outputは加工しない

---

## 成功判定

Scene Boundaryについては、

- 授業開始
- 休み時間
- 放課後
- 下校
- 帰宅
- 夜

など、指定Sceneより先へ進まないことを重視します。

Reveal Policyについては、

- みず葉が隼太を気にかける理由を説明しない
- 過去の事件を新規に説明しない
- Scene Questionへ直接回答しない

ことを重視します。

---

## ファイル

- `parameters.yaml`
- `constraints/scene_boundary.yaml`
- `constraints/reveal_constraints.yaml`
- `evaluation_plan.md`
- `outputs/`
