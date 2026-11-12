# Kannagi Diary Benchmark v1.0

## Purpose

This directory is a frozen benchmark snapshot for evaluating LLM-based narrative generation.

It is **not** the latest production data for the fictional work. The production project may continue to change, while this benchmark remains fixed so that experiments can be compared under the same input conditions.

## Benchmark Scene

- Project: かんなぎダイアリー / Kannabi Memorandum
- Scene: EP01_SC02
- Title: 何も起きない朝
- Setting: 六ッ川高校・昇降口〜教室
- Benchmark version: v1.0

## Data Layers

This benchmark separates two kinds of data.

### reference/

Human-authored narrative design information that existed before prose generation.

These files are provided so that readers can distinguish:
- what the human author had already designed,
- what was converted into structured LLM input,
- and what the LLM added during generation.

### inputs/EP01_SC02/

The structured data actually used as the basis of the benchmark experiments.

- scene_card.yaml
- character_context.yaml
- addressing_rules.yaml
- style_guide.yaml

The benchmark experiments may combine these files differently depending on the condition being tested.

For example, the Config Ablation experiment uses:

- A0: Scene Card only
- A1: A0 + Character Context
- A2: A1 + Addressing Rules
- A3: A2 + Style Guide

## Important Experimental Constraint

The Character Context in this benchmark is intentionally limited to information supplied during the experiment.

In particular, some production-story information about the characters is omitted when it was not part of the benchmark input. This prevents later production revisions or hidden background knowledge from contaminating the evaluation.

## Provenance

Production source repository:

`tokyoscarecrow/kannagi-diary-devlog`

Reference commit at benchmark preparation:

`5ebb5a86d0683ccf8980fb468b644d3899dad097`

See `manifest.yaml` for the source files and blob identifiers used to construct this snapshot.

## Versioning Policy

Files under `benchmark/v1.0/` are frozen.

If the benchmark definition changes, create a new version such as `v1.1` or `v2.0` rather than modifying v1.0.

## License

Benchmark and narrative documentation are licensed under CC BY-NC 4.0.

See:

`benchmark/LICENSE.md`
