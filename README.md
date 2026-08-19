# AI Teacher Prompt Library

> **A professional, version-controlled publishing repository for creating the world's most comprehensive collection of AI prompts for educators.**

---

# Overview

The **AI Teacher Prompt Library** is a long-term publishing project designed to create premium AI prompt packs for teachers, school leaders, teaching assistants, tutors and educational professionals.

The repository serves as the **single source of truth** for all content. Every prompt, chapter, template and publication is maintained here before being exported into professionally formatted Microsoft Word and PDF books.

The project aims to provide practical, evidence-informed, classroom-ready prompts that help educators save time, improve teaching quality and make effective use of generative AI tools such as ChatGPT.

---

# Vision

To create the most comprehensive teacher AI prompt library available.

The completed library will include more than **1,500 high-quality prompts** organised into specialist prompt packs and supported by a consistent editorial standard and publishing workflow.

---

# Project Objectives

- Produce commercially publishable prompt books.
- Maintain one authoritative source for all content.
- Use consistent prompt architecture across every publication.
- Ensure every prompt is classroom-ready and copy-and-paste ready.
- Support rapid future expansion.
- Enable automated production of Word and PDF editions.

---

# Repository Structure

```
AI-Teacher-Prompt-Pack/
│
├── README.md
├── STYLE_GUIDE.md
├── PROMPT_GUIDELINES.md
├── BOOK_SPECIFICATION.md
├── BUILD.md
├── ROADMAP.md
│
├── docs/
│
├── templates/
│
├── books/
│
├── assets/
│
├── exports/
│
└── build/
```

---

# Repository Purpose

This repository is divided into six logical areas.

## 1. Books

Contains the source manuscript for every publication.

Examples include:

- Primary Teacher Prompt Pack
- Secondary Teacher Prompt Pack
- Assessment & Grading Pack
- Parent Communication Pack
- Classroom Management Pack
- 30-Day AI Implementation Planner
- Teacher AI Prompt Library (Complete Edition)

Markdown files inside this folder are considered the master manuscript.

---

## 2. Templates

Reusable templates used throughout the project.

Examples include:

- Prompt Template
- Lesson Template
- Assessment Template
- Planner Template

Templates ensure consistency across every publication.

---

## 3. Assets

Contains all supporting resources.

Examples:

- Book covers
- Icons
- Images
- Branding
- Diagrams

---

## 4. Build

Contains scripts, templates and configuration used to generate finished publications.

This folder should never contain book content.

---

## 5. Exports

Contains generated output.

Examples:

```
DOCX

PDF

EPUB
```

Files inside this folder should be treated as generated artefacts rather than source content.

---

## 6. Documentation

Contains project documentation.

Examples include:

- Editorial decisions
- Publishing checklist
- Release notes
- Design decisions

---

# Publishing Workflow

The publishing workflow follows a simple principle:

**Markdown is the single source of truth.**

```
Markdown

↓

Editorial Review

↓

Git Commit

↓

Build

↓

DOCX

↓

PDF

↓

Release
```

Books should never be edited directly in Word unless correcting final formatting issues before publication.

---

# Prompt Standard

Every prompt within this repository follows the same architecture.

```
Purpose

ROLE

CONTEXT

TASK

REQUIREMENTS

OUTPUT FORMAT

QUALITY CHECKS

OPTIONAL CUSTOMISATION

Pro Tip

Related Prompts
```

The complete specification is defined in:

`PROMPT_GUIDELINES.md`

---

# Editorial Standards

Every publication follows the standards defined in:

- STYLE_GUIDE.md
- PROMPT_GUIDELINES.md
- BOOK_SPECIFICATION.md

These standards should not be bypassed.

---

# Educational Standards

Where appropriate, prompts should align with recognised educational practice including:

- National Curriculum for England
- Early Years Foundation Stage Framework
- Rosenshine's Principles of Instruction
- Retrieval Practice
- Cognitive Load Theory
- Formative Assessment
- Adaptive Teaching
- Universal Design for Learning (UDL)
- Metacognition

The aim is to create prompts that are evidence-informed while remaining practical for everyday classroom use.

---

# Books in Development

Current planned publications include:

- Primary Teacher Prompt Pack
- Secondary Teacher Prompt Pack
- Assessment & Grading Pack
- Parent Communication Pack
- Classroom Management Pack
- 30-Day AI Implementation Planner
- Teacher AI Prompt Library – Complete Edition

Additional specialist volumes may be added in future releases.

---

# Version Control

This repository uses Git for version control.

All significant changes should be committed with meaningful commit messages.

Example:

```
Completed English chapter

Added Prompt Template

Updated Editorial Style Guide

Expanded Assessment Prompt Pack
```

---

# Branch Strategy

Recommended workflow:

```
main

↓

feature/<topic>

↓

review

↓

merge
```

For solo development, working directly on `main` is acceptable until collaboration becomes necessary.

---

# Build Process

The build process is documented in:

`BUILD.md`

Do not duplicate build instructions elsewhere in the repository.

---

# Contributing

When adding new content:

1. Follow `PROMPT_GUIDELINES.md`.
2. Follow `STYLE_GUIDE.md`.
3. Ensure UK English spelling is used.
4. Maintain consistent formatting.
5. Verify prompt numbering.
6. Check related prompt references.
7. Commit changes with a descriptive message.

---

# Quality Commitment

Every publication produced from this repository should be:

- Accurate
- Practical
- Professional
- Evidence-informed
- Classroom-ready
- Consistently formatted
- Commercially publishable

Quality takes precedence over speed.

---

# Roadmap

Project milestones and planned publications are maintained in:

`ROADMAP.md`

---

# Licence

Copyright © 2026.

All rights reserved.

This repository is intended for the development of commercial educational publications.

Do not redistribute source material without permission.

---

# Revision History

| Version | Date | Summary |
|----------|------|---------|
| 1.0.0 | 3 August 2026 | Initial repository documentation |
