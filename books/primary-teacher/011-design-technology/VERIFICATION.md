# Primary Design & Technology Verification

## Status

**Current status: Structural QA complete. Execution verification pending.**

Design & Technology contains 100 workflows across 10 workflow families. The subject is not frozen until representative execution testing and targeted risk-based spot checks are recorded.

## Structural QA

**Result: 100/100 workflows structurally present.**

| Family | IDs | Count | Structural status |
|---|---|---:|---|
| DT Enquiry & Curriculum Planning | DE-01 to DE-10 | 10 | PASS |
| Design, Research & User Needs | DR-01 to DR-10 | 10 | PASS |
| Structures, Mechanisms & Mechanical Systems | SM-01 to SM-10 | 10 | PASS |
| Electrical Systems & Control | EC-01 to EC-10 | 10 | PASS |
| Materials, Textiles & Construction | MT-01 to MT-10 | 10 | PASS |
| Cooking & Nutrition | CN-01 to CN-10 | 10 | PASS |
| Prototyping, Making & Iteration | PM-01 to PM-10 | 10 | PASS |
| Evaluation, Technical Vocabulary & Explanation | EV-01 to EV-10 | 10 | PASS |
| Assessment, Misconceptions & Intervention | AMI-01 to AMI-10 | 10 | PASS |
| Inclusion, Adaptation & Classroom Implementation | IA-01 to IA-10 | 10 | PASS |
| **Total** | **DE-01 to IA-10** | **100** | **PASS** |

### Structural checks completed

- [x] Framework exists and defines the 100-workflow architecture.
- [x] Ten workflow families are represented.
- [x] Each family contains exactly 10 workflow IDs.
- [x] Workflow IDs follow the family taxonomy.
- [x] All workflows use the established ROLE, CONTEXT, TASK, REQUIREMENTS, OUTPUT FORMAT, QUALITY CHECKS and OPTIONAL CUSTOMISATION structure.
- [x] DT-specific quality gates are reflected across the workflow set.
- [x] Inclusion and adaptation workflows preserve the distinction between access support and changing the learning objective.
- [x] Practical safety is explicitly considered in relevant workflows.
- [x] The subject framework separates structural QA from execution verification.

## Representative execution test plan

Representative execution testing will sample **20 workflows**, with at least two workflows from each family. Tests should use realistic primary-school teacher inputs and assess whether the generated output is directly usable without requiring prompt repair.

### Representative coverage

- DE: 2
- DR: 2
- SM: 2
- EC: 2
- MT: 2
- CN: 2
- PM: 2
- EV: 2
- AMI: 2
- IA: 2

**Total: 20 representative execution tests.**

## Targeted risk-based spot checks

A further **16 targeted spot checks** should cover higher-risk DT behaviours:

1. Technical accuracy of structures and mechanisms
2. Electrical safety and circuit reasoning
3. Material-property claims
4. Food hygiene and safety
5. Tool and equipment adaptations
6. Accessibility without construct loss
7. Design criteria and measurable specifications
8. Evidence-based troubleshooting
9. Prototype versus finished-product distinctions
10. Fair practical assessment
11. Misconception diagnosis
12. Technical vocabulary accuracy
13. User-need and design-criteria alignment
14. Resource and classroom feasibility
15. Pupil agency in open-ended design tasks
16. Safe handling of uncertainty and missing technical information

## Execution acceptance criteria

A workflow passes representative execution when the generated result:

- follows the requested task and output format;
- is technically accurate for the supplied context;
- is suitable for the stated primary age group;
- is practical within the stated classroom constraints;
- contains appropriate safety controls where relevant;
- preserves pupil agency where the design brief permits choice;
- distinguishes observation, evidence, inference and judgement where relevant;
- does not invent specifications, material properties, tool capabilities or technical facts;
- provides enough information for a teacher to use the result without an unnecessary iteration cycle.

## Remediation rule

Any failed representative test or spot check must be traced to the specific workflow, corrected at source, and re-tested. A subject freeze cannot be issued on authorship or structural completeness alone.

## Freeze criteria

The subject may be marked **FROZEN** only when:

- 100/100 workflows remain structurally valid;
- 20/20 representative execution tests pass, or any failures are remediated and re-tested successfully;
- 16/16 targeted risk spot checks pass, or any failures are remediated and re-tested successfully;
- verification evidence is recorded with test date and model used;
- no unresolved critical technical, safety, assessment-validity or inclusion defects remain.

## Verification record

**Structural QA:** PASS

**Representative execution:** PENDING

**Targeted spot checks:** PENDING

**Subject freeze:** NOT YET AUTHORISED

**Next review:** 2026-12-02
