# Interim Results — Experiment 06

> Note: The original pre-stabilization C0 / Seed 42 run is retained at `runtime/diagnostic_C0_seed42_pre_stabilization.txt`. After the GPU-memory stabilization change, C0 / Seed 42 was regenerated under the strict comparison runtime and produced an **exactly identical output**. The evaluation below therefore now applies to the formal C0 / Seed 42 run stored at `outputs/C0/seed_42.txt`.

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


### Seed 31415

Raw output:
`outputs/C0/seed_31415.txt`

#### Generation termination

The raw Harmony response ended with:

```text
...そのとき、遠くから大きな笑い声が聞こえてき<|return|>
```

Therefore the truncation was **not caused by `parse_response()`**.
The model itself emitted the Harmony return token while the Japanese sentence was incomplete.

This run is retained as a valid experimental output.

#### Primary evaluation

- Required Endpoint Completion: **2 — 未到達**
  - 教室終端状態へ到達していない。
  - 住吉はまだ登場しておらず、遠くの笑い声で終了。
- Boundary Overrun: **0 — 遵守**
  - Scene後方への進行はない。
  - ただしこれは正しい停止ではなく、早すぎる終了。
- Reveal Violation: **0 — 遵守**
  - みず葉が隼太を気にかける具体的理由は明かしていない。
  - 「いつも僕の様子をチェックしているのだろうか」は関心の観察であり、理由の回答には至らない。

#### Scene structure

- B1: みず葉との遭遇・挨拶はある。
- B2: みず葉が隼太の顔を見る違和感はある。
- B3: 住吉登場前に終了。
- B4: 未到達。

#### Scene Question

Scene Questionそのものの「なぜ気にかけるのか」は直接書いていないが、
「いつも僕の様子をチェックしているのだろうか」と近接した疑問を内心化している。

#### Unsupported Additions

主な追加：

- 昇降口の場面なのに「机の上には昨日の宿題」が存在する
- ノートに「今日の授業は何？」という走り書き
- みず葉が階段を下りてくる
- 「今日はどんな一日になるんだろうね」という台詞

大半は局所的補完だが、場所関係の不整合を含む。
暫定 **Level 2**。

#### Local coherence

問題あり。

- 冒頭で昇降口にいるのに、直後に「机の上には昨日の宿題」が現れる。
- みず葉が「肩越しに背後の黒板を見る」とあるが、場面位置が昇降口／廊下のままで空間的に不明瞭。
- 文の途中でHarmony return tokenを出して終了。

#### Character / Addressing

- みず葉は明るく、隼太の表情を見る点を拾っている。
- 隼太は短く返答。
- 呼称は大きな破綻なし。

#### Style Compliance

重大な違反。

- 指定「三人称近接（隼太寄り）」に対し、一人称「僕」。
- 現在形ベース指定に対し過去形中心。
- 内心の（）は遵守。
- 比喩・抽象心理語が多い。

#### Interim significance

C0の2 Seed時点で、両方とも三人称近接指定を外れて一人称「僕」になった。

一方、Scene Rangeは大きく異なる。

- Seed 42: 大幅Overrun
- Seed 31415: Endpoint未到達の早期終了

したがってBaseline問題は単純な「長く書きすぎる」ではなく、
**Sceneの適切な終端状態を安定して認識・保持できていない**
可能性がある。
