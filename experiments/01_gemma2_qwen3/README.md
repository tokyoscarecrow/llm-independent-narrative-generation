# Experiment 01 — Gemma 2 2B IT vs Qwen3-8B

## 目的

LLM非依存のナラティブ生成方式が、商用クラウドLLMだけでなく、Kaggle上で動作するオープンLLMでも成立するかを確認するための初期比較実験です。

固定された物語設計データを入力し、

- Scene構造を維持できるか
- Character Contextを利用できるか
- 呼称ルールを守れるか
- Style Guideを反映できるか
- 設定外の補完や反復がどの程度発生するか

を観察しました。

## Benchmark

- Benchmark: `benchmark/v1.0`
- Scene: `EP01_SC02`
- Title: 「何も起きない朝」

比較に使用した基本入力は次の4レイヤーです。

```text
Scene Card
+ Character Context
+ Addressing Rules
+ Style Guide
```

Gemma 2では、この4レイヤーを一度に投入する前に、Scene Cardのみ、Character Context追加、生成パラメータ調整などの段階的検証も行っています。

## 実行環境

- Platform: Kaggle Notebook
- GPU: Tesla T4 × 2
- Framework: Hugging Face Transformers
- Local / Open LLM inference

正確なライブラリの固定バージョンは、当時の保存記録からは確認できていません。

## Models

### Gemma 2 2B IT

- Model ID: `google/gemma-2-2b-it`
- Parameter scale: 2B class

### Qwen3-8B

- Model ID: `Qwen/Qwen3-8B`
- Parameter scale: 8B class
- Chat template: non-thinking mode
- `enable_thinking=False`

## 実験の流れ

### 1. Gemma 2 2B IT

まずGemma 2で、構造化されたナラティブ仕様をどこまで利用できるかを確認しました。

Scene Cardのみでは、本文生成自体は可能でしたが、

- ラベルや説明的表現が本文へ混入する
- 入力にない情報を補完する
- 同じ段落や表現を反復する
- 抽象的な指示をそのまま台詞や説明へ変換する

といった問題が見られました。

Character Context と Addressing Rules を追加すると、

- 人物情報の一部を利用する
- みず葉の距離感や接触傾向を描写する
- 呼称の精度が上がる

といった改善がありました。

一方で、複数のBeatや制約を長く維持する能力には限界がありました。

反復についてはgeneration parametersの調整で大きく抑制できましたが、ナラティブ構造理解そのものが改善したわけではありませんでした。

### 2. Qwen3-8B

次に、同じ構造化入力をQwen3-8Bへ与えました。

最初はGemma 2で調整したgeneration parametersをそのまま使用しましたが、固有名詞の崩れなどが発生しました。

その後、Qwen3のnon-thinking生成向け設定へ変更すると、出力は大きく安定しました。

確認できた主な特徴は次の通りです。

- 固有名詞が安定
- B1 → B4 のScene構造を概ね維持
- Reveal Policyを維持
- 反復崩壊なし
- 一部に一人称誤りあり
- 抽象的な心理語の使用傾向は残る

## 重要な方法論上の判断

この比較では、最終的に**すべてのモデルへ完全に同一のdecoding parametersを強制していません**。

理由は、同一パラメータが各モデルにとって同等に適切とは限らず、実用性比較ではモデル固有の推奨設定を使用する方が妥当と判断したためです。

したがって本実験は、

> 同一decoding条件での純粋なモデル性能比較

ではなく、

> 同一のナラティブ仕様を、それぞれのモデルを適切に動作させた条件でどこまで実装できるか

を見る**実用比較**として位置づけます。

## 暫定結論

### Gemma 2 2B IT

個々の設定値や人物情報を読むことはできる一方、

- 複数の制約
- Beatの順序
- 長距離の整合性
- 抽象的なナラティブ指示

を同時に維持することは難しい。

### Qwen3-8B

同じ構造化入力をより高いレベルで利用でき、

- Scene構造
- 伏線管理
- 人物関係
- 呼称
- 長めの生成

を比較的安定して維持できた。

一方で、抽象的な心理表現を直接文章化する傾向など、後の実験でも継続して観察される問題が残りました。

## Raw Outputs

生の生成本文は `outputs/` に保存します。

現在の実験記録から正確に復元できない出力については、後から文章を再構成せず、原データが確認できたものだけを追加します。

## Parameters

生成条件は `parameters.yaml` を参照してください。
