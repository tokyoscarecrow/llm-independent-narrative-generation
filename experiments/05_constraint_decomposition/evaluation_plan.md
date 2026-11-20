# Evaluation Plan — Experiment 05

## 評価方針

B0〜B3を各3 Seedで生成し、合計12 runを比較します。

```text
B0 × 3
B1 × 3
B2 × 3
B3 × 3
= 12 runs
```

B0はExperiment 04 A3と同条件ですが、Experiment 05ではruntime / library差の混入を避けるため、既存A3出力をそのままbaselineにはせず、同じKaggle sessionでB0も3 Seedすべて再生成します。既存A3は歴史的比較資料としてのみ参照します。

---

## 1. Scene Boundary Score

### 0 — 遵守

指定された教室内で終了し、次の出来事へ進まない。

### 1 — 軽微な延長

Scene終端後に短い説明や余韻があるが、新しいイベントは始まらない。

### 2 — 明確な境界逸脱

授業、休み時間、放課後など、次の時間帯・イベントへ進む。

### 3 — 大幅な逸脱

複数Scene相当を進み、帰宅・夜・翌日などまで生成する。

---

## 2. Reveal Violation Score

### 0 — 遵守

理由は伏せられ、疑問だけが残る。

### 1 — 軽微な具体化

理由そのものではないが、伏線が少し具体的すぎる。

### 2 — 部分的回答

みず葉の動機や過去を部分的に説明する。

### 3 — 明示的回答

Scene Questionへ直接回答する、またはSC03相当の情報を明かす。

---

## 3. Unsupported Additions

既存のLevel 0〜3を使用します。

特にLevel 2〜3の件数を条件間で比較します。

---

## 4. Secondary Checks

- Scene Question
- Character consistency
- Addressing
- Proper nouns
- Local coherence
- Meta-information leakage
- Style compliance

constraint追加によって、別の制御項目が悪化していないかも確認します。

---

## 5. 判定

### H1 support

B1およびB3で、B0/B2よりScene Boundary Scoreが低下する。

### H2 support

B2およびB3で、B0/B1よりReveal Violation Scoreが低下する。

### H3 support

B3で両方のScoreが同時に低い。

### H4 support

B1〜B3でCharacter / Addressing / Style等に大きな悪化がない。

---

## 6. 注意

3 Seedのみなので、統計的有意差を主張する実験ではありません。

目的は、

> 高次制約の構造化によって、複数Seedで一貫した方向性の改善が見られるか

を確認することです。
