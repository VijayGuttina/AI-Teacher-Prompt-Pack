---
title: "Primary Teacher Prompt Pack: Assessment Planning & Curriculum Alignment"
book: "Primary Teacher Prompt Pack"
chapter: "018 Assessment"
family: "Assessment Planning & Curriculum Alignment"
subject_code: "ASSESSMENT"
status: "workflows"
version: "1.0"
---

# Assessment Planning & Curriculum Alignment

This family contains ten copy/paste-ready workflows for designing assessment around curriculum intent, valid evidence and proportionate teacher workload.

## Assessment-specific controls

Use these controls throughout the family:

- Define the assessment purpose before choosing the method.
- Identify the intended learning construct and distinguish it from incidental barriers.
- State what the assessment is and is not intended to measure.
- Use meaningful evidence rather than generating assessment for its own sake.
- Do not invent statutory requirements, school policy, prior attainment or assessment thresholds.
- Where current statutory or school-specific information matters, flag it for authoritative verification.
- Do not infer SEND, EAL, ability or a misconception from limited evidence.
- Keep assessment proportionate to the decision it supports.
- Preserve curriculum ambition when planning access adaptations.
- Avoid unnecessary pupil data and unnecessary teacher workload.
- Use UK English and no em dash character in generated output.

## AS-01: Build an Assessment Plan From Curriculum Objectives

**Difficulty:** Beginner  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 900 to 1,300 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** assessment planning, curriculum alignment, formative assessment, primary

### Purpose
Turn supplied curriculum objectives into a proportionate assessment plan showing what evidence is needed, when it should be gathered and what teaching decision it will support.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Unit: [UNIT]
- Curriculum Objectives: [CURRICULUM_OBJECTIVES]
- Prior Learning: [PRIOR_LEARNING]
- Unit Length: [UNIT_LENGTH]
- Existing Assessment Arrangements: [EXISTING_ASSESSMENT]

### ROLE
Act as an experienced primary teacher and assessment lead who prioritises construct validity, useful evidence and manageable assessment workload.

### CONTEXT
Use the supplied curriculum objectives and planning information. If a statutory or school-specific assessment requirement is not supplied, do not invent it. Identify it as a verification point where relevant.

### TASK
Create an assessment plan for the unit. For each objective, identify the intended construct, evidence needed, suitable assessment opportunity, timing and teaching decision supported by the evidence.

### REQUIREMENTS
- Separate knowledge, skill, application, reasoning and transfer where relevant.
- Include a mixture of light-touch formative checks and only the summative evidence genuinely required.
- Identify prerequisite knowledge that should be checked.
- State what should not be treated as evidence of attainment.
- Keep the number of formal assessment events proportionate.

### OUTPUT FORMAT
Provide: Unit assessment intent; objective-to-construct map; assessment opportunities; evidence required; decision supported; accessibility considerations; workload check; information requiring verification.

### QUALITY CHECKS
Check that every assessment has a clear purpose, every claimed judgement has relevant evidence, and no assessment event exists solely to generate data.

### OPTIONAL CUSTOMISATION
Add [SCHOOL_ASSESSMENT_POLICY] or [REPORTING_REQUIREMENTS] where supplied.

**Example Input:** Year 5 mathematics; six-week fractions unit; objectives supplied; weekly lessons; school wants two planned checkpoints.

**Example Output:** The plan identifies early prerequisite checks, short formative evidence during teaching and one end-of-unit judgement, rather than creating a test for every objective.

**Teacher Tip:** Ask what decision each assessment result will change. If the answer is none, reconsider collecting it.

**Related Workflows:** AS-02, AS-03, AS-06

---

## AS-02: Map Assessment Evidence to Learning Objectives

**Difficulty:** Beginner  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 700 to 1,000 words  
**Typical generation time:** 30 to 60 seconds  
**Curriculum tags:** assessment mapping, learning objectives, construct validity

### Purpose
Create a clear map showing how each learning objective will be evidenced without confusing incidental task demands with the intended construct.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Objectives: [OBJECTIVES]
- Existing Tasks: [EXISTING_TASKS]
- Assessment Context: [FORMATIVE_OR_SUMMATIVE]

### ROLE
Act as a primary assessment specialist focused on construct validity and curriculum alignment.

### CONTEXT
Use only the supplied objectives and tasks. If an objective is ambiguous, identify the ambiguity rather than inventing a curriculum interpretation.

### TASK
Map each objective to the evidence a pupil would need to produce to demonstrate the intended learning.

### REQUIREMENTS
For each objective, identify: construct; acceptable evidence; useful task types; incidental barriers; possible access adaptations; evidence that would be insufficient; confidence considerations.

### OUTPUT FORMAT
Use a table followed by a short set of recommendations for gaps, duplication or weak alignment.

### QUALITY CHECKS
Check that the evidence demonstrates the objective itself. Do not use neatness, speed, confidence, handwriting or reading demand as attainment evidence unless explicitly part of the construct.

### OPTIONAL CUSTOMISATION
Add [PUPIL_RESPONSE_MODES] or [ACCESS_ADAPTATIONS].

**Example Input:** Year 3 science objective: explain how shadows change during the day; existing worksheet relies heavily on extended writing.

**Example Output:** The map identifies explanation and interpretation of observations as the construct and notes that an extended written response is only one possible evidence route.

**Teacher Tip:** Explicitly write one sentence beginning “This assessment is not intended to measure...” for complex tasks.

**Related Workflows:** AS-01, AS-05, AS-09

---

## AS-03: Design a Proportionate Assessment Calendar

**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 800 to 1,200 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** assessment calendar, workload, formative assessment, summative assessment

### Purpose
Design an assessment calendar that provides useful evidence across a term without creating excessive testing, marking or data-entry workload.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subjects: [SUBJECTS]
- Term Dates: [TERM_DATES]
- Curriculum Priorities: [CURRICULUM_PRIORITIES]
- Existing Assessment Events: [EXISTING_EVENTS]
- School Reporting Points: [REPORTING_POINTS]

### ROLE
Act as a primary assessment lead designing a practical assessment calendar for a busy school.

### CONTEXT
Treat supplied school arrangements as authoritative. Do not invent statutory deadlines or school requirements.

### TASK
Create a term assessment calendar balancing formative checks, planned summative evidence, moderation and reporting requirements.

### REQUIREMENTS
- Avoid clustering high-workload assessments unnecessarily.
- Identify low-burden evidence opportunities.
- Protect curriculum teaching time.
- Include moderation only where it adds value.
- Flag events that appear duplicative or unsupported by a clear decision.

### OUTPUT FORMAT
Provide a calendar table with date/period, subject, purpose, evidence, workload level and decision supported, followed by a workload risk review.

### QUALITY CHECKS
Check that the calendar is feasible for teachers and pupils and that every formal assessment has a defined use.

### OPTIONAL CUSTOMISATION
Add [STAFFING_CONSTRAINTS], [MODERATION_WINDOWS] and [REPORTING_FORMAT].

**Example Input:** Year 6; autumn term; three core subjects; existing weekly quizzes; two reporting windows; no additional statutory dates supplied.

**Example Output:** The calendar reduces duplicate end-of-unit tests and uses existing classroom evidence where it can answer the same question reliably.

**Teacher Tip:** Treat assessment time as a curriculum resource. More data is not automatically better evidence.

**Related Workflows:** AS-01, AS-07, AS-10

---

## AS-04: Plan Assessment Around Prerequisite Knowledge

**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 700 to 1,100 words  
**Typical generation time:** 30 to 60 seconds  
**Curriculum tags:** prerequisite knowledge, assessment planning, sequencing, diagnostic assessment

### Purpose
Identify the prior knowledge that must be secure enough for new learning to be meaningful and design light-touch checks before teaching proceeds too far.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- New Learning: [NEW_LEARNING]
- Expected Prior Learning: [EXPECTED_PRIOR_LEARNING]
- Available Evidence: [AVAILABLE_EVIDENCE]

### ROLE
Act as a primary teacher who uses assessment to understand readiness for new learning without turning prerequisite checks into unnecessary testing.

### CONTEXT
Use the supplied curriculum sequence and evidence. Treat missing prior-learning information as a reason to propose a quick check, not as permission to invent pupil attainment.

### TASK
Identify prerequisite knowledge and create a short readiness assessment with interpretation guidance and teaching responses.

### REQUIREMENTS
- Prioritise prerequisites that materially affect the new construct.
- Keep the check brief.
- Distinguish missing knowledge from language, reading or task-access barriers.
- Provide a response for secure, partial and insecure evidence.

### OUTPUT FORMAT
Provide: prerequisite map; 5 to 10 item check; answer guidance; interpretation rules; immediate teaching responses; recheck point.

### QUALITY CHECKS
Do not label pupils from the check or assume that an incorrect response has one fixed cause.

### OPTIONAL CUSTOMISATION
Add [KNOWN_LANGUAGE_OR_ACCESS_NEEDS].

**Example Input:** Year 4 mathematics; new learning is equivalent fractions; prerequisite knowledge includes multiplication facts and understanding unit fractions.

**Example Output:** The check targets the prerequisite concepts rather than giving pupils a long generic mathematics test.

**Teacher Tip:** Check only prerequisites that you will actually use in the next teaching sequence.

**Related Workflows:** AS-02, AS-11, AS-31

---

## AS-05: Audit an Existing Assessment for Curriculum Alignment

**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 900 to 1,300 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** assessment audit, curriculum alignment, construct validity, quality assurance

### Purpose
Review an existing quiz, test, task or assessment against the stated learning objectives and identify unnecessary, missing or invalid components.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Learning Objectives: [LEARNING_OBJECTIVES]
- Assessment Material: [ASSESSMENT_MATERIAL]
- Known Access Requirements: [ACCESS_REQUIREMENTS]

### ROLE
Act as an experienced primary assessment lead conducting a construct-validity audit.

### CONTEXT
Analyse the supplied material rather than assuming that every question is appropriate. Do not invent curriculum requirements that are not supplied.

### TASK
Audit each assessment item and classify its alignment, evidence value, incidental demand and recommended action.

### REQUIREMENTS
For each item identify: objective assessed; construct; alignment strength; incidental barriers; duplication; ambiguity; accessibility issue; action: retain, revise, replace or remove.

### OUTPUT FORMAT
Use an item-by-item audit table followed by the three highest-priority improvements and a revised assessment blueprint.

### QUALITY CHECKS
Check that proposed changes improve validity without silently lowering the intended learning demand.

### OPTIONAL CUSTOMISATION
Add [MARK_SCHEME] and [SCHOOL_ASSESSMENT_CRITERIA] if available.

**Example Input:** Year 5 geography end-of-unit quiz on rivers; teacher supplies five objectives and a 20-question quiz.

**Example Output:** The audit identifies several questions that test vocabulary recall while the objective requires geographical explanation, and recommends replacing them with evidence of explanation.

**Teacher Tip:** The strongest audit question is “What decision will this item help me make?”

**Related Workflows:** AS-02, AS-06, AS-08

---

## AS-06: Create a Formative Assessment Plan Within a Lesson Sequence

**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 800 to 1,200 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** formative assessment, responsive teaching, lesson sequence, checking understanding

### Purpose
Build purposeful checks into a lesson sequence so that evidence leads to a clear teaching decision rather than becoming assessment for assessment's sake.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Learning Objective: [OBJECTIVE]
- Lesson Sequence: [LESSON_SEQUENCE]
- Likely Errors: [LIKELY_ERRORS]
- Available Resources: [RESOURCES]

### ROLE
Act as an experienced primary teacher using formative assessment to adapt teaching in real time.

### CONTEXT
The supplied lesson sequence is the starting point. Use the smallest number of checks needed to support useful decisions.

### TASK
Insert formative assessment points at moments where evidence can change teaching.

### REQUIREMENTS
For each check provide: purpose; prompt/task; expected evidence; likely responses; interpretation; teacher decision; quick recheck.

### OUTPUT FORMAT
Use a lesson timeline table followed by decision rules for secure, partial and insecure understanding.

### QUALITY CHECKS
Every check must support a plausible instructional decision. Avoid excessive questioning or checks that simply confirm participation.

### OPTIONAL CUSTOMISATION
Add [CLASSROOM_ROUTINES] and [ASSESSMENT_TOOLS].

**Example Input:** Year 2 English; objective: use conjunctions to extend sentences; 45-minute lesson; mini-whiteboards available.

**Example Output:** A short hinge check occurs after modelling, with a planned response for pupils who confuse conjunction choice with punctuation.

**Teacher Tip:** A formative check is valuable only when you already know what you will do with the evidence.

**Related Workflows:** AS-01, AS-11, AS-31

---

## AS-07: Build an End-of-Unit Assessment Blueprint

**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 1,000 to 1,500 words  
**Typical generation time:** 45 to 75 seconds  
**Curriculum tags:** summative assessment, assessment blueprint, curriculum alignment, construct validity

### Purpose
Create an assessment blueprint before writing questions so the final assessment samples the intended curriculum appropriately and avoids accidental over-weighting of easy or superficial content.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Unit: [UNIT]
- Objectives: [OBJECTIVES]
- Relative Importance of Objectives: [OBJECTIVE_WEIGHTING]
- Assessment Duration: [DURATION]
- Response Modes: [RESPONSE_MODES]

### ROLE
Act as a primary assessment designer with expertise in assessment blueprinting and construct validity.

### CONTEXT
Use only the supplied objectives and weightings. If no weighting is provided, propose a transparent rationale rather than claiming an official weighting.

### TASK
Design a blueprint specifying what evidence will be collected, how much assessment space each construct receives and how different item types contribute evidence.

### REQUIREMENTS
Include: construct coverage; objective weighting; item/task types; approximate item count; marks where useful; reasoning/application opportunities; accessibility considerations; answer evidence; limitations of the assessment.

### OUTPUT FORMAT
Provide: assessment purpose; construct map; blueprint table; item-type distribution; scoring approach; access notes; coverage audit; limitations and verification points.

### QUALITY CHECKS
Check that item volume reflects curriculum importance rather than convenience. Avoid false claims that the blueprint is standardised or statutory unless supplied and verified.

### OPTIONAL CUSTOMISATION
Add [MARKING_TIME_LIMIT] and [SCHOOL_STANDARDISATION_REQUIREMENTS].

**Example Input:** Year 6 science; electricity unit; six objectives; 45-minute assessment; teacher wants both knowledge and application evidence.

**Example Output:** The blueprint gives core concepts sufficient representation while reserving explicit space for interpreting a circuit scenario rather than measuring only recall.

**Teacher Tip:** Blueprint first, questions second. It exposes gaps before question-writing creates sunk effort.

**Related Workflows:** AS-02, AS-05, AS-51

---

## AS-08: Review Assessment Workload and Evidence Value

**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 800 to 1,200 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** assessment workload, evidence value, marking, assessment leadership

### Purpose
Audit an assessment approach for teacher and pupil workload and identify where evidence can be gathered more efficiently without reducing assessment quality.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subjects: [SUBJECTS]
- Current Assessment Approach: [CURRENT_APPROACH]
- Teacher Time Available: [TEACHER_TIME]
- Pupil Time Available: [PUPIL_TIME]
- Decisions the Data Must Support: [DECISIONS]

### ROLE
Act as a primary assessment lead reviewing assessment workload, usefulness and proportionality.

### CONTEXT
Treat workload estimates as planning estimates rather than exact measurements unless actual timings are supplied.

### TASK
Identify assessment activities that generate useful evidence, low-value evidence, duplicate evidence or evidence that cannot support the stated decisions.

### REQUIREMENTS
For each activity state: purpose; evidence produced; decision supported; teacher workload; pupil burden; duplication; recommended action.

### OUTPUT FORMAT
Provide an evidence-value matrix followed by a revised proportionate assessment approach.

### QUALITY CHECKS
Do not recommend removing evidence solely to save time if it is necessary for a valid judgement. Conversely, do not preserve high-workload assessment with no clear use.

### OPTIONAL CUSTOMISATION
Add [MARKING_METHODS] and [EXISTING_DATA_SYSTEM].

**Example Input:** Weekly written quizzes across four subjects, plus half-term tests and detailed written marking; school wants to reduce workload without losing useful evidence.

**Example Output:** The review identifies overlapping checks and recommends retaining high-value formative evidence while reducing duplicate written marking.

**Teacher Tip:** Ask whether the evidence changes planning, feedback, intervention or reporting. If it changes none of these, challenge its place in the system.

**Related Workflows:** AS-03, AS-10, AS-41

---

## AS-09: Design Assessment Access Without Changing the Construct

**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 800 to 1,300 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** assessment access, SEND, EAL, construct validity, inclusion

### Purpose
Plan accessibility adaptations that remove incidental barriers while preserving the knowledge, skill or reasoning the assessment is intended to measure.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Assessment Objective: [ASSESSMENT_OBJECTIVE]
- Assessment Task: [ASSESSMENT_TASK]
- Known Access Requirements: [ACCESS_REQUIREMENTS]
- Response Mode Available: [RESPONSE_MODE]

### ROLE
Act as a primary assessment and inclusion specialist focused on construct-valid access.

### CONTEXT
Use only the access information supplied by the teacher. Do not diagnose pupils or infer needs from the assessment result.

### TASK
Analyse the assessment for incidental barriers and recommend adaptations, stating whether each adaptation preserves or changes the construct.

### REQUIREMENTS
Consider layout, language load, reading demand, processing time, response mode, visual presentation, technology, chunking and oral rehearsal where appropriate. For every adaptation explain its impact on validity.

### OUTPUT FORMAT
Provide: construct statement; barrier analysis; adaptation table; construct impact; teacher decision points; verification notes.

### QUALITY CHECKS
Flag adaptations that could change the construct. For language-dependent assessments, distinguish language access from changing the language demand that is itself being assessed.

### OPTIONAL CUSTOMISATION
Add [SCHOOL_AGREED_ADJUSTMENTS] where supplied.

**Example Input:** Year 5 science explanation assessment; pupil has supplied information indicating reduced handwriting access; scientific explanation is the intended construct.

**Example Output:** Allowing an appropriate alternative response mode may preserve the science construct, while replacing explanation with selecting an answer would need separate validity consideration.

**Teacher Tip:** Do not ask “How can I make this easier?” Ask “What is getting in the way of demonstrating the intended learning?”

**Related Workflows:** AS-02, AS-71, AS-81

---

## AS-10: Create an Assessment Quality Assurance Checklist

**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 700 to 1,100 words  
**Typical generation time:** 30 to 60 seconds  
**Curriculum tags:** assessment QA, quality assurance, curriculum alignment, moderation

### Purpose
Create a practical quality assurance checklist for reviewing an assessment before it reaches pupils or is used to make a judgement.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Assessment Type: [ASSESSMENT_TYPE]
- Learning Objectives: [LEARNING_OBJECTIVES]
- Assessment Material: [ASSESSMENT_MATERIAL]
- School Requirements: [SCHOOL_REQUIREMENTS]

### ROLE
Act as a primary assessment lead preparing a proportionate pre-use quality assurance review.

### CONTEXT
Use the supplied assessment and objectives. Treat school requirements as authoritative only where supplied. Flag current statutory requirements for verification rather than inventing them.

### TASK
Create a checklist that tests assessment purpose, construct, evidence, accessibility, reliability, workload and usability before release.

### REQUIREMENTS
Include checks for: objective alignment; construct clarity; item/task validity; coverage; ambiguity; answer accuracy; marking guidance; accessibility; pupil workload; teacher workload; moderation needs; data use; privacy; current-policy verification.

### OUTPUT FORMAT
Use a three-level checklist: Must fix before use; Should review; Optional improvement. Add a short sign-off section recording unresolved uncertainty and teacher judgement.

### QUALITY CHECKS
The checklist must distinguish genuine validity risks from cosmetic preferences. It must not imply that passing the checklist removes the need for professional judgement.

### OPTIONAL CUSTOMISATION
Add [MODERATION_CRITERIA], [MARKING_GUIDANCE] and [SCHOOL_QA_PROCESS].

**Example Input:** Year 6 geography assessment; teacher supplies objectives, questions and answer guidance; school has a local QA process.

**Example Output:** The checklist identifies an ambiguous question as a must-fix issue, a formatting preference as a review item and records the school-specific QA step as an external requirement.

**Teacher Tip:** Use the checklist before printing or assigning the assessment. It is cheaper to fix validity problems before pupils complete the task.

**Related Workflows:** AS-05, AS-07, AS-71
