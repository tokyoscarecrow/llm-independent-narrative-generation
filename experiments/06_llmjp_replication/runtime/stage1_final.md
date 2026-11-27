# Stage 1 Runtime Compatibility — Final

## Status

**PASS**

## Environment

- Date: 2026-11-27
- Python: 3.12.13
- PyTorch: 2.10.0+cu128
- Transformers: 5.0.0
- CUDA runtime: 12.8
- GPU: Tesla T4 x2
- Compute capability: 7.5 / 7.5
- dtype used: float16
- device_map: auto

## Model

- `llm-jp/llm-jp-4-8b-instruct`
- model class: `LlamaForCausalLM`
- tokenizer class: `Llmjp4Tokenizer`
- chat template: available
- `parse_response()`: available

## Device Placement

- GPU 0: embeddings + layers 0–12
- GPU 1: layers 13–31 + norm + rotary embedding + lm_head

## Smoke Test

Raw decoded Harmony response:

```text
<|channel|>final<|message|>薄明かりの中、金色の稲穂が朝露に揺れている。
遠くの山々は淡い霧に包まれ、静かな風が木漏れ日を運んできた。
小川のせせらぎだけが耳に残り、一日の始まりを告げている。<|return|>
```

Parsed final content:

```text
薄明かりの中、金色の稲穂が朝露に揺れている。
遠くの山々は淡い霧に包まれ、静かな風が木漏れ日を運んできた。
小川のせせらぎだけが耳に残り、一日の始まりを告げている。
```

## Verdict

- model load: PASS
- T4 x2 distribution: PASS
- tokenizer/chat template: PASS
- Harmony parser: PASS
- Japanese generation: PASS
- special-token corruption: not observed
- repetition collapse: not observed

## Output Policy

Narrative raw outputs in Experiment 06 store the parsed Harmony `content` field.

Harmony channel markers are protocol metadata and are retained only in runtime diagnostics.

## Note on BF16

`torch.cuda.is_bf16_supported()` returned true in this runtime.

However, FP16 already passed the complete runtime test. To avoid introducing a new runtime variable after successful validation, Experiment 06 will remain on FP16.
