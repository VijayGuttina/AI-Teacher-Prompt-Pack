# Commercial V1 publication checklist

## Build
- [ ] Run `python build/qa-commercial.py`
- [ ] Run `python build/build-commercial.py`
- [ ] Create `build/commercial-reference.docx`
- [ ] Generate the DOCX
- [ ] Generate the PDF

## Automated QA
- [ ] 127 prompts present
- [ ] Prompt numbers 001-127 are unique and sequential
- [ ] Required commercial metadata is present
- [ ] No em dash or en dash
- [ ] No TODO, TBD or placeholder text
- [ ] Source and assembled prompt sequences match

## Visual QA
- [ ] Cover looks professional
- [ ] TOC is correct
- [ ] Major sections start on new pages
- [ ] Prompt headings stay with their content
- [ ] Prompt blocks wrap correctly
- [ ] No blank pages
- [ ] No orphaned headings
- [ ] Page numbers appear correctly
- [ ] Header/footer treatment is consistent
- [ ] Tables and links render correctly

## Content QA
- [ ] UK English
- [ ] No unnecessary repetition
- [ ] Prompts are practical and copy/paste ready
- [ ] Teacher judgement and safeguarding boundaries are clear
- [ ] No artificial prompt-count inflation

## Final release
- [ ] PDF copy/paste tested
- [ ] DOCX editability tested
- [ ] Final page count recorded
- [ ] Version number is V1.0
- [ ] Release filenames are correct
- [ ] GitHub PR updated
