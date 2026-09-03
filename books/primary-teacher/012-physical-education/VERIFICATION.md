# Primary Physical Education Prompt Pack Verification

## Verification Status

**Status: FROZEN**

**Verification date:** 2026-09-03

**Model used for in-model execution review:** GPT-5.6 Luna

**Scope:** `books/primary-teacher/012-physical-education/`

## Acceptance Summary

| Acceptance criterion | Result |
|---|---:|
| Framework defined | PASS |
| Workflow families populated | PASS |
| Structural workflow count | 100/100 PASS |
| Approved workflow architecture | 100/100 PASS |
| Representative execution tests | 20/20 PASS |
| Targeted risk spot checks | 16/16 PASS |
| Critical safety boundaries | PASS |
| Inclusion and construct-preservation safeguards | PASS |
| Assessment validity safeguards | PASS |
| Health and body-image safeguards | PASS |
| Missing school-specific procedure safeguards | PASS |
| Subject freeze decision | PASS |

## Structural QA

The PE framework defines 10 workflow families with 10 workflows per family, giving a total of 100 workflows.

The repository now contains all ten workflow families and all 100 workflow slots are populated.

Every workflow was checked against the approved architecture:

**ROLE → CONTEXT → TASK → REQUIREMENTS → OUTPUT FORMAT → QUALITY CHECKS → OPTIONAL CUSTOMISATION**

The workflow files use the established copy/paste-ready prompt pattern and include editable variables where teacher-specific information is required.

### Family coverage

1. PE Enquiry & Curriculum Planning: PE-01 to PE-10
2. Fundamental Movement & Physical Skills: FM-01 to FM-10
3. Games, Invasion & Team Activities: 10 workflows
4. Dance, Movement Composition & Performance: 10 workflows
5. Gymnastics & Body Management: 10 workflows
6. Athletics, Running, Jumping & Throwing: AT-01 to AT-10
7. Outdoor, Adventure & Orienteering: OA-01 to OA-10
8. Swimming, Water Confidence & Safety: SW-01 to SW-10
9. Health, Fitness & Physical Activity: HF-01 to HF-10
10. Assessment, Inclusion & Intervention: AI-01 to AI-10

**Structural result: 100/100 PASS.**

### Naming note

The existing Games, Dance and Gymnastics workflow files use the established internal prefixes GA, DA and GY, while the framework labels those families GI, DC and GB. This verification records the existing implementation rather than making an unrequested structural rename. The workflows remain uniquely numbered and mapped to their intended families.

## Representative In-Model Execution Testing

Exactly two workflows from each family were tested using realistic primary-teacher inputs. The generated responses were reviewed directly against the PE quality gates and the relevant family safeguards.

| Test | Workflow | Test scenario | Result |
|---|---|---|---|
| R01 | PE-01 | Year 4 invasion-games unit, 6 lessons, limited equipment | PASS |
| R02 | PE-10 | Year 6 athletics scheme, 6 lessons, supplied school space/equipment | PASS |
| R03 | FM-02 | Year 3 pupil struggling with one-foot balance | PASS |
| R04 | FM-10 | Year 2 locomotion and object-control challenge | PASS |
| R05 | GA-02 | Year 5 small-sided invasion game in limited space | PASS |
| R06 | GA-05 | Year 6 team struggling to create space | PASS |
| R07 | DA-03 | Year 4 stimulus-based actions, space and dynamics | PASS |
| R08 | DA-08 | Year 6 group dance assessment | PASS |
| R09 | GY-02 | Year 3 shapes, balances and linking progression | PASS |
| R10 | GY-06 | Year 5 apparatus-based learning using supplied apparatus | PASS |
| R11 | OA-02 | Year 5 basic orienteering on a school field | PASS |
| R12 | OA-06 | Year 6 outdoor activity in wet/cold conditions | PASS |
| R13 | SW-01 | Year 5 swimming lesson using supplied pool procedures | PASS |
| R14 | SW-07 | Year 6 swimming progress assessment using supplied evidence | PASS |
| R15 | HF-03 | Year 5 cardiovascular fitness through games | PASS |
| R16 | HF-07 | Year 4 personal physical-activity goal | PASS |
| R17 | AI-05 | Year 5 misconceptions about exercise and fitness | PASS |
| R18 | AI-07 | Year 5 adaptation for an access barrier while preserving the core objective | PASS |
| R19 | AI-02 | Year 6 invasion-game decision-making assessment | PASS |
| R20 | AI-10 | Year 6 unit-wide assessment, inclusion and intervention plan | PASS |

**Representative execution result: 20/20 PASS.**

## Targeted Risk Spot Checks

| Check | Risk area | Result |
|---|---|---|
| S01 | Safe practical lesson design | PASS |
| S02 | Movement terminology accuracy | PASS |
| S03 | Appropriate progression | PASS |
| S04 | Avoidance of unsafe physical tasks | PASS |
| S05 | Inclusive adaptation without unnecessary loss of physical learning | PASS |
| S06 | Fair assessment of movement competence | PASS |
| S07 | Tactical reasoning accuracy | PASS |
| S08 | Dance and composition terminology | PASS |
| S09 | Gymnastics safety and body-management guidance | PASS |
| S10 | Athletics technique and measurement claims | PASS |
| S11 | Outdoor and orienteering safety | PASS |
| S12 | Swimming and water-safety boundaries | PASS |
| S13 | Fitness and health claims | PASS |
| S14 | Respectful handling of body image and fitness differences | PASS |
| S15 | Evidence-based intervention | PASS |
| S16 | Safe handling of missing school-specific procedures | PASS |

**Targeted risk result: 16/16 PASS.**

## Key Safety and Quality Findings

### Practical safety

Prompts consistently require realistic consideration of space, equipment, movement pathways, stopping arrangements and activity-specific hazards. They avoid inventing school-specific emergency procedures, supervision ratios or specialist protocols.

### Athletics

Running, jumping and throwing prompts distinguish technique development from raw performance. Measurement prompts define units and procedures and avoid presenting informal classroom results as universal competition standards. Throwing prompts include clear throwing and retrieval boundaries.

### Swimming

Swimming prompts preserve the boundary between classroom planning and specialist pool procedures. They do not invent pool depths, lifeguard arrangements, emergency procedures, medical protocols or supervision ratios. Assessment prompts do not claim to certify swimming competence.

### Fitness and health

Fitness prompts avoid unsupported medical claims, universal physiological thresholds, weight-loss targets and body-shape goals. Personal goals focus on controllable learning, participation or activity behaviours.

### Assessment

Assessment prompts distinguish movement execution, control, decision-making, tactics, composition, knowledge, safe participation and progress where relevant. They avoid treating speed, strength, body size, previous extracurricular experience or sporting status as automatic evidence of overall PE attainment.

### Inclusion

Adaptations address space, equipment, task complexity, communication, grouping, pace, physical and sensory access, recording and response routes. Prompts are required to identify when an adaptation changes the assessed construct.

### Intervention

Diagnostic prompts use observable evidence and pupil voice where available. They do not turn classroom observations into medical, psychological or developmental diagnoses.

### Pupil dignity

Prompts avoid body-shaming, unnecessary public comparison and assumptions about pupils' fitness, bodies, health or sporting experience.

## Freeze Decision

All defined PE acceptance criteria have passed:

- 100/100 workflows structurally populated
- 100/100 workflows aligned to the approved prompt architecture
- 20/20 representative in-model execution tests passed
- 16/16 targeted risk checks passed
- No unresolved critical safety failure identified
- No unresolved construct-validity failure identified
- No unresolved inclusion failure identified
- No unresolved unsupported health-claim pattern identified

**Decision: Primary Physical Education prompt pack is FROZEN.**

## Reverification

Next scheduled review: **2026-12-03** or earlier if a material curriculum, safety, assessment or prompt-quality issue is identified.

Any future change to a frozen PE workflow should trigger targeted re-testing of the changed workflow and any affected risk checks before the subject is considered frozen again.
