# LLM-independent Narrative Generation

LLM非依存のナラティブ生成を検証するための実験リポジトリです。

人間がナラティブデザインを行い、その設計情報を Scene Card / Character Context / Addressing Rules / Style Guide などの構造化データとして外部化し、異なるLLMへ同一条件で入力したとき、どこまで設計意図を保持して本文を生成できるかを比較します。

## English Summary

This repository explores model-independent narrative generation.

Narrative design is created by a human author and externalized as structured specifications. Different LLMs are then evaluated on how faithfully they implement the same narrative design as prose.

## 研究目的

一般的な「AIと対話しながら物語そのものを作る」方式ではなく、以下の役割分担を前提とします。

```text
Narrative Design
      ↓
Structured Config
      ↓
     LLM
      ↓
    Prose
```

物語の構成、キャラクター、シーンの目的、Beat、伏線、情報開示などは人間側で設計し、LLMは主としてその設計を本文へ実装する役割を担います。

主な検証対象は次の通りです。

- 同一の構造化仕様が異なるLLMでどこまで通用するか
- モデルごとに何を正しく理解し、何を無視・補完するか
- モデルサイズや日本語特化がナラティブ制御へ与える影響
- Scene Card / Character Context / Addressing Rules / Style Guide の各レイヤーが、生成結果へどのような効果を持つか
- 設定外補完、シーン境界逸脱、伏線の過剰説明などをどこまで抑制できるか

## 基本構造 / Core Idea

```text
Narrative Design → Structured Config → LLM → Prose
```

## Benchmark

**Kannagi Diary Benchmark v1.0**

実験作品『かんなぎダイアリー / Kannabi Memorandum』の EP01_SC02「何も起きない朝」を固定ベンチマークとして使用します。

Benchmark v1.0 は作品の最新版ではなく、LLM比較実験の再現性を確保するために固定したスナップショットです。

詳細：

`benchmark/v1.0/`

## Experiments / 実験

1. Gemma 2 2B IT vs Qwen3-8B
2. Gemma 3 4B runtime test
3. Qwen3-8B vs Qwen3-Swallow-8B
4. Config Ablation（A0〜A3）

## Repository Structure

このリポジトリでは、次の要素を分離して管理します。

- `benchmark/` — 固定された実験用入力・参照資料
- `experiments/` — 各実験の条件、出力、ログ
- `notebooks/` — Kaggle等で使用する実行コード
- `reports/` — 実験レポート
- `docs/` — 方法論、評価基準、用語定義

## Methodology / 研究方法

共通の研究方法論：

- [研究方法論 / Methodology](./docs/methodology.md)
- [評価基準 / Evaluation Criteria](./docs/evaluation_criteria.md)

## Reproducibility / 再現性

各実験では、可能な限り以下を記録します。

- 使用モデル
- 実行環境
- generation parameters
- Seed
- Benchmark version
- 実際の入力ファイル
- 生の生成結果
- 評価結果

生成結果は、人手で修正した本文と混同しないよう、原則として未加工の状態で保存します。

## Articles / 記事

Qiitaにて、実験過程と結果を順次公開予定です。

## License / ライセンス

このリポジトリでは、用途に応じて複数のライセンスを使用します。

### Code / コード

ソースコード、Notebook、実行スクリプトは [MIT License](./LICENSE) で公開します。

### Benchmark and Documentation / ベンチマーク・文書

`benchmark/` 以下のナラティブベンチマーク資料および関連文書は [CC BY-NC 4.0](./benchmark/LICENSE.md) で公開します。

フィクション作品 **『かんなぎダイアリー / Kannabi Memorandum』** のキャラクター、設定、物語要素の著作権は作者に帰属します。CC BY-NC 4.0 は同ライセンス条件下での利用を許諾するものであり、著作権そのものを譲渡するものではありません。
