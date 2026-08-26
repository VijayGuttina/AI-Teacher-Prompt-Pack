# Geography Execution Test Plan

**Purpose:** Representative execution QA before subject freeze.

**Execution standard:** Run the tests against GPT-5.6 Luna using realistic teacher inputs. Record the exact input, output judgement, defects, remediation and re-test result in the execution log. Do not mark all workflows verified merely because representative tests pass.

## 20-test suite

| Test | Workflow | Primary gate |
|---|---|---|
| G-01 | LP-03 | Accurate locational/place comparison |
| G-02 | MS-04 | Scale and distance fidelity |
| G-03 | MS-08 | Map evidence vs inference |
| G-04 | PG-01 | Physical-process accuracy |
| G-05 | PG-07 | Misconception diagnosis |
| G-06 | HG-02 | Evidence-led place comparison |
| G-07 | HG-07 | Human-impact balance |
| G-08 | GF-01 | Fieldwork feasibility |
| G-09 | GF-04 | Actual-data fidelity |
| G-10 | GF-06 | Evidence-based conclusion |
| G-11 | CW-01 | Weather/climate distinction |
| G-12 | CW-05 | Environmental evidence discipline |
| G-13 | SR-02 | Settlement spatial reasoning |
| G-14 | SR-07 | Evidence-based decision making |
| G-15 | IS-03 | Sustainability balance |
| G-16 | IS-07 | Stakeholder attribution discipline |
| G-17 | GV-02 | Vocabulary precision |
| G-18 | GV-08 | Vocabulary vs concept diagnosis |
| G-19 | GA-02 | Diagnostic assessment quality |
| G-20 | GA-08 | Adaptive-task construct preservation |

## Pass criteria

A test passes when the output is factually and geographically accurate, uses the supplied evidence faithfully, is appropriate for the stated year group, preserves geographical disciplinary demand, avoids fabricated information, and is directly usable by a teacher after normal checking.

## Failure handling

Any material failure requires the underlying workflow or framework to be corrected, then the failed test re-run. Record all material defects in the execution log. A representative pass supports confidence in the workflow family but is not evidence that every untested workflow has been individually executed.
