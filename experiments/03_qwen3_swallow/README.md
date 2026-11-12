# Experiment 03 — Qwen3-8B vs Qwen3-Swallow-8B

## 目的

日本語特化モデルである Qwen3-Swallow-8B-SFT-v0.2 を、Qwen3-8Bと同じBenchmark v1.0で比較し、

> 日本語能力の強化が、ナラティブ制御能力の向上にもつながるか

を確認する実験です。

本実験では、単純な文章の自然さだけでなく、

- Scene構造
- Reveal Policy
- 設定外補完
- Scene境界
- Scene Question
- 抽象心理表現
- 固有名詞
- キャラクター整合性

を重点的に観察しました。

## Benchmark

- Benchmark: `benchmark/v1.0`
- Scene: `EP01_SC02`
- Input stack:
  - Scene Card
  - Character Context
  - Addressing Rules
  - Style Guide

## Models

### Qwen3-8B

- Model ID: `Qwen/Qwen3-8B`
- non-thinking mode
- `enable_thinking=False`

### Qwen3-Swallow-8B-SFT-v0.2

- Model ID: `tokyotech-llm/Qwen3-Swallow-8B-SFT-v0.2`
- 日本語向けSFTモデル

## 比較上の注意

Qwen3-Swallowでは、元のQwen3と同じ形でのthinking toggleを使えないため、本実験は厳密な「一変数だけを変更した比較」ではありません。

そのため、このExperiment 03は、

> 日本語特化モデルを実用条件で使った場合、ナラティブ生成上どのような傾向が出るか

を見る**実用比較**として扱います。

## Seed

Qwen3-Swallowでは、次の3 Seedを固定しました。

- 42
- 31415
- 27182

複数Seedを使う目的は、生成結果の違いを楽しむことではなく、

- Seedごとに変わる現象
- Seedを変えても繰り返す現象

を分離するためです。

## Qwen3-Swallowで確認した主な傾向

3 Seedすべてで、日本語そのものは比較的流暢かつ安定していました。

固有名詞も大きく崩れませんでした。

一方、複数Seedで繰り返し確認された問題があります。

### 1. 抽象的な心理表現

- 「胸の奥」
- 「何か」
- 「微かな不安」
- 「違和感」
- 「予感」

など、抽象心理語を多用する傾向が残りました。

### 2. 設定外補完

Scene Cardに存在しない出来事や関係情報を補う傾向が見られました。

### 3. 物理的距離の過剰解釈

Character Contextの「みず葉は隼太との距離が近い」という情報から、

- 手をつなぐ
- 必要以上に接触する

など、入力より強い行動へ発展させるケースがありました。

### 4. 伏線の過剰具体化

Scene QuestionやReveal Policyに対して、

> 伏線として残す

のではなく、

- 理由を具体化する
- Scene Questionを台詞化する
- 読者に答えを説明する

方向へ進むケースがありました。

### 5. Scene境界の逸脱

特に重要だったのが、指定Sceneを超えて物語を完結させようとする傾向です。

入力では「朝の登校〜教室」のSceneであるにもかかわらず、

- 授業
- 放課後
- 帰宅
- 夜
- バス移動

など、その先まで生成するケースが確認されました。

### 6. メタ情報の漏出

一部runでは、

- Style Guideの用語
- 「常体のまま」
- 「次の章で明らかになるだろう」

といった、制作側の設計情報に近い表現が本文へ混入しました。

## 3 Seedで繰り返したことの意味

1回だけなら、sampling上の偶然と考えることもできます。

しかし3 Seedで、

- 抽象心理表現
- 設定外補完
- Scene境界逸脱
- 伏線の過剰説明

が繰り返されたことから、これらは単なる偶然ではなく、モデルと入力の組み合わせに由来する**傾向**として扱う方が妥当と判断しました。

## 暫定結論

Qwen3-Swallowは、日本語の流暢さや固有名詞の安定性では良好でした。

しかし、

> 日本語が自然であること  
> ≠  
> 構造化されたナラティブ仕様への忠実度が高いこと

という結果になりました。

むしろ、文章を「小説らしく完成させる」能力が強いほど、

- 情報を補う
- Sceneを先へ進める
- 伏線を説明する

という方向に働く場合があります。

この結果から、

> Japanese fluency と instruction fidelity は別の評価軸である

という知見を得ました。

## 関連ファイル

- `parameters.yaml`
- `evaluation_summary.md`
- `outputs/README.md`
