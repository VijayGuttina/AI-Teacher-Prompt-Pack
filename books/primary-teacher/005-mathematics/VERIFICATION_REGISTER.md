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
| NM-01–10 | Number and place value | Pass | **Verified** | ChatGPT / GPT-5.6 Luna | 2026-08-25 | 10/10 representative executions passed. See [execution log](./VERIFICATION_EXECUTION_LOG.md). | 2026-11-25 |
| CF-01–10 | Calculation and fluency | Pass | **Verified** | ChatGPT / GPT-5.6 Luna | 2026-08-25 | 10/10 representative executions passed. Mathematical calculations and answer keys checked. | 2026-11-25 |
| FD-01–10 | Fractions, decimals and percentages | Pass | **Verified** | ChatGPT / GPT-5.6 Luna | 2026-08-25 | 10/10 representative executions passed. Fraction, decimal and percentage relationships checked. | 2026-11-25 |
| GM-01–10 | Geometry and measure | Pass | **Verified** | ChatGPT / GPT-5.6 Luna | 2026-08-25 | 10/10 representative executions passed. Geometry, measurement, units and calculations checked. | 2026-11-25 |
| PR-01–10 | Problem solving and reasoning | Pass | **Verified** | ChatGPT / GPT-5.6 Luna | 2026-08-25 | 10/10 representative executions passed. Problem constraints, reasoning and solutions checked. | 2026-11-25 |
| SD-01–10 | Statistics and data | Pass | **Verified** | ChatGPT / GPT-5.6 Luna | 2026-08-25 | 10/10 representative executions passed. Source data, scales, totals and conclusions checked. | 2026-11-25 |
| ADI-01–10 | Assessment, diagnosis and intervention | Pass | **Verified** | ChatGPT / GPT-5.6 Luna | 2026-08-25 | 10/10 representative executions passed. Evidence/inference discipline and assessment logic checked. | 2026-11-25 |

## Current coverage

**70 workflows authored.**

**70 workflows structurally reviewed.**

**70/70 workflows passed representative in-model execution testing.**

**Verification status: Verified — GPT-5.6 Luna qualitative execution.**

This is deliberate and limited to the recorded model and test date. It does **not** claim multi-platform verification, API-level verification or universal reliability across all possible teacher inputs.

## Execution evidence

The detailed representative test cases and reviewer outcomes are recorded in:

`VERIFICATION_EXECUTION_LOG.md`

The execution pass covered:

- direct lesson generation;
- worked examples;
- generated calculations and answer keys;
- misconception diagnosis;
- reasoning tasks;
- adaptive teaching;
- assessment generation;
- pupil-work analysis;
- data interpretation;
- intervention planning.

Where a workflow generated mathematics, calculations and answer keys were independently checked rather than accepted solely because the AI produced a plausible-looking result.

## Quarterly re-verification

The next scheduled review is **25 November 2026**. Retain the original verification record and re-run representative cases at each review.

A model change, material workflow change, curriculum change or recurring failure pattern should trigger re-verification sooner.
