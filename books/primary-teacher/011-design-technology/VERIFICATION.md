# Primary Design & Technology Verification

## Status

**Current status: Structural QA complete. Execution verification in progress.**

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

## Representative execution test plan

Representative execution testing samples **20 workflows**, with at least two workflows from each family. Tests use realistic primary-school teacher inputs and assess whether the generated output is directly usable without requiring prompt repair.

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
| R01 | DE-01 Plan a Design & Technology Unit | Year 5; mechanical toy; 6 lessons; cardboard, dowel, split pins and hand tools | PASS | Generated unit structure can separate research, design, making, testing and evaluation; practical work is preserved; output requires realistic timing, resources and safety. |
| R02 | DE-10 Plan a Design Challenge | Year 4; create a freestanding structure for a toy figure; limited card, paper straws and masking tape | PASS | Brief can retain multiple viable solutions and meaningful constraints without prescribing a single construction approach; agency and justification are explicit. |
| R03 | EC-05 Diagnose Circuit Faults | Year 6; battery, two wires, bulb and holder; bulb does not light | PASS | Troubleshooting starts from observable evidence, checks one plausible cause at a time and distinguishes connection, component and power possibilities; safe checks and recording are explicit. |
| R04 | CN-05 Teach Food Hygiene and Safety | Year 5; preparing a no-cook fruit snack with classroom knives and chopping boards | PASS | Output structure covers before, during and after routines, relevant hygiene, tool use, cleaning and school-specific procedure boundaries without inventing an allergen-control process. |
| R05 | DR-01 Research the User | Year 5; design a desk organiser for pupils; teacher supplies intended users and classroom context | PASS | Research questions can elicit functional needs without unnecessary personal data; outputs connect findings to design implications and the brief. |
| R06 | DR-09 Investigate Material Suitability | Year 6; compare card, corrugated cardboard and plywood for a small structure; required property is stiffness | PASS | Prompt requires comparison against the supplied functional requirement, uses established or supplied properties, and explicitly flags uncertainty rather than inventing material performance. |
| R07 | SM-03 Investigate Levers | Year 5; card strip, ruler, pivot and small classroom load | PASS | Output can define pivot, load and effort accurately, structure a manageable investigation and record observations without overstating mechanical advantage. |
| R08 | SM-09 Diagnose Mechanism Failure | Year 6; linkage moves unevenly and catches at one point | PASS | Prompt separates observed behaviour from hypotheses and requires discriminating checks before diagnosis, reducing unsupported causal claims. |
| R09 | MT-02 Investigate Material Properties | Year 4; compare paper, card and fabric for flexibility | PASS | Investigation defines the property, uses a manageable comparison, separates observation from conclusion and includes practical safety guidance. |
| R10 | MT-10 Adapt Materials and Construction Tasks for Inclusion | Year 5; textile joining task; pupil needs adapted access to tools and recording | PASS | Adaptation preserves the construction objective, considers grip, workspace, sequencing and recording, and distinguishes access support from changing the learning demand. |
| R11 | PM-05 Testing a Prototype | Year 5; prototype container must hold a stated classroom load and remain stable | PASS | Test design links directly to success criteria, uses observable evidence and consistent conditions, and supports evidence-led improvement decisions. |
| R12 | PM-06 Iterative Improvement | Year 6; prototype vehicle veers to one side during repeated tests | PASS | Workflow requires pupils to identify evidence, generate alternatives, select a justified modification, retest and record whether performance improved. |

**Representative execution progress: 12/20 PASS.**

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

**Representative execution:** 12/20 PASS, 8 pending

**Targeted spot checks:** PENDING

**Subject freeze:** NOT YET AUTHORISED

**Last execution update:** 2026-09-02

**Next review:** 2026-12-02
