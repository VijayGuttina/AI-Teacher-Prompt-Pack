# Primary Design & Technology Verification

## Status

**Current status: Verification complete. Subject frozen.**

Design & Technology contains 100 workflows across 10 workflow families. Representative execution testing and targeted risk-based spot checks are complete.

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

## Representative execution test plan

Representative execution testing samples **20 workflows**, with exactly two workflows from each family. Tests use realistic primary-school teacher inputs and assess whether the generated output is directly usable without requiring prompt repair.

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

A further **16 targeted spot checks** cover higher-risk DT behaviours:

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

## Representative execution record

**Model used:** GPT-5.6 Luna

| Test | Workflow | Representative input | Result | Verification evidence |
|---|---|---|---|---|
| R01 | DE-01 Plan a Design & Technology Unit | Year 5; mechanical toy; 6 lessons; cardboard, dowel, split pins and hand tools | PASS | Generated unit structure separates research, design, making, testing and evaluation; practical work is preserved; timing, resources and safety are explicit. |
| R02 | DE-10 Plan a Design Challenge | Year 4; create a freestanding structure for a toy figure; limited card, paper straws and masking tape | PASS | Brief retains multiple viable solutions and meaningful constraints without prescribing a single construction approach; agency and justification are explicit. |
| R03 | EC-05 Diagnose Circuit Faults | Year 6; battery, two wires, bulb and holder; bulb does not light | PASS | Troubleshooting starts from observable evidence, checks plausible causes systematically and distinguishes connection, component and power possibilities; safe checks are explicit. |
| R04 | CN-05 Teach Food Hygiene and Safety | Year 5; preparing a no-cook fruit snack with classroom knives and chopping boards | PASS | Routine covers before, during and after controls, relevant hygiene, tool use, cleaning and school-procedure boundaries without inventing an allergen-control process. |
| R05 | DR-01 Research the User | Year 5; design a desk organiser for pupils; teacher supplies intended users and classroom context | PASS | Research questions elicit functional needs without unnecessary personal data and connect findings to design implications and the brief. |
| R06 | DR-09 Investigate Material Suitability | Year 6; compare card, corrugated cardboard and plywood for a small structure; required property is stiffness | PASS | Comparison is tied to the supplied functional requirement and flags uncertainty rather than inventing material performance. |
| R07 | SM-03 Investigate Levers | Year 5; card strip, ruler, pivot and small classroom load | PASS | Activity defines pivot, load and effort accurately, structures a manageable investigation and records observations without overstating mechanical advantage. |
| R08 | SM-09 Diagnose Mechanism Failure | Year 6; linkage moves unevenly and catches at one point | PASS | Workflow separates observed behaviour from hypotheses and requires discriminating checks before diagnosis. |
| R09 | MT-02 Investigate Material Properties | Year 4; compare paper, card and fabric for flexibility | PASS | Investigation defines the property, supports a manageable comparison, separates observation from conclusion and includes practical safety guidance. |
| R10 | MT-10 Adapt Materials and Construction Tasks for Inclusion | Year 5; textile joining task; pupil needs adapted access to tools and recording | PASS | Adaptation preserves the construction objective and considers grip, workspace, sequencing and recording while distinguishing access support from changed learning demand. |
| R11 | PM-05 Testing a Prototype | Year 5; prototype container must hold a stated classroom load and remain stable | PASS | Test design links directly to success criteria, uses observable evidence and consistent conditions, and supports evidence-led improvement decisions. |
| R12 | PM-06 Iterative Improvement | Year 6; prototype vehicle veers to one side during repeated tests | PASS | Workflow requires evidence, alternative explanations, a justified modification, retest and an evidence-based improvement decision. |
| R13 | EV-02 Evaluate Against a Specification | Year 5; pencil holder with 4 supplied specification points; pupils have test results | PASS | Each specification point becomes an observable criterion with evidence, met/partly met/not met judgement, explanation and improvement; unsupported preference is excluded from the judgement. |
| R14 | EV-06 Explain Why a Material or Component Was Chosen | Year 6; choose between card and corrugated cardboard for a small divider; teacher supplies the relevant properties | PASS | Output connects supplied properties to function, compares an alternative and distinguishes evidence-based reasoning from preference without inventing properties. |
| R15 | AMI-02 Identify Misconceptions | Year 5; pupils' written explanations of why a structure collapsed | PASS | Analysis distinguishes misconception from incomplete work, cites evidence, expresses confidence and proposes a diagnostic follow-up rather than treating every error as a misconception. |
| R16 | AMI-04 Practical Skills Assessment | Year 6; assess accurate and safe use of a junior hacksaw for a taught cutting task | PASS | Assessment focuses on observable preparation, tool handling, technique, accuracy, safety and independence, with product quality kept separate from the practical skill judgement. |
| R17 | IA-01 Adapt a DT Task Without Changing the Core Objective | Year 5; prototype joining task; pupil has difficulty with fine-motor manipulation | PASS | Adaptations address access through sequencing, stabilisation, tool/resource choices and support while keeping the core construction objective explicit. |
| R18 | IA-05 Accessible Recording and Evaluation | Year 6; evaluate a moving toy; written recording creates an access barrier | PASS | Alternative routes such as annotated drawing, oral response and structured evidence tables are compared by the evidence they capture, with validity cautions where equivalence is not assured. |
| R19 | EC-08 Plan Testing for Electrical Designs | Year 6; simple battery, switch and lamp product with supplied specification | PASS | Specification points are converted into observable, safe tests with expected outcomes and results recording; testing is kept distinct from final evaluation. |
| R20 | CN-08 Investigate Taste, Texture and Appearance | Year 5; compare two teacher-approved fruit snack variations using agreed sensory criteria | PASS | Investigation defines criteria before testing, keeps comparisons consistent, provides accessible recording, respects allergies and sensory differences, and does not pressure pupils to taste. |

**Representative execution progress: 20/20 PASS.**

## Targeted spot-check record

| Check | Risk area | Result | Verification evidence |
|---|---|---|---|
| S01 | Technical accuracy of structures and mechanisms | PASS | Mechanism workflows distinguish observable movement, component roles and causal hypotheses; no unsupported mechanical claims are required. |
| S02 | Electrical safety and circuit reasoning | PASS | Circuit workflows use supplied components, systematic fault-finding and explicit safe checks; they do not encourage unsafe experimentation. |
| S03 | Material-property claims | PASS | Material-selection prompts require supplied or well-established properties and explicitly prevent invented performance claims. |
| S04 | Food hygiene and safety | PASS | Food workflows separate general hygiene principles from school-specific procedures and do not invent allergy-control arrangements. |
| S05 | Tool and equipment adaptations | PASS | Inclusion workflow requires barrier analysis, safety considerations, supervision requirements and consideration of how adaptations affect the intended skill. |
| S06 | Accessibility without construct loss | PASS | Adaptation workflows explicitly distinguish access support from changing the learning objective and preserve the core DT demand where possible. |
| S07 | Design criteria and measurable specifications | PASS | Specification-led evaluation converts requirements into observable checks and evidence-based judgements. |
| S08 | Evidence-based troubleshooting | PASS | Mechanism and circuit diagnosis require observation, plausible hypotheses, discriminating checks and recorded evidence. |
| S09 | Prototype versus finished-product distinctions | PASS | Prototype testing is framed as evidence about a testable representation and does not imply that a prototype is automatically a finished product. |
| S10 | Fair practical assessment | PASS | Practical assessment separates observable skill performance from unrelated product polish, prior experience or resource advantage. |
| S11 | Misconception diagnosis | PASS | Assessment prompts require evidence before diagnosing misconceptions and distinguish misconceptions from careless or incomplete responses. |
| S12 | Technical vocabulary accuracy | PASS | Vocabulary and explanation workflows require technically accurate definitions and reject oversimplification that changes meaning. |
| S13 | User-need and design-criteria alignment | PASS | Research, evaluation and comparison workflows repeatedly anchor judgements to user purpose, brief and specification. |
| S14 | Resource and classroom feasibility | PASS | Planning and implementation workflows require explicit materials, tools, timing, room setup and resource constraints rather than assuming unlimited provision. |
| S15 | Pupil agency in open-ended design tasks | PASS | Design challenges preserve multiple viable solutions and reward reasoning against the brief rather than conformity to a teacher-selected answer. |
| S16 | Safe handling of uncertainty and missing technical information | PASS | Prompts consistently instruct the model not to invent specifications, material properties, tool capabilities or technical facts and to flag uncertainty where evidence is insufficient. |

**Targeted spot checks: 16/16 PASS.**

## Remediation rule

Any failed representative test or spot check must be traced to the specific workflow, corrected at source, and re-tested. No remediation was required for the recorded verification set.

## Freeze criteria

The subject is marked **FROZEN** because:

- 100/100 workflows remain structurally valid;
- 20/20 representative execution tests pass;
- 16/16 targeted risk spot checks pass;
- verification evidence is recorded with test date and model used;
- no unresolved critical technical, safety, assessment-validity or inclusion defects were identified.

## Verification record

**Structural QA:** PASS

**Representative execution:** 20/20 PASS

**Targeted spot checks:** 16/16 PASS

**Subject freeze:** AUTHORISED

**Last execution update:** 2026-09-02

**Next review:** 2026-12-02
