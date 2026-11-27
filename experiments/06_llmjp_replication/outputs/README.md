# Raw Outputs — Experiment 06

## Layout

```text
C0/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

C1/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

C2/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

C3/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt
```

## Policy

- Raw outputは未加工で保存する
- 失敗・反復・境界逸脱・Reveal違反を削除しない
- 評価コメントは別ファイルへ記録する
- 都合のよいSeedだけを選ばない
- Runtime Testの出力はNarrative Raw Outputに含めない
