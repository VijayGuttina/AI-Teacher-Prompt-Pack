# Prompt Master Specification

## 1. Purpose

This document is the canonical authoring contract for every reusable prompt in the AI Teacher Prompt Pack.

It defines the metadata, structure, inheritance rules, content requirements and quality controls that authors and automated generation processes must follow.

It is a **specification**, not a prompt library and not a worked example.

Individual prompts must not copy global framework content into every entry.

---

## 2. Architecture and inheritance

Prompts inherit from the relevant framework layers:

```text
GLOBAL PROMPT STANDARD
        ↓
MASTER PROMPT FRAMEWORK
        ↓
PRIMARY / SECONDARY TEACHER FRAMEWORK
        ↓
SUBJECT OR PROFESSIONAL-PRACTICE FRAMEWORK
        ↓
TEACHING WORKFLOW
        ↓
INDIVIDUAL PROMPT
```

The prompt entry contains only task-specific information that is not already supplied by an inherited framework.

---

## 3. Mandatory prompt metadata

Every prompt must contain the following metadata unless a publication specification explicitly states otherwise.

| Field | Required | Purpose |
|---|:---:|---|
| Prompt ID | Yes | Unique stable identifier |
| Title | Yes | Clear teacher-facing name |
| Book / Product | Yes | Publication in which the prompt appears |
| Module | Yes | Library module |
| Workflow ID | Yes | Stable workflow reference |
| Version | Yes | Content version |
| Last Updated | Yes | Maintenance date |
| Prompt Difficulty | Yes | Beginner / Intermediate / Advanced |
| AI Model Compatibility | Yes | Supported model family information |
| Expected Output Length | Yes | Typical generated output |
| Typical Generation Time | Yes | Approximate user-facing expectation |
| Curriculum Tags | Yes where applicable | Phase, year group, subject, strand and theme |
| Editable Variables | Yes | Inputs the teacher can customise |
| Example Input | Recommended | Demonstrates practical use |
| Example Output | Recommended | Demonstrates expected result |

---

## 4. Required prompt structure

Each individual prompt should use the following structure.

```text
PROMPT ID
TITLE

Purpose

Prompt Difficulty

AI Model Compatibility

Expected Output Length

Typical Generation Time

Curriculum Tags

Editable Variables

ROLE
CONTEXT
TASK
REQUIREMENTS
OUTPUT FORMAT
QUALITY CHECKS
OPTIONAL CUSTOMISATION

Example Input
Example Output

Teacher Tip
Related Workflows
```

Sections may be omitted only where the inherited framework or workflow makes them genuinely unnecessary.

---

## 5. Purpose

Explain:

- what the workflow does;
- the teacher problem it solves;
- when it is most useful;
- what the teacher needs to provide.

Keep this concise and practical.

---

## 6. Prompt Difficulty

Use one of:

- **Beginner** - straightforward variables and output; minimal AI experience required.
- **Intermediate** - multiple variables, judgement or structured iteration may be useful.
- **Advanced** - complex inputs, specialist judgement, multi-stage reasoning or substantial customisation.

Difficulty describes **teacher use**, not the intellectual difficulty of the teaching task.

---

## 7. AI Model Compatibility

Compatibility metadata should be concise.

Do not reproduce large model comparison tables in every prompt.

Use the current project model compatibility guidance and identify exceptions only where they materially affect use.

The default expectation is compatibility with current mainstream general-purpose AI assistants, including ChatGPT, Claude, Gemini and Microsoft Copilot, unless the workflow has a specific dependency.

Do not claim that a model supports a feature unless the claim is known to be reliable.

---

## 8. Expected Output Length

Describe the expected result in practical terms, for example:

- Short: under 500 words
- Medium: approximately 500–1,000 words
- Long: approximately 1,000–2,000 words
- Extended: 2,000+ words

Where useful, specify expected sections or artefacts rather than relying only on word count.

---

## 9. Typical Generation Time

Use broad expectations rather than false precision.

Example:

```text
Typical generation: under 1 minute
```

Do not include model-by-model timing tables unless a product specifically requires them and the information is current.

---

## 10. Curriculum Tags

Use only relevant tags.

Possible dimensions include:

- Phase
- Year group
- Subject
- Strand
- Curriculum objective
- Teaching theme
- Assessment context
- Specialist need

Do not invent statutory curriculum references. Where a specific curriculum claim matters, verify it before publication.

---

## 11. Editable Variables

Variables are central to the modular architecture.

Each variable should identify:

| Variable | Required | Example | Notes |
|---|:---:|---|---|
| Year Group | Yes/No | Year 4 | Use only where relevant |
| Subject | Yes/No | English | Usually inherited where possible |
| Topic | Yes/No | Persuasive writing | Task dependent |
| Learning Objective | Yes/No | Write a persuasive paragraph | Task dependent |
| Ability / attainment | No | Mixed attainment | Use practical descriptions |
| SEND / accessibility | No | Dyslexia-friendly scaffolding | Never require unnecessary disclosure |
| EAL | No | Beginner English learner | Use only where relevant |
| Duration | No | 60 minutes | Task dependent |
| Resources | No | Visualiser, mini-whiteboards | Task dependent |
| Existing material | No | Paste pupil work | Required for analysis workflows |

Do not create separate prompts for variables that can reasonably be changed within one reusable workflow.

---

## 12. ROLE

The ROLE section should define only the specialist role required for the workflow.

Global teaching identity should normally be inherited from the relevant framework.

Avoid inflated credentials such as "award-winning" unless they materially improve the task.

Prefer precise expertise, for example:

```text
Act as an experienced primary English teacher and literacy specialist.
```

---

## 13. CONTEXT

Specify the information the AI needs to perform the workflow.

Use clearly labelled variables.

Do not repeat framework assumptions already inherited from higher layers.

If information may be missing, state how the AI should handle missing inputs.

For example:

- make a clearly labelled reasonable assumption;
- ask for missing information only when it materially changes the result;
- otherwise proceed using a sensible default.

The default product philosophy is **minimal unnecessary iteration**.

---

## 14. TASK

State the exact teacher task.

The task should describe the intended outcome, not merely the topic.

Weak:

```text
Help with reading.
```

Strong:

```text
Create a set of inference questions from the supplied text that require pupils to use evidence and explain their reasoning.
```

---

## 15. REQUIREMENTS

List only workflow-specific requirements.

Requirements should cover material constraints such as:

- number of outputs;
- age appropriateness;
- differentiation;
- evidence requirements;
- curriculum alignment;
- accessibility;
- answer keys;
- teacher notes;
- resource limitations;
- safeguarding constraints.

Do not repeat global quality standards here.

---

## 16. OUTPUT FORMAT

Specify exactly how the result should be structured.

Use headings, tables, numbered sections or other structures when they improve classroom usability.

Avoid excessive formatting requirements that do not improve the output.

---

## 17. QUALITY CHECKS

Quality checks should be specific to the workflow.

Examples:

- questions must be answerable from the supplied text;
- mathematical calculations must be checked;
- assessment criteria must match the stated objective;
- differentiated versions must preserve the core learning objective;
- generated activities must fit the stated lesson duration.

Global quality rules are inherited and should not be copied into every prompt.

---

## 18. OPTIONAL CUSTOMISATION

Include only useful customisation options that teachers can realistically change.

Examples:

- year group;
- ability range;
- curriculum framework;
- lesson duration;
- available technology;
- school planning format;
- intervention context.

Do not create a long list of hypothetical options merely to make the prompt appear comprehensive.

---

## 19. Example Input

Where useful, provide a compact example showing how a teacher would complete the variables.

The example should represent a realistic classroom situation.

Do not use examples that imply invented statutory requirements.

---

## 20. Example Output

Where included, provide an excerpt that demonstrates the quality and structure expected from the AI.

An excerpt is normally preferable to a full generated output.

---

## 21. Teacher Tip

Provide one or two genuinely useful usage suggestions.

Avoid generic advice such as "be specific" unless the tip explains exactly what specificity matters for this workflow.

---

## 22. Related Workflows

Reference stable workflow IDs rather than a long list of individual prompt numbers.

For example:

```text
Related Workflows
- ENG-R-03 Retrieval Questions
- ENG-R-04 Inference Questions
- ENG-V-01 Vocabulary in Context
```

---

## 23. Prompt length standard

A reusable prompt should normally be substantially shorter than the legacy prompts.

Target:

- **Typical:** 50–150 lines
- **Complex:** 150–250 lines
- **Exceptional:** 250+ lines only where justified by genuine task complexity

Prompt length is not a quality metric.

A concise prompt with strong variables and inherited framework rules is preferred to a long prompt containing repeated instructions.

---

## 24. Inheritance rule

Before adding any instruction to an individual prompt, ask:

> Is this already defined by a higher framework layer?

If yes, do not repeat it unless the workflow requires a meaningful exception.

This rule applies particularly to:

- teacher role;
- UK English;
- general primary pedagogy;
- generic SEND principles;
- EAL principles;
- safeguarding;
- generic output quality;
- model compatibility;
- generic lesson structures.

---

## 25. Duplication rule

Do not create separate prompts merely because one variable changes.

Examples that should normally be one workflow:

- Year 3 vs Year 4
- History vs geography when the workflow is generic source analysis
- 30-minute vs 60-minute lesson
- easier vs harder output
- printable vs digital version

Create separate workflows only where the task logic or subject-specific requirements materially differ.

---

## 26. Safety and professional judgement

AI output is assistive content, not authoritative professional judgement.

Prompts involving pupil information, safeguarding, SEND, behaviour, assessment decisions or sensitive communication must minimise unnecessary personal data and should instruct teachers to review outputs before use.

Prompts must not encourage the AI to make unsupported diagnoses, safeguarding determinations or high-stakes decisions about pupils.

Where appropriate, the output should distinguish:

- generated suggestion;
- teacher judgement;
- information requiring verification.

---

## 27. UK education alignment

Where a prompt refers to UK curriculum or statutory requirements, use the relevant current framework and avoid unsupported claims.

For England, this may include:

- National Curriculum
- EYFS statutory framework
- relevant DfE guidance
- statutory assessment arrangements

Other UK nations must not be treated as interchangeable with England.

---

## 28. Validation checklist

Before a prompt is accepted into the library, verify:

### Structure

- [ ] Prompt ID is unique.
- [ ] Title describes a real teacher workflow.
- [ ] Required metadata is present.
- [ ] Variables are clearly defined.
- [ ] Prompt follows the required structure.

### Architecture

- [ ] Global instructions are not unnecessarily repeated.
- [ ] Subject-specific rules come from the correct framework.
- [ ] The workflow is not a duplicate of an existing workflow.
- [ ] Legitimate variations are handled through variables where possible.

### Teaching quality

- [ ] Task has a clear teacher use case.
- [ ] Output is age appropriate.
- [ ] Curriculum claims are accurate where applicable.
- [ ] Differentiation does not simply reduce the learning objective.
- [ ] Assessment requirements match the intended learning.

### AI quality

- [ ] Instructions are unambiguous.
- [ ] Output format is explicit.
- [ ] Workflow can normally be used without unnecessary iteration.
- [ ] Quality checks are task-specific.
- [ ] The teacher is prompted to verify high-stakes content where appropriate.

### Commercial usability

- [ ] A teacher can understand the value quickly.
- [ ] The prompt saves meaningful preparation time.
- [ ] Variables make the workflow reusable.
- [ ] The workflow could reasonably stand alone as a useful product feature.

---

## 29. File naming

Subject and module files should follow the repository taxonomy.

Individual workflow files should use stable IDs where individual files are required.

Where multiple compact prompts are logically grouped, a module file may contain multiple entries. The architecture does not require one file per prompt.

---

## 30. Versioning

Prompt versions should change when the task logic, requirements or output contract materially changes.

Minor editorial corrections do not necessarily require a new major version.

The repository Git history remains the authoritative record of source changes.

---

## 31. Generation policy

New prompt generation must be **gap-driven**.

Do not continue a numerical sequence simply because the next ID is available.

Before creating a new workflow:

1. Check the workflow inventory.
2. Search existing source material.
3. Check for an existing reusable workflow.
4. Check whether the need can be handled through variables.
5. Create a new workflow only when there is a genuine gap or materially better task design.

---

## 32. Canonical principle

> **Build a comprehensive library of teacher workflows, not a library of repetitive prompt text.**

The purpose of this specification is to make the library scalable, maintainable, commercially useful and practical for teachers.
