from pathlib import Path

import torch
from huggingface_hub import model_info
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "llm-jp/llm-jp-4-8b-instruct"
MODEL_REVISION = "098f2b2cf33021eba19a6d3582aa3d071ccc0aff"

BASE_DIR = Path(".")
BENCHMARK = BASE_DIR / "benchmark/v1.0/inputs/EP01_SC02"
EXP = BASE_DIR / "experiments/06_llmjp_replication"

BASE_INSTRUCTION = """以下の情報をもとに、指定されたシーンの小説本文を生成してください。
与えられた情報を尊重し、指定されたシーンの本文を書いてください。"""

def read_text(path):
    return Path(path).read_text(encoding="utf-8")

def strip_publication_note(text):
    return text.split("\nbenchmark_note:", 1)[0].rstrip()

def resolve_model_revision():
    return MODEL_REVISION

def load_model_and_tokenizer(revision=None):
    if revision is None:
        revision = MODEL_REVISION

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID,
        revision=revision,
        trust_remote_code=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        revision=revision,
        dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    return revision, model, tokenizer

def build_prompt(condition):
    scene_card = read_text(BENCHMARK / "scene_card.yaml")
    character_context = strip_publication_note(
        read_text(BENCHMARK / "character_context.yaml")
    )
    addressing_rules = strip_publication_note(
        read_text(BENCHMARK / "addressing_rules.yaml")
    )
    style_guide = read_text(BENCHMARK / "style_guide.yaml")

    parts = [
        BASE_INSTRUCTION,
        "# Scene Card\n" + scene_card,
        "# Character Context\n" + character_context,
        "# Addressing Rules\n" + addressing_rules,
        "# Style Guide\n" + style_guide,
    ]

    if condition in ("C1", "C3"):
        parts.append(
            "# Scene Boundary\n"
            + read_text(EXP / "constraints/scene_boundary.yaml")
        )

    if condition in ("C2", "C3"):
        parts.append(
            "# Reveal Constraints\n"
            + read_text(EXP / "constraints/reveal_constraints.yaml")
        )

    return "\n\n".join(parts)

def generate_one(model, tokenizer, condition="C0", seed=42):
    prompt = build_prompt(condition)

    messages = [{"role": "user", "content": prompt}]
    formatted = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    inputs = tokenizer(formatted, return_tensors="pt").to(model.device)

    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    with torch.no_grad():
        generated = model.generate(
            **inputs,
            max_new_tokens=2000,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.05,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated_ids = generated[0][inputs["input_ids"].shape[1]:].tolist()
    raw_response = tokenizer.decode(generated_ids)

    parsed = tokenizer.parse_response(raw_response)
    content = parsed.get("content")

    if not content:
        raise RuntimeError(
            f"No parsed final content returned. Raw response: {raw_response!r}"
        )

    return {
        "prompt": prompt,
        "raw_harmony_response": raw_response,
        "content": content,
        "parsed_role": parsed.get("role"),
        "parsed_thinking": parsed.get("thinking"),
    }
