# Primary History Execution Test Plan

**Purpose:** Provide representative execution tests for History before workflows are marked `Verified`.

## Test design

The suite deliberately tests risk patterns rather than pretending that one generic test validates every workflow. After representative tests pass, remaining workflows receive targeted spot checks, especially where their behaviour differs materially from the tested pattern.

## Representative execution suite

| Test | Family | Risk/pattern |
|---|---|---|
| HT-01 | Enquiry | Open historical question rather than recall-only task |
| HT-02 | Enquiry | Evidence-led conclusion |
| HT-03 | Chronology | Sequencing and duration |
| HT-04 | Change/continuity | Distinguishing genuine change from superficial difference |
| HT-05 | Sources | Provenance and usefulness |
| HT-06 | Sources | Inference versus observation |
| HT-07 | Sources | No fabricated quotation/provenance |
| HT-08 | Interpretation | Comparing historical interpretations |
| HT-09 | Causation | Multiple causes and qualification |
| HT-10 | Significance | Explicit significance criteria |
| HT-11 | Ancient History | Avoiding anachronism and cultural overgeneralisation |
| HT-12 | British History | Contextual accuracy and scope |
| HT-13 | Local History | No invented local facts/sources |
| HT-14 | Comparison | Fair comparison using common criteria |
| HT-15 | Vocabulary | Historical terminology used meaningfully |
| HT-16 | Historical writing | Evidence-based explanation |
| HT-17 | Assessment | Misconception diagnosis from supplied evidence |
| HT-18 | Intervention/adaptation | Preserve historical reasoning while improving access |
| HT-19 | Assessment | Evidence-to-teaching decision traceability |
| HT-20 | Cross-family | Mixed workflow output completeness and teacher usability |

## Execution record requirements

For each test record:

- exact prompt/workflow ID
- representative input
- AI tool
- exact model/model family
- test date
- output result
- pass/fail decision
- reviewer notes
- any correction made
- re-test result where applicable

## Pass criteria

A test passes only when the output is:

- historically accurate for the supplied context
- appropriately cautious where evidence is incomplete
- free of invented quotations, sources, dates or provenance
- suitable for the stated primary phase/year group
- aligned to the workflow objective
- explicit about evidence versus inference where relevant
- usable by a teacher without requiring the AI to guess missing information
- safe and practical where classroom activities or fieldwork are involved

## Failure handling

Any material factual or disciplinary failure moves the affected workflow to `Tested - Fix Required`. The workflow is corrected and re-tested before it can become `Verified`.

A representative family-level pass does not automatically mark all workflows in that family as verified.
