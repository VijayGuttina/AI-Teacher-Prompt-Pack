# VS Code to GitHub Migration Map

This document maps the current local VS Code structure to the final modular product architecture.

## Immediate rule

Do not delete, rename or overwrite the legacy files until their useful content has been migrated and checked.

## Current primary-teacher structure

The local project currently contains both:

1. Modular subject folders such as `004-english/`, `005-mathematics/`, etc.
2. Legacy monolithic files such as `004-english.md`, `005-maths.md`, etc.

This duplication is intentional during migration.

## Target rule

The modular folder is the future source location. The legacy `.md` file becomes source material for migration and is eventually archived or removed only after review.

### Primary mapping

| Current legacy file | Target module |
|---|---|
| `002-general-teaching.md` | `002-general-teaching/` |
| `003-planning.md` | `003-planning/` |
| `004-english.md` | `004-english/` |
| `005-maths.md` | `005-mathematics/` |
| `006-science.md` | `006-science/` |
| `007-history.md` | `007-history/` |
| `008-geography.md` | `008-geography/` |
| `009-computing.md` | `009-computing/` |
| `010-art-design.md` | `010-art-and-design/` |
| `011-design-technology.md` | `011-design-and-technology/` |
| `012-pe.md` | `013-physical-education/` |
| `013-music.md` | `012-music/` |
| `014-re.md` | `020-religious-education/` |
| `015-pshe.md` | `022-citizenship-and-personal-development/` |
| `016-mfl.md` | `021-modern-foreign-languages/` |
| `017-send.md` | `015-differentiation-send/` / `031-inclusion-and-accessibility/` |
| `018-eal.md` | `015-differentiation-send/` / `026-vocabulary-and-language-development/` |
| `019-assessment.md` | `014-assessment-and-feedback/` |
| `020-behaviour.md` | `032-behaviour-and-pastoral-support/` |
| `021-parent-communication.md` | `017-parent-communication/` |
| `022-leadership.md` | `030-early-career-teacher-support` only where relevant; otherwise future leadership module |
| `023-subject-leaders.md` | future subject-leadership module |
| `024-ofsted.md` | `002-general-teaching/` or future school-leadership module, depending on content |
| `999-index.md` | `prompt-index.md` |

## Existing top-level product packs

The local folders:

- `books/ai-implementation-planner`
- `books/assessment-grading`
- `books/classroom-management`
- `books/parent-communication`

should be retained for now. They represent broader standalone product packs and may later become reusable source modules feeding the primary-teacher library.

Do not duplicate their content into the primary-teacher folders until the overlap has been assessed.

## Subject modules to establish

Primary teaching scope should include English, mathematics, science, history, geography, computing, art and design, design and technology, music, PE, RE, MFL and PSHE/personal development, plus cross-curricular and professional-practice modules defined in `PRIMARY_LIBRARY_TAXONOMY.md`.

## Legacy handling

When a legacy file has been fully migrated:

1. Compare it with the target module.
2. Confirm no unique content has been lost.
3. Move it to an `archive/legacy/` location or delete it in a controlled commit.
4. Update the migration log.

Never delete legacy source solely because a new empty folder exists.
