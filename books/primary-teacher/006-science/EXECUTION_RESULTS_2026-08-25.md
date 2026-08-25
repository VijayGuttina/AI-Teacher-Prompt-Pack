# Primary Science Execution QA Results — 25 August 2026

**AI tool:** ChatGPT
**Model:** GPT-5.6 Luna
**Test date:** 25 August 2026
**Test type:** In-model qualitative execution of representative workflows

## Results

| ID | Workflow | Result | Key QA finding |
|---|---|---|---|
| SCI-T01 | WS-03 Fair test planner | PASS | Variables, controls and practical method can be specified coherently. |
| SCI-T02 | WS-09 Conclusion and evidence builder | PASS | Output can distinguish observation/data from conclusion and limitation. |
| SCI-T03 | LH-02 Plant structure and function | PASS | Structure/function relationships remain age-appropriate and scientifically accurate. |
| SCI-T04 | LH-10 Living-things misconception diagnosis | PASS | Diagnosis is framed as hypothesis and requires discriminating evidence. |
| SCI-T05 | MC-04 Changes of state | PASS | Terminology and distinction between state change and new-substance change are preserved. |
| SCI-T06 | MC-07 Separation techniques | PASS | Methods are selected according to relevant physical properties. |
| SCI-T07 | FM-03 Friction investigation | PASS | Test design supports comparison and identifies appropriate controls. |
| SCI-T08 | FM-05 Balanced/unbalanced forces | PASS | Output avoids the common error that balanced forces mean no forces act. |
| SCI-T09 | LE-06 Simple circuits | PASS | Circuit component relationships and practical safety constraints are explicit. |
| SCI-T10 | LE-09 Physics misconception diagnosis | PASS | Diagnostic questions distinguish possible causes rather than asserting one. |
| SCI-T11 | ES-03 Earth rotation and day/night | PASS | Model correctly attributes day/night to Earth's rotation and flags model simplification. |
| SCI-T12 | ES-04 Moon phases | PASS | Output distinguishes phases from eclipses and uses an appropriate model. |
| SCI-T13 | CH-03 Classification key builder | PASS | Branching decisions can be made logically from observable characteristics. |
| SCI-T14 | CH-05 Environmental impact case study | PASS | Evidence, inference and value judgement remain separated. |
| SCI-T15 | ADI-02 Science hinge question | PASS | Distractors can represent plausible misconceptions and support diagnostic interpretation. |
| SCI-T16 | ADI-04 Analyse pupil science work | PASS | Observable errors are separated from hypotheses about causes. |
| SCI-T17 | ADI-06 Targeted intervention | PASS | Intervention is tied to evidenced need and includes an exit criterion. |
| SCI-T18 | ADI-08 Adapt science task | PASS | Adaptation preserves the intended scientific concept/evidence demand. |

## Overall result

**18/18 representative executions passed.**

No systemic blocking issue was identified in the representative execution set. The workflows consistently preserved the principal Science quality gates: factual accuracy, age appropriateness, enquiry validity, evidence/inference distinction, practical feasibility, diagnostic discipline and preservation of scientific demand during adaptation.

## Verification limitation

This is qualitative in-model execution evidence for GPT-5.6 Luna on 25 August 2026. It is **not** evidence of universal reliability, multi-platform compatibility, API performance, or exhaustive execution of all 80 workflows. The remaining workflows require targeted spot checks before the complete subject is described as fully execution-verified.

## Next action

Run targeted spot checks across the remaining workflows, with particular attention to workflows that materially differ from the representative tests. Update `VERIFICATION_REGISTER.md` only after those checks are completed.
