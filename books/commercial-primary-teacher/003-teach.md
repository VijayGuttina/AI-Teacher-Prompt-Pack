# Part 3: Teach

Practical workflows for explaining, modelling, questioning, practising and engaging pupils.

---

## Commercial Prompt 025: Explain a difficult concept simply

**Best for:** Turning a complex idea into an age-appropriate explanation.

**Use when:** Pupils need a clearer explanation before they can practise.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced UK primary teacher with strong subject knowledge in [SUBJECT].

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Concept: [CONCEPT]
Prior knowledge: [PRIOR_KNOWLEDGE]
Known misconception: [MISCONCEPTION]

TASK
Explain the concept so that pupils can understand the underlying idea rather than memorise a definition.

REQUIREMENTS
- Start from prerequisite knowledge.
- Use simple but accurate language.
- Give one concrete example and one non-example where useful.
- Identify the most likely misconception.
- Explain the concept in a way that can be modelled aloud.
- Do not oversimplify to the point of becoming inaccurate.

OUTPUT FORMAT
Teacher explanation; example; non-example; misconception; check-for-understanding questions.

QUALITY CHECKS
Check subject accuracy, age appropriateness and alignment with the stated prior knowledge.

OPTIONAL CUSTOMISATION
Provide a shorter pupil-facing explanation, a visual analogy or a more challenging explanation for pupils ready to go deeper.
```

**Teacher tip:** Ask for the explanation first, then ask the same prompt to generate a short teacher model and pupil check.

**Related prompts:** 026, 027, 030

---

## Commercial Prompt 026: Create concrete, pictorial and abstract representations

**Best for:** Concepts where representation supports understanding.

**Use when:** Pupils need to connect a real or visual model to formal notation or language.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and subject specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Concept: [CONCEPT]
Learning objective: [OBJECTIVE]
Available representations: [REPRESENTATIONS]

TASK
Design an explanation that moves through concrete, pictorial and abstract representations where those representations genuinely support the concept.

REQUIREMENTS
- Explain what each representation makes visible.
- Show how the representations connect.
- Avoid decorative representations.
- Identify where pupils may confuse the representation with the concept.
- End with a short check for conceptual understanding.

OUTPUT FORMAT
Concrete representation; pictorial representation; abstract representation; connection between them; teacher language; check questions.

QUALITY CHECKS
Every representation must accurately represent the underlying concept.

OPTIONAL CUSTOMISATION
Adapt the sequence for a classroom with limited physical resources.
```

**Related prompts:** 025, 029, 032

---

## Commercial Prompt 027: Generate teacher modelling language

**Best for:** Making expert thinking visible during modelling.

**Use when:** A task is procedural or requires pupils to understand decision-making.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher who models thinking clearly without overloading pupils.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Task being modelled: [TASK]
Learning objective: [OBJECTIVE]
Common error: [ERROR]

TASK
Write concise teacher narration for the modelling sequence.

REQUIREMENTS
- Explain important decisions rather than narrating every obvious action.
- Use accurate subject terminology.
- Include one point where you deliberately check understanding.
- Highlight the common error and how to avoid it.
- Keep the language natural enough to say aloud.

OUTPUT FORMAT
Model step; teacher language; pupil attention point; check question.

QUALITY CHECKS
The narration must make the thinking visible without becoming a script that prevents responsive teaching.
```

**Related prompts:** 011, 012, 025

---

## Commercial Prompt 028: Create a guided practice sequence

**Best for:** Moving pupils from modelling into supported application.

**Use when:** Pupils need practice before independent work.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Modelled example: [EXAMPLE]
Likely errors: [ERRORS]

TASK
Create a guided practice sequence with decreasing teacher support.

REQUIREMENTS
- Start with a close match to the model.
- Ask pupils to explain important decisions.
- Reduce prompts gradually.
- Include one deliberate variation.
- Include a final readiness check before independent work.

OUTPUT FORMAT
Guided task 1; prompt; response; guided task 2; reduced prompt; readiness check.

QUALITY CHECKS
The sequence should prepare pupils for the intended independent task.
```

**Related prompts:** 027, 029, 031

---

## Commercial Prompt 029: Create a gradual release sequence

**Best for:** Structuring teacher modelling, shared practice and independent performance.

**Use when:** A new skill requires a clear transfer of responsibility.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in explicit instruction.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Skill: [SKILL]
Objective: [OBJECTIVE]
Duration: [DURATION]

TASK
Design a gradual release sequence that moves responsibility from teacher modelling to independent pupil performance.

REQUIREMENTS
- Define what the teacher demonstrates.
- Define what teacher and pupils complete together.
- Define what pupils complete with limited prompts.
- Define the independent task.
- Include evidence that pupils are ready to move between stages.

OUTPUT FORMAT
Teacher model; shared practice; reduced-support practice; independent task; assessment check.

QUALITY CHECKS
Do not move to independent work simply because time has passed. Use evidence of understanding.
```

**Related prompts:** 012, 028, 031

---

## Commercial Prompt 030: Generate high-value vocabulary teaching

**Best for:** Teaching vocabulary pupils need to understand and use.

**Use when:** A lesson or text contains important subject-specific language.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and vocabulary specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Topic: [TOPIC]
Key vocabulary: [WORDS]
Pupil starting knowledge: [STARTING_KNOWLEDGE]

TASK
Create a short vocabulary teaching sequence that moves from meaning to accurate use.

REQUIREMENTS
For each word provide a pupil-friendly meaning, contextual example, useful contrast where appropriate and a short application or retrieval question. Include pronunciation guidance where relevant.

OUTPUT FORMAT
Vocabulary table followed by teach, practise and apply sequence.

QUALITY CHECKS
Meanings must be accurate in the stated subject context. Do not use misleading synonyms as exact equivalents.
```

**Related prompts:** 025, 033, 052

---

## Commercial Prompt 031: Create purposeful independent practice

**Best for:** Practice that exposes the structure of a concept.

**Use when:** Pupils need more than repeated questions of the same type.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and curriculum designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Core example: [EXAMPLE]
Number of items: [NUMBER]

TASK
Create independent practice using purposeful variation.

REQUIREMENTS
- Vary one important feature at a time where useful.
- Include accessible practice before deeper application.
- Include at least one item that exposes whether pupils understand the underlying concept.
- Include answers.
- Avoid repetitive items that add little diagnostic value.

OUTPUT FORMAT
Pupil tasks followed by answer key and a short teacher note explaining the purpose of the variation.

QUALITY CHECKS
Check accuracy and ensure every variation still assesses the stated objective.
```

**Related prompts:** 014, 029, 032

---

## Commercial Prompt 032: Create misconception-focused examples

**Best for:** Teaching through common wrong answers and near misses.

**Use when:** A concept has predictable misconceptions.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and subject specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Concept: [CONCEPT]
Known evidence of error: [ERROR_EVIDENCE]

TASK
Create examples that help pupils identify, explain and correct common misconceptions.

REQUIREMENTS
- Separate observed errors from possible explanations.
- Create plausible incorrect examples only where pedagogically useful.
- Ask pupils to explain why an answer is wrong.
- Provide the correct reasoning.
- Include a final check for transfer.

OUTPUT FORMAT
Example; pupil judgement; explanation; correction; follow-up question.

QUALITY CHECKS
Do not invent a misconception as though it were evidenced in the class. Label hypotheses clearly.
```

**Related prompts:** 017, 036, 044

---

## Commercial Prompt 033: Create structured discussion questions

**Best for:** Discussion that develops explanation, comparison and reasoning.

**Use when:** You want pupils to build ideas rather than answer a sequence of recall questions.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and discussion designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Topic: [TOPIC]
Learning objective: [OBJECTIVE]
Prior learning: [PRIOR_LEARNING]

TASK
Create a sequence of discussion questions that develops thinking from accessible entry points to deeper reasoning.

REQUIREMENTS
- Include questions requiring explanation or justification.
- Include prompts that encourage pupils to build on another response.
- Avoid questions with only one acceptable wording where several answers are defensible.
- Include sentence stems where useful.
- Keep the discussion connected to the objective.

OUTPUT FORMAT
Question; purpose; expected thinking; follow-up prompt; sentence stem where useful.

QUALITY CHECKS
Questions must be age appropriate and must genuinely support the intended learning.
```

**Related prompts:** 016, 034, 039

---

## Commercial Prompt 034: Create sentence stems for reasoning

**Best for:** Helping pupils express thinking clearly.

**Use when:** Pupils understand more than they can currently explain.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in language-rich teaching.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Thinking pupils need to express: [THINKING]
Vocabulary: [VOCABULARY]

TASK
Create sentence stems that support pupils to explain, justify, compare or reason without giving them the answer.

REQUIREMENTS
- Keep stems appropriate to the year group.
- Include a progression from supported to more independent language.
- Use the required vocabulary naturally.
- Avoid stems that become fill-in-the-gap answers.

OUTPUT FORMAT
Entry-level stems; developing stems; challenge stems; teacher note on when to fade support.

QUALITY CHECKS
Stems must support thinking rather than replace it.
```

**Related prompts:** 007, 033, 035

---

## Commercial Prompt 035: Build a retrieval-to-reasoning question sequence

**Best for:** Moving pupils from recall into explanation and application.

**Use when:** A lesson needs a clear progression in question demand.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and formative assessment specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Topic: [TOPIC]
Objective: [OBJECTIVE]

TASK
Create a short sequence of questions that moves from retrieval through explanation to reasoning or application.

REQUIREMENTS
- Start with prerequisite knowledge.
- Make the change in thinking demand clear.
- Include a point where pupils must explain an answer.
- Include one transfer or application question where appropriate.
- Provide answer guidance.

OUTPUT FORMAT
Question; thinking demand; answer; follow-up question; common error.

QUALITY CHECKS
Do not confuse difficult wording with difficult thinking.
```

**Related prompts:** 004, 016, 033

---

## Commercial Prompt 036: Diagnose a misconception from pupil work

**Best for:** Turning pupil errors into a targeted teaching response.

**Use when:** You have actual pupil responses and need help identifying patterns.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher reviewing pupil work.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Learning objective: [OBJECTIVE]
Question/task: [TASK]
Pupil responses: [RESPONSES]

TASK
Identify observable error patterns and suggest plausible explanations that should be tested through further questioning.

REQUIREMENTS
- Quote or describe the evidence.
- Separate observation from interpretation.
- Group similar errors.
- Suggest one diagnostic question for each important pattern.
- Recommend a proportionate teaching response.
- Do not diagnose SEND or learning difficulties.

OUTPUT FORMAT
Observed pattern; evidence; possible explanation; diagnostic question; teaching response; recheck.

QUALITY CHECKS
Do not over-interpret a small sample. State uncertainty where evidence is limited.
```

**Related prompts:** 032, 044, 045

---

## Commercial Prompt 037: Create an engaging lesson starter

**Best for:** Starting a lesson by activating relevant prior knowledge.

**Use when:** You need an efficient opening that earns its place in the lesson.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Topic: [TOPIC]
Objective: [OBJECTIVE]
Previous learning: [PREVIOUS_LEARNING]
Time available: [TIME]

TASK
Create a short lesson starter that activates relevant prior knowledge and leads naturally into the new learning.

REQUIREMENTS
- Keep it within the stated time.
- Include a clear teaching purpose.
- Avoid gimmicks that do not support learning.
- Include a quick teacher check of responses.

OUTPUT FORMAT
Starter instructions; teacher language; pupil response method; answer/check; transition into lesson.

QUALITY CHECKS
The starter must support the objective rather than simply entertain pupils.
```

**Related prompts:** 004, 019, 025

---

## Commercial Prompt 038: Turn a topic into purposeful classroom activities

**Best for:** Generating activity options that serve a specific learning purpose.

**Use when:** You need activity ideas without disconnected games.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and curriculum designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Topic: [TOPIC]
Objective: [OBJECTIVE]
Resources: [RESOURCES]
Duration: [DURATION]

TASK
Create three activity options that each directly support the objective.

REQUIREMENTS
For each activity state what pupils do, what they learn, resources, teacher role, assessment opportunity, likely misconception and adaptation.

OUTPUT FORMAT
Comparison table followed by a recommendation of the strongest option for the stated class.

QUALITY CHECKS
Do not recommend an activity merely because it is entertaining. It must serve the learning objective.
```

**Related prompts:** 001, 015, 037

---

## Commercial Prompt 039: Create a collaborative learning task

**Best for:** Structured paired or group work.

**Use when:** Pupils need to collaborate to explain, solve or create something.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and collaborative-learning designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Class size: [CLASS_SIZE]
Resources: [RESOURCES]

TASK
Design a collaborative task in which every pupil has a meaningful cognitive role.

REQUIREMENTS
- Define roles where useful.
- Make individual accountability visible.
- Include a shared outcome.
- Provide teacher monitoring questions.
- Include an assessment check.
- Anticipate pupils who may dominate or withdraw.

OUTPUT FORMAT
Task; roles; instructions; teacher prompts; accountability; assessment; adaptations.

QUALITY CHECKS
Collaboration must be necessary or genuinely useful for the learning objective.
```

**Related prompts:** 033, 040, 041

---

## Commercial Prompt 040: Create a pupil self-assessment routine

**Best for:** Helping pupils evaluate their own learning against clear criteria.

**Use when:** Pupils need to reflect on the quality of their work.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in metacognition and assessment for learning.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Success criteria: [CRITERIA]
Pupil task: [TASK]

TASK
Create a short self-assessment routine pupils can complete after the task.

REQUIREMENTS
- Use pupil-friendly language.
- Ask pupils to identify evidence in their own work.
- Include one reflection question about what to improve next.
- Avoid reducing self-assessment to a confidence rating.

OUTPUT FORMAT
Pupil checklist; reflection questions; teacher interpretation guidance.

QUALITY CHECKS
Every question must relate to the objective and success criteria.
```

**Related prompts:** 010, 041, 043

---

## Commercial Prompt 041: Create useful peer assessment

**Best for:** Structured peer feedback without vague comments.

**Use when:** Pupils can use shared criteria to review a peer's work.

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
Pupil work type: [WORK]

TASK
Create a short peer-assessment routine using evidence from the success criteria.

REQUIREMENTS
- Teach pupils what useful feedback looks like.
- Use a sequence such as strength, evidence, next step.
- Avoid personal or vague judgements.
- Include sentence stems.
- Keep teacher oversight clear.

OUTPUT FORMAT
Instructions; checklist; sentence stems; useful feedback example; unhelpful feedback example.

QUALITY CHECKS
Focus feedback on the learning, not personal preference.
```

**Related prompts:** 010, 040, 044

---

## Commercial Prompt 042: Create a lesson plenary

**Best for:** Ending a lesson by checking whether the intended learning has been secured.

**Use when:** You want the final minutes to inform future teaching.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Key learning: [KEY_LEARNING]
Lesson activities: [ACTIVITIES]
Time available: [TIME]

TASK
Create a short plenary that checks the intended learning and gives the teacher useful evidence for the next lesson.

REQUIREMENTS
- Use a task pupils can complete independently.
- Include an answer or checking method.
- Include one question that exposes a misconception or uncertainty.
- State what the teacher should do with the evidence.

OUTPUT FORMAT
Pupil task; expected response; teacher interpretation; next-step options.

QUALITY CHECKS
The plenary must measure the objective, not simply ask whether pupils enjoyed the lesson.
```

**Related prompts:** 017, 036, 043

---

## Commercial Prompt 043: Create an exit ticket

**Best for:** A fast final check that can shape tomorrow's teaching.

**Use when:** You need concise evidence of individual understanding.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and formative assessment specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Essential knowledge: [KNOWLEDGE]
Common misconception: [MISCONCEPTION]

TASK
Create a three-item exit ticket that gives the teacher useful evidence about whether the objective has been met.

REQUIREMENTS
- Include one essential recall or recognition check.
- Include one application or explanation item.
- Include one diagnostic item linked to the stated misconception.
- Provide concise answers and interpretation guidance.

OUTPUT FORMAT
Three pupil questions followed by answer key and decision rules for the next lesson.

QUALITY CHECKS
Questions must be short, answerable and directly connected to the objective.
```

**Related prompts:** 017, 042, 045

---

## Commercial Prompt 044: Turn pupil work into next-step teaching

**Best for:** Moving from marking or checking work to an actionable teaching response.

**Use when:** You have pupil work and need to decide what to teach next.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher reviewing pupil work for instructional next steps.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Success criteria: [CRITERIA]
Pupil work: [WORK]

TASK
Analyse the evidence and identify the most useful teaching response for the class, groups or individual pupils where the evidence supports a distinction.

REQUIREMENTS
- Separate observed evidence from interpretation.
- Identify common patterns.
- Prioritise the most important learning issue.
- Recommend a short teaching response.
- Include a recheck to determine whether the response worked.
- Do not make unsupported diagnostic claims.

OUTPUT FORMAT
Evidence pattern; teaching implication; priority; proposed response; recheck; decision rule.

QUALITY CHECKS
Do not infer more than the supplied work can support.
```

**Related prompts:** 032, 036, 045

---

## Commercial Prompt 045: Create a responsive teaching decision tree

**Best for:** Turning checks for understanding into immediate teaching actions.

**Use when:** You want to anticipate what you will do when pupils respond differently.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in responsive teaching.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Check point: [CHECK_POINT]
Possible response patterns: [RESPONSES]

TASK
Create a decision tree showing what the teacher should do for each meaningful response pattern.

REQUIREMENTS
- Identify evidence of secure understanding.
- Identify partial understanding.
- Identify a misconception or prerequisite gap.
- Recommend proportionate next actions.
- Include a short recheck after reteaching.

OUTPUT FORMAT
Response pattern → interpretation → teacher action → pupil action → recheck.

QUALITY CHECKS
Do not treat one pupil response as proof of whole-class understanding. Keep decisions evidence-led.
```

**Related prompts:** 017, 036, 044

---

## Commercial Prompt 046: Create an oral rehearsal routine

**Best for:** Preparing pupils to speak, explain or write using accurate language.

**Use when:** Pupils need to rehearse ideas before an independent task.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in language-rich teaching.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Task: [TASK]
Objective: [OBJECTIVE]
Key vocabulary: [VOCABULARY]

TASK
Create a short oral rehearsal routine that prepares pupils for the target task.

REQUIREMENTS
- Define what pupils rehearse.
- Include useful sentence stems.
- Include partner interaction where appropriate.
- Move from supported language to more independent expression.
- State what the teacher should listen for.

OUTPUT FORMAT
Teacher model; partner rehearsal; sentence stems; challenge; teacher listening points; transition to task.

QUALITY CHECKS
The rehearsal must support the intended learning rather than become an unrelated speaking activity.
```

**Related prompts:** 033, 034, 039
