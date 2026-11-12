# Raw Outputs

このディレクトリには、Experiment 01で実際に生成された**未加工の本文**を保存します。

## 方針

- 誤字・固有名詞崩れも修正しない
- 反復も削除しない
- 人間による補筆を行わない
- 評価コメントを本文へ書き込まない
- 原データが確認できない出力を、記憶や要約から再構成しない

## 現在の状態

過去の実験結果については、チャット記録・保存ログ・Notebook出力などから原文を確認できたものだけを順次追加します。

正確な原文を確認できないrunについては、READMEやレポートに観察結果を記載しても、raw outputとしては保存しません。

## 推奨ファイル名

今後追加する場合は、例えば次の形式を使用します。

```text
gemma2_2b_it/
  run_scene_card_only.txt
  run_character_addressing.txt
  run_tuned_decoding.txt
  run_full_stack.txt

qwen3_8b/
  run_initial_parameters_seed42.txt
  run_qwen_parameters_seed42.txt
```

ファイル名は実際の保存データと対応する場合のみ作成します。
