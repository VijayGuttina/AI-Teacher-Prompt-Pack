# Primary Teacher Library: Initial Content Audit

## Audit status

**Audit type:** Structural and sample-content audit

**Date:** 21 August 2026

**Repository:** `VijayGuttina/AI-Teacher-Prompt-Pack`

**Purpose:** Establish what already exists before any further large-scale prompt generation.

## Executive finding

The repository contains substantial valuable source material, but it is still in a transitional state between the original long-form prompt-book model and the new modular workflow model.

The correct next action is **not** to generate more long-form prompts. The correct action is to inventory and consolidate the existing material into reusable teaching workflows.

## Evidence reviewed

The audit reviewed the repository tree, the primary-teacher taxonomy, the master and primary frameworks, the English framework, the migration plan, the General Teaching source file and representative long-form English content.

### Current source scale

- `books/primary-teacher/004-english.md` is approximately **1.06 MB** and contains the long-form English library.
- The existing project history has generated English prompts through **PT-ENG-057**.
- `books/primary-teacher/003-planning.md` is approximately **201 KB** and its front matter currently declares `prompt_count: 60` and `chapter: General Teaching`.
- The repository therefore contains a significant amount of reusable source material already. Continuing the old one-prompt-at-a-time process would increase duplication rather than improve product coverage.

## Structural findings

### 1. Legacy monolithic files coexist with modular directories

Examples include:

- `004-english.md` alongside `004-english/`
- `005-maths.md` alongside `005-mathematics/`
- `003-planning.md` alongside `003-planning/`

The directory versions are currently mostly placeholders while the large `.md` files contain the substantive legacy content.

**Decision:** Preserve the legacy files during migration. Do not delete them yet.

### 2. Chapter/file naming is not yet authoritative

`003-planning.md` currently contains front matter identifying the chapter as **General Teaching**, including a General Teaching prompt set. This means the filename and content taxonomy are not reliably aligned.

**Decision:** Treat the taxonomy and workflow inventory as authoritative during migration. Do not infer content ownership solely from filenames.

### 3. English is already highly developed but overly expanded

The first English prompt contains a full ROLE, CONTEXT, TASK, REQUIREMENTS, OUTPUT FORMAT, QUALITY CHECKS and OPTIONAL CUSTOMISATION layer, plus metadata, examples, tips, common mistakes and related prompts. Subsequent prompts repeat much of the same structure.

The English-specific framework already exists and contains the reusable English teaching rules and quality gates.

**Decision:** Refactor English by extracting inherited material and retaining only workflow-specific instructions in each prompt.

### 4. General teaching contains reusable cross-subject workflows

The General Teaching source explicitly includes workflows such as lesson planning and differentiation. These overlap with functions that would otherwise be repeated inside individual subject modules.

**Decision:** Keep cross-subject workflows in the General Teaching layer and reference them from subject modules where appropriate instead of recreating them.

### 5. The master specification requires correction before it becomes the canonical contract

The current `PROMPT_MASTER_SPECIFICATION.md` contains a fully populated English prompt example rather than a clean master authoring specification. It should therefore not be treated as the final metadata/schema contract for future automated generation.

**Decision:** Before mass migration or new generation, convert the master specification into a true schema/contract document and move any example prompt content out of it.

## Repetition patterns identified

The legacy prompt format repeatedly embeds information that belongs at framework level, including:

- AI model compatibility tables
- generic role descriptions
- general primary teaching principles
- SEND/EAL principles
- generic lesson structures
- generic quality checks
- generic output guidance
- repeated examples and pro tips
- repeated related-prompt navigation

This is precisely the duplication the modular architecture is intended to remove.

## Target content model

The migration should transform:

```text
Large standalone prompt
        ↓
Teacher workflow
        ↓
Reusable variables
        ↓
Unique task instructions
        ↓
Inherited framework rules
        ↓
Compact prompt entry
```

The target is normally a **50–150 line prompt entry**, with longer entries retained only where the additional task-specific detail materially improves output quality.

## What must be preserved

During migration, preserve:

- genuinely useful teacher workflows
- strong task instructions
- subject-specific constraints
- useful editable variables
- high-quality examples where they demonstrate non-obvious usage
- useful answer guidance
- subject-specific quality gates
- valuable curriculum distinctions

Do not preserve duplication merely because it already exists.

## What should normally be removed from individual prompts

Where already inherited from the framework, remove repeated:

- global role instructions
- general UK-primary assumptions
- generic AI model compatibility tables
- generic lesson structures
- generic quality gates
- generic SEND/EAL guidance
- generic tips
- generic common mistakes
- generic related-prompt descriptions

## Migration priority

1. Correct the canonical prompt specification.
2. Build the workflow inventory.
3. Audit General Teaching and Planning for overlap.
4. Consolidate high-frequency cross-subject workflows.
5. Refactor English using the English framework.
6. Refactor Mathematics and other substantive modules as source material becomes available.
7. Create compact subject/workflow entries only for genuine gaps.
8. Build the final prompt index.
9. Build publication editions from the curated source library.

## Stop condition for new generation

Do **not** resume sequential generation such as `PT-ENG-058`, `PT-ENG-059`, etc. until the workflow inventory identifies a genuine uncovered workflow or a materially improved replacement.

The next generated content should be driven by a documented gap, not by the next unused prompt number.
