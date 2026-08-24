# Primary English Workflow Library

English is organised by **job to be done**, not by AI tool and not by a flat list of prompts.

## Architecture

```text
Global Prompt Standard
        ↓
Master Prompt Framework
        ↓
Primary Teacher Framework
        ↓
English Framework
        ↓
English Workflow
        ↓
AI Output
```

The English Framework supplies subject-specific rules inherited by all workflows. Individual workflows contain only the information that makes the task materially different. See `004-english-framework.md` and `PROMPT_MASTER_SPECIFICATION.md` for the governing standards.

## Workflow Index

| ID | Workflow | File | Primary use |
|---|---|---|---|
| RD-01 | Reading retrieval | `reading.md` | Recall and retrieval |
| RD-02 | Reading inference | `reading.md` | Evidence-based inference |
| RD-03 | Reading vocabulary in context | `reading.md` | Word meaning |
| RD-04 | Reading prediction | `reading.md` | Prediction from evidence |
| RD-05 | Reading explanation | `reading.md` | Explain ideas and evidence |
| RD-06 | Summarise text | `reading.md` | Concise summarising |
| RD-07 | Compare texts / characters | `reading.md` | Comparative reading |
| RD-08 | Analyse author choices | `reading.md` | Language and structural choices |
| RD-09 | Reading misconception diagnosis | `reading.md` | Diagnose reading difficulty |
| RD-10 | Reading intervention | `reading.md` | Targeted support |
| RD-11 | Guided reading | `reading.md` | Small-group / guided reading |
| RD-12 | Whole-class reading | `reading.md` | Whole-class sequence |
| WR-01 | Writing lesson sequence | `writing.md` | Writing instruction |
| WR-02 | Model text | `writing.md` | Teacher modelling |
| WR-03 | Writing plan / organiser | `writing.md` | Planning |
| WR-04 | Sentence construction | `writing.md` | Sentence-level practice |
| WR-05 | Paragraph construction | `writing.md` | Organisation of ideas |
| WR-06 | Vocabulary and word choice | `writing.md` | Precision and effect |
| WR-07 | Editing / proofreading | `writing.md` | Editing accuracy |
| WR-08 | Writing scaffold | `writing.md` | Adaptive support |
| WR-09 | Independent writing task | `writing.md` | Independent application |
| WR-10 | Greater-depth writing | `writing.md` | Depth and control |
| WR-11 | Assess writing | `writing.md` | Evidence-based assessment |
| WR-12 | Diagnose writing misconceptions | `writing.md` | Diagnostic teaching |
| GPS-01 | Grammar lesson sequence | `grammar-punctuation-spelling.md` | Grammar instruction |
| GPS-02 | Grammar explanation | `grammar-punctuation-spelling.md` | Pupil explanation |
| GPS-03 | Grammar practice | `grammar-punctuation-spelling.md` | Practice |
| GPS-04 | Grammar misconception diagnosis | `grammar-punctuation-spelling.md` | Diagnosis |
| GPS-05 | Punctuation teaching | `grammar-punctuation-spelling.md` | Punctuation instruction |
| GPS-06 | Punctuation proofreading | `grammar-punctuation-spelling.md` | Editing |
| GPS-07 | Spelling pattern lesson | `grammar-punctuation-spelling.md` | Spelling instruction |
| GPS-08 | Spelling retrieval | `grammar-punctuation-spelling.md` | Retrieval |
| GPS-09 | GPS assessment | `grammar-punctuation-spelling.md` | Assessment |
| GPS-10 | Adapt GPS practice | `grammar-punctuation-spelling.md` | SEND / EAL / adaptive teaching |
| GPS-11 | Edit pupil writing for GPS | `grammar-punctuation-spelling.md` | Analysis |
| GPS-12 | GPS retrieval starter | `grammar-punctuation-spelling.md` | Lesson starter |
| VO-01 | Vocabulary teaching sequence | `vocabulary-oracy.md` | Vocabulary instruction |
| VO-02 | Vocabulary in context | `vocabulary-oracy.md` | Contextual meaning |
| VO-03 | Vocabulary retrieval | `vocabulary-oracy.md` | Retention |
| VO-04 | Vocabulary for writing | `vocabulary-oracy.md` | Writing vocabulary |
| VO-05 | Speaking and listening activity | `vocabulary-oracy.md` | Purposeful talk |
| VO-06 | Structured discussion / debate | `vocabulary-oracy.md` | Discussion |
| VO-07 | Oral rehearsal before writing | `vocabulary-oracy.md` | Talk for writing |
| VO-08 | Classroom questioning | `vocabulary-oracy.md` | Teacher questioning |
| VO-09 | Academic language / sentence stems | `vocabulary-oracy.md` | Language access |
| VO-10 | Vocabulary misconception diagnosis | `vocabulary-oracy.md` | Diagnostic teaching |
| VO-11 | Oracy assessment checklist | `vocabulary-oracy.md` | Observation |
| VO-12 | Adapt vocabulary / oracy | `vocabulary-oracy.md` | Adaptive teaching |
| PH-01 | Phonics lesson sequence | `phonics.md` | Systematic phonics |
| PH-02 | GPC practice | `phonics.md` | Grapheme-phoneme correspondence |
| PH-03 | Blending / segmenting | `phonics.md` | Decoding / encoding |
| PH-04 | Decodable text | `phonics.md` | Application |
| PH-05 | Phonics assessment | `phonics.md` | Formative assessment |
| PH-06 | Phonics misconception diagnosis | `phonics.md` | Diagnostic teaching |
| PH-07 | Phonics intervention | `phonics.md` | Targeted intervention |
| PH-08 | Adapt phonics activity | `phonics.md` | Adaptive teaching |
| HW-01 | Handwriting lesson sequence | `handwriting.md` | Handwriting instruction |
| HW-02 | Letter formation practice | `handwriting.md` | Letter formation |
| HW-03 | Joining / fluency practice | `handwriting.md` | Transcription fluency |
| HW-04 | Handwriting misconception diagnosis | `handwriting.md` | Diagnostic support |
| HW-05 | Handwriting practice sheet | `handwriting.md` | Printable practice |
| HW-06 | Adapt handwriting activity | `handwriting.md` | Adaptive teaching |

## Current coverage

**62 workflows** across six English strands:

- Reading: 12
- Writing: 12
- Grammar, punctuation and spelling: 12
- Vocabulary and oracy: 12
- Phonics: 8
- Handwriting: 6

This is intentionally a **workflow library**, not a target-driven collection of hundreds of near-duplicate prompts.

## Model and verification metadata

AI compatibility is maintained as metadata rather than repeated inside every prompt. The verification record should identify:

- AI tool
- Exact model / model family
- Test date
- Verification result
- Reviewer notes
- Next scheduled review

A workflow marked `Verified` means it has been tested against the recorded model and produced an output meeting its quality gates. It does **not** mean that future model versions are guaranteed to behave identically.

### Verification cadence

- Quarterly re-verification for published workflows.
- Immediate review when a major model or platform change is known to affect output behaviour.
- Failed verification moves the workflow to `Review Required` until corrected and retested.

## Worked examples

Worked examples belong at the **workflow-category level** in the published book rather than being duplicated blindly after every prompt. Each category should show:

1. Teacher input
2. Workflow used
3. Representative AI output
4. Why the output is useful
5. What the teacher should check or customise

This keeps the final product useful as a searchable reference without turning it into an unnecessarily large wall of text.

## Publication principle

The final publication should be organised around teacher outcomes and jobs to be done. Tool-specific guidance belongs in compatibility metadata and appendices, not in the main navigation.
