# Runtime Records — Experiment 06

Stage 1のRuntime Compatibility結果を保存する。

保存対象：

- Python version
- PyTorch version
- Transformers version
- CUDA runtime
- GPU model / count
- compute capability
- BF16 support result
- dtype
- device map
- model load warnings
- generation warnings
- Smoke Test raw output
- failure traceback（発生した場合）

## Rule

Runtime条件の調整はNarrative Benchmark開始前に完了する。

C0 Seed 42開始後は、C0〜C3の途中でruntime / generation条件を変更しない。

変更が必要になった場合、そのrunは同一比較系列から除外し、別runとして記録する。
