# Part 5: Adapt

Practical workflows for removing barriers while preserving learning intent.

---

## Commercial Prompt 071: Adapt a lesson for accessibility

**Best for:** Making an existing lesson more accessible without changing its core objective.

**Use when:** Pupils face barriers in language, processing, attention, sensory access or task organisation.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in adaptive teaching and accessibility.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Lesson: [LESSON]
Known barrier: [BARRIER]
Available resources: [RESOURCES]

TASK
Adapt the lesson to remove the stated barrier while preserving the intended learning demand.

REQUIREMENTS
Provide practical changes to instructions, modelling, resources, response mode and task organisation. Explain which changes remove access barriers and which, if any, alter the learning objective.

OUTPUT FORMAT
Original barrier; adaptation; why it helps; teacher action; pupil action; check for understanding.

QUALITY CHECKS
Do not automatically make the task easier. Preserve the construct being taught.
```

**Related prompts:** 072, 073, 075

---

## Commercial Prompt 072: Create scaffolds that can be faded

**Best for:** Temporary support rather than permanent simplification.

**Use when:** Pupils need help to access a complex task.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and scaffolding specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Task: [TASK]
Barrier: [BARRIER]

TASK
Create a sequence of temporary scaffolds and explain how each can be reduced as pupils become more independent.

REQUIREMENTS
Use modelling, prompts, worked examples, visual support or structured steps only where they address the stated barrier. Define a fading point for each scaffold.

OUTPUT FORMAT
Barrier; scaffold; teacher prompt; pupil action; fading point; independent check.

QUALITY CHECKS
Scaffolds must support access without doing the core thinking for pupils.
```

**Related prompts:** 071, 078, 082

---

## Commercial Prompt 073: Adapt instructions for pupils who struggle with language

**Best for:** Making task instructions easier to process without reducing the learning objective.

**Use when:** The task language itself is creating an unnecessary barrier.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in clear instructional language.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Original instructions: [INSTRUCTIONS]
Known language barrier: [BARRIER]

TASK
Rewrite the instructions so pupils can understand the process while retaining the intended cognitive demand.

REQUIREMENTS
Use short steps, clear verbs, essential vocabulary and a brief example where useful. Identify subject vocabulary that should remain rather than being simplified away.

OUTPUT FORMAT
Pupil-facing instructions; key vocabulary; teacher note; optional visual sequence.

QUALITY CHECKS
Do not remove important subject terminology or simplify the task beyond the stated barrier.
```

**Related prompts:** 071, 074, 077

---

## Commercial Prompt 074: Adapt a task for EAL learners

**Best for:** Supporting access to learning for pupils developing English.

**Use when:** Language demands may prevent pupils from demonstrating the intended subject learning.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in EAL and subject-language development.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Task: [TASK]
Language demands: [LANGUAGE_DEMANDS]
Known pupil language profile: [PROFILE]

TASK
Identify unnecessary language barriers and provide adaptations that preserve the subject learning.

REQUIREMENTS
Include vocabulary support, visuals, sentence stems, modelling and response options where useful. Do not assume limited English means limited subject knowledge.

OUTPUT FORMAT
Barrier; adaptation; pupil support; subject demand preserved; teacher check.

QUALITY CHECKS
Do not lower subject expectations solely because language support is needed.
```

**Related prompts:** 073, 075, 077

---

## Commercial Prompt 075: Create an accessible reading task

**Best for:** Making a reading activity accessible while preserving the comprehension goal.

**Use when:** Text complexity or task design is blocking access.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary English teacher specialising in adaptive reading.

CONTEXT
Year group: [YEAR_GROUP]
Reading objective: [OBJECTIVE]
Text: [TEXT]
Observed barrier: [BARRIER]

TASK
Adapt the activity to reduce the unnecessary barrier while preserving the reading skill being assessed.

REQUIREMENTS
Consider chunking, vocabulary pre-teaching, oral rehearsal, question sequencing, visual support and response format. Do not replace the intended reading skill with simple recall.

OUTPUT FORMAT
Barrier; adaptation; adapted questions/task; support; independent check.

QUALITY CHECKS
Make clear what remains unchanged about the reading construct.
```

**Related prompts:** 071, 073, 078

---

## Commercial Prompt 076: Create an accessible maths task

**Best for:** Removing language, layout or processing barriers in mathematics.

**Use when:** Pupils can understand the mathematics but struggle with the way the task is presented.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary mathematics teacher specialising in adaptive teaching.

CONTEXT
Year group: [YEAR_GROUP]
Objective: [OBJECTIVE]
Original task: [TASK]
Observed barrier: [BARRIER]

TASK
Adapt the task while preserving the intended mathematics.

REQUIREMENTS
Consider representation, layout, vocabulary, chunking, worked examples and response method. Do not reduce mathematical reasoning merely to make the task accessible.

OUTPUT FORMAT
Barrier; adaptation; revised task; mathematical demand preserved; teacher check.

QUALITY CHECKS
Verify every calculation, representation and answer.
```

**Related prompts:** 071, 075, 079

---

## Commercial Prompt 077: Create communication support for a lesson

**Best for:** Helping pupils participate when expressive or receptive language is a barrier.

**Use when:** Pupils need structured ways to understand and communicate learning.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in communication-friendly classroom practice.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Lesson activity: [ACTIVITY]
Communication barrier: [BARRIER]

TASK
Create practical communication supports that allow pupils to participate without changing the learning objective.

REQUIREMENTS
Include visual cues, sentence stems, vocabulary, response choices, modelling and opportunities for rehearsal where appropriate.

OUTPUT FORMAT
Support; how to use it; pupil response; fading option.

QUALITY CHECKS
Do not assume that one communication support suits every pupil.
```

**Related prompts:** 073, 074, 078

---

## Commercial Prompt 078: Adapt a task for attention and executive function

**Best for:** Helping pupils organise a complex task.

**Use when:** The learning is accessible but the process of managing the task is not.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in executive-function support.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Task: [TASK]
Observed barrier: [BARRIER]

TASK
Break the task into manageable stages while preserving the intended thinking.

REQUIREMENTS
Include a clear sequence, visual or written checklist, start prompt, stopping points and completion check. Identify which supports can be faded.

OUTPUT FORMAT
Task stages; support; teacher prompt; pupil check; fading point.

QUALITY CHECKS
Do not remove the reasoning or independence the task is intended to develop.
```

**Related prompts:** 072, 075, 077
