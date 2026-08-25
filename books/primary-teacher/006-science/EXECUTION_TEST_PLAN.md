# Primary Science Execution Test Plan

**Purpose:** Execute representative tests against the Science workflow library without repeating 80 near-identical manual tests.

## Test strategy

The library will be tested by workflow family first, then spot-checked at workflow level. A representative test must exercise the principal failure mode for the family rather than merely confirm that text is generated.

## Representative execution set

| Test | Workflow | Primary QA target |
|---|---|---|
| SCI-T01 | WS-03 Fair test planner | Variable/control validity, practical feasibility |
| SCI-T02 | WS-09 Conclusion and evidence builder | Evidence-to-conclusion discipline |
| SCI-T03 | LH-02 Plant structure and function | Biological factual accuracy |
| SCI-T04 | LH-10 Living-things misconception diagnosis | Evidence vs inference |
| SCI-T05 | MC-04 Changes of state | Scientific terminology and conceptual accuracy |
| SCI-T06 | MC-07 Separation techniques | Method validity |
| SCI-T07 | FM-03 Friction investigation | Measurement and control validity |
| SCI-T08 | FM-05 Balanced/unbalanced forces | Conceptual accuracy |
| SCI-T09 | LE-06 Simple circuits | Circuit accuracy and safety |
| SCI-T10 | LE-09 Physics misconception diagnosis | Diagnostic discrimination |
| SCI-T11 | ES-03 Day/night | Model accuracy and misconception control |
| SCI-T12 | ES-04 Moon phases | Model accuracy and misconception control |
| SCI-T13 | CH-03 Classification key builder | Logical consistency |
| SCI-T14 | CH-05 Environmental impact case study | Evidence/inference/value distinction |
| SCI-T15 | ADI-02 Science hinge question | Assessment validity and distractors |
| SCI-T16 | ADI-04 Analyse pupil science work | Evidence discipline and actionable diagnosis |
| SCI-T17 | ADI-06 Targeted intervention | Intervention alignment |
| SCI-T18 | ADI-08 Adapt science task | Preservation of scientific demand |

## Execution protocol

For each test:

1. Use a realistic teacher input.
2. Run the workflow unchanged except for editable variables.
3. Record the exact AI tool and model/model family.
4. Record the execution date.
5. Inspect the complete output.
6. Check the family-specific QA target plus the global Science quality gate.
7. Record Pass, Fix Required or Re-test.
8. If a systemic issue is found, fix the framework/workflow before spot-checking dependent workflows.

## Global pass criteria

A representative execution may be marked `Verified` only when:

- the science is factually accurate;
- the output is appropriate to the stated year group;
- enquiry design is scientifically valid where relevant;
- observations, data, inference and conclusions are distinguished;
- practical guidance is feasible and includes sensible safety notes where relevant;
- diagnostic claims are proportionate to the evidence;
- adaptations preserve the intended scientific demand;
- answer keys and examples are internally consistent.

## Status policy

The 18 tests above are representative execution tests, not a licence to claim that every workflow has been individually tested. After the family tests pass, the remaining workflows receive targeted spot checks. Any workflow that materially differs in risk or behaviour must receive its own execution test.

## Review

After the execution set is complete, update `VERIFICATION_REGISTER.md` with the exact model, test date, representative input, result, reviewer notes and next review date. Do not use `Verified` as a generic synonym for authored or structurally reviewed.
