# Prompt Protocol — Experiment 05

## 目的

Experiment 05では、Experiment 04 A3と同じプロンプト構成をBaselineとして使用し、追加constraintだけを変更します。

## Base Instruction

Experiment 04で使用した生成指示：

```text
以下の情報をもとに、指定されたシーンの小説本文を生成してください。
与えられた情報を尊重し、指定されたシーンの本文を書いてください。
```

この2文以外の追加自然言語指示は加えません。

## Prompt Order

Baseline（B0）の連結順：

```text
Base Instruction

# Scene Card
<scene_card.yaml>

# Character Context
<character_context.yaml>

# Addressing Rules
<addressing_rules.yaml>

# Style Guide
<style_guide.yaml>
```

B1では末尾に：

```text
# Scene Boundary
<scene_boundary.yaml>
```

B2では末尾に：

```text
# Reveal Constraints
<reveal_constraints.yaml>
```

B3では両方をこの順序で追加します。

## Publication-only Notes

`benchmark/v1.0/inputs/EP01_SC02/character_context.yaml` と
`addressing_rules.yaml` には、Benchmark公開時に追加した
`benchmark_note:` セクションがあります。

これらがExperiment 04の実入力に含まれていた証拠はないため、
Experiment 05の生成入力からは除外します。

除外対象は `benchmark_note:` 以降の公開用注記だけです。
YAML本体のその他の内容・順序は変更しません。

## Chat Template

```python
messages = [{"role": "user", "content": prompt}]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)
```

## Generation

```text
do_sample = true
temperature = 0.7
top_p = 0.8
top_k = 20
min_p = 0.0
max_new_tokens = 2000
```

Seed:

- 42
- 31415
- 27182

## Experimental Rule

評価対象runでは出力後に追加指示を行いません。

入力または実行条件を変更した場合は、別runとして扱います。
