import os
import torch
from pathlib import Path

BASE_DIR = Path(".")
BENCHMARK = BASE_DIR / "benchmark/v1.0/inputs/EP01_SC02"
EXP = BASE_DIR / "experiments/05_constraint_decomposition"

BASE_INSTRUCTION = """以下の情報をもとに、指定されたシーンの小説本文を生成してください。
与えられた情報を尊重し、指定されたシーンの本文を書いてください。"""

def read_text(path):
    return Path(path).read_text(encoding="utf-8")

def strip_publication_note(text):
    # benchmark_note is repository documentation added after the original experiment.
    return text.split("\nbenchmark_note:", 1)[0].rstrip()

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

    if condition in ("B1", "B3"):
        parts.append(
            "# Scene Boundary\n"
            + read_text(EXP / "constraints/scene_boundary.yaml")
        )

    if condition in ("B2", "B3"):
        parts.append(
            "# Reveal Constraints\n"
            + read_text(EXP / "constraints/reveal_constraints.yaml")
        )

    return "\n\n".join(parts)

def generate_one(model, tokenizer, condition="B1", seed=42):
    prompt = build_prompt(condition)

    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    messages = [{"role": "user", "content": prompt}]
    formatted = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )

    inputs = tokenizer(formatted, return_tensors="pt").to(model.device)

    with torch.no_grad():
        generated = model.generate(
            **inputs,
            max_new_tokens=2000,
            do_sample=True,
            temperature=0.7,
            top_p=0.8,
            top_k=20,
            min_p=0.0,
        )

    new_tokens = generated[0][inputs["input_ids"].shape[1]:]
    output = tokenizer.decode(new_tokens, skip_special_tokens=True)

    return prompt, output
