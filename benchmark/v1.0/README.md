# Kannagi Diary Benchmark v1.0

『かんなぎダイアリー / Kannabi Memorandum』を用いた、LLMナラティブ生成比較用の固定ベンチマークです。

## 目的

このディレクトリは、LLMによるナラティブ生成を同一条件で比較評価するための**固定スナップショット**です。

ここに保存されている資料は、作品制作側の最新版ではありません。作品本編は今後も改稿される可能性がありますが、Benchmark v1.0 は実験条件を維持するため変更しません。

## Benchmark Scene / 対象シーン

- Project: かんなぎダイアリー / Kannabi Memorandum
- Scene: EP01_SC02
- Title: 何も起きない朝
- Setting: 六ッ川高校・昇降口〜教室
- Benchmark version: v1.0

## データの構成

このBenchmarkでは、**人間が事前に設計していた作品情報**と、**実験でLLMへ実際に与える入力情報**を分離しています。

### reference/

人間が本文生成以前に作成していたナラティブ設計上の参照資料です。

これらを公開する目的は、次の3点を区別できるようにすることです。

- 人間があらかじめ設計していた内容
- その中からLLM入力へ変換・抽出された内容
- LLMが生成時に独自に追加した内容

`reference/` の情報が、すべて自動的にLLMへ入力されるわけではありません。

### inputs/EP01_SC02/

Benchmark実験の基礎入力として使用する構造化データです。

- `scene_card.yaml`
- `character_context.yaml`
- `addressing_rules.yaml`
- `style_guide.yaml`

実験条件によって、これらを組み合わせて使用します。

たとえば Config Ablation 実験では、次の4条件を比較します。

- A0: Scene Card only
- A1: A0 + Character Context
- A2: A1 + Addressing Rules
- A3: A2 + Style Guide

## 重要な実験上の制約

このBenchmarkの Character Context は、**実験時にLLMへ与えた情報だけ**に限定しています。

作品制作側には、キャラクターについてより多くの背景設定があります。しかし、それらが実験入力に含まれていなかった場合は、Benchmark入力にも追加しません。

特に、伏線の答えや後のシーンで開示される情報を事前に与えると、LLMが本来知らない情報まで使って本文を書けてしまいます。

そのため、

> 制作側では既知だが、実験入力には含まれない情報

を意図的に残しています。

これは、後から得た作品知識や設定変更がBenchmark評価へ混入することを防ぐためです。

## Provenance / 出典

制作側ソースリポジトリ：

`tokyoscarecrow/kannagi-diary-devlog`

Benchmark作成時の参照コミット：

`5ebb5a86d0683ccf8980fb468b644d3899dad097`

このスナップショットを構成する元ファイルとblob SHAは `manifest.yaml` に記録しています。

## Versioning Policy / バージョン管理方針

`benchmark/v1.0/` 以下は固定します。

Benchmark定義を変更する必要が生じた場合は、v1.0を書き換えるのではなく、

- `v1.1`
- `v2.0`

など、新しいバージョンを作成します。

## License / ライセンス

Benchmarkおよびナラティブ関連文書は **CC BY-NC 4.0** で公開します。

詳細：

`benchmark/LICENSE.md`
