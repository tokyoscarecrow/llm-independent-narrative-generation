# Evaluation Summary — Experiment 05

## Experiment

**High-level Constraint Decomposition**

Model:

- Qwen/Qwen3-8B
- enable_thinking: false

Benchmark:

- EP01_SC02
- benchmark/v1.0

Seeds:

- 42
- 31415
- 27182

Conditions:

- B0: Baseline
- B1: + Scene Boundary
- B2: + Reveal Constraints
- B3: + Scene Boundary + Reveal Constraints

---

## 1. Score Summary

### Required Endpoint Completion

| Condition | Seed 42 | Seed 31415 | Seed 27182 |
|---|---:|---:|---:|
| B0 | 2 | 2 | 2 |
| B1 | 0 | 0 | 0 |
| B2 | 0 | 0 | 0 |
| B3 | 0 | 0 | 0 |

### Boundary Overrun

| Condition | Seed 42 | Seed 31415 | Seed 27182 |
|---|---:|---:|---:|
| B0 | 0 | 0 | 0 |
| B1 | 0 | 0 | 1 |
| B2 | 0 | 3 | 0 |
| B3 | 0 | 0 | 2 |

### Reveal Violation

| Condition | Seed 42 | Seed 31415 | Seed 27182 |
|---|---:|---:|---:|
| B0 | 0 | 2 | 0 |
| B1 | 0 | 0 | 0 |
| B2 | 0 | 0 | 1 |
| B3 | 0 | 1 | 0 |

---

## 2. H1 — Scene Boundary decomposition

### Hypothesis

Scene Boundaryを明示的な開始・終了・禁止イベントへ分解すると、
Scene境界制御が改善する。

### Result

**部分的に支持。**

B1では3/3 SeedでRequired Endpoint Completionが2→0となり、
必要終点へ到達した。

一方、B2でも3/3 SeedでEndpoint Completionが0となったため、

> Endpoint改善がScene Boundary constraint固有の効果である

とは、この3 Seedだけでは断定できない。

ただしBoundary Overrunでは、

- B1: 0 / 0 / 1
- B2: 0 / 3 / 0

となり、Scene Boundaryを持つB1の方が大幅越境を抑えている。

またB3でも2/3 SeedはOverrun 0だったが、
Seed 27182では授業開始後へ進んだ。

したがってScene Boundary constraintは、

> 必要終点への到達と停止を安定化する方向に働くが、
> stop ruleを保証するものではない

と評価する。

---

## 3. H2 — Reveal decomposition

### Hypothesis

Reveal Policyをallowed / forbidden informationへ分解すると、
伏線の過剰説明やScene Questionへの直接回答が減少する。

### Result

**限定的に支持。**

B2では3 Seedすべて、
みず葉の具体的な動機・過去事件そのものは明かさなかった。

B0ではSeed 31415で、
「隼太が今日も元気でいてくれて嬉しいだけ」
という理由らしき回答が生成されていた。

この意味で、

> 具体的な答えを出さない

という狭いReveal controlには効果が見られる。

一方で、

- Scene Questionの直書き
- 「理由は分からない」という説明文への変換
- design-language leakage
- 「次章で知る」等のメタ予告

は安定して抑制できなかった。

したがってReveal Constraintsは、

> 情報開示そのもの

には比較的効くが、

> その情報をどう暗示するか

という表現レベルの制御には弱い。

---

## 4. H3 — Combined constraints

### Hypothesis

Scene BoundaryとReveal Constraintsを併用しても、
それぞれの効果を維持できる。

### Result

**限定的に支持。**

B3では3 Seedすべて、

- 必要終点へ到達
- 具体的Revealを回避

した。

しかしSeed 27182では、

- 授業開始
- 授業の合間

まで進み、Boundary Overrun 2となった。

さらに、

> 「次章へとつながる、小さな導線だった。」

という明示的Meta-information Leakageも発生した。

したがって、

> 異なるconstraintは同時利用可能だが、
> すべての制約を完全に同時遵守する保証はない

と評価する。

---

## 5. H4 — Existing layers remain stable

### Hypothesis

constraint追加によって、
Character / Addressing / Style等が大きく悪化しない。

### Result

**概ね支持。**

B1〜B3を通して、

- Character tendencies
- Addressing
- Proper names
- 三人称近接
- 常体

は大きく崩れていない。

一方、

- 現在形ベース
- 内心の（）表記
- 抽象心理表現の抑制

はBaselineから一貫して弱く、
constraint追加によって改善も悪化もしていない。

---

## 6. Main Finding

Experiment 05で最も重要な知見は、

> **高次のナラティブ意図を局所的・検査可能なconstraintへ分解すると、
> そのconstraintが担当する対象について制御が改善する傾向がある。**

という点。

ただし、

> **constraintを明示しただけでは遵守は保証されない。**

特に、

- stop rule
- meta-information leakage
- Scene Questionの暗示化
- 抽象概念の演技化

は依然として不安定。

---

## 7. A More Important Distinction

Experiment 05から、
高次制約には少なくとも2種類ある可能性が見えてきた。

### State / Range Constraints

例：

- どこから始める
- どこまで進む
- どの情報を出してよい / いけない
- どのイベントを開始してはいけない

これらは比較的構造化しやすく、
constraint decompositionの効果も観察しやすい。

### Realization Constraints

例：

- 問いを直接書かず、読者に感じさせる
- 説明せず行動で示す
- 伏線を自然に暗示する
- design languageを本文へ露出しない

これらは、
allowed / forbidden listだけでは十分に制御できなかった。

この差はNarrative IR設計上、重要な可能性がある。

---

## 8. Implication for Narrative IR

Narrative IRを単なる「詳細なプロンプト」として考えるのではなく、

```text
Narrative Intent
      ↓
State / Range Constraints
      +
Realization Strategy
      ↓
Model
      ↓
Prose
```

のように、

1. **何が成立していなければならないか**
2. **それを本文上どう実現するか**

を分離する必要がある可能性がある。

Experiment 05は、
この二層を区別する必要性を示した最初の実験と位置づけられる。

---

## 9. Next Research Direction

次の実験候補は、

> **Realization Strategyを独立したレイヤーとして形式化できるか**

の検証。

具体的には、

- Scene Questionを本文へ直接書かない
- 抽象心理語を直接使わない
- 行動 / 表情 / 感覚へ変換する
- Meta-languageを本文へ出さない
- 指定された意味を「説明」ではなく「演技」で実装する

といった規則を、

単純な禁止リストではなく、
**変換規則 / realization rules**
として与える方法を検討する。

これはExperiment 06候補とする。
