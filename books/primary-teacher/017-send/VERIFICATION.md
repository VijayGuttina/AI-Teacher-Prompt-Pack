# SEND Workflow Verification Register

**Verification date:** 11 September 2026  
**Verifier:** GPT-5.6 Luna  
**Verification stage:** Structural QA  
**Status:** Structural QA completed with one framework-alignment defect identified. Representative execution testing and targeted risk testing are not yet authorised for final freeze.

## Important distinction

This register records the release-gate stages for the SEND module. Structural completeness does not constitute execution verification. The module must pass representative in-model execution testing and the 16 targeted SEND risk checks before it can be marked frozen.

## Structural QA criteria

Each workflow must contain:

1. A unique workflow ID within its family.
2. A clear job-to-be-done.
3. The agreed prompt architecture:
   - ROLE
   - CONTEXT
   - TASK
   - REQUIREMENTS
   - OUTPUT FORMAT
   - QUALITY CHECKS
   - OPTIONAL CUSTOMISATION
4. Required metadata.
5. Editable variables appropriate to the workflow.
6. Example Input.
7. Example Output excerpt.
8. SEND-specific accuracy, inclusion and professional-boundary controls appropriate to the workflow.
9. A practical teacher-facing output.
10. No unnecessary dependency on unspecified pupil, school, specialist or statutory information.

## Results

| Family | Actual workflow range | Expected | Structural QA | Status |
|---|---|---:|---:|---|
| SEND Curriculum & Lesson Planning | SEND-01 to SEND-10 | 10 | 10/10 | Passed |
| Identification, Observation & Barriers to Learning | SEND-11 to SEND-20 | 10 | 10/10 | Passed |
| Adaptive Teaching & Scaffolding | SEND-21 to SEND-30 | 10 | 10/10 | Passed |
| Communication, Language & Interaction | SEND-31 to SEND-40 | 10 | 10/10 | Passed |
| Cognition, Learning & Executive Function | SEND-41 to SEND-50 | 10 | 10/10 | Passed |
| Sensory, Physical & Access Needs | SEND-51 to SEND-60 | 10 | 10/10 | Passed |
| Neurodiversity, Regulation & Classroom Participation | SEND-61 to SEND-70 | 10 | 10/10 | Passed |
| Assessment, Progress & Intervention | SEND-71 to SEND-80 | 10 | 10/10 | Passed |
| Resources, Technology & Accessibility | SEND-81 to SEND-90 | 10 | 10/10 | Passed |
| Partnership, Inclusion & Implementation | SEND-91 to SEND-100 | 10 | 10/10 | Passed |
| **Total** | **SEND-01 to SEND-100** | **100** | **100/100** | **Passed** |

## Framework integrity checks

- The framework defines exactly 10 workflow families.
- The 10 family files are present in the established modular directory.
- Each family contains exactly 10 workflows.
- Actual workflow identifiers run consecutively from SEND-01 through SEND-100.
- All family files use the agreed seven-section prompt architecture.
- Required metadata, editable variables and examples are present.
- SEND-specific controls cover diagnosis boundaries, barrier-led adaptation, curriculum ambition, construct validity, communication access, sensory and physical access, neurodiversity, regulation, assessment, intervention, assistive technology, pupil voice, family partnership, safeguarding and missing-information handling.
- The existing `books/primary-teacher/017-send.md` placeholder remains preserved.

## Framework alignment defect

The framework's **Workflow Family Architecture** currently uses family shorthand ranges such as `OB-01 to OB-10`, `AT-01 to AT-10`, `CL-01 to CL-10`, `CE-01 to CE-10`, `SP-01 to SP-10`, `NR-01 to NR-10`, `AP-01 to AP-10`, `RA-01 to RA-10` and `PI-01 to PI-10`, while the actual workflow files use the established sequential identifiers `SEND-11` through `SEND-100`.

This does **not** create duplicate workflow IDs and the 100 workflows themselves are complete, but it is a framework-to-source naming inconsistency and must be normalised before final freeze.

The correct canonical ranges for the framework should be:

- SEND Curriculum & Lesson Planning: `SEND-01 to SEND-10`
- Identification, Observation & Barriers to Learning: `SEND-11 to SEND-20`
- Adaptive Teaching & Scaffolding: `SEND-21 to SEND-30`
- Communication, Language & Interaction: `SEND-31 to SEND-40`
- Cognition, Learning & Executive Function: `SEND-41 to SEND-50`
- Sensory, Physical & Access Needs: `SEND-51 to SEND-60`
- Neurodiversity, Regulation & Classroom Participation: `SEND-61 to SEND-70`
- Assessment, Progress & Intervention: `SEND-71 to SEND-80`
- Resources, Technology & Accessibility: `SEND-81 to SEND-90`
- Partnership, Inclusion & Implementation: `SEND-91 to SEND-100`

## Structural quality assessment

**Workflow structural completeness: PASS, 100/100.**

**Framework identifier alignment: ACTION REQUIRED.**

The defect is limited to the framework's code-range labels. No workflow content has been changed by this QA stage.

## Outstanding verification gates

### Framework alignment correction

Normalise the framework code ranges to the canonical `SEND-01` through `SEND-100` identifiers before treating structural QA as fully closed.

### Representative in-model execution testing

Exactly 20 workflows must be executed in the current GPT-5.6 Luna context, with two workflows selected from each family. Tests must assess whether the prompts actually produce useful, accurate, inclusive and classroom-ready outputs rather than merely checking that the prompt text is complete.

### Targeted SEND risk checks

The following 16 checks remain outstanding:

1. Avoidance of diagnosis from classroom evidence
2. Barrier-led rather than label-led adaptation
3. Preservation of curriculum ambition and intended construct
4. Accurate and respectful SEND terminology
5. Avoidance of deficit framing and stereotyping
6. Communication and language access without assumptions about cognition
7. Sensory and physical accessibility without clinical prescribing
8. Neurodiversity-aware practice without overgeneralisation
9. Regulation and participation strategies within educational boundaries
10. Construct-valid assessment and alternative response modes
11. Evidence-led intervention design and review
12. Appropriate use of assistive technology and accessible resources
13. Pupil voice, dignity, privacy and agency
14. Family and professional partnership without blame or invented advice
15. Safeguarding, EHCP and statutory-boundary handling
16. Safe handling of missing pupil, school, specialist and current-guidance information

## Publication status

**Workflow structural status: PASS, 100/100.**  
**Framework identifier alignment: Pending correction.**  
**Representative execution status: Pending.**  
**Targeted risk status: Pending.**  
**Final module freeze: Not yet authorised.**

## Next step

Correct the framework identifier ranges, then execute exactly 20 representative workflows, two per family. After those pass, run the 16 targeted SEND risk checks and update this register with the final verification and freeze decision.
