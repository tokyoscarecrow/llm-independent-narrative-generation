# Prompt Protocol — Experiment 06

## Principle

Experiment 05と同じNarrative Specificationを使用する。

モデル固有差として変更するのは、
LLM-jp tokenizer / chat templateと、Stage 2で確定するgeneration parametersのみ。

## Base Instruction

```text
以下の情報をもとに、指定されたシーンの小説本文を生成してください。
与えられた情報を尊重し、指定されたシーンの本文を書いてください。
```

追加の自然言語指示は加えない。

## Prompt Order

C0:

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

C1:

```text
C0
+ # Scene Boundary
  <scene_boundary.yaml>
```

C2:

```text
C0
+ # Reveal Constraints
  <reveal_constraints.yaml>
```

C3:

```text
C0
+ # Scene Boundary
  <scene_boundary.yaml>
+ # Reveal Constraints
  <reveal_constraints.yaml>
```

## Publication-only Notes

Benchmark公開時に追加した `benchmark_note:` は生成入力から除外する。

対象：

- `character_context.yaml`
- `addressing_rules.yaml`

除外対象は `benchmark_note:` 以降のみ。
その他の内容・順序は変更しない。

## Chat Template

LLM-jpモデル付属tokenizerのchat templateをそのまま使用する。

```python
chat = [{"role": "user", "content": prompt}]

input_ids = tokenizer.apply_chat_template(
    chat,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt",
)
```

OpenAI Harmony互換形式を意識したtemplateだが、
外部Harmony tokenizerは使用しない。

## Generation

Stage 1 Runtime Test成功後、Stage 2で確定する。

確定後はC0〜C3の12 run中で変更しない。

## Seeds

- 42
- 31415
- 27182

## Experimental Rule

評価対象runでは出力後に追加指示・対話修正を行わない。

入力・runtime・generation条件を変更した場合、
同一比較runとして扱わない。
