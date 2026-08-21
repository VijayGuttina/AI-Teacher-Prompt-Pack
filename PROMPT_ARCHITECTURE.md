# Prompt Architecture

## Objective

Build a commercially useful teacher prompt library without duplicating the same instructions hundreds of times.

## Four-layer model

1. **Global layer**
   - PROMPT_MASTER_SPECIFICATION.md
   - Shared metadata, authoring standards, safety/quality expectations, compatibility and editorial rules.

2. **Teaching layer**
   - MASTER_PROMPT_FRAMEWORK.md
   - Shared role, context handling, task design, differentiation, assessment, output and quality principles.

3. **Subject layer**
   - Subject-specific pedagogical rules, curriculum language, common output structures and subject quality gates.

4. **Prompt layer**
   - A concise prompt entry containing only the unique teaching objective, variables, requirements and any genuinely prompt-specific quality checks.

## Inheritance principle

A prompt entry is interpreted as:

`Global Specification + Teaching Framework + Subject Framework + Prompt Specification + User Variables`

The prompt entry must not restate inherited material unless an intentional override is required.

## Target size

Most individual prompt entries should be approximately 50-150 lines. Exceptional prompts may be longer when the complexity materially improves the teacher's result.

## Product design

The product should optimise for:

- time saved
- classroom readiness
- reliable outputs
- discoverability
- customisation
- practical teaching value

It should not optimise for raw prompt count or page count.

## Recommended library structure

- 15-25 reusable teaching engines/frameworks
- 50-75 high-value master prompts
- 100-150 subject-specific prompts
- 30-40 assessment prompts
- 20-30 classroom-management prompts
- 20-30 parent-communication prompts
- 10-15 implementation workflows

The final product can expose many use cases through variables and prompt combinations without storing a separate giant prompt for every permutation.

## Prompt entry rule

Each prompt entry should contain:

1. ID and title
2. Purpose
3. Editable variables
4. Prompt-specific role/context override, only if needed
5. Task
6. Unique requirements
7. Output requirements or reference to the inherited output structure
8. Prompt-specific quality checks
9. Example input/output where it materially improves usability
10. Related prompts
11. Editorial status

Do not repeat the full global role, compatibility table, curriculum taxonomy, common differentiation rules, common quality gates, common metadata or generic teacher advice in every entry.
