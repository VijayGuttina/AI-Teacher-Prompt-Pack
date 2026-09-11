from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "books" / "commercial-primary-teacher"
BUILD = ROOT / "exports" / "markdown" / "AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.md"

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

PROMPT_RE = re.compile(r"^## Commercial Prompt (\d+):\\s*(.+)$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"\[[A-Z][A-Z0-9_ /&-]{2,}\]")


def fail(message: str) -> None:
    raise SystemExit(f"QA FAILED: {message}")


def main() -> None:
    missing = [name for name in PARTS if not (SOURCE / name).exists()]
    if missing:
        fail("missing source files: " + ", ".join(missing))

    combined = "\n\n".join(
        (SOURCE / name).read_text(encoding="utf-8") for name in PARTS
    )

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
        if "<!-- PAGEBREAK -->" not in built:
            fail("built Markdown contains no portable PAGEBREAK markers")

    print("Commercial QA passed")
    print(f"Prompts: {len(numbers)}")
    print(f"Source files: {len(PARTS)}")
    if BUILD.exists():
        print(f"Built Markdown: {BUILD}")


if __name__ == "__main__":
    main()
