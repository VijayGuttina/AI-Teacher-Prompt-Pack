# Commercial V1 build status

Updated after the publication-pipeline pass.

- Commercial edition: V1.0
- Commercial prompts: 127
- Source of truth: `books/commercial-primary-teacher/`
- Build script: `build/build-commercial.py`
- Automated QA: `build/qa-commercial.py`
- Page-break filter: `build/pagebreak.lua`
- Reference DOCX generator: `build/create-commercial-reference.py`
- PDF layout header: `build/commercial-pdf-header.tex`
- Publication checklist: `build/publication-checklist.md`
- Generated release binaries are intentionally not committed until the local publication build and visual QA have been completed.

## Publication formatting fixes

The PDF build now uses `build/commercial-pdf-header.tex` to enable line wrapping for long fenced prompt blocks. This prevents long copy-and-paste instructions from running into the A4 page margin or being clipped by the PDF layout.

Commercial prompt labels remain explicitly bold in the Markdown source, including **Best for**, **Use when**, **Difficulty**, **Copy and paste**, **Example input**, **Example output**, **Teacher tip** and **Related prompts**. This preserves the intended scanning hierarchy across DOCX and PDF.

## Next execution step

From the repository root run:

```powershell
python build/qa-commercial.py
python build/build-commercial.py
python build/create-commercial-reference.py
```

Then generate the DOCX and PDF using the commands in `build/README.md`, followed by the visual QA checklist in `build/publication-checklist.md`.
