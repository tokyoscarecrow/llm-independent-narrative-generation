# 評価基準 — Evaluation Criteria

この文書は、本リポジトリで行うナラティブ生成実験の共通評価基準を定義します。

数値スコア化そのものを目的とせず、異なるExperiment間で同じ観点から比較できることを重視します。

---

## 1. Scene Structure / Scene構造

### 評価対象

- Beatの順序
- Scene Goal
- Sceneの開始位置
- Sceneの終了位置
- 必要な出来事の有無

### 良好

Scene Cardに定義されたBeatが概ね順序通りに実装される。

### 問題例

- Beatが欠落する
- B2とB3が逆転する
- 同じBeatを何度も繰り返す
- Scene終了後も新しい展開を続ける

---

## 2. Scene Question

### 評価対象

Scene Cardに設定された中心的な問いが、Scene内で適切に機能しているか。

### 良好

Scene Questionが読者の疑問として残り、Sceneの感情的フックになる。

### 問題例

- Scene Question自体を台詞として読み上げる
- Questionの主語・目的語が反転する
- Scene内で答えまで説明する

---

## 3. Character Consistency / キャラクター整合性

### 評価対象

Character Contextに定義された、

- 性格
- 行動傾向
- 話し方
- 一人称
- 距離感
- 反応傾向

が維持されているか。

### 問題例

- 無口な人物が長広舌になる
- 明るい人物が理由なく陰鬱になる
- 一人称が変わる
- 関係性にない行動を取る

---

## 4. Addressing / 呼称

### 評価対象

Addressing Rulesに従い、人物同士の呼び方が正しいか。

### 問題例

指定：

```text
みず葉 → 隼太 = 「隼太」
```

生成：

```text
「隼太くん」
「あなた」
```

など。

呼称は局所的かつ明示的な制約であり、本研究では比較的評価しやすい項目です。

---

## 5. Proper Nouns / 固有名詞

### 評価対象

- 人名
- 地名
- 組織名
- 作品固有語

が崩れず維持されるか。

### 問題例

- 漢字の一部が英語tokenへ崩れる
- 別人名へ変化する
- 読み違いを本文へ混入する

---

## 6. Reveal Policy / 情報開示制御

### 評価対象

Scene内で、

- 何を明かしてよいか
- 何を伏せるべきか

が守られているか。

### 良好

「伏線のみ」と指定された情報は、疑問や違和感として残る。

### 問題例

- 理由を説明する
- 動機を台詞で明かす
- 後のSceneで判明する情報を先に出す
- 「次章で明らかになる」などメタ的に説明する

---

## 7. Unsupported Additions / 設定外補完

入力に存在しない情報を、LLMが独自に追加した度合いを評価します。

### Level 0 — Natural Realization

入力情報を自然な具体描写へ変換しただけ。

例：

- 「距離が近い」→ 隣に並ぶ
- 「表情を見る」→ 顔を覗き込む

物語上の新情報は増えていない。

### Level 1 — Harmless Supplementation

設定にない細部だが、物語上ほぼ影響しない。

例：

- 教科書
- ポスター
- 朝の雑談
- 軽い天候描写

### Level 2 — Story-Meaningful Addition

物語上意味を持つ新規情報や出来事を追加する。

例：

- 今日テストがある
- 放課後に約束がある
- 体育の時間に話す予定を作る

### Level 3 — Plot / Reveal Change

設定、プロット、伏線、情報開示を変更する。

例：

- キャラクターの過去を新規作成
- Scene Questionの答えを生成
- 未設定の関係変化を確定
- 後の展開を先に決める

---

## 8. Scene Boundary / Scene境界

### 評価対象

指定された時間・場所・Scene範囲を守るか。

### 良好

EP01_SC02なら、

> 昇降口〜教室

の範囲でSceneを終了する。

### 問題例

- 授業まで進む
- 放課後へ進む
- 帰宅する
- 夜まで描写する
- 次Scene相当の出来事を開始する

---

## 9. Local Coherence / 局所整合性

文章内部の短距離整合性を評価します。

### 問題例

- Aが質問したのにBではなくCが答える
- すでに学校へ到着しているのに「一緒に登校する？」と言う
- 直前の動作と矛盾する
- 人物の位置関係が破綻する

MacroなScene構造とは別に評価します。

---

## 10. Meta-information Leakage / メタ情報漏出

Scene CardやStyle Guideなどの**制作側メタ情報**が、そのまま本文へ露出していないかを評価します。

### 問題例

- 「常体のまま」
- 「このSceneでは」
- 「次の章で明らかになる」
- 「奨太郎が登場した」
- Beat名やScene Goalを文章中で説明する

---

## 11. Style Compliance / 文体制御

### 評価対象

Style Guideで指定された、

- narrator person
- tense
- register
- sentence length
- dialogue format
- inner monologue format
- explanation density

など。

### Local / Mechanical Rules

比較的守られやすい傾向：

- 「」を使う
- （）を使う
- 常体
- 短文傾向

### Global / Abstract Rules

守られにくい傾向：

- 現在形を維持する
- 説明を減らす
- 行動だけで感情を示す
- 抽象心理表現を使わない
- 伏線を暗示に留める

---

## 12. Abstract Psychological Language / 抽象心理表現

本研究では、以下のような表現が反復するかを別途観察します。

例：

- 何か
- 違和感
- 胸の奥
- 心の奥
- 不安
- 予感

これら自体を禁止するわけではありません。

ただし、Scene Cardに書かれた抽象概念を、そのまま本文の心理説明へ変換している場合、

> 構造化された設計概念を、具体的な演技・行動へ変換できていない

可能性があります。

---

## 13. Repetition / 反復

### 評価対象

- 同一段落
- 同一文
- 同一フレーズ
- 同一意味内容

が不自然に繰り返されないか。

反復は、

- generation parameters
- model capability

の両方が原因になり得るため、他項目と分けて記録します。

---

## 14. Runtime Compatibility

ローカル／オープンLLMでは、本文品質評価の前に実行可能性を確認します。

### Pass

- 通常文が生成される
- 特殊token反復がない
- 例外停止しない
- 再実行可能

### Fail

- NaN / inf
- CUDA assertion
- pad token反復
- 特殊token反復
- quantization error
- 正常本文が出ない

Runtime Failの場合、Narrative Qualityは**Not Evaluated**とします。

---

## 15. 評価時の基本ルール

評価では、次を区別します。

### Input Failure

仕様自体に必要情報がない。

### Sampling Variation

Seedによってのみ発生する単発の現象。

### Model Tendency

複数Seedで繰り返す現象。

### Runtime Failure

モデル品質を評価する前の実行環境上の問題。

この区別を行うことで、

> 一度変な出力が出た  
> = モデルが悪い

という単純な結論を避けます。
