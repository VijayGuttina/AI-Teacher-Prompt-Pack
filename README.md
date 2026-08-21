# AI Teacher Prompt Pack

A modular prompt system for primary teachers. The project is designed around reusable master frameworks, subject modules, and concise prompt specifications rather than hundreds of duplicated long-form prompts.

## Architecture

- `PROMPT_MASTER_SPECIFICATION.md` - global metadata and authoring contract
- `PROMPT_ARCHITECTURE.md` - modular prompt system and inheritance model
- `MASTER_PROMPT_FRAMEWORK.md` - reusable teacher-task generation framework
- `books/primary-teacher/001-master-framework.md` - primary-teacher operating layer
- `books/primary-teacher/004-english-framework.md` - English-specific layer
- `books/primary-teacher/004-english.md` - compact individual English prompt entries
- `docs/MIGRATION_PLAN.md` - migration from duplicated long-form prompts

## Authoring principle

Do not repeat global role instructions, quality gates, metadata, or common output structures inside every prompt. Individual prompts should contain only the information that makes them meaningfully different.
