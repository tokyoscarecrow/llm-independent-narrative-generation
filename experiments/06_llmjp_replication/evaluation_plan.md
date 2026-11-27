# Evaluation Plan — Experiment 06

## 目的

LLM-jp内部でC0〜C3を比較した後、
Experiment 05のQwen3 B0〜B3との反応パターンを比較する。

合計12 narrative runs:

```text
C0 × 3
C1 × 3
C2 × 3
C3 × 3
= 12 runs
```

---

## 1. Required Endpoint Completion

### 0 — 到達

教室まで進み、住吉登場後に日常が戻り、
理由不明の予感を残して終了。

### 1 — 部分到達

必要要素の一部はあるが、
場所または終端状態が曖昧。

### 2 — 未到達

指定終点状態まで進まず途中終了。

---

## 2. Boundary Overrun

### 0 — 遵守

指定Sceneより後の出来事を開始しない。

### 1 — 軽微な延長

短い余韻・説明のみで、新イベントは開始しない。

### 2 — 明確な境界逸脱

授業、休み時間、放課後などへ進む。

### 3 — 大幅な逸脱

帰宅、夜、翌日など複数Scene相当へ進む。

---

## 3. Reveal Violation

### 0 — 遵守

理由を伏せ、疑問だけを残す。

### 1 — 軽微な具体化

答えではないが伏線を狭く具体化する。

### 2 — 部分的回答

みず葉の動機や過去を部分的に説明する。

### 3 — 明示的回答

Scene Questionへの直接回答またはSC03相当情報を開示。

---

## 4. Unsupported Additions

Experiment 05と同じLevel 0〜3を使用。

- Level 0: supplied informationの自然な具体化
- Level 1: harmless supplementation
- Level 2: story-meaningful new information / event
- Level 3: setting / plot / foreshadowing / reveal structureを変更

---

## 5. Secondary Checks

- Scene structure / Beat order
- Scene Question handling
- Character consistency
- Addressing
- Proper nouns
- Local coherence
- Meta-information leakage
- Design-language leakage
- Style compliance
- Abstract psychological language
- Repetition

---

## 6. Within-model Hypothesis Evaluation

### H1

C1/C3でScene RangeがC0/C2より安定するか。

### H2

C2/C3で具体的RevealがC0/C1より減るか。

### H3

State / Range controlに比べ、
Scene Question暗示化・Meta-language抑制などRealization-level controlが不安定か。

### H4

Constraint追加によってCharacter / Addressing / Styleが大きく悪化しないか。

---

## 7. Cross-model Comparison

Qwen3とLLM-jpで比較するのは、
単純な「文章の上手さ」ではなく以下。

- Boundary constraintへの反応
- Reveal constraintへの反応
- Scene Questionの処理
- Meta-information leakage
- Unsupported Additions
- local/mechanical constraintsとglobal/abstract constraintsの差

比較表：

```text
Qwen3   B0 B1 B2 B3
          ↕  ↕  ↕  ↕
LLM-jp  C0 C1 C2 C3
```

---

## 8. Statistical Scope

3 Seedのみの探索的実験であり、
統計的有意差は主張しない。

目的は、

> 同じNarrative Specificationに対するconstraint response patternが
> モデルをまたいで再現するか

を観察すること。
