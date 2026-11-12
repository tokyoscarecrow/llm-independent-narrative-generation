# 評価サマリー — Experiment 02

## 評価結果

**Narrative Quality: Not Evaluated**

Gemma 3 4B ITについて、Benchmark v1.0を用いた物語生成品質評価は行っていません。

理由は、通常の日本語本文を安定して生成できるbaseline inferenceを構築できなかったためです。

## この実験で分かったこと

### 1. パラメータ数と導入容易性は別問題

4Bモデルだからといって、8Bモデルより必ず扱いやすいとは限りません。

Experiment 01ではQwen3-8BをKaggle T4環境で実行できました。

一方、Experiment 02のGemma 3 4Bでは、より小さいparameter scaleにもかかわらず、dtypeや量子化方式を変えても正常生成に到達できませんでした。

### 2. 「モデル性能」と「実行可能性」を分離して評価する必要がある

オープンLLMの比較では、少なくとも次の2段階を分ける必要があります。

```text
Stage 1: Runtime compatibility
  ↓
Stage 2: Task / narrative quality
```

Stage 1を通過していないモデルを、Stage 2の品質で他モデルと比較することはできません。

### 3. ローカルLLMではソフトウェアスタックも評価対象になる

商用APIでは隠蔽されている、

- dtype
- quantization
- GPU architecture
- model class
- library implementation
- device mapping

といった要素が、ローカル／オープンLLMでは直接結果へ影響します。

したがって、実用性評価では「モデルの能力」だけでなく、

> 自分の環境で安定して動かせるか

も独立した評価軸になります。

## 今後同モデルを再検証する場合

将来、以下の条件が変わった場合は再試験する価値があります。

- GPU世代
- VRAM容量
- Transformersバージョン
- bitsandbytes対応
- Gemma 3実装側の更新
- 推奨dtype / quantization手順

再検証する場合は、Experiment 02を上書きせず、新しいExperimentまたは再検証runとして記録します。
