from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "books" / "commercial-primary-teacher"
BUILD = ROOT / "exports" / "markdown" / "AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.md"
PAGEBREAK_LUA = ROOT / "build" / "pagebreak.lua"

PARTS = [
    "000-front-matter.md",
    "001-quick-start.md",
    "002-plan.md",
    "003-teach.md",
    "004-assess.md",
    "005-adapt.md",
    "005-adapt-continued.md",
    "006-subject-toolkit.md",
    "006-subject-toolkit-continued.md",
    "007-save-time.md",
    "999-index.md",
]

PROMPT_RE = re.compile(r"^## Commercial Prompt (\d+):\s*(.+)$", re.MULTILINE)
PROMPT_BLOCK_RE = re.compile(r"(?ms)^## Commercial Prompt (\d+):.*?(?=^## Commercial Prompt \d+:|\Z)")
VARIABLE_RE = re.compile(r"\[([A-Z][A-Z0-9_]+)\]")
PAGEBREAK_RE = re.compile(r"^:::\s*\{\s*\.pagebreak\s*\}\s*$", re.MULTILINE)


def fail(message: str) -> None:
    raise SystemExit(f"QA FAILED: {message}")


def main() -> None:
    missing = [name for name in PARTS if not (SOURCE / name).exists()]
    if missing:
        fail("missing source files: " + ", ".join(missing))

    combined = "\n\n".join(
        (SOURCE / name).read_text(encoding="utf-8") for name in PARTS
    )

    front_matter = (SOURCE / "000-front-matter.md").read_text(encoding="utf-8")
    if re.search(r"(?m)^author:\s*", front_matter):
        fail("author metadata must not appear in the opening title metadata; keep the author in the body only")

    prompt_matches = PROMPT_RE.findall(combined)
    numbers = [int(number) for number, _ in prompt_matches]
    expected = list(range(1, len(numbers) + 1))

    if not numbers:
        fail("no Commercial Prompt headings found")
    if numbers != expected:
        fail(f"prompt numbering is not sequential: first mismatch in {numbers[:15]}...")
    if len(numbers) != len(set(numbers)):
        fail("duplicate commercial prompt numbers found")
    if "—" in combined or "–" in combined:
        fail("en dash or em dash found; use commas, colons or parentheses instead")
    if "TODO" in combined or "TBD" in combined or "PLACEHOLDER" in combined:
        fail("placeholder text found")

    required = [
        "Best for:",
        "Use when:",
        "Difficulty:",
        "Copy and paste:",
    ]
    for label in required:
        if label not in combined:
            fail(f"required commercial field missing: {label}")

    if len(numbers) < 120:
        fail(f"commercial edition contains only {len(numbers)} prompts; minimum is 120")

    if BUILD.exists():
        built = BUILD.read_text(encoding="utf-8")
        built_matches = [int(n) for n, _ in PROMPT_RE.findall(built)]
        if built_matches != numbers:
            fail("built Markdown prompt numbering does not match source files")
        if not PAGEBREAK_RE.search(built):
            fail("built Markdown contains no portable PAGEBREAK markers")

        blocks = PROMPT_BLOCK_RE.findall(built)
        if len(blocks) != len(numbers):
            fail("built Markdown prompt block count does not match prompt count")

        for number, block in [(int(m.group(1)), m.group(0)) for m in PROMPT_BLOCK_RE.finditer(built)]:
            variables = set(VARIABLE_RE.findall(block))
            if variables and "**Example values**" not in block:
                fail(f"Commercial Prompt {number:03d} has variables but no Example values section")
            if variables:
                example_section = block.split("**Example values**", 1)[1].split("**Copy and paste:**", 1)[0]
                missing_variables = [
                    f"[{variable}]" for variable in sorted(variables)
                    if f"`[{variable}]`" not in example_section
                ]
                if missing_variables:
                    fail(
                        f"Commercial Prompt {number:03d} is missing example values for: "
                        + ", ".join(missing_variables)
                    )

        if "frontier-model agnostic" not in built.lower():
            fail("built Markdown is missing the model compatibility statement")
        if "ChatGPT, Claude, Gemini" not in built:
            fail("built Markdown is missing the major model compatibility examples")

    if not PAGEBREAK_LUA.exists():
        fail("build/pagebreak.lua is missing")
    lua = PAGEBREAK_LUA.read_text(encoding="utf-8")
    if 'text == "Copy and paste:"' not in lua:
        fail("layout filter does not explicitly handle the Copy and paste label")
    if "latex_prompt_box" not in lua or ("\\begin{framed}" not in lua and "\\begin{shaded}" not in lua):
        fail("layout filter does not contain the PDF prompt container")
    if 'prompt_table(el.text)' not in lua:
        fail("layout filter no longer contains the DOCX prompt container")

    print("Commercial QA passed")
    print(f"Prompts: {len(numbers)}")
    print(f"Source files: {len(PARTS)}")
    if BUILD.exists():
        print(f"Built Markdown: {BUILD}")
        print("Example values: validated for every variable used by every commercial prompt")
        print("Model compatibility: frontier-model agnostic")
    print("Opening author metadata: not rendered")
    print("Copy and paste label: explicit layout control")
    print("DOCX prompt container: enabled")
    print("PDF prompt container: enabled")


if __name__ == "__main__":
    main()
