from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "books" / "commercial-primary-teacher"
OUTPUT = ROOT / "exports" / "markdown" / "AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.md"
COVER = SOURCE / "assets" / "AI-Prompt-Toolkit-for-Primary-Teachers-cover.jpg"
COVER_EXPORT = ROOT / "exports" / "covers" / "AI-Prompt-Toolkit-for-Primary-Teachers-cover.jpg"

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

PAGE_BREAK = "::: { .pagebreak }\n:::"
VARIABLE_RE = re.compile(r"\[([A-Z][A-Z0-9_]+)\]")
PROMPT_RE = re.compile(r"(?ms)(^## Commercial Prompt \d+:.*?)(?=^## Commercial Prompt \d+:|\Z)")

SUBJECT_DEFAULTS = {
    "002-plan.md": ("Mathematics", "Fractions", "Identify and explain equivalent fractions"),
    "003-teach.md": ("English", "Persuasive writing", "Write a persuasive paragraph using reasons and supporting evidence"),
    "004-assess.md": ("Mathematics", "Fractions", "Identify and explain equivalent fractions"),
    "005-adapt.md": ("English", "Persuasive writing", "Write a persuasive paragraph using clear reasons and supporting evidence"),
    "005-adapt-continued.md": ("Mathematics", "Fractions", "Add fractions with related denominators"),
    "006-subject-toolkit.md": ("English", "Reading comprehension", "Identify and explain evidence from a text"),
    "006-subject-toolkit-continued.md": ("Science", "States of matter", "Explain how heating and cooling can change the state of a material"),
    "007-save-time.md": ("English", "Persuasive writing", "Improve an existing classroom resource without changing its learning purpose"),
}


def strip_yaml_front_matter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip()
    return text


def inject_cover(text: str) -> str:
    if not COVER.exists():
        raise SystemExit(
            f"Missing commercial cover asset: {COVER}\n"
            "Place the customer-facing cover image at this path before building."
        )

    # The generated Markdown lives under exports/markdown, so this relative
    # path deliberately points back to the canonical source asset.
    cover_ref = "../../books/commercial-primary-teacher/assets/AI-Prompt-Toolkit-for-Primary-Teachers-cover.jpg"
    cover_block = (
        f"![AI Prompt Toolkit for Primary Teachers]({cover_ref}){{width=6.53in height=9.80in}}\n\n"
        f"{PAGE_BREAK}\n\n"
    )

    yaml_match = re.match(r"(?s)^(---\n.*?\n---\n\n)(.*)$", text)
    if yaml_match:
        return yaml_match.group(1) + cover_block + yaml_match.group(2)
    return cover_block + text


def infer_defaults(source_name: str, prompt: str) -> tuple[str, str, str]:
    subject, topic, objective = SUBJECT_DEFAULTS.get(
        source_name,
        ("Mathematics", "Fractions", "Identify and explain equivalent fractions"),
    )

    title_match = re.search(r"^## Commercial Prompt \d+:\s*(.+)$", prompt, re.MULTILINE)
    title = title_match.group(1).lower() if title_match else ""

    # Subject toolkit prompts are deliberately inferred from their local content.
    if source_name.startswith("006-"):
        for key, values in [
            ("math", ("Mathematics", "Fractions", "Identify and explain equivalent fractions")),
            ("science", ("Science", "States of matter", "Explain how heating and cooling change the state of water")),
            ("history", ("History", "Anglo-Saxons", "Explain why Anglo-Saxon kingdoms developed in different parts of England")),
            ("geography", ("Geography", "Rivers", "Explain how rivers change from source to mouth")),
            ("comput", ("Computing", "Algorithms", "Explain how a sequence of instructions solves a problem")),
            ("art", ("Art and Design", "Colour and texture", "Experiment with colour and texture to create a planned effect")),
            ("design", ("Design and Technology", "Structures", "Design and evaluate a stable structure for a stated purpose")),
            ("physical", ("Physical Education", "Invasion games", "Use space and movement effectively in a team game")),
            ("music", ("Music", "Rhythm and notation", "Perform and create rhythmic patterns accurately")),
            ("relig", ("Religious Education", "Beliefs and practice", "Explain how a belief is expressed through practice")),
            ("pshe", ("PSHE", "Relationships", "Explain how respectful communication supports healthy relationships")),
            ("mfl", ("Modern Foreign Languages", "Everyday language", "Use familiar vocabulary in short spoken exchanges")),
        ]:
            if key in title or key in prompt.lower():
                subject, topic, objective = values
                break

    return subject, topic, objective


def example_for(variable: str, source_name: str, prompt: str) -> str:
    subject, topic, objective = infer_defaults(source_name, prompt)
    examples = {
        "YEAR_GROUP": "Year 4",
        "SUBJECT": subject,
        "TOPIC": topic,
        "CURRENT_TOPIC": topic,
        "UNIT": topic,
        "OBJECTIVE": objective,
        "LEARNING_OBJECTIVE": objective,
        "NEW_LEARNING_OBJECTIVE": objective,
        "END_GOAL": objective,
        "OUTCOME": "A completed pupil task demonstrating the stated learning objective",
        "EXPECTED_PUPIL_OUTCOME": "A completed pupil task demonstrating the stated learning objective",
        "DURATION": "60 minutes",
        "LESSON_DURATION": "60 minutes",
        "TIME": "10 minutes",
        "TIME_AVAILABLE": "10 minutes",
        "NUMBER": "6",
        "NUMBER_OF_QUESTIONS": "6",
        "NUMBER_OF_ITEMS": "8",
        "NUMBER_OF_LESSONS": "6",
        "LENGTH": "6 lessons",
        "PRIOR_LEARNING": "Pupils can identify common fractions and explain simple equivalent fractions",
        "KNOWN_PRIOR_LEARNING": "Pupils can identify common fractions and explain simple equivalent fractions",
        "PREVIOUS_LEARNING": "Pupils can identify common fractions and explain simple equivalent fractions",
        "KNOWN_PREVIOUS_LEARNING": "Pupils can identify common fractions and explain simple equivalent fractions",
        "PRIOR_KNOWLEDGE": "Pupils can identify common fractions and explain simple equivalent fractions",
        "KNOWN_KNOWLEDGE": "Pupils can identify common fractions and explain simple equivalent fractions",
        "STARTING_KNOWLEDGE": "Pupils understand the basic meaning of the key terms in the topic",
        "ESSENTIAL_KNOWLEDGE": "Key vocabulary, core facts and prerequisite knowledge needed for the objective",
        "KNOWLEDGE": "The essential facts, vocabulary and concepts pupils need for the objective",
        "PREREQUISITES": "Secure understanding of the prerequisite concept and relevant vocabulary",
        "RESOURCES": "Mini-whiteboards, printed task sheets, visual examples and classroom textbooks",
        "RESOURCES_AVAILABLE": "Mini-whiteboards, printed task sheets and visual examples",
        "AVAILABLE_RESOURCES": "Mini-whiteboards, printed task sheets and visual examples",
        "CLASS_CONSIDERATIONS": "Mixed attainment; several pupils benefit from vocabulary support",
        "CLASS_SIZE": "30 pupils",
        "CONTEXT": "A mixed-attainment Year 4 mainstream primary class",
        "CLASS_CONTEXT": "A mixed-attainment Year 4 mainstream primary class",
        "TASK": "A short independent task requiring pupils to apply the stated learning",
        "CORE_TASK": "Complete a short task applying the stated learning objective",
        "TASK_BEING_MODELLED": "Solve or complete one representative example of the target task",
        "EXAMPLE": "A worked example showing the intended method and reasoning",
        "MODELLED_EXAMPLE": "A worked example showing the intended method and reasoning",
        "BARRIERS": "Unfamiliar vocabulary and difficulty organising the steps of the task",
        "KNOWN_BARRIERS": "Unfamiliar vocabulary and difficulty organising the steps of the task",
        "DIFFICULTY": "Pupils can start the task but struggle to organise the steps independently",
        "OBSERVED_DIFFICULTY": "Pupils can start the task but struggle to organise the steps independently",
        "MISCONCEPTION": "Pupils may confuse the procedure with the underlying concept",
        "MISCONCEPTIONS": "Pupils may confuse the procedure with the underlying concept",
        "LIKELY_MISCONCEPTION": "Pupils may apply a familiar rule without checking whether it fits the new context",
        "LIKELY_MISCONCEPTIONS": "Pupils may apply a familiar rule without checking whether it fits the new context",
        "ERROR": "Pupils apply the correct method but make an error at the final step",
        "ERRORS": "Errors in method selection, sequencing or final calculation",
        "COMMON_ERROR": "Using the correct-looking method without explaining why it applies",
        "ERROR_EVIDENCE": "Several pupils give the same incorrect response or omit the same reasoning step",
        "EVIDENCE": "Pupil responses from a recent class task or assessment",
        "PUPIL_EVIDENCE": "Most pupils can complete the core task accurately but explanations are inconsistent",
        "PUPIL_WORK": "A short sample of anonymised pupil work from the task",
        "PUPIL_RESPONSES": "Anonymised responses from six pupils showing a mixture of secure and insecure understanding",
        "RESPONSE": "An anonymised pupil response showing an incorrect answer or incomplete reasoning",
        "RESPONSES": "Anonymised pupil responses from the same assessment task",
        "WORD": "evaporation",
        "WORDS": "evaporation, condensation, melting, freezing",
        "VOCABULARY": "evaporation, condensation, melting, freezing",
        "KEY_VOCABULARY": "evaporation, condensation, melting, freezing",
        "EXAMPLES": "A teacher model and one strong pupil example",
        "ARRANGEMENTS": "Short formative checks during lessons and an end-of-unit assessment",
        "ASSESSMENT": "A short end-of-unit assessment containing eight questions",
        "ASSESSMENT_TASK": "An eight-question assessment covering the stated objective",
        "ASSESSMENT_EVIDENCE": "Pupil responses from a recent low-stakes assessment",
        "ACTIVITIES": "Retrieval starters, exit tickets, written marking and end-of-unit tests",
        "RECORDING": "Teacher assessment notes and the school's existing tracking system",
        "POINTS": "Weekly retrieval checks and one end-of-unit assessment",
        "CONSTRAINTS": "Avoid adding formal assessment workload beyond existing school expectations",
        "FEEDBACK": "Your explanation is clear. Now justify why you chose that method.",
        "CRITERIA": "Accurate subject vocabulary; clear explanation; evidence or example; correct conclusion",
        "SUCCESS_CRITERIA": "Accurate content, clear explanation and evidence that directly supports the objective",
        "GROUP_SIZE": "6 pupils",
        "TIME_AVAILABLE": "15 minutes",
        "TERM": "Autumn term, 12 teaching weeks",
        "SUBJECTS": "English, Mathematics, Science and History",
        "SCHOOL_CONSTRAINTS": "Use existing assessment points and avoid unnecessary additional recording",
        "RECORDING_REQUIREMENTS": "Record only evidence needed for existing planning, reporting or intervention decisions",
        "CONCERN": "Teachers are spending too much time recording assessment information that does not change teaching",
        "NUMBER_OF_LESSONS": "6",
        "CURRICULUM_GUIDANCE": "The school's existing medium-term plan and relevant statutory curriculum objectives",
        "SCHOOL_SEQUENCE": "The school's existing medium-term plan",
        "SCHOOL_SEQUENCE_OR_CURRICULUM_GUIDANCE": "The school's existing medium-term plan and relevant statutory curriculum objectives",
        "TEACHING_POINT": "The point where pupils must understand the difference between the two key concepts",
        "SEQUENCE": "Retrieval, explanation, modelling, guided practice and independent application",
        "PATTERNS": "Secure responses, partial responses, a common misconception and missing prerequisite knowledge",
        "AVAILABLE_REPRESENTATIONS": "Counters, diagrams, number lines and formal notation",
        "REPRESENTATIONS": "Counters, diagrams, number lines and formal notation",
        "THINKING": "Explain why the method works and justify the answer",
        "INPUT": "Anonymised classroom material relevant to the stated task",
        "TEXT": "A 500-word age-appropriate extract selected by the teacher",
        "SOURCE_TEXT": "A 500-word extract from the class reading text",
        "RESOURCE": "An existing worksheet or lesson resource used with the class",
        "RESOURCE_CONTENT": "An existing classroom worksheet that needs adapting",
        "MATERIAL": "An existing teacher-created classroom resource",
    }
    if variable in examples:
        return examples[variable]
    return f"Relevant {variable.replace('_', ' ').lower()} for a Year 4 {subject.lower()} lesson"


def add_example_values(prompt: str, source_name: str) -> str:
    if "**Example values:**" in prompt or "**Example values**" in prompt:
        return prompt

    match = re.search(r"(?ms)(\*\*Difficulty:\*\*.*?\n\n)(\*\*Copy and paste:\*\*)", prompt)
    if not match:
        return prompt

    variables = []
    for var in VARIABLE_RE.findall(prompt):
        if var not in variables:
            variables.append(var)

    if not variables:
        return prompt

    rows = ["**Example values**", "", "| Variable | Example |", "|---|---|"]
    for var in variables:
        rows.append(f"| `[{var}]` | {example_for(var, source_name, prompt)} |")
    rows.append("")
    rows.append("Replace these examples with your own information before running the prompt.")
    rows.append("")

    return prompt[: match.start(2)] + "\n".join(rows) + match.group(2) + prompt[match.end(2) :]


def enrich_prompts(text: str, source_name: str) -> str:
    return PROMPT_RE.sub(lambda m: add_example_values(m.group(1), source_name), text)


def load_sections() -> list[str]:
    missing = [name for name in PARTS if not (SOURCE / name).exists()]
    if missing:
        raise SystemExit("Missing commercial source files: " + ", ".join(missing))
    if not COVER.exists():
        raise SystemExit(
            f"Missing commercial cover asset: {COVER}\n"
            "Place the customer-facing cover image at this path before building."
        )

    sections = []
    for name in PARTS:
        text = (SOURCE / name).read_text(encoding="utf-8")
        if name == "000-front-matter.md":
            text = inject_cover(text)
        else:
            text = strip_yaml_front_matter(text)
            text = enrich_prompts(text, name)
        sections.append(text.rstrip())
    return sections


def main() -> None:
    sections = load_sections()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    COVER_EXPORT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(COVER, COVER_EXPORT)
    OUTPUT.write_text(
        f"\n\n{PAGE_BREAK}\n\n".join(sections) + "\n",
        encoding="utf-8",
    )
    print(f"Built {OUTPUT}")
    print(f"Cover: {COVER_EXPORT}")


if __name__ == "__main__":
    main()
