# AI Prompt Toolkit for Primary Teachers
## Commercial Edition V1 curation manifest

**Product price:** £24.99 regular
**Launch price:** £19.99
**Edition:** Commercial V1.0
**Target:** 120+ genuinely useful workflows, approximately 180–220 pages
**Source:** Existing verified primary-teacher master library

---

## Product rule

This manifest defines the commercial selection. It is deliberately smaller than the master library.

The commercial edition is not a dump of the repository. It is a curated teacher product built around the jobs teachers perform repeatedly and the workflows that save meaningful preparation time.

No new master-library families are required simply to reach the commercial target.

---

## Target allocation

| Commercial part | Target workflows | Primary purpose |
|---|---:|---|
| Plan | 24 | Planning, sequencing, objectives, differentiation and resources |
| Teach | 22 | Explanations, modelling, questioning, activities and retrieval |
| Assess | 18 | Formative assessment, diagnosis, feedback and assessment planning |
| Adapt | 16 | SEND, accessibility, scaffolding and responsive teaching |
| Subject Toolkit | 30 | High-value subject workflows across completed subject libraries |
| Save Time | 10 | Reuse, transform, adapt and repurpose existing teacher materials |
| **Total** | **120** | |

A small number of additional exceptional workflows may be included if they materially improve the product. Do not add filler to hit a page or prompt count.

---

# 1. Plan

### Source pool
- `books/primary-teacher/003-planning.md`
- `books/primary-teacher/002-general-teaching/`
- selected English, Mathematics and Science planning workflows

### Candidate selection
- PT-GEN-001 to PT-GEN-018: strongest cross-subject planning workflows
- PT-GEN-019 to PT-GEN-024: sequencing, objectives, differentiation and resource planning candidates
- 003-planning candidates should replace any legacy prompt where a newer modular workflow is clearly better

### Selection tests
- Does it solve a recurring planning task?
- Does it save at least a meaningful block of preparation time?
- Can one prompt serve multiple year groups through variables?
- Does the output have a useful classroom-ready structure?

**Target: 24 workflows.**

---

# 2. Teach

### Source pool
- `books/primary-teacher/003-planning.md` where teaching workflows are stronger than planning equivalents
- English reading, vocabulary and writing workflows
- Mathematics number, calculation and problem-solving workflows
- Science completed workflow library

### Candidate selection
- PT-GEN-025 to PT-GEN-032: general teaching candidates
- English: retrieval, inference, vocabulary, explanation, guided reading and discussion candidates
- Mathematics: explanation, modelling, fluency and reasoning candidates
- Science: explanation, enquiry and misconception candidates

**Target: 22 workflows.**

---

# 3. Assess

### Source pool
- `books/primary-teacher/018-assessment/assessment-planning-curriculum-alignment.md`
- `books/primary-teacher/018-assessment/formative-assessment-checking-understanding.md`
- selected completed subject assessment/diagnosis workflows

### Priority workflows
- AS-01 to AS-10
- AS-11 to AS-20

### Commercial selection
Select 18 from AS-01 to AS-20, prioritising:
- assessment planning
- hinge questions
- checking understanding
- exit tickets
- diagnostic questioning
- responsive teaching
- assessment workload
- quality assurance

Assessment expansion AS-21 to AS-100 remains paused for V1.

**Target: 18 workflows.**

---

# 4. Adapt

### Source pool
- `books/primary-teacher/017-send/`
- general teaching workflows
- relevant English and Mathematics adaptive workflows

### Priority
Select workflows that help a mainstream primary teacher adapt an existing lesson without lowering the intended learning demand.

Prioritise:
- scaffolding
- accessibility
- communication support
- executive-function support
- sensory/access adaptations
- responsive intervention
- inclusive participation

Do not turn the commercial section into a specialist SEND manual. The product is for mainstream primary teachers and should give them practical adaptations they can use immediately.

**Target: 16 workflows.**

---

# 5. Subject Toolkit

The subject section should demonstrate the breadth of the wider library without attempting to reproduce every subject workflow.

| Subject | Target |
|---|---:|
| English | 4 |
| Mathematics | 5 |
| Science | 4 |
| History | 2 |
| Geography | 2 |
| Computing | 2 |
| Art & Design | 2 |
| Design & Technology | 2 |
| Physical Education | 2 |
| Music | 2 |
| Religious Education | 1 |
| PSHE | 1 |
| Modern Foreign Languages | 1 |
| **Total** | **30** |

### Subject selection rule
Choose workflows with a clear teacher job-to-be-done. Prefer workflows that:
- are reusable across year groups;
- create an immediately usable classroom output;
- demonstrate subject-specific value that a generic prompt cannot reproduce;
- are already structurally verified and execution-tested in the source library.

SEND is represented in Adapt rather than duplicated here.

---

# 6. Save Time

### Source pool
Use the strongest existing workflows for transforming material teachers already have.

Priorities:
- turn notes into a lesson/resource
- adapt an existing lesson
- generate questions from supplied material
- convert a resource into multiple formats
- create differentiated versions
- create retrieval from existing content
- create examples from existing work
- repurpose a lesson sequence
- summarise teacher material into a usable planning format
- produce classroom-ready variations

**Target: 10 workflows.**

---

# Commercial quality gate

Every selected workflow must pass all of these checks before inclusion:

- [ ] Real teacher problem
- [ ] Meaningful time saving
- [ ] Strong first-pass output
- [ ] Minimal iteration normally required
- [ ] Clear editable variables
- [ ] Distinct from neighbouring workflows
- [ ] Useful across more than one narrow scenario where possible
- [ ] Professionally bounded
- [ ] Teacher judgement preserved
- [ ] No unnecessary pupil personal data
- [ ] UK English
- [ ] No em dash
- [ ] Existing source workflow is verified or receives final commercial QA before release

---

# Commercial presentation rule

The commercial book will not expose the full master-library metadata for every workflow.

Each published workflow will use:

1. Prompt number and title
2. Best for
3. Use when
4. Difficulty
5. Copy and paste
6. Example input
7. Example output
8. Teacher tip
9. Related prompts

The full master-library metadata remains in the source library.

---

# Product positioning

**120+ AI Prompts for Primary Teachers**

**Plan faster. Teach better. Assess smarter. Save hours every week.**

Supporting claim:

**200+ pages of practical guidance, examples and classroom-ready workflows.**

The primary value proposition is usefulness and time saved, not page count.

---

# Price architecture

**Regular price: £24.99**

**Launch price: £19.99**

Future editable DOCX bundle can be positioned at £29.99 without changing the core V1 product.

Do not add pricing language to individual prompts. Pricing belongs in the commercial front matter, sales page and release metadata.

---

# Build order

1. Freeze this manifest.
2. Resolve exact source workflow IDs for each candidate slot.
3. Extract selected workflows from the verified source library.
4. Reformat them into the commercial presentation.
5. Renumber sequentially as Commercial Prompt 001 onwards.
6. Add commercial examples and teacher tips where the source lacks a suitable example.
7. Build Plan, Teach, Assess, Adapt, Subject Toolkit and Save Time chapters.
8. Build indexes and cross-references.
9. Generate DOCX and A4 PDF from the Markdown master.
10. Run final editorial, copyability and layout QA.

---

## Status

**Stage:** Scope and curation architecture frozen

**Next build task:** Resolve the exact 120 source workflow IDs and create the commercial Markdown master without generating new master-library workflows unnecessarily.
