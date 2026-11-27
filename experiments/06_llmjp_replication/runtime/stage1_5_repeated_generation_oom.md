# Stage 1.5 Runtime Stability — Repeated Generation OOM

## Trigger

After successful Stage 1 and successful C0 / Seed 42 generation,
C0 / Seed 31415 failed during prefill.

## Error

```text
OutOfMemoryError: CUDA out of memory.
Tried to allocate 148.00 MiB.
GPU 1 total capacity: 14.56 GiB
GPU 1 free: 102.81 MiB
PyTorch allocated: 14.26 GiB
```

The failure occurred in
`scaled_dot_product_attention()`
during the initial prefill forward pass.

## Classification

**Runtime stability issue — not a Seed or Narrative Quality result.**

The failure happened before sampling began, so it is not attributed to Seed 31415.

## Likely cause

The original `device_map="auto"` placement left too little GPU headroom for:

- prompt prefill activations
- attention working memory
- KV cache / generation buffers

The original map placed embeddings + layers 0–12 on GPU 0 and
layers 13–31 + norm + rotary embedding + lm_head on GPU 1.

GPU 1 was nearly saturated at prefill.

## Adjustment

The model-loading policy is changed before continuing the evaluation series:

```python
device_map="balanced"
max_memory={
    0: "12GiB",
    1: "12GiB",
    "cpu": "24GiB",
}
```

This intentionally reserves approximately 2.5 GiB of physical capacity
per T4 beyond the model-weight placement limit.

The runner also performs:

- `gc.collect()`
- `torch.cuda.empty_cache()`

before and after each run.

## Experimental consequence

Because the runtime allocation policy changed after C0 / Seed 42,
the previously generated C0 / Seed 42 output remains preserved as a diagnostic run,
but the strict 12-run comparison series must restart from **C0 / Seed 42**
under the stabilized runtime.

No narrative input, decoding parameter, model revision, or Seed is changed.
