# Primary Mathematics Workflow Library

Mathematics is organised by teacher job-to-be-done rather than a flat list of prompts.

## Architecture

```text
Global Prompt Standard
        ↓
Master Prompt Framework
        ↓
Primary Teacher Framework
        ↓
Mathematics Framework
        ↓
Mathematics Workflow
        ↓
AI Output
```

## Current workflow coverage

| Strand | Workflows |
|---|---:|
| Number and place value | 10 |
| Calculation and fluency | 10 |
| Fractions, decimals and percentages | 10 |
| Geometry and measure | 10 |
| Problem solving and reasoning | 10 |
| Statistics and data | 10 |
| Assessment, diagnosis and intervention | 10 |
| **Current library total** | **70** |

The original 72-workflow figure was a planning ceiling, not a requirement to manufacture additional workflows. The library is intentionally frozen at 70 because each workflow represents a materially different teacher job-to-be-done.

## Quality standard

Every workflow inherits the Mathematics Framework and includes appropriate mathematical accuracy checks. Generated calculations, answer keys, examples, units and notation must be checked before publication.

## Verification standard

Each published workflow receives verification metadata recording:

- AI tool
- Exact model / model family
- Test date
- Representative test input
- Verification result
- Reviewer notes
- Next scheduled review

The current library has completed representative in-model execution testing on **ChatGPT / GPT-5.6 Luna on 25 August 2026**.

**70/70 workflows passed.**

This is qualitative execution verification for the recorded model and date. It does not claim multi-platform, API-level or universal reliability.

See:

- `VERIFICATION_REGISTER.md`
- `VERIFICATION_EXECUTION_LOG.md`

## Worked examples

The final publication will provide worked examples at category level rather than repeating large demonstrations after every workflow.

Each example should show:

1. Teacher input
2. Workflow used
3. Representative output
4. Why it is useful
5. What the teacher should check or customise

## Commercial design principle

The Mathematics book should feel like a searchable professional reference tool. It should not become a wall of repetitive prompts merely to increase the advertised prompt count.

## Repository hygiene

Empty legacy placeholders have been removed. The active subject modules are the seven files represented in the current workflow coverage table above.
