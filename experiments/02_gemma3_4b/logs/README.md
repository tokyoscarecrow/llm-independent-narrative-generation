# Logs

このディレクトリには、Experiment 02で得られた実行ログを保存します。

## 保存方針

- error messageは可能な限り原文のまま保存する
- warningを要約する場合は、元ログと分離する
- 正常出力が存在しない場合、推測で本文を再構成しない
- Notebookのセル出力と手動評価を混同しない
- 同一条件の再実行結果はrun単位で分ける

## 現在の状態

保持記録から確認できる代表的な現象は、`failure_matrix.md` と `parameters.yaml` に整理しています。

完全な生ログが確認できた場合のみ、このディレクトリへ追加します。

## 想定ファイル名

```text
fp16_sampling.log
fp16_greedy.log
fp32_two_gpu.log
bf16_single_gpu.log
bnb_4bit.log
bnb_8bit.log
```

これらは実際の元ログが確認できた場合にのみ作成します。
