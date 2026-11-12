# Experiment 04 — Qwen3-8B Config Ablation A0–A3

## 目的

Qwen3-8Bを固定し、入力するConfigレイヤーだけを段階的に追加することで、

> Scene Card / Character Context / Addressing Rules / Style Guide が、それぞれ生成結果のどの部分へ効くのか

を確認するアブレーション実験です。

モデル比較ではなく、**入力仕様の構造そのものを評価する実験**です。

## 固定条件

- Model: `Qwen/Qwen3-8B`
- `enable_thinking=False`
- Benchmark: `benchmark/v1.0`
- Scene: `EP01_SC02`
- Seeds:
  - 42
  - 31415
  - 27182

Generation parameters:

```text
temperature = 0.7
top_p = 0.8
top_k = 20
min_p = 0.0
do_sample = true
max_new_tokens = 2000
```

## Ablation Conditions

### A0 — Scene Card only

入力：

- Scene Card

### A1 — + Character Context

入力：

- Scene Card
- Character Context

### A2 — + Addressing Rules

入力：

- Scene Card
- Character Context
- Addressing Rules

### A3 — + Style Guide

入力：

- Scene Card
- Character Context
- Addressing Rules
- Style Guide

## 評価軸

- Scene構造
- Scene Question
- Character consistency
- 呼称・固有名詞
- 具体描写
- 設定外補完
- Scene境界
- Reveal Policy
- メタ情報漏出
- 局所整合性
- 文体制御

設定外補完は、以下のレベルで整理します。

```text
Level 0:
入力情報を自然に具体化しただけで、物語上の新情報を追加しない

Level 1:
物語上ほぼ無害な補完

Level 2:
新しい出来事・関係・背景など、物語上意味を持つ情報を追加

Level 3:
設定、プロット、伏線、情報開示を変更するレベルの追加
```

## A0で分かったこと

Scene Cardだけでも、

- B1 → B4の大枠
- Scene Question
- Sceneの基本目的

は比較的維持されました。

一方、キャラクターや学校生活の具体情報が不足しているため、

- 体育
- 宿題
- テスト
- スマートフォン
- ニュース

など、モデル独自の補完が入りました。

Seed 42では補完した「体育」の予定から、実際に体育のSceneまで話が進むなど、Scene境界逸脱も確認されました。

### A0の役割

**Scene Card → 何が起きるか / Scene構造**

という機能が最も明確に見えました。

## A1で分かったこと

Character Contextを加えると、

- 隼太の短い返答
- みず葉の距離の近さ
- みず葉が表情を見る行動
- 奨太郎の明るさ

など、人物固有の振る舞いが明確に反映されました。

一方で、

- Scene構造そのものはA0時点ですでに成立している
- 設定外補完は消えない
- 抽象心理表現は減らない
- Addressing Rulesがないため「隼太くん」「あなた」など呼称揺れが起こる

という結果でした。

### A1の役割

**Character Context → キャラクターがどう振る舞うか**

## A2で分かったこと

Addressing Rulesを加えると、3 Seedすべてで呼称精度が明確に改善しました。

特に、A1で「隼太くん」となった箇所が、A2では指定通り「隼太」になったケースがあり、局所制約としての効果がはっきり確認できました。

一方、

- Scene構造
- Character Contextの効果
- Reveal Policy
- 抽象心理表現

には大きな改善はありませんでした。

Seed 42では、Scene Questionを直接台詞化して答えまで言わせるReveal Policy違反も発生しましたが、他Seedでは再現しなかったため、Addressing Rulesの因果効果ではなくsampling variationと判断しています。

### A2の役割

**Addressing Rules → 誰が誰を何と呼ぶか**

## A3で分かったこと

Style Guideを加えると、局所的・形式的なルールは比較的よく反映されました。

### 効果が確認できたもの

- 常体
- 会話「」
- 内心（）
- 短文傾向
- 三人称近接・隼太寄り

### 効果が弱かったもの

- 現在形ベース
- 説明を最小限にする
- 行動・表情・感覚を優先する
- 抽象心理表現を抑える

「具体描写が増える」ケースはありましたが、

> 抽象表現を具体描写へ置き換える

のではなく、

> 具体描写を追加した上で、さらに抽象説明も行う

という形になりやすく、説明量そのものは十分に減りませんでした。

### A3の役割

**Style Guide → 表面形式には効くが、高次の文体制御には弱い**

## 全体結果

4条件を比較すると、各レイヤーの役割がかなり明確に分かれました。

```text
Scene Card
→ 何が起きるか / Scene構造

Character Context
→ キャラクターがどう振る舞うか

Addressing Rules
→ 誰が誰を何と呼ぶか

Style Guide
→ 表記・文体の局所形式
```

## 最も重要な知見

LLMは、

> 局所的・明示的・機械的な制約

ほど守りやすく、

> 抽象的・全体的・長距離の制約

ほど守りにくい傾向がありました。

本実験では、概ね次のような強弱が見られました。

### 強い

- 固定呼称
- 括弧形式
- 短文傾向
- 短い返答などの人物傾向

### 中程度

- 物理的距離
- 性格傾向
- MacroなScene構造

### 弱い

- 時制の統一
- 「説明するな」
- 感情を行動だけで示す
- 伏線を暗示のまま保持する

## 次の課題

高次の制約については、単にStyle Guideを長くするだけでは解決しない可能性があります。

今後は、

- 生成前の仕様分割
- 生成後のレビュー
- 段階生成
- 制約検査
- 別モデル／別パスによる校正

など、**生成そのものとは別の処理段階**を設ける必要がある可能性があります。

## 関連ファイル

- `parameters.yaml`
- `results_by_condition.md`
- `evaluation_summary.md`
- `outputs/README.md`
