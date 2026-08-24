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

## Planned workflow coverage

| Strand | Initial target |
|---|---:|
| Number and place value | 10 |
| Calculation and fluency | 10 |
| Fractions, decimals and percentages | 10 |
| Geometry and measure | 10 |
| Problem solving and reasoning | 12 |
| Statistics and data | 8 |
| Assessment, diagnosis and intervention | 12 |
| **Initial library target** | **72** |

The target is a planning ceiling, not a requirement to manufacture 72 workflows. A workflow should only be added when it represents a materially different teacher job-to-be-done.

## Quality standard

Every workflow must inherit the mathematics framework and include appropriate mathematical accuracy checks. Generated calculations, answer keys, examples, units and notation must be checked before publication.

## Verification standard

Each published workflow will receive verification metadata recording:

- AI tool
- Exact model / model family
- Test date
- Representative test input
- Verification result
- Reviewer notes
- Next scheduled review

The initial verification status for newly authored workflows is `Not Yet Tested` until a representative execution has been performed.

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
