# Commercial V1 publication build

This directory contains the reproducible publication pipeline for the **AI Prompt Toolkit for Primary Teachers, Commercial Edition V1.0**.

The source of truth remains the Markdown under `books/commercial-primary-teacher/`. DOCX and PDF are generated outputs.

## Prerequisites

Install locally:

- Python 3.10+
- Pandoc
- XeLaTeX, normally via TeX Live or MiKTeX
- Python package `python-docx`

Windows users can use PowerShell. Pandoc and MiKTeX are suitable choices for the publication workflow.

## Build order

Run from the repository root:

```powershell
python build/qa-commercial.py
python build/build-commercial.py
python build/qa-commercial.py
```

The first QA pass validates the source library. The build assembles the commercial Markdown. The second QA pass validates the assembled publication.

## Create the reference DOCX

The reference DOCX is formatting only. It does not contain the commercial prompt library.

Run:

```powershell
python build/create-commercial-reference.py
```

This creates:

```text
build/commercial-reference.docx
```

It controls the publication styling used by Pandoc, including:

- A4 portrait page size
- 2 cm top/bottom margins
- 2.5 cm left margin
- 2 cm right margin
- Aptos typography
- 11 pt body text
- Heading 1 at 18 pt bold
- Heading 2 at 16 pt bold
- Heading 3 at 14 pt bold
- 1.15 line spacing
- 6 pt paragraph spacing
- page numbers
- header/footer treatment
- hyperlink styling
- readable prompt blocks

If the visual design changes, update the generator and recreate the reference DOCX rather than editing the generated reference file manually.

## Generate DOCX

Once `build/commercial-reference.docx` exists:

```powershell
pandoc exports/markdown/AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.md `
  --from markdown `
  --to docx `
  --toc `
  --number-sections `
  --reference-doc=build/commercial-reference.docx `
  --lua-filter=build/pagebreak.lua `
  -o exports/docx/AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.docx
```

## Generate PDF

```powershell
pandoc exports/markdown/AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.md `
  --from markdown `
  --pdf-engine=xelatex `
  --toc `
  --number-sections `
  --lua-filter=build/pagebreak.lua `
  -V geometry:a4paper `
  -V geometry:top=20mm `
  -V geometry:bottom=20mm `
  -V geometry:left=25mm `
  -V geometry:right=20mm `
  -o exports/pdf/AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.pdf
```

## Why the page-break filter exists

The commercial Markdown uses a neutral Pandoc `pagebreak` block between major parts. `build/pagebreak.lua` converts it to a real page break for both DOCX and PDF. This avoids putting raw LaTeX page-break commands into the master Markdown.

## QA checks

`qa-commercial.py` checks:

- all commercial source files exist
- prompt headings exist
- prompt numbers are sequential
- prompt numbers are unique
- at least 120 commercial prompts exist
- required commercial fields are present
- em dashes and en dashes are absent
- placeholder/TODO text is absent
- the assembled Markdown matches the source prompt sequence
- portable page-break blocks are present

The final PDF and DOCX still require visual inspection before release. Automated QA cannot reliably detect orphan headings, bad page breaks, poor prompt wrapping or other layout defects.

## Release outputs

```text
exports/
├── markdown/
│   └── AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.md
├── docx/
│   └── AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.docx
└── pdf/
    └── AI-Prompt-Toolkit-for-Primary-Teachers-v1.0.pdf
```

Generated files are release artefacts. Do not edit them directly. Fix the Markdown source or the reference template and rebuild.
