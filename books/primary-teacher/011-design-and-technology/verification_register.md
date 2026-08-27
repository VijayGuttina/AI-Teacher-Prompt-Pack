# Primary Design & Technology Verification Register

**Subject:** Primary Design & Technology  
**Workflow count:** 100  
**Structural QA status:** PASS  
**Execution status:** 0/100

## Status definitions

- `Not Yet Tested` — no representative model execution recorded.
- `Structural QA Pass` — workflow structure, safeguards and subject alignment checked.
- `Tested - Fix Required` — execution identified a material defect.
- `Verified` — representative execution and targeted checks passed.
- `Re-verify` — previously verified workflow changed or requires renewed testing.

## Workflow inventory

| Family | IDs | Count | Structural QA | Execution | Status |
|---|---|---:|---|---:|---|
| Design, Users & Ideas | DU-01–DU-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Materials, Tools, Making & Technical Skills | MT-01–MT-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Cooking, Nutrition & Food Skills | CN-01–CN-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Mechanisms & Electrical Systems | ME-01–ME-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Structures, Textiles & Product Construction | ST-01–ST-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Testing, Evaluation & Iteration | TE-01–TE-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Assessment, Misconceptions & Intervention | AMI-01–AMI-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Inclusion, Progression & Classroom Implementation | IP-01–IP-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Digital Design, CAD & Computing Integration | DC-01–DC-10 | 10 | Pass | 0/10 | Not Yet Tested |
| Curriculum, Sustainability & Cross-Curricular D&T | CS-01–CS-10 | 10 | Pass | 0/10 | Not Yet Tested |
| **Total** | | **100** | **100/100 Pass** | **0/100** | **Execution Testing Pending** |

## Structural QA result

All 100 workflows have been reviewed against the D&T framework and the Prompt Master Specification at workflow-entry level.

**Result: PASS.**

Checks completed:

- 100 unique workflow IDs across 10 coherent families;
- every entry contains ROLE, CONTEXT, TASK, REQUIREMENTS, OUTPUT FORMAT, QUALITY CHECKS and OPTIONAL CUSTOMISATION;
- workflows are aligned to the D&T framework and its design-make-evaluate emphasis;
- design agency is protected where multiple valid solutions exist;
- evaluation is tied to explicit criteria rather than personal taste;
- diagnosis distinguishes evidence from assumptions about pupil ability, effort or motivation;
- technical, food, electrical and tool workflows contain proportionate safety controls;
- inclusion workflows distinguish access support from lowering the intended learning demand;
- digital and cross-curricular workflows preserve D&T disciplinary integrity;
- sustainability workflows prohibit invented evidence and flag claims requiring verification;
- workflows are compact and variable-driven rather than unnecessarily duplicated.

## Minor editorial finding

The workflow architecture is intentionally compact. Full prompt metadata such as version, model compatibility, expected output length, examples, teacher tips and related workflows belongs at the publication/prompt layer and is governed by `PROMPT_MASTER_SPECIFICATION.md`; it is not required to be repeated inside every compact workflow entry.

## Required execution metadata

Every actual test record must capture the AI tool, exact model/model family, test date, representative input, expected behaviour, observed result, reviewer notes, remediation and verification status. A future review date must be recorded when a workflow is verified.

## Representative execution requirement

Before the subject is frozen, execute at least two representative workflows from each family. This gives 20 representative workflows across the complete library. Systemic defects must trigger additional testing of the affected family rather than relying on the minimum sample.

## D&T-specific risk controls

Testing must explicitly examine:

1. design agency and legitimate variation in solutions;
2. accuracy of technical, material, mechanism and electrical explanations;
3. safe tool, equipment and food-practice guidance;
4. distinction between observed product evidence and assumptions about pupil motivation or ability;
5. fair and construct-valid product assessment;
6. evidence-based testing, evaluation and iteration;
7. inclusion adaptations that preserve intended design/technical learning where possible;
8. authentic rather than superficial computing and cross-curricular links;
9. sustainability claims that are evidence-based and appropriately caveated;
10. practical feasibility under realistic classroom constraints.

## Verification boundary

Structural QA and authorship are not model execution. No workflow may be labelled `Verified` without recorded execution evidence.

## Freeze criterion

D&T can be frozen only after all 100 workflows have passed structural QA, the representative execution pass has been completed, material failures have been remediated, targeted spot checks have passed, and this register has been updated accordingly.

## Review cycle

After verification, review quarterly and sooner following a material model change, curriculum change, workflow revision or identified defect.
