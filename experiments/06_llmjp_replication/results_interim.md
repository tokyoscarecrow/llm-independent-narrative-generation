# Interim Results — Experiment 06

> Note: The original C0 / Seed 42 run was generated before the GPU-memory stabilization change and has been moved to `runtime/diagnostic_C0_seed42_pre_stabilization.txt`. Its evaluation below is retained only as a diagnostic observation and is **not part of the strict 12-run comparison series**. The strict series restarts from C0 / Seed 42 after runtime stabilization.

## C0 — Baseline

### Seed 42

Raw output:
`outputs/C0/seed_42.txt`

#### Primary evaluation

- Required Endpoint Completion: **0 — 到達**
  - 教室まで到達。
  - 住吉が登場。
  - 一度は日常の空気が戻る。
- Boundary Overrun: **3 — 大幅な逸脱**
  - 授業開始。
  - 次の科目。
  - 放課後。
  - 授業終了後の廊下。
  - 翌日の朝まで進行。
  - 複数Scene相当を連続生成している。
- Reveal Violation: **1 — 軽微な具体化**
  - 具体的な過去事件やみず葉の真の動機は明かしていない。
  - ただし「みず葉が僕のことを大切に思ってくれているという事実だ」と、関係性の意味を一段具体化している。
  - 「ただの幼馴染以上の意味があるのか」という方向づけも追加している。

#### Scene structure

Scene CardのB1〜B4に対応する要素は一部存在するが、
Scene単位としては大きく崩れている。

- B1相当: みず葉との登校
- B2相当: みず葉の視線・違和感
- B3相当: 住吉登場で空気が和らぐ
- B4相当: 予感

しかしB4後に終了せず、

- 授業
- 次の科目
- 放課後
- 授業後
- 翌朝

まで生成を継続。

#### Scene Question

Scene Questionを複数回ほぼ直接言語化している。

- 「どうして彼女はいつも僕の顔を覗き込むんだろう？」
- 「なぜ、みず葉はいつも僕のことを気にかけているのだろう？」
- 「なぜ、みず葉は僕を気にかけ続けるのか？」

暗示ではなく、設計上の問いを主人公の内心として反復。

#### Unsupported Additions

多数。特に意味・設定に関わる追加が大きい。

- みず葉と隼太が教室まで手を握って歩く
- 「昨日の放課後」にみず葉が急に黙り込んだ出来事
- 体育がサッカー
- 数学のテスト
- 次の科目
- 突然の雨
- 「もうすぐ夏休み」という9月設定との矛盾
- 「あの夏の日、何かが変わった」という未設定の過去
- 住吉がサッカー部であることを示唆
- 放課後のサッカー部練習
- 雨上がりの虹
- 翌朝の新Scene

複数の追加が設定・過去・Scene範囲を変更するため **Level 3**。

#### Local coherence

重大な問題あり。

- 九月上旬・二学期初日なのに「もうすぐ夏休みだね」。
- 「授業が始まり」→「次の科目」→「放課後」→「チャイムが鳴り、授業が終了」と時間進行が粗い。
- 住吉が授業中に「勢いよく入ってきた」ように描かれる。
- みず葉が「数学のテスト」と発言し、入力にない時間割情報を確定する。

#### Character / Addressing

部分的遵守。

- 隼太: 短い返答の傾向あり。
- みず葉: 明るく、隼太の顔を見る。
- 住吉: 陽気。
- 呼称自体は概ね指定範囲。

一方、
- みず葉と隼太の手つなぎはCharacter Contextの「距離が近い」を過剰解釈。
- 隼太がみず葉へ「はい」と返すなど、指定された常体・幼馴染の関係性から不自然な箇所あり。

#### Style Compliance

重大な違反。

- Narrator Person: **不遵守**
  - 指定は「三人称近接（隼太寄り）」。
  - 出力は一貫して一人称「僕」。
- Tense:
  - 現在形ベース指定に対し過去形中心。
- Register:
  - 常体は概ね維持。
- Inner Monologue:
  - （）を使用しており形式は遵守。
- Description:
  - 抽象心理表現が非常に多い。
- Sentence Length:
  - 短文中心というより長めの叙述も多い。

#### Meta-information / Design-language leakage

直接的な「次章」語はないが、

- 「新たな物語が始まるのだった」

と作者的・メタ的な締めを生成。

またScene Questionをそのまま繰り返しており、
design intentの本文露出が強い。

#### Repetition

意味反復が目立つ。

- 「なぜ、みず葉は…気にかけているのか」
- 「何かが違う / 何かが揺れている / 何かが起きる」
- 「心の奥」
- 予感・未来への説明

token loopではないが、設計上の疑問と抽象心理語を繰り返す。

#### C0 Seed 42の暫定解釈

LLM-jp Baselineでは、

1. Scene Cardの主要要素自体は拾う
2. しかしSceneを一つの閉じた単位として停止しない
3. Character Contextの局所傾向は利用する
4. Style Guideの視点指定（三人称近接）は大きく破る
5. Scene Questionを内心として直接反復する
6. 入力にない出来事・過去・授業・季節情報を積極的に補完する

という特徴が観測された。

ただし1 Seedのみなので、
これをLLM-jp固有傾向とはまだ断定しない。
