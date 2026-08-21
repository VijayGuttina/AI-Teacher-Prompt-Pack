# Migration Plan: Long-Form Prompts to Modular Prompt System

## Decision

Stop generating new prompts in the old fully expanded format after PT-ENG-057. New prompts use the modular architecture.

## Preserve

Existing long-form prompts remain as source material. They should not be deleted until reviewed and refactored.

## Refactor order

1. Extract duplicated global metadata and authoring rules into `PROMPT_MASTER_SPECIFICATION.md` when available.
2. Extract common teaching instructions into `MASTER_PROMPT_FRAMEWORK.md`.
3. Extract primary-specific rules into `books/primary-teacher/001-master-framework.md`.
4. Extract English-specific rules into `books/primary-teacher/004-english-framework.md`.
5. Reduce each prompt to its unique specification.
6. Remove repeated examples, generic tips and common quality gates unless they add prompt-specific value.
7. Create a prompt index so teachers can find prompts by task, year group and output.

## Target

Aim for most individual prompts to be 50-150 lines. Keep longer prompts only where the additional detail materially improves the generated result.

## Product strategy

The commercial product should be organised around teaching workflows and use cases, not raw prompt count. A curated library plus reusable frameworks can generate hundreds of practical variations without storing hundreds of near-duplicate giant prompts.

## Immediate action

PT-ENG-058 onward should use the compact format. Existing PT-ENG-001 through PT-ENG-057 can be progressively refactored later.
