# Raw Outputs — Experiment 05

## Layout

```text
B0/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

B1/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

B2/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt

B3/
  seed_42.txt
  seed_31415.txt
  seed_27182.txt
```

## Policy

- Raw outputは未加工で保存する
- Scene境界逸脱部分も削除しない
- Reveal Policy違反も修正しない
- 評価コメントは別ファイルに記録する
- 再生成した場合はrunを区別し、都合のよい出力だけを選ばない
