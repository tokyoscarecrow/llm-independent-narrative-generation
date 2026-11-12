# Experiment 02 — Gemma 3 4B Runtime Compatibility on Kaggle T4

## 目的

Gemma 3 4B ITをKaggle NotebookのTesla T4環境で実行し、Benchmark v1.0を用いたナラティブ生成評価へ進めるかを確認するためのruntime compatibility実験です。

この実験では、**物語生成品質の比較評価まで到達していません**。

複数のdtype、モデルクラス、GPU配置、量子化方式を試しましたが、安定した日本語本文生成を確立できなかったためです。

したがって、このExperiment 02の主題は、

> Gemma 3 4Bは物語生成に向いているか

ではなく、

> Gemma 3 4BをKaggle T4環境で安定して推論できるか

です。

## Benchmark

- Benchmark: `benchmark/v1.0`
- Scene: `EP01_SC02`
- Title: 「何も起きない朝」

ただし、Benchmark本文生成の品質評価に入る前のsanity test段階で推論異常が継続したため、ナラティブ評価は実施していません。

## 実行環境

- Platform: Kaggle Notebook
- GPU: Tesla T4 × 2
- Framework: Hugging Face Transformers
- Model: `google/gemma-3-4b-it`

当時の正確なTransformers / PyTorch / bitsandbytesの固定バージョンは、保持記録から完全には確認できていません。

## 試行した主な条件

### 1. FP16 + sampling

Gemma 3 ConditionalGeneration系の実行で、sampling時に数値異常が発生しました。

代表的な症状：

```text
probability tensor contains either inf, nan or element < 0
```

CUDA assertionを伴うケースもありました。

### 2. FP16 + greedy

samplingを切り、greedy decodingへ変更しました。

しかし正常な本文は生成されず、

```text
<pad>
<pad>
<pad>
...
```

のようにtoken 0相当の出力が反復しました。

### 3. FP32 + 2 GPU split

FP32で2GPUへ分割し、`Gemma3ForCausalLM` を使用する構成も試しました。

この条件では、

- 改行
- `bod`

などの特殊・非本文トークンに近い出力が反復し、正常な日本語本文にはなりませんでした。

### 4. BF16 + single GPU

BF16・単一GPUでも試行しました。

この場合も、特定token（保持記録ではtoken 107）に偏り、改行の反復となって正常生成には至りませんでした。

### 5. bitsandbytes 4bit

4bit量子化も試しましたが、bitsandbytes内部のquantization state周辺で `AssertionError` が発生しました。

### 6. bitsandbytes 8bit

8bit量子化ではモデルロードまでは進みました。

ただし実行時には、

```text
MatMul8bitLt: inputs will be cast from torch.bfloat16 to float16 during quantization
```

といったwarningが大量に出力され、正常な日本語本文生成には至りませんでした。

## 結果

今回のKaggle T4環境では、Gemma 3 4B ITについて、

- FP16
- FP32
- BF16
- 4bit
- 8bit
- sampling
- greedy
- single GPU
- multi GPU split

など複数条件を試しても、安定した日本語本文生成を確立できませんでした。

そのため、EP01_SC02のナラティブ生成品質は**評価不能**としました。

## 重要な解釈

この結果から、

> Gemma 3 4Bは物語生成能力が低い

とは結論しません。

今回確認できたのは、

> このKaggle T4環境・ライブラリ構成・dtype / quantization条件では、安定推論環境を構築できなかった

という点までです。

## 得られた知見

この実験から、ローカル／オープンLLMの実用性を考える際には、モデルサイズだけでは不十分だと分かりました。

```text
小さいモデル
≠
必ず軽い
≠
必ず動かしやすい
```

実際の運用可否には、

- GPU architecture
- VRAM
- dtype
- quantization
- model implementation
- Transformers / bitsandbytes等のライブラリ対応

が大きく影響します。

## Experiment 01との違い

Experiment 01では、モデルを正常に動かした上でナラティブ生成品質を比較しました。

Experiment 02では、その前段階である

> 「安定した推論が可能か」

を通過できませんでした。

したがって、この実験はナラティブ性能比較ではなく、**runtime compatibility / deployabilityの記録**として扱います。

## 関連ファイル

- `parameters.yaml` — 試行条件
- `failure_matrix.md` — 条件ごとの結果一覧
- `evaluation_summary.md` — 実験結果の解釈
- `logs/README.md` — ログ保存方針
