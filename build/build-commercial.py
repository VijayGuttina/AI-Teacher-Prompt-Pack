from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "books" / "commercial-primary-teacher"
OUTPUT = ROOT / "exports" / "markdown" / "AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.md"

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


def strip_yaml_front_matter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip()
    return text


def main() -> None:
    missing = [name for name in PARTS if not (SOURCE / name).exists()]
    if missing:
        raise SystemExit("Missing commercial source files: " + ", ".join(missing))

    sections = []
    for name in PARTS:
        text = (SOURCE / name).read_text(encoding="utf-8")
        if name != "000-front-matter.md":
            text = strip_yaml_front_matter(text)
        sections.append(text.rstrip())

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n\n\\newpage\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT}")


if __name__ == "__main__":
    main()
