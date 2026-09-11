# Part 4: Assess

Assessment workflows designed to produce useful evidence without creating unnecessary workload.

---

## Commercial Prompt 047: Build an assessment plan from learning objectives

**Best for:** Making assessment purposeful across a unit.

**Use when:** You have objectives but need to decide what evidence to collect.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher and assessment leader.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Unit: [UNIT]
Learning objectives: [OBJECTIVES]
Existing assessment arrangements: [ARRANGEMENTS]

TASK
Create a proportionate assessment plan showing what evidence is needed, when it will be collected and how it will inform teaching.

REQUIREMENTS
- Link every assessment activity to an objective.
- Distinguish formative from summative purposes.
- Prefer useful evidence over excessive recording.
- Include misconceptions and prerequisite knowledge where relevant.
- Identify what does not need to be formally recorded.

OUTPUT FORMAT
Objective; purpose; evidence; method; timing; teacher response; recording requirement.

QUALITY CHECKS
Check that assessment is proportionate and that each assessment has a clear decision attached to it.
```
**Teacher tip:** Ask what you can stop recording as well as what you should assess.

**Related prompts:** 048, 054, 063

---

## Commercial Prompt 048: Map assessment evidence to an objective

**Best for:** Checking whether an assessment actually measures the learning intended.

**Use when:** You have an assessment task and want to test its alignment.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary assessment reviewer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Learning objective: [OBJECTIVE]
Assessment task: [TASK]

TASK
Map each part of the assessment to the intended learning and identify anything that introduces irrelevant difficulty.

REQUIREMENTS
Show what is being assessed, what evidence demonstrates it, and any incidental barrier that could distort the result.

OUTPUT FORMAT
Assessment item; intended construct; evidence required; incidental demand; recommendation.

QUALITY CHECKS
Do not claim an assessment is valid simply because it is related to the topic.
```
**Related prompts:** 047, 049, 057

---

## Commercial Prompt 049: Audit an assessment for validity

**Best for:** Finding tasks that assess the wrong thing.

**Use when:** An assessment feels harder than the learning objective suggests.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary assessment and curriculum specialist.

CONTEXT
Objective: [OBJECTIVE]
Assessment: [ASSESSMENT]
Year group: [YEAR_GROUP]
Resources and curriculum context: [CONTEXT]

TASK
Audit the assessment for construct alignment, accessibility, clarity, coverage and unnecessary barriers.

REQUIREMENTS
Identify strengths, threats to validity, missing evidence and specific revisions. Preserve genuine challenge that belongs to the construct.

OUTPUT FORMAT
Keep; revise; remove; add; reason; priority.

QUALITY CHECKS
Separate construct difficulty from reading, language, presentation or resource demands that are not part of the intended learning.
```
**Related prompts:** 048, 057, 067

---

## Commercial Prompt 050: Create a hinge question

**Best for:** Deciding whether pupils are ready to move on.

**Use when:** A misconception would make the next stage ineffective.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher specialising in formative assessment.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Teaching point: [TEACHING_POINT]
Likely misconception: [MISCONCEPTION]

TASK
Create three hinge-question options and recommend the strongest.

REQUIREMENTS
Include plausible responses linked to likely thinking, interpretation of each response and the teacher action that should follow.

OUTPUT FORMAT
Question; responses; interpretation; action.

QUALITY CHECKS
The question must reveal understanding of the concept, not simply recall of wording.
```
**Related prompts:** 051, 053, 060

---

## Commercial Prompt 051: Create an exit ticket

**Best for:** A short individual check at the end of a lesson.

**Use when:** You need evidence to shape tomorrow's teaching.

**Difficulty:** Beginner

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher and formative assessment specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Key knowledge: [KNOWLEDGE]
Misconception: [MISCONCEPTION]

TASK
Create a three-item exit ticket.

REQUIREMENTS
Include one essential knowledge check, one application or explanation item and one diagnostic item. Provide answers and simple decision rules.

OUTPUT FORMAT
Pupil questions; answer key; next-lesson actions.

QUALITY CHECKS
Every item must directly relate to the objective.
```
**Related prompts:** 050, 052, 060

---

## Commercial Prompt 052: Create a low-stakes knowledge check

**Best for:** Quick recall checks without unnecessary pressure.

**Use when:** You need to see whether important knowledge is secure.

**Difficulty:** Beginner

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher specialising in retrieval practice.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Knowledge to assess: [KNOWLEDGE]
Number of items: [NUMBER]

TASK
Create a short low-stakes knowledge check with answers.

REQUIREMENTS
Mix recall formats where useful. Keep questions unambiguous and focus on high-value knowledge.

OUTPUT FORMAT
Pupil check followed by answer key and a short interpretation guide.

QUALITY CHECKS
Do not introduce irrelevant reading or reasoning demand unless it is part of the intended construct.
```
**Related prompts:** 051, 053, 058

---

## Commercial Prompt 053: Diagnose an assessment error

**Best for:** Distinguishing an error from a deeper misunderstanding.

**Use when:** A pupil answer is wrong and the reason is unclear.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher analysing assessment evidence.

CONTEXT
Objective: [OBJECTIVE]
Question: [QUESTION]
Pupil response: [RESPONSE]
Known prior learning: [PRIOR_LEARNING]

TASK
Analyse what the response demonstrates, what it does not demonstrate and what diagnostic question would help distinguish possible explanations.

REQUIREMENTS
Separate evidence from hypothesis. Do not infer SEND, ability or underlying diagnosis. Suggest one or two targeted follow-up checks.

OUTPUT FORMAT
Observed evidence; possible explanations; diagnostic question; teaching response; recheck.

QUALITY CHECKS
Do not over-interpret one response.
```
**Related prompts:** 049, 054, 060

---

## Commercial Prompt 054: Create a diagnostic assessment sequence

**Best for:** Finding the source of a learning gap.

**Use when:** Several pupils are struggling and you need better evidence before reteaching.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher and diagnostic assessment designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Observed difficulty: [DIFFICULTY]
Possible prerequisites: [PREREQUISITES]

TASK
Create a short diagnostic sequence that distinguishes between missing knowledge, insecure prerequisite knowledge and a misconception.

REQUIREMENTS
Use a small number of carefully chosen questions. Explain what each response would indicate and what teaching response would follow.

OUTPUT FORMAT
Diagnostic item; expected response; alternative response; interpretation; next action.

QUALITY CHECKS
Do not claim certainty where several explanations remain plausible.
```
**Related prompts:** 053, 055, 063

---

## Commercial Prompt 055: Create feedback that leads to improvement

**Best for:** Turning feedback into a next action rather than a comment.

**Use when:** Pupils need to improve work after assessment.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher and feedback specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Success criteria: [CRITERIA]
Pupil work: [WORK]

TASK
Create concise feedback that identifies what is working, what needs improvement and the specific action the pupil should take.

REQUIREMENTS
- Link feedback to the objective.
- Prioritise one or two improvements.
- Avoid generic praise.
- Give pupils an opportunity to act on the feedback.

OUTPUT FORMAT
Strength; improvement; next action; pupil response task.

QUALITY CHECKS
Feedback must be actionable and proportionate.
```
**Related prompts:** 056, 064, 070

---

## Commercial Prompt 056: Generate marking guidance

**Best for:** Making marking or checking more consistent.

**Use when:** You have a task but need clear criteria for judging responses.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher and assessment designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Task: [TASK]
Expected evidence: [EVIDENCE]

TASK
Create concise marking or checking guidance.

REQUIREMENTS
- Identify essential evidence.
- Distinguish secure, developing and not-yet-secure responses where useful.
- Include examples of acceptable variation.
- Avoid rewarding presentation unless it is part of the construct.

OUTPUT FORMAT
Criterion; secure evidence; developing evidence; common error; teacher response.

QUALITY CHECKS
Criteria must match the objective and allow reasonable alternative answers where appropriate.
```
**Related prompts:** 048, 055, 057

---

## Commercial Prompt 057: Create an end-of-unit assessment blueprint

**Best for:** Designing a balanced end-of-unit assessment before writing the questions.

**Use when:** You need coverage without over-testing.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary curriculum and assessment leader.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Unit: [UNIT]
Learning objectives: [OBJECTIVES]
Essential knowledge: [KNOWLEDGE]

TASK
Create an assessment blueprint before individual questions are written.

REQUIREMENTS
Map objectives to evidence, question types, approximate weighting and thinking demand. Identify any objective that should be assessed through practical or observed evidence rather than a written question.

OUTPUT FORMAT
Objective; evidence; item type; demand; weighting; notes.

QUALITY CHECKS
Avoid false precision and excessive assessment. Every item must have a clear purpose.
```
**Related prompts:** 047, 049, 056

---

## Commercial Prompt 058: Audit a knowledge assessment for coverage

**Best for:** Checking whether a quiz or test covers the right knowledge.

**Use when:** You already have questions and want to find gaps or over-representation.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher and assessment reviewer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Unit: [UNIT]
Knowledge expected: [KNOWLEDGE]
Existing assessment: [ASSESSMENT]

TASK
Audit the assessment for coverage, balance, duplication and unnecessary difficulty.

OUTPUT FORMAT
Covered well; under-covered; over-tested; unclear; recommended changes.

QUALITY CHECKS
Do not invent curriculum requirements. Base the audit on the supplied knowledge and objectives.
```
**Related prompts:** 052, 057, 067

---

## Commercial Prompt 059: Create a formative assessment plan within a lesson

**Best for:** Building checks into teaching rather than adding assessment afterwards.

**Use when:** A lesson needs planned points for checking understanding.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher specialising in formative assessment.

CONTEXT
Lesson objective: [OBJECTIVE]
Lesson sequence: [SEQUENCE]
Key misconceptions: [MISCONCEPTIONS]
Duration: [DURATION]

TASK
Identify the minimum useful checks for understanding and specify what the teacher should do with each result.

OUTPUT FORMAT
Lesson point; check; response method; interpretation; action; recheck.

QUALITY CHECKS
Avoid excessive checking. Every check must support a teaching decision.
```
**Related prompts:** 050, 051, 060

---

## Commercial Prompt 060: Create a responsive assessment decision tree

**Best for:** Making assessment evidence immediately useful.

**Use when:** You want clear actions for secure, partial and insecure understanding.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher.

CONTEXT
Objective: [OBJECTIVE]
Assessment evidence: [EVIDENCE]
Possible response patterns: [PATTERNS]

TASK
Create a decision tree linking each response pattern to the most proportionate teaching action.

REQUIREMENTS
Include secure understanding, partial understanding, misconception and prerequisite gaps where relevant. Include a recheck.

OUTPUT FORMAT
Evidence → interpretation → action → recheck.

QUALITY CHECKS
Do not make high-stakes decisions from limited evidence.
```
**Related prompts:** 053, 054, 059

---

## Commercial Prompt 061: Create an assessment workload audit

**Best for:** Reducing assessment activity that produces little useful evidence.

**Use when:** Teachers are spending too much time assessing or recording.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary assessment leader reviewing workload and evidence value.

CONTEXT
Current assessment activities: [ACTIVITIES]
Recording requirements: [RECORDING]
Curriculum context: [CONTEXT]
Teacher workload concern: [CONCERN]

TASK
Audit the current approach and identify what should be retained, simplified, combined or stopped.

REQUIREMENTS
For each activity assess purpose, evidence value, workload and decision made from the evidence.

OUTPUT FORMAT
Activity; purpose; evidence value; workload; keep/change/stop; recommendation.

QUALITY CHECKS
Do not recommend removing assessment without considering the teaching decision it supports.
```
**Related prompts:** 047, 062, 067

---

## Commercial Prompt 062: Create a proportionate assessment calendar

**Best for:** Planning assessment across a term without over-testing.

**Use when:** You need to coordinate formative and summative activity.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary assessment leader.

CONTEXT
Term length: [TERM]
Year group: [YEAR_GROUP]
Subjects: [SUBJECTS]
Existing assessment points: [POINTS]
School constraints: [CONSTRAINTS]

TASK
Create a proportionate assessment calendar showing major assessment points and lighter formative checks.

REQUIREMENTS
Avoid clustering high-workload activities. Link each major assessment to a decision or reporting need.

OUTPUT FORMAT
Week; assessment; purpose; workload; evidence use.

QUALITY CHECKS
Keep the calendar realistic and avoid inventing statutory dates.
```
**Related prompts:** 047, 061, 067

---

## Commercial Prompt 063: Plan intervention from assessment evidence

**Best for:** Moving from an identified gap to a focused intervention.

**Use when:** Assessment evidence shows a specific area needs attention.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher and intervention planner.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Assessment evidence: [EVIDENCE]
Available time: [TIME]
Group size: [GROUP_SIZE]

TASK
Create a short intervention plan linked directly to the assessment evidence.

REQUIREMENTS
State the identified gap, baseline, teaching response, practice, recheck and decision rule. Separate evidence from hypothesis.

OUTPUT FORMAT
Baseline; intervention; practice; recheck; decision.

QUALITY CHECKS
Do not diagnose underlying difficulties from limited evidence.
```
**Related prompts:** 053, 054, 060

---

## Commercial Prompt 064: Create improvement time after feedback

**Best for:** Ensuring feedback changes pupil work.

**Use when:** You have given feedback and need a short improvement task.

**Difficulty:** Beginner

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Feedback given: [FEEDBACK]
Pupil work: [WORK]
Time available: [TIME]

TASK
Create a short improvement activity that requires pupils to act on the feedback.

REQUIREMENTS
- Keep the improvement directly connected to the feedback.
- Make the success condition visible.
- Include a quick recheck.

OUTPUT FORMAT
Pupil instruction; model if needed; improvement task; recheck.

QUALITY CHECKS
The task should improve learning, not simply require pupils to copy a corrected answer.
```
**Related prompts:** 055, 056, 070

---

## Commercial Prompt 065: Create a simple moderation activity

**Best for:** Building shared understanding of assessment criteria.

**Use when:** Teachers need to compare judgements and discuss evidence.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary assessment leader.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective/criteria: [CRITERIA]
Sample work: [WORK]

TASK
Create a moderation activity that supports professional discussion about the evidence in the work.

REQUIREMENTS
- Ask teachers to make an initial judgement before discussion where useful.
- Identify evidence supporting the judgement.
- Surface borderline cases and disagreement.
- Avoid forcing agreement where evidence is genuinely ambiguous.

OUTPUT FORMAT
Moderation instructions; evidence prompts; discussion questions; agreed principles; unresolved points.

QUALITY CHECKS
Keep the focus on evidence against criteria, not personal preference.
```
**Related prompts:** 056, 066, 067

---

## Commercial Prompt 066: Create a standardisation checklist

**Best for:** Improving consistency in marking or assessment.

**Use when:** Several teachers are applying the same criteria.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary assessment leader.

CONTEXT
Assessment: [ASSESSMENT]
Criteria: [CRITERIA]
Year group: [YEAR_GROUP]
Known inconsistencies: [ISSUES]

TASK
Create a practical standardisation checklist for teachers using the assessment.

REQUIREMENTS
Include interpretation of criteria, acceptable variation, common borderline cases, evidence expectations and when to seek moderation.

OUTPUT FORMAT
Checklist with examples and decision points.

QUALITY CHECKS
The checklist must improve consistency without pretending that professional judgement can be eliminated.
```
**Related prompts:** 065, 067

---

## Commercial Prompt 067: Create an assessment quality assurance checklist

**Best for:** Final review before an assessment is used.

**Use when:** A quiz, task or end-of-unit assessment has been drafted.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary assessment quality reviewer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Assessment: [ASSESSMENT]

TASK
Create a final QA checklist and use it to identify any issues in the supplied assessment.

REQUIREMENTS
Check alignment, coverage, clarity, answerability, accessibility, workload, accuracy, scoring and whether the task measures the intended construct.

OUTPUT FORMAT
Pass/check; issue; impact; recommended fix; final decision.

QUALITY CHECKS
Flag uncertainty rather than silently making assumptions.
```
**Related prompts:** 049, 057, 066

---

## Commercial Prompt 068: Create a pupil-friendly assessment rubric

**Best for:** Making quality criteria clear before pupils begin.

**Use when:** A task requires several dimensions of quality.

**Difficulty:** Intermediate

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher and assessment designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Success criteria: [CRITERIA]
Task: [TASK]

TASK
Create a concise rubric pupils can understand and use.

REQUIREMENTS
Use clear descriptors for developing, secure and stronger performance where useful. Focus on evidence of learning rather than presentation or compliance.

OUTPUT FORMAT
Rubric table followed by pupil self-check questions.

QUALITY CHECKS
Descriptors must be observable and directly connected to the objective.
```
**Related prompts:** 010, 056, 067

---

## Commercial Prompt 069: Identify what an assessment cannot tell you

**Best for:** Preventing over-interpretation of assessment results.

**Use when:** A score or result risks being treated as more meaningful than it is.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary assessment leader.

CONTEXT
Assessment: [ASSESSMENT]
Result/evidence: [RESULT]
Intended construct: [CONSTRUCT]

TASK
Explain what the evidence supports, what it does not support and what further evidence would be needed before making a stronger judgement.

OUTPUT FORMAT
Supported conclusion; unsupported conclusion; uncertainty; further evidence needed; practical next step.

QUALITY CHECKS
Do not infer ability, diagnosis or long-term attainment from limited evidence.
```
**Related prompts:** 053, 067, 070

---

## Commercial Prompt 070: Turn assessment evidence into a next-lesson plan

**Best for:** Closing the loop between assessment and teaching.

**Use when:** You have evidence from a check and need to decide tomorrow's lesson response.

**Difficulty:** Advanced

**Copy and paste:**
```text
ROLE
Act as an experienced primary teacher using assessment evidence to plan next steps.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective assessed: [OBJECTIVE]
Evidence: [EVIDENCE]
Time available next lesson: [TIME]

TASK
Create a short next-lesson response based on the evidence.

REQUIREMENTS
- Identify the highest-priority learning issue.
- Retain secure learning through brief retrieval.
- Reteach only what the evidence shows is needed.
- Include guided and independent reapplication.
- End with a recheck.

OUTPUT FORMAT
Evidence summary; lesson objective; retrieval; reteaching; practice; recheck; decision.

QUALITY CHECKS
Do not reteach everything because some pupils made errors. Use the evidence to target the response.
```
**Related prompts:** 044, 045, 063, 064
