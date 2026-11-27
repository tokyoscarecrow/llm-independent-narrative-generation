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


### Seed 27182

Raw output:
`outputs/C0/seed_27182.txt`

#### Primary evaluation

- Required Endpoint Completion: **0 — 到達**
  - 教室へ到達。
  - 住吉が登場。
  - 住吉の明るさで空気が和らぐ。
  - 理由不明の違和感／疑問を残す。
- Boundary Overrun: **1 — 軽微な延長**
  - 授業開始直前まで進み、終端後の描写が長い。
  - 明確な授業内容・放課後・翌日までは進まない。
  - ただし教室到達後に再びドアを開けて廊下へ出たような空間的不整合がある。
- Reveal Violation: **2 — 部分的回答**
  - 「夏祭りの夜」「二人が最後に約束した言葉」「続く沈黙の時間」という具体的な過去を新規創作。
  - みず葉が「もし何か起きたら、私が手伝う」と述べ、気にかける意味を保護・支援方向へ狭める。
  - 真の理由の明示ではないが、伏線を具体化しすぎている。

#### Scene structure

B1〜B4に相当する主要要素は揃っている。

- B1: みず葉との登校・教室移動
- B2: みず葉が隼太を見る違和感
- B3: 住吉登場で空気回復
- B4: 理由不明の疑問・予感

構造自体はC0三本中もっとも完結している。

#### Scene Question

Scene Questionをほぼそのまま直接本文化。

```text
「なぜ、みず葉は俺を気にかけてくれるのだろう？」
```

暗示ではなく明示的な疑問文。

#### Unsupported Additions

重大な新規情報が多数ある。

- 隼太が遅刻している設定
- 前日に文化祭があった設定
- 文化祭ステージの具体的記憶
- 数学教師の交代
- 新教材
- 夏祭りの夜
- 二人が交わした最後の約束
- その後の沈黙
- みず葉の「何か起きたら手伝う」
- 9月上旬なのに桜の花びら

物語上の過去・関係性・学校状況・伏線を変更するため **Level 3**。

#### Local coherence

重大な問題あり。

- 「二学期初日」の前日が文化祭になっている。
- 9月上旬なのに桜の花びらが舞う。
- 教室へ入った後、席につく流れの直後に再び「教室のドアを開け」、三人の足音が廊下へ響く。
- 「季節は秋へと移り変わろうとしていた」と9月上旬の季節認識が曖昧。
- 「ロッカーの鍵」「水たまり」など未設定物が場面構造を混乱させる。

#### Character / Addressing

部分的違反。

- みず葉→隼太「隼太」: 遵守。
- みず葉→住吉は指定「住吉」だが、出力は **「奨太郎」**: 違反。
- 隼太の一人称はCharacter Contextでは「僕」だが、Scene Questionでは **「俺」**: 違反。
- 住吉の陽気さは拾っている。

#### Style Compliance

重大な違反。

- 地の文自体は三人称だが、会話が
  `**みず葉**：`
  `**隼太**：`
  のような脚本・台本形式へ崩れる。
- 「小説本文」というOutput Formatから逸脱。
- 現在形ベース指定に対し過去形中心。
- 内心を（）で表す点は拾うが、台詞ラベルと組み合わされ脚本化。
- 抽象心理・比喩が多い。

#### Meta-information / Design-language leakage

非常に強い。

- Scene title `「何も起きない朝」` を内心として直接使用。
- Scene Questionを直接使用。
- 最終行:
  `―ここで物語は次の章へと続く。―`
  と明示的なメタ予告。

#### C0 — 3 Seed Summary

| Seed | Endpoint | Overrun | Reveal | Unsupported |
|---|---:|---:|---:|---|
| 42 | 0 | 3 | 1 | 3 |
| 31415 | 2 | 0 | 0 | 2 |
| 27182 | 0 | 1 | 2 | 3 |

### C0 Baseline observations

#### 1. Scene endpoint control is unstable

Three seeds show three different stopping behaviors.

- Seed 42: major overrun to class / after school / next morning
- Seed 31415: early termination before Sumiyoshi appears
- Seed 27182: reaches endpoint but continues with a mild extension

Therefore the baseline issue is not simply verbosity.
The model does not stably realize the Scene Card's intended endpoint.

#### 2. Style / output-form control is weak

- Seeds 42 and 31415 shift into first-person narration despite the third-person-close requirement.
- Seed 27182 keeps third-person narration but shifts dialogue into labeled script format.
- Present-tense preference is not maintained.

Different seeds violate the Style Guide in different ways.

#### 3. Semantic supplementation is aggressive

Across seeds, the model invents:

- school schedules
- tests / teachers / club activities
- weather events
- previous-day events
- summer memories
- festivals / promises
- relationship implications

Some additions contradict the supplied September / second-semester setting.

#### 4. High-level intent leaks into prose

Across seeds, design intent is often verbalized rather than realized.

- Scene Question becomes internal dialogue.
- Scene title appears directly in Seed 27182.
- Meta-story closure appears in Seeds 42 and 27182.

#### 5. Local character cues are easier than global realization rules

Despite major global failures, the model often preserves:

- Mizuha's brightness
- Mizuha watching Shunta
- Shunta's short replies
- Sumiyoshi's cheerful energy

This resembles the earlier observation that local/mechanical information is easier to realize than global/abstract narrative intent.

### C0 provisional conclusion

LLM-jp-4-8b-instruct can use the Scene Card and Character Context to construct a recognizable version of the scene, but the baseline does not stably control:

- where the scene ends
- output form
- narrative viewpoint
- unsupported semantic additions
- implicit handling of the Scene Question

The three-seed baseline is sufficiently unstable to make C1 Scene Boundary a meaningful next test.


## C1 — Scene Boundary

### Seed 42

Raw output:
`outputs/C1/seed_42.txt`

#### Primary evaluation

- Required Endpoint Completion: **0 — 到達**
  - 教室へ到達。
  - 住吉が登場。
  - 住吉の明るさで空気が和らぐ。
  - 理由不明の予感を残す。
- Boundary Overrun: **2 — 明確な境界逸脱**
  - 先生が黒板に数式を書き、授業が開始。
  - 授業終了まで進行。
  - 次の体育へ移行。
  - C1のforbidden_after_endに明示された「授業開始後の出来事」を描写している。
- Reveal Violation: **0 — 遵守**
  - みず葉が隼太を気にかける具体的理由は明かしていない。
  - ただし「みず葉が自分を気に掛け続ける理由は…掴めなかった」とScene Questionを説明的に言語化しているため、Realization-level controlは弱い。

#### Scene Boundary effect relative to C0 / Seed 42

- C0 Seed 42: Endpoint 0 / Overrun 3
- C1 Seed 42: Endpoint 0 / Overrun 2

Scene Boundary追加により、翌朝まで進む大幅逸脱は抑えられたが、
required_state到達後のstop_ruleは守られなかった。

したがってこのSeedでは **partial improvement**。

#### Scene structure

B1〜B4は概ね成立。

- B1: みず葉との朝
- B2: みず葉の視線・違和感
- B3: 住吉登場で空気回復
- B4: 理由不明の予感

ただしB4後も授業開始・授業終了・次時限へ進行。

#### Scene Question / Realization

具体的な答えは出していないが、

```text
みず葉が自分を気に掛け続ける理由は、
今日の短いやり取りだけでは掴めなかった。
```

と、設計上の疑問を説明的に本文化。

暗示化ではなく「理由は不明」と説明する方式。

#### Unsupported Additions

主要な追加：

- 先生がすでに黒板前に座っている
- 住吉が遅刻ぎりぎり
- 住吉が机の上に飛び乗る
- 教師が数式を書く
- 次の授業が体育
- 桜並木（9月上旬と季節矛盾）
- 教室の灯りが暗くなる
- 次の授業で何かが起きるという予告

Scene進行と学校状況を新規追加しており **Level 3**。

#### Character / Addressing

- みず葉の明るさ、隼太を見る傾向は保持。
- 住吉の陽気さも保持。
- 呼称の大きな逸脱は少ない。
- ただし「水葉」という表記揺れ／誤記が1箇所ある。

#### Style Compliance

C0より改善。

- 地の文は三人称で、隼太寄り。
- 一人称Narratorへの崩れはない。
- 内心（）も使用。

ただし、
- 過去形中心でpresent-tense preferenceを守らない。
- 抽象心理語が多い。
- 「心の中でつぶやくように言ったが、口には出さなかった」など表現が不安定。

#### Meta-information leakage

最後に、

```text
――以上が、二学期初日の教室で交わされた、
静かで確かな“何も起きない”朝の物語です。
```

と作者的メタ要約を付加。

Scene title相当の「何も起きない」を本文外メタ表現として露出。

#### Cross-model note

Experiment 05 Qwen3 B1 Seed 42は Endpoint 0 / Overrun 0 だった。

LLM-jp C1 Seed 42は Endpoint 0 / Overrun 2。

同じScene Boundary constraintでも、
このSeedではQwen3ほどstop_ruleが効いていない。

ただし単一Seed比較なので、C1三本が揃うまではモデル差と断定しない。
