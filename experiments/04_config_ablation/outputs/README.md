# Raw Outputs

Experiment 04の生出力保存用ディレクトリです。

## Conditions

```text
A0/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

A1/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

A2/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

A3/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt
```

## 保存方針

- 生成本文は未加工
- 誤字・呼称ミスも修正しない
- Scene境界逸脱部分を削除しない
- 人間による評価コメントを本文に混ぜない
- 原文が確認できないrunは記憶から再構成しない

## 注意

A1 Seed 42については、実験途中に入力状態の確認・再生成を行っています。

Benchmark記録として保存する場合は、**最終的に有効と判断したrunのみ**をraw outputとして採用し、途中の無効runと混同しないようにします。
