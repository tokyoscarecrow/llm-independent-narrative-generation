# 条件別結果 — Experiment 04

## A0 — Scene Card only

### Seed 42

- B1 → B4の大枠は維持
- Scene Questionの向きが一部台詞内で反転
- 「体育の時間に話す」という予定を新規追加
- その後、実際に体育のSceneまで生成
- Scene境界逸脱
- 抽象心理語が多い

### Seed 31415

- A0の中では最も構造忠実度が高い
- B1 → B4が明瞭
- Scene Question保持
- Scene境界も概ね維持
- 宿題・テスト・ポスター等の軽い補完
- 抽象心理語は残存

### Seed 27182

- 必要要素は概ね保持
- B2 / B3の順序がやや曖昧
- スマートフォンやニュース等を補完
- Scene境界は概ね維持
- 抽象心理語は残存

### A0まとめ

Scene CardだけでもMacroなScene構造はかなり制御できる。

一方、人物や日常行動の空白はモデルが独自に補う。

---

## A1 — + Character Context

### Seed 42

- 隼太の短い返答
- みず葉の距離の近さ
- みず葉が表情を見る行動
- 奨太郎の明るさ

などが明確に反映。

A0で見られた大きな体育Scene補完は消え、Scene境界は安定。

一方、みず葉が一部で丁寧体を使うなど、人物制御は完全ではない。

### Seed 31415

- Character Contextの効果は明確
- Addressing Rulesがないため、みず葉→隼太が「隼太くん」
- 宿題・テスト等の補完は残る
- Scene Question保持
- Scene境界は良好

### Seed 27182

- 人物傾向が強く反映
- 「あなた」など呼称揺れ
- 局所的な会話整合性の問題
- 到着後に「一緒に登校する？」と発言するなど時系列上の不自然さ
- Macro構造は維持

### A1まとめ

Character Contextは人物行動を制約する。

ただし、イベントや世界の空白を埋める補完は止めない。

---

## A2 — + Addressing Rules

### Seed 42

- 呼称は指定通り
- Character Contextの効果も維持
- 一方、Scene Questionを直接台詞化
- みず葉が「わたしが、隼太に会いたいからだよ」と部分的に答える
- Reveal Policy違反

### Seed 31415

- A1で「隼太くん」だった箇所が、A2では「隼太」に修正
- 全呼称が指定通り
- Character Contextの効果維持
- Reveal Policy良好
- Scene境界良好
- 一部Beatの入り組み

### Seed 27182

- 全呼称が指定通り
- Scene Question保持
- Reveal Policy良好
- Scene境界良好
- 抽象説明は残る

### A2まとめ

Addressing Rulesは呼称という局所制約に強く効く。

一方、Scene構造やReveal Policyそのものを改善するものではない。

---

## A3 — + Style Guide

### Seed 42

- 内心の（）使用が明確
- 常体
- 短文傾向
- 時制は現在形に統一されず、過去形が混在
- 「何か」「違和感」「心に残る」等の抽象表現が残る
- Scene Questionを内心で繰り返す
- 「奨太郎が登場した」など設計語に近い表現あり

### Seed 31415

- B1 → B4が比較的明瞭
- Reveal Policy良好
- Scene境界良好
- （）による内心あり
- 現在形と過去形が混在
- 具体的な視線・距離描写は増える
- ただし抽象説明も併記される

### Seed 27182

- 短文傾向が特に強い
- 呼称・人物傾向・Reveal Policyは良好
- B2 / B4的な違和感を繰り返す傾向
- Scene Questionを複数回明示
- 抽象心理表現が多い
- 時制は混在

### A3まとめ

Style Guideは、

- 常体
- 「」
- （）
- 短文傾向

など、表面形式には比較的強く効く。

一方、

- 時制統一
- Show, don't tell
- 説明の抑制
- 抽象心理表現の抑制

には弱い。
