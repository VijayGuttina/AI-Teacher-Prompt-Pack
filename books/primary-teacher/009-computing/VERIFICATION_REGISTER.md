# Computing Verification Register

**Subject:** Primary Computing  
**Workflow count:** 100  
**Verification status:** **Verified / Subject Frozen**  
**Last updated:** 26 August 2026

## Verification policy

Structural QA and execution verification are separate. Authoring a workflow does not constitute model testing. A workflow is individually verified only when it has been executed with a recorded model, date, representative input, output judgement and reviewer notes.

## Status definitions

- **Not Yet Tested:** Authored but no execution evidence recorded.
- **Structural QA Pass:** Workflow meets the repository architecture and Computing quality gates.
- **Tested - Fix Required:** Execution exposed a material defect requiring revision.
- **Verified:** Execution evidence reviewed and workflow passed the stated quality gates.
- **Re-verify:** Previously verified workflow requires review following a material change.

## Register summary

| ID range | Workflow family | Structural QA | Representative execution | Targeted spot checks | Status |
|---|---|---|---|---|---|
| CS-01–CS-10 | Computer Systems & Digital Devices | Pass | CT-01, CT-02 | SC-01 | Verified |
| NC-01–NC-10 | Networks & Connectivity | Pass | CT-03, CT-04 | SC-02 | Verified |
| PT-01–PT-10 | Programming & Computational Thinking | Pass | CT-05, CT-06 | SC-03, SC-04 | Verified |
| DI-01–DI-10 | Data & Information | Pass | CT-07, CT-08 | SC-05, SC-06 | Verified |
| DC-01–DC-10 | Creating Digital Content | Pass | CT-09, CT-10 | SC-07 | Verified |
| OS-01–OS-10 | Online Safety & Responsible Use | Pass | CT-11, CT-12 | SC-08, SC-09 | Verified |
| DL-01–DL-10 | Digital Literacy & Productivity | Pass | CT-13, CT-14 | SC-10 | Verified |
| AD-01–AD-10 | Algorithms, Decomposition & Problem Solving | Pass | CT-15, CT-16 | SC-11, SC-12 | Verified |
| VE-01–VE-10 | Vocabulary, Explanation & Misconceptions | Pass | CT-17, CT-18 | SC-13, SC-14 | Verified |
| CA-01–CA-10 | Assessment, Diagnosis & Intervention | Pass | CT-19, CT-20 | SC-15, SC-16 | Verified |

## Verification evidence

**Representative execution:** 20/20 passed using GPT-5.6 Luna on 26 August 2026.  
**Targeted spot checks:** 16/16 passed on 26 August 2026.  
**Material remediation required:** None.

The testing specifically examined technical accuracy, code/environment assumptions, computational-thinking demand, data fidelity, privacy and online safety, accessibility, evidence-based diagnosis and assessment alignment. No material defects were identified.

## Important scope limitation

This register does **not** claim that all 100 workflows were individually executed. The verified status is subject-level/family-level verification based on representative execution plus targeted spot checks. Individual workflow execution remains a future enhancement where higher assurance is required.

## Subject freeze

Computing is frozen for the current release. Future changes to the framework, workflow wording, safety safeguards or model assumptions should trigger targeted re-verification.

## Review cadence

Recommended next formal review: **24 November 2026**, or sooner following a material model change, curriculum change, or identified technical issue.
