import platform
import sys

import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "llm-jp/llm-jp-4-8b-instruct"

print("=== Environment ===")
print("Python:", sys.version.replace("\n", " "))
print("Platform:", platform.platform())
print("PyTorch:", torch.__version__)
print("Transformers:", transformers.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA runtime:", torch.version.cuda)

if not torch.cuda.is_available():
    raise RuntimeError(
        "CUDA is not available. This runtime test requires a GPU-enabled "
        "Kaggle session. Enable T4 x2, restart the session, then rerun."
    )

print("GPU count:", torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    print(
        f"GPU {i}:",
        torch.cuda.get_device_name(i),
        "capability=",
        torch.cuda.get_device_capability(i),
    )
print("torch.cuda.is_bf16_supported():", torch.cuda.is_bf16_supported())

print("\n=== Load tokenizer ===")
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    trust_remote_code=True,
)
print("Tokenizer:", tokenizer.__class__.__name__)
print("Has chat template:", bool(tokenizer.chat_template))
print("Has parse_response:", hasattr(tokenizer, "parse_response"))

print("\n=== Load model (FP16 / device_map=auto) ===")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)
model.eval()

print("Model:", model.__class__.__name__)
print("Model dtype:", next(model.parameters()).dtype)
print("HF device map:", getattr(model, "hf_device_map", None))

print("\n=== Smoke test ===")
messages = [
    {
        "role": "user",
        "content": "日本語で、秋の朝の静かな風景を3文だけ書いてください。"
    }
]

prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

torch.manual_seed(42)
torch.cuda.manual_seed_all(42)

with torch.no_grad():
    generated = model.generate(
        **inputs,
        max_new_tokens=120,
        do_sample=True,
        top_p=0.95,
        temperature=0.7,
        repetition_penalty=1.05,
    )

generated_ids = generated[0][inputs["input_ids"].shape[1]:].tolist()

# Preserve the raw decoded Harmony response for runtime diagnostics.
raw_response = tokenizer.decode(generated_ids)

print("\n=== Raw decoded response ===")
print(raw_response)

if not hasattr(tokenizer, "parse_response"):
    raise RuntimeError(
        "Tokenizer does not expose parse_response(). "
        "The official LLM-jp-4 Transformers workflow requires the bundled parser."
    )

parsed = tokenizer.parse_response(raw_response)
content = parsed.get("content")

print("\n=== Parsed response ===")
print("Role:", parsed.get("role"))
print("Thinking:", parsed.get("thinking"))
print("Content:")
print(content)

print("\n=== Runtime verdict checklist ===")
print("- Model load completed")
print("- Chat template applied")
print("- Harmony response parser available")
print("- Japanese final content parsed")
print("- Inspect parsed content for repetition / corruption")
