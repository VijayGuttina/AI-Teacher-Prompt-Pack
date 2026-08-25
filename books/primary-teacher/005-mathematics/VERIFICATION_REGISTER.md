# Primary Mathematics Workflow Verification Register

**Purpose:** Record execution-based verification of the Mathematics workflow library.

**Important:** A workflow must not be labelled `Verified` merely because its structure or wording has been reviewed. `Verified` requires a representative execution with the recorded AI tool/model and inspection of the resulting output.

## Status definitions

- `Not Yet Tested` — authored but no representative execution recorded.
- `Structural QA Pass` — architecture and content reviewed; execution not yet recorded.
- `Tested - Fix Required` — execution completed and one or more issues require correction.
- `Verified` — representative execution completed, output inspected, and no blocking issue identified for the recorded test case.
- `Re-verify` — previously verified workflow requiring a scheduled or model-change review.

## Verification protocol

For each workflow:

1. Use a realistic teacher input appropriate to the workflow.
2. Record the exact AI tool and model/model family available at test time.
3. Record the test date.
4. Inspect factual, mathematical, pedagogical and formatting accuracy.
5. Check that the workflow produces the intended teacher outcome.
6. Record defects and corrections.
7. Re-run after a substantive correction.
8. Record the next scheduled review date.

## Current register

| ID range | Workflow module | Structural QA | Execution status | Tool/model | Test date | Reviewer notes | Next review |
|---|---|---|---|---|---|---|---|
| NM-01–10 | Number and place value | Pass | Not Yet Tested | — | — | Execution required | Quarterly |
| CF-01–10 | Calculation and fluency | Pass | Not Yet Tested | — | — | Execution required | Quarterly |
| FD-01–10 | Fractions, decimals and percentages | Pass | Not Yet Tested | — | — | Execution required | Quarterly |
| GM-01–10 | Geometry and measure | Pass | Not Yet Tested | — | — | Execution required | Quarterly |
| PR-01–10 | Problem solving and reasoning | Pass | Not Yet Tested | — | — | Execution required | Quarterly |
| SD-01–10 | Statistics and data | Pass | Not Yet Tested | — | — | Execution required | Quarterly |
| ADI-01–10 | Assessment, diagnosis and intervention | Pass | Not Yet Tested | — | — | Execution required | Quarterly |

## Current coverage

**70 workflows authored.**

**70 workflows structurally reviewed.**

**0 workflows execution-verified.**

This distinction is deliberate. The library's commercial quality claim should be based on recorded execution evidence rather than authorship alone.

## Test-case design

The execution pass should use representative cases covering:

- direct lesson generation
- worked examples
- generated calculations and answer keys
- misconception diagnosis
- reasoning tasks
- adaptive teaching
- assessment generation
- pupil-work analysis
- data interpretation
- intervention planning

Where a workflow generates mathematics, answer accuracy must be independently checked rather than accepted solely because the AI produced a plausible-looking result.

## Quarterly re-verification

When a workflow is verified, retain the original verification record. On each quarterly pass, re-run a representative case and record whether the output remains acceptable. A model change, material workflow change or recurring failure pattern should trigger re-verification sooner.
