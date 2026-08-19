# AI Teacher Prompt Library
# Book Specification

**Version:** 1.0.0

**Status:** Approved

**Applies To:** Every book, workbook, planner and companion guide within the AI Teacher Prompt Library.

---

# Purpose

This document defines the publishing standards for every book produced from this repository.

Its purpose is to ensure every publication has a consistent appearance, structure, navigation, branding and reading experience.

This specification applies to all digital and printed editions.

---

# Publishing Principles

Every publication should be:

- Professional
- Consistent
- Easy to navigate
- Print friendly
- Kindle friendly (future)
- Commercially publishable
- Easy to maintain

---

# Target Formats

Every publication should be produced in the following formats where applicable.

| Format | Required |
|---------|----------|
| Markdown | ✓ |
| Microsoft Word (.docx) | ✓ |
| PDF | ✓ |
| EPUB | Future |
| HTML | Future |

Markdown is the master source.

All other formats are generated from Markdown.

---

# Book Sizes

## Standard Digital Edition

A4

Portrait

Recommended for:

- Printable resources
- School use
- Editable DOCX

---

## Standard Print Edition

6 x 9 inch

Portrait

Recommended for:

- Amazon KDP
- Paperback
- Hardback

---

# Page Margins

A4

Top: 2 cm

Bottom: 2 cm

Left: 2.5 cm

Right: 2 cm

Inside margins should increase for printed editions.

---

# Typography

## Primary Font

A clean sans-serif font.

Recommended:

- Aptos
- Calibri
- Source Sans Pro

---

## Headings

Heading 1

18 pt

Bold

Heading 2

16 pt

Bold

Heading 3

14 pt

Bold

Body

11 pt

---

# Line Spacing

Body text

1.15

Paragraph spacing

6 pt after

---

# Colour Palette

Primary

Navy

Secondary

Teal

Accent

Gold

Neutral

Dark Grey

Use colour sparingly.

Books must remain readable when printed in black and white.

---

# Page Numbering

Front matter

Roman numerals

i

ii

iii

Main content

Arabic numerals

1

2

3

---

# Front Matter

Every book should include the following.

1. Cover

2. Copyright

3. Disclaimer

4. About this Book

5. Who this Book is For

6. How to Use this Book

7. Table of Contents

8. Introduction

---

# Back Matter

Every book should include:

Appendix (where relevant)

Glossary

Prompt Index

Subject Index

Acknowledgements (optional)

About the Author

Other Books in the Series

Version Information

---

# Chapter Structure

Each chapter should begin on a new page.

Every chapter should contain:

Introduction

Prompt List

Chapter Summary (optional)

---

# Prompt Layout

Every prompt must follow the structure defined in:

PROMPT_GUIDELINES.md

No exceptions.

---

# Prompt Components

Every prompt should contain:

- Prompt Number
- Prompt Title
- Purpose
- Prompt
- Pro Tip
- Related Prompts

---

# Tables

Use tables where they improve readability.

Examples:

Planning

Assessment

Rubrics

Checklists

Comparisons

Avoid unnecessary tables.

---

# Images

Images are optional.

Where used:

Store in:

assets/images/

Use:

PNG

SVG

Avoid screenshots where possible.

---

# Icons

Icons may be used consistently throughout the books.

Recommended callouts:

💡 Pro Tip

⚠ Important

✅ Checklist

📚 Further Reading

🎯 Objective

Icons should support readability rather than decorate pages.

---

# Callout Boxes

Use callout boxes for:

Tips

Warnings

Examples

Common mistakes

Best practice

---

# Code Blocks

Prompt text should be presented in clearly separated blocks where appropriate to make copying easy.

Do not split prompts across pages unnecessarily.

---

# Navigation

Every publication should include:

Clickable Table of Contents (digital)

Bookmarks (PDF)

Consistent heading hierarchy

Prompt numbering

Cross references

---

# Hyperlinks

Internal links should be used where appropriate.

External links should be limited to trusted educational or official sources.

---

# Accessibility

Publications should be accessible.

Use:

Meaningful headings

Readable font sizes

Sufficient spacing

Alternative text for images where possible

Avoid colour-only meaning.

---

# Branding

Every publication should include:

Consistent cover design

Series branding

Edition number

Version number

Repository URL (optional)

Copyright notice

---

# Naming Convention

Book filenames should follow this format.

Primary-Teacher-Prompt-Pack-v1.0.docx

Primary-Teacher-Prompt-Pack-v1.0.pdf

Assessment-Grading-Pack-v1.0.pdf

Avoid spaces in filenames.

---

# Folder Structure

Generated books should be exported to:

exports/

Recommended structure:

exports/
├── docx/
├── pdf/
├── epub/
└── archive/

---

# Versioning

Books use Semantic Versioning.

Major release

1.0.0

New chapters

1.1.0

Minor improvements

1.1.1

Editorial corrections

1.1.2

---

# Build Process

Master Source

↓

Markdown

↓

Pandoc

↓

DOCX

↓

PDF

↓

Release

Markdown remains the single source of truth.

---

# Quality Assurance

Before publication every book should pass the following checks.

✓ All prompts follow PROMPT_GUIDELINES.md

✓ All formatting follows STYLE_GUIDE.md

✓ Table of Contents generated

✓ Page numbers correct

✓ Links working

✓ Prompt numbering sequential

✓ UK English spelling

✓ Grammar checked

✓ No placeholder text

✓ Images present where required

✓ Version number updated

✓ Revision history updated

---

# Release Checklist

Before publishing verify:

- Cover complete
- Front matter complete
- TOC complete
- Prompt numbering correct
- Cross references checked
- PDF tested
- DOCX tested
- Print layout reviewed
- Metadata updated
- Git tag created

---

# Future Publications

This specification supports:

- Primary Teacher Prompt Pack
- Secondary Teacher Prompt Pack
- Assessment & Grading Pack
- Parent Communication Pack
- Classroom Management Pack
- Teaching Assistant Pack
- School Leadership Pack
- SEND Pack
- AI Image Prompt Library
- AI Worksheet Library
- AI Presentation Library
- Teacher AI Prompt Library (Complete Edition)

---

# Revision History

| Version | Date | Summary |
|----------|------|---------|
| 1.0.0 | 3 August 2026 | Initial book specification |

---

**End of Document**