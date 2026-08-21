# Primary Teacher AI Prompt Library Blueprint

## 1. Purpose

This blueprint defines the commercial and editorial architecture for the Primary Teacher AI Prompt Library.

The objective is not to maximise prompt count. The objective is to provide broad, practical coverage of the real workflows primary teachers perform, using reusable prompt systems that can be adapted across year groups, subjects, abilities and classroom contexts.

The library should therefore be treated as a **teaching workflow system**, not a catalogue of hundreds of isolated prompts.

## 2. Product principle

One strong workflow can replace many near-identical prompts.

A workflow should expose the variables that materially change the output, for example:

- Year group
- Subject
- Topic
- Learning objective
- Curriculum requirement
- Lesson duration
- Ability range
- SEND / accessibility requirements
- Prior learning
- Resource constraints
- Desired output

The library should avoid separate prompts when the only difference is a year group, topic, difficulty level or output variation that can be controlled through variables.

## 3. Layered architecture

```text
GLOBAL PROMPT MASTER SPECIFICATION
        ↓
MASTER TEACHER FRAMEWORK
        ↓
PRIMARY TEACHER OPERATING FRAMEWORK
        ↓
LIBRARY MODULE
        ↓
SUBJECT / WORKFLOW FRAMEWORK
        ↓
REUSABLE PROMPT
        ↓
VARIABLES + EXAMPLE + TEACHER TIP
```

## 4. Product layers

### Layer 1: Core operating system

These are shared across the entire primary library:

1. Master framework
2. Primary teacher framework
3. Prompt specification
4. Quality standards
5. UK education context
6. AI safety and verification guidance
7. Prompt usage instructions

### Layer 2: Teacher workflow modules

These cover recurring teacher jobs regardless of subject:

1. Planning
2. Assessment and feedback
3. Differentiation and adaptive teaching
4. Classroom management
5. Parent and carer communication
6. Inclusion, SEND and accessibility
7. Teacher workload and organisation
8. Intervention and catch-up
9. Home learning
10. Assemblies and school events
11. Professional reflection and development
12. AI implementation

### Layer 3: Curriculum subjects

1. English
2. Mathematics
3. Science
4. History
5. Geography
6. Computing
7. Art and Design
8. Design and Technology
9. Music
10. Physical Education
11. Religious Education
12. Modern Foreign Languages
13. PSHE / RSHE / Personal Development

### Layer 4: Cross-curricular specialist modules

1. Reading across the curriculum
2. Writing across the curriculum
3. Oracy and discussion
4. Vocabulary and language development
5. Phonics and early reading
6. EYFS transition and foundations
7. SATs and statutory assessment preparation
8. Intervention and targeted support
9. Enrichment and clubs
10. Educational visits and trips

## 5. Recommended workflow coverage

The following is the initial target range. These are **workflow targets, not mandatory prompt counts**.

| Module | Target workflows |
|---|---:|
| General teaching | 20-30 |
| Planning | 25-35 |
| English | 35-45 |
| Mathematics | 30-40 |
| Science | 20-30 |
| History | 15-25 |
| Geography | 15-25 |
| Computing | 15-25 |
| Art and Design | 12-20 |
| Design and Technology | 12-20 |
| Music | 12-20 |
| PE | 12-20 |
| RE | 12-20 |
| MFL | 12-20 |
| PSHE / RSHE | 15-25 |
| Assessment and feedback | 25-35 |
| Differentiation / SEND | 25-35 |
| Classroom management | 20-30 |
| Parent communication | 20-25 |
| Workload / organisation | 15-20 |
| Intervention / catch-up | 15-20 |
| Cross-curricular specialist | 30-40 |

These ranges are deliberately bounded. The library should not expand simply to satisfy a numerical target.

## 6. What constitutes a workflow

A workflow should solve a recognisable teacher task from start to finish.

Examples:

- Turn a learning objective into a differentiated lesson sequence.
- Generate retrieval questions from a topic.
- Create an exit ticket aligned to the lesson objective.
- Analyse a pupil response and identify misconceptions.
- Produce three levels of scaffolding for a writing task.
- Convert a curriculum objective into a sequence of lessons.
- Create vocabulary instruction for a topic.
- Draft a professional parent communication from teacher notes.
- Produce an intervention activity from an identified misconception.
- Adapt a worksheet for accessibility needs.

A workflow is **not** simply a minor variation such as changing "Year 3" to "Year 4".

## 7. Individual prompt entry standard

Each reusable prompt should normally contain:

1. Prompt ID
2. Prompt title
3. Category
4. Workflow
5. Purpose
6. Difficulty
7. AI model compatibility
8. Expected output length
9. Typical generation time
10. Curriculum tags
11. Editable variables
12. Example input
13. Example output
14. The copy-and-paste prompt
15. Quality checks
16. Teacher tip
17. Related workflows

The exact field names and ordering remain governed by `PROMPT_MASTER_SPECIFICATION.md`.

## 8. Prompt inheritance

Global instructions should not be copied into every prompt.

For example, the following belong in the framework layer rather than repeated in every entry:

- Act as an experienced primary teacher.
- Use UK English.
- Keep outputs age appropriate.
- Avoid invented curriculum claims.
- Flag uncertainty where necessary.
- Follow safeguarding constraints.
- Use clear classroom-ready formatting.

Individual prompts should contain only task-specific requirements.

## 9. Product packaging

The underlying library should support multiple commercial products without duplicating the source content.

### Primary Teacher Complete Library

A broad collection of the primary workflows and subject systems.

### Subject Packs

Examples:

- Primary English AI Prompt Pack
- Primary Mathematics AI Prompt Pack
- Primary Science AI Prompt Pack

### Professional Workflow Packs

Examples:

- Assessment and Grading
- Parent Communication
- Classroom Management
- Differentiation and SEND
- Planning

### Implementation Products

Examples:

- 30-Day AI Implementation Planner
- AI Quick-Start Toolkit
- Teacher AI Workflow Cards

A source workflow may therefore appear in more than one product through controlled publishing metadata, without creating multiple independent copies.

## 10. Commercial design principle

The product should sell **time saved and teaching capability**, not raw prompt volume.

A teacher should be able to open the book and quickly answer:

- What can I use this for?
- What information do I need to provide?
- What will AI produce?
- How do I customise it?
- What should I check before using the result?

Every workflow should support those decisions.

## 11. Migration strategy

Existing long-form prompt material is treated as source content.

Migration sequence:

```text
Legacy prompt
    ↓
Identify teacher task
    ↓
Assign module
    ↓
Detect duplicates
    ↓
Extract variables
    ↓
Consolidate variants
    ↓
Apply master specification
    ↓
Quality review
    ↓
Reusable workflow
```

No legacy content should be deleted until its useful information has been assessed.

## 12. Content prioritisation

When choosing what to retain or create, prioritise:

### Tier 1: High-frequency teacher jobs

Tasks teachers perform regularly and for which AI can provide substantial time savings.

### Tier 2: High-value specialist workflows

Tasks that require expertise, differentiation or complex preparation.

### Tier 3: Occasional workflows

Useful but less frequent tasks such as trips, assemblies or special events.

### Tier 4: Decorative or low-value variations

Near-duplicate prompts, trivial rewrites and prompts that add little beyond changing a variable should not be retained as separate workflows.

## 13. Definition of done

The Primary Teacher Library is not complete when it contains a particular number of prompts.

A module is complete when:

- its major teacher workflows are covered;
- obvious gaps have been assessed;
- duplicate prompts have been consolidated;
- variables are reusable;
- prompts meet the master specification;
- outputs are practical and classroom-ready;
- examples demonstrate real use;
- quality checks are explicit;
- the module can be packaged independently if commercially useful.

## 14. Current implementation priority

The build should proceed in this order:

1. Finalise architecture and taxonomy.
2. Audit existing long-form source content.
3. Build the workflow inventory.
4. Consolidate duplicate prompts.
5. Finalise core teaching workflows.
6. Finalise English and Mathematics.
7. Build remaining core subjects.
8. Build specialist and cross-curricular modules.
9. Build publishing metadata and indexes.
10. Produce commercial book editions.

The immediate priority is **workflow inventory and migration**, not further one-by-one prompt generation.
