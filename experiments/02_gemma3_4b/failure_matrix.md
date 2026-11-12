# Failure Matrix — Gemma 3 4B on Kaggle T4

この表は、保持されている実験記録から確認できる主な試行条件と結果を整理したものです。

| 条件 | GPU / dtype | decoding / quantization | 結果 |
|---|---|---|---|
| FP16 sampling | T4 / FP16 | sampling | inf / NaN系の確率tensorエラー、CUDA assertion |
| FP16 greedy | T4 / FP16 | greedy | `<pad>`相当tokenの反復 |
| FP32 2GPU | T4×2 / FP32 | standard generation | 改行・`bod`様出力の反復 |
| BF16 single GPU | T4 / BF16 | standard generation | token 107 / 改行様出力の反復 |
| bitsandbytes 4bit | T4 | 4bit | quantization state周辺でAssertionError |
| bitsandbytes 8bit | T4 | 8bit | loadは進むがwarning大量発生、正常本文なし |

## 判定基準

本実験では、以下を満たした場合のみナラティブ評価へ進む予定でした。

1. 日本語の通常文が連続して生成される
2. 特殊tokenやpad tokenの反復がない
3. generationが例外で停止しない
4. 同一条件で再実行可能
5. EP01_SC02を入力して少なくとも本文として評価できる

今回の試行では、いずれの条件もこの基準を満たしませんでした。

## 注意

ここでの「failed」は、Gemma 3 4Bというモデルそのものの品質評価ではありません。

あくまで、

> 当時のKaggle T4環境と使用ライブラリ構成で、安定した推論パイプラインを確立できなかった

という意味です。
