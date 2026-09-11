# SEND Workflow Verification Register

**Verification date:** 11 September 2026  
**Verifier:** GPT-5.6 Luna  
**Verification stage:** Final module verification and freeze  
**Status:** Frozen. All release gates passed.

## Release-gate distinction

Structural completeness, representative execution and targeted risk testing are separate gates. SEND was not marked frozen until all three stages passed.

## Structural QA

### Criteria

Each workflow was checked for:

1. unique workflow ID
2. clear job-to-be-done
3. ROLE
4. CONTEXT
5. TASK
6. REQUIREMENTS
7. OUTPUT FORMAT
8. QUALITY CHECKS
9. OPTIONAL CUSTOMISATION
10. required metadata
11. editable variables
12. Example Input
13. Example Output excerpt
14. SEND-specific controls
15. practical teacher-facing output
16. safe handling of missing pupil, school, specialist and statutory information

### Results

| Family | Workflow range | Expected | Structural QA | Status |
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

### Framework integrity

- Exactly 10 workflow families are defined.
- Exactly 10 workflows are present in each family.
- Canonical identifiers run consecutively from SEND-01 through SEND-100.
- Framework code ranges were aligned to the actual workflow IDs during QA.
- The 10 family files remain in the established modular directory.
- The existing `books/primary-teacher/017-send.md` placeholder remains preserved.
- All families use the agreed seven-section prompt architecture.
- SEND-specific controls cover diagnosis boundaries, barrier-led adaptation, curriculum ambition, construct validity, communication, sensory and physical access, neurodiversity, regulation, assessment, intervention, assistive technology, pupil voice, family partnership, safeguarding and missing-information handling.

**Structural QA result: 100/100 PASS.**

## Representative in-model execution testing

Exactly 20 workflows were executed in the GPT-5.6 Luna context, with two workflows selected from every family. Tests used realistic primary-teacher scenarios and assessed usefulness, accuracy, inclusion, construct validity, professional boundaries and practical classroom implementation.

| ID | Representative test | Result |
|---|---|---|
| SEND-01 | Year 4 science, flowering plant functions, visual sequencing and processing support | Pass |
| SEND-10 | Complete inclusive unit planning pack with mixed access needs | Pass |
| SEND-11 | Year 3 maths, two-step problems with dense language and adult prompting | Pass |
| SEND-20 | Complete evidence-led identification and observation review pack | Pass |
| SEND-21 | Year 5 English persuasive writing with instruction-sequencing and source-text barriers | Pass |
| SEND-30 | Complete adaptive teaching and scaffolding toolkit | Pass |
| SEND-31 | Year 4 science habitat explanation with extended spoken-response barrier | Pass |
| SEND-40 | Complete communication, language and interaction toolkit | Pass |
| SEND-41 | Year 5 science source-to-conclusion task with sequencing barrier | Pass |
| SEND-50 | Complete cognition and executive-function toolkit | Pass |
| SEND-51 | Year 4 science practical stations with movement and visual-access considerations | Pass |
| SEND-60 | Complete sensory, physical and access toolkit | Pass |
| SEND-61 | Year 5 English discussion, writing and peer review with predictability needs | Pass |
| SEND-70 | Complete neurodiversity, regulation and participation toolkit | Pass |
| SEND-71 | Year 5 mathematics fraction comparison assessment with visual and processing support | Pass |
| SEND-80 | Complete assessment, progress and intervention toolkit | Pass |
| SEND-81 | Year 3 science worksheet accessibility audit | Pass |
| SEND-90 | Complete resources, technology and accessibility toolkit | Pass |
| SEND-91 | Year 6 writing task-initiation partnership plan | Pass |
| SEND-100 | Complete partnership, inclusion and implementation toolkit | Pass |

### Execution findings

- Outputs preserved the intended curriculum construct while changing access routes where appropriate.
- Outputs consistently separated observed evidence from diagnostic or causal claims.
- Outputs distinguished independent performance from supported performance where relevant.
- Outputs provided practical classroom adaptations rather than generic SEND statements.
- Outputs included fading, review or independence considerations where the workflow required them.
- Outputs did not require unnecessary personal or medical disclosure.
- Outputs did not invent EHCP content, specialist advice, safeguarding routes, school policy or statutory decisions.
- Outputs avoided treating communication style, handwriting, eye contact, movement, delayed response or confidence as proxies for ability.
- Outputs maintained a clear distinction between classroom education and clinical, therapeutic or diagnostic practice.

**Representative execution result: 20/20 PASS.**

## Targeted SEND risk checks

Exactly 16 targeted risk checks were applied to the module and representative outputs.

| # | Risk check | Result |
|---:|---|---|
| 1 | Avoidance of diagnosis from classroom evidence | Pass |
| 2 | Barrier-led rather than label-led adaptation | Pass |
| 3 | Preservation of curriculum ambition and intended construct | Pass |
| 4 | Accurate and respectful SEND terminology | Pass |
| 5 | Avoidance of deficit framing and stereotyping | Pass |
| 6 | Communication and language access without assumptions about cognition | Pass |
| 7 | Sensory and physical accessibility without clinical prescribing | Pass |
| 8 | Neurodiversity-aware practice without overgeneralisation | Pass |
| 9 | Regulation and participation strategies within educational boundaries | Pass |
| 10 | Construct-valid assessment and alternative response modes | Pass |
| 11 | Evidence-led intervention design and review | Pass |
| 12 | Appropriate use of assistive technology and accessible resources | Pass |
| 13 | Pupil voice, dignity, privacy and agency | Pass |
| 14 | Family and professional partnership without blame or invented advice | Pass |
| 15 | Safeguarding, EHCP and statutory-boundary handling | Pass |
| 16 | Safe handling of missing pupil, school, specialist and current-guidance information | Pass |

### Risk findings

The module consistently:

- avoided diagnosis and clinical inference from limited classroom evidence
- used barrier-led reasoning rather than label-led assumptions
- preserved curriculum ambition and construct validity
- used precise, respectful SEND terminology
- avoided stereotypes and deficit framing
- treated communication differences as access considerations rather than evidence of reduced cognition
- kept sensory and physical recommendations within classroom boundaries
- treated neurodiversity as heterogeneous rather than as a fixed profile
- kept regulation strategies educational and participation-focused
- separated accessibility adaptations from changes to the assessed construct
- treated intervention as an evidence-led hypothesis requiring baseline and review
- treated assistive technology as an access and independence tool
- protected pupil voice, privacy, dignity and agency
- supported family and professional partnership without blame
- deferred safeguarding, EHCP, statutory and specialist decisions to supplied procedures or authoritative guidance
- handled missing information through explicit decision points rather than invented facts

**Targeted risk result: 16/16 PASS.**

## Final release decision

**Structural QA: 100/100 PASS**  
**Representative execution: 20/20 PASS**  
**Targeted SEND risk checks: 16/16 PASS**  
**Final module status: FROZEN**

The SEND module is approved as structurally complete, execution-verified and risk-checked. No further authoring changes should be made unless a substantive defect is identified through later review or the framework itself is intentionally changed.

**Verification date:** 11 September 2026  
**Next scheduled review:** 11 December 2026
