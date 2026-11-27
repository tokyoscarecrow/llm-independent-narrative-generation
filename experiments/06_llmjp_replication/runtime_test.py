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

if torch.cuda.is_available():
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
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
print("Tokenizer:", tokenizer.__class__.__name__)
print("Has chat template:", bool(tokenizer.chat_template))

print("\n=== Load model (FP16 / device_map=auto) ===")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    device_map="auto",
)
model.eval()

print("Model:", model.__class__.__name__)
print("Model dtype:", next(model.parameters()).dtype)
print("HF device map:", getattr(model, "hf_device_map", None))

print("\n=== Smoke test ===")
chat = [
    {
        "role": "user",
        "content": "日本語で、秋の朝の静かな風景を3文だけ書いてください。"
    }
]

input_ids = tokenizer.apply_chat_template(
    chat,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt",
)

# With device_map=auto, input should begin on the embedding/input device.
first_device = next(model.parameters()).device
input_ids = input_ids.to(first_device)

torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(42)

with torch.no_grad():
    generated = model.generate(
        input_ids,
        max_new_tokens=120,
        do_sample=True,
        top_p=0.95,
        temperature=0.7,
        repetition_penalty=1.05,
    )

new_tokens = generated[0][input_ids.shape[1]:]
output = tokenizer.decode(new_tokens, skip_special_tokens=True)

print("\n=== Generated text ===")
print(output)

print("\n=== Runtime verdict checklist ===")
print("- Model load completed")
print("- Chat template applied")
print("- Japanese text generated")
print("- Inspect output manually for special-token leakage / repetition")
