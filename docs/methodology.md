# 研究方法論 — Methodology

この文書は、本リポジトリで行うLLMナラティブ生成実験の共通方法論を定義します。

個別のExperimentでは、ここで定義した原則を前提とし、各モデルや実験条件に固有の差分だけを記録します。

---

## 1. 研究目的

本研究では、

> 人間がナラティブデザインを行い、その設計情報を構造化データとしてLLMから分離した場合、異なるLLMがどこまで同じ設計意図を本文として実装できるか

を検証します。

一般的な「AIと対話しながら物語を共同制作する」方式とは異なり、物語そのものの主要な意思決定は人間側で行います。

LLMには主として、

> 構造化されたナラティブ仕様を文章へ変換する

役割を与えます。

---

## 2. 基本構造

本研究の基本フローは次の通りです。

```text
Human Narrative Design
        ↓
Structured Specification
        ↓
       LLM
        ↓
Generated Prose
        ↓
Evaluation
```

人間が設計する主な要素：

- 世界観
- テーマ
- キャラクター
- エピソード構成
- Scene構成
- Scene Goal
- Scene Question
- Conflict
- Beat
- Reveal Policy
- 情報開示順
- 伏線

LLMへ与える構造化レイヤー：

- Scene Card
- Character Context
- Addressing Rules
- Style Guide

---

## 3. 「もっとこうして」で修正しない

本研究では、初回生成結果に対して、

- もっと自然に
- もっとキャラクターらしく
- この伏線は説明しないで
- 会話を増やして

といった対話的な追加修正を、評価対象runの中では原則として行いません。

理由は、

> 最初の仕様をLLMが正しく解釈できたのか  
> それとも人間との追加対話で修正されたのか

を分離するためです。

基本単位は、

```text
Input
  ↓
One generation run
  ↓
Evaluation
```

です。

改善する場合は、

- Scene Cardを変更する
- Character Contextを追加する
- Addressing Rulesを分離する
- Style Guideを変更する
- generation parametersを変更する

など、入力仕様または実行条件を明示的に変更し、別runとして記録します。

---

## 4. Benchmarkの固定

比較実験では、作品制作側の最新版をそのまま使い続けません。

`benchmark/v1.0/` のような固定スナップショットを作成し、同一条件比較の基準とします。

Benchmarkは、

- 制作側の参照情報
- 実際のLLM入力

を分離します。

```text
reference/
  人間が事前に持っていた作品設計

inputs/
  実験時にLLMへ実際に渡す構造化入力
```

Benchmark v1.0は、原則として変更しません。

変更が必要な場合は、新しいversionを作成します。

---

## 5. 人間の知識とLLM入力を混同しない

制作側では既知であっても、LLMへ与えていない情報は評価上「未知」として扱います。

たとえば、

- キャラクターの過去
- 伏線の答え
- 後のSceneで判明する設定
- 作者だけが知っている裏設定

を入力していない場合、LLMがそれを知っていることを前提に評価しません。

逆に、LLMがそれらに相当する内容を勝手に生成した場合は、

> 設定外補完

として評価します。

---

## 6. モデル比較と実用比較

本研究では、すべてのExperimentを厳密な一変数比較として扱いません。

モデルごとに、

- 推奨generation parameters
- chat template
- thinking mode
- dtype
- quantization
- runtime requirements

が異なるためです。

そのため比較を大きく2種類に分けます。

### 6.1 Strict Comparison

可能な範囲で条件を固定し、一要因の違いを比較します。

例：

- Config Ablation A0〜A3
- Seed比較

### 6.2 Practical Comparison

同一のナラティブ仕様を、各モデルに適した実行条件で与えます。

例：

- Gemma 2 vs Qwen3
- Qwen3 vs Qwen3-Swallow

この場合、

> 同一decoding parametersであること

よりも、

> 各モデルが現実的な適切条件で動作していること

を優先します。

---

## 7. Runtime CompatibilityとTask Qualityを分離する

オープンLLMでは、モデル品質以前に安定推論できるかどうかが問題になります。

そのため評価を二段階に分けます。

```text
Stage 1
Runtime Compatibility
  ↓
Stage 2
Narrative / Task Quality
```

Stage 1を通過していない場合、Stage 2の品質評価は行いません。

例：

- Gemma 3 4B on Kaggle T4

この場合、

> 品質が低い

ではなく、

> 当該環境では安定推論を確立できず、品質評価不能

と記録します。

---

## 8. Seedの扱い

`do_sample=True` の場合、Seedはsamplingに使用する乱数系列の初期値です。

本研究では、複数Seedを使って、

- 1回だけ現れる現象
- Seedを変えても繰り返す現象

を区別します。

複数Seedで再現する問題は、

> sampling accident

ではなく、

> model + input specificationに由来する傾向

である可能性が高いと判断します。

ただし、Seed固定は完全な再現性を保証しません。

以下が変わると、同一Seedでも結果が変わる可能性があります。

- model version
- library version
- GPU
- quantization
- generation implementation

---

## 9. Raw Outputを加工しない

生成結果を保存する場合は、原則として未加工で保存します。

- 誤字を直さない
- 固有名詞崩れを直さない
- 反復を削除しない
- Scene境界逸脱部分を切らない
- 人間のコメントを本文へ混ぜない

人間による評価は、別ファイルへ記録します。

---

## 10. 原文がない場合は再構成しない

過去のExperimentを整理する際、

- 生ログ
- Notebook output
- 保存済み本文

が確認できない場合は、記憶や要約から本文を再構成しません。

その場合は、

- 観察結果
- 保持されているerror message
- 確認済みparameter
- 評価メモ

だけを記録します。

---

## 11. 評価対象

本研究では、単純な「文章の上手さ」だけを評価しません。

主な評価対象は、

- Scene構造
- Scene Question
- Character consistency
- Addressing
- Proper nouns
- Reveal Policy
- Scene boundary
- Unsupported additions
- Local coherence
- Meta-information leakage
- Style compliance

です。

詳細は、

`docs/evaluation_criteria.md`

を参照してください。

---

## 12. 研究上の基本姿勢

本研究の目的は、

> どのLLMが一番小説を書くのが上手いか

をランキングすることではありません。

確認したいのは、

> 同じナラティブ仕様を与えたとき、各モデルがどのレイヤーをどの程度利用できるか

です。

そのため、成功例だけでなく、

- 失敗
- 誤解
- 補完
- Scene逸脱
- runtime failure

も研究結果として保存します。
