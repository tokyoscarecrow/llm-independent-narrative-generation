# Stage 1 Runtime Attempt 2

## Date

2026-11-27

## Environment

- Python: 3.12.13
- PyTorch: 2.10.0+cu128
- Transformers: 5.0.0
- CUDA available: true
- CUDA runtime: 12.8
- GPU count: 2
- GPU 0: Tesla T4, compute capability 7.5
- GPU 1: Tesla T4, compute capability 7.5
- torch.cuda.is_bf16_supported(): true

## Tokenizer

- downloaded successfully
- chat template present

## Model Load

- model: `llm-jp/llm-jp-4-8b-instruct`
- class: `LlamaForCausalLM`
- dtype: float16
- device_map: automatic split across both Tesla T4 GPUs
- layers 0–12 placed on GPU 0
- layers 13–31, norm, rotary embedding and lm_head placed on GPU 1

## Smoke Test

Generation completed successfully.

Observed decoded output began with:

```text
final 薄明かりの中、金色の稲穂が朝露に揺れている。
...
```

Japanese generation quality was normal and no repetition failure occurred.

## Interpretation

### Runtime Compatibility

**PASS**

The model loaded in FP16 across T4 x2 and generated coherent Japanese.

### Harmony Output Handling

The literal-looking `final` prefix is not treated as narrative content.

LLM-jp-4 chat models use Harmony-style channels. The official Transformers cookbook uses the tokenizer bundled with the model and parses generated responses with `tokenizer.parse_response()`.

The runtime script is therefore updated to:

- use `trust_remote_code=True`
- preserve the raw decoded Harmony response for diagnostics
- use `tokenizer.parse_response()`
- expose only the parsed `content` field as final application text

A final parser smoke test is required before Stage 1 is closed.

## Status

- GPU runtime: PASS
- model load: PASS
- Japanese generation: PASS
- repetition/special-token corruption: PASS
- response parsing: pending confirmation
