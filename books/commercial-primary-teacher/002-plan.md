# Part 2: Plan

Planning prompts that reduce preparation time while keeping the teacher in control.

---

## Commercial Prompt 001: Create a complete lesson plan

**Best for:** Building a teachable lesson from a clear learning objective.

**Use when:** You know what pupils need to learn but need the lesson sequence, modelling, practice and assessment organised.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced UK primary teacher and curriculum planner.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Topic: [TOPIC]
Learning objective: [LEARNING_OBJECTIVE]
Lesson duration: [DURATION]
Prior learning: [PRIOR_LEARNING]
Resources available: [RESOURCES]
Class considerations: [CLASS_CONSIDERATIONS]

TASK
Create a complete lesson plan that moves pupils from retrieval and explanation through teacher modelling, guided practice, independent application and a short assessment check.

REQUIREMENTS
- Keep every activity tightly connected to the learning objective.
- Identify essential prior knowledge.
- Include teacher modelling and at least one worked example where appropriate.
- Include purposeful questioning.
- Build in a short check for understanding before independent work.
- Include a realistic amount of pupil work for the stated duration.
- Include support and challenge without changing the core learning objective.

OUTPUT FORMAT
1. Lesson overview
2. Prior knowledge
3. Key vocabulary
4. Retrieval starter
5. Teacher explanation and modelling
6. Guided practice
7. Independent task
8. Adaptations and challenge
9. Assessment checks
10. Resources
11. Timing

QUALITY CHECKS
Check that the sequence fits the lesson duration, the assessment measures the stated objective, examples are accurate and no activity exists merely to fill time.

OPTIONAL CUSTOMISATION
Adapt for a shorter lesson, intervention group, mixed attainment class or limited resources.
```

**Example input:** Year 4 science, states of matter, 60 minutes, pupils know common materials.

**Example output:** A timed sequence with retrieval, particle-model explanation, teacher modelling, guided classification, independent application and a final check.

**Teacher tip:** Paste your existing lesson format into the prompt if your school uses a fixed planning template.

**Related prompts:** 002, 004, 007, 015

---

## Commercial Prompt 002: Turn a learning objective into a lesson sequence

**Best for:** Moving quickly from curriculum intent to teachable steps.

**Use when:** You have the objective but are unsure how to sequence the learning.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary curriculum specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Topic: [TOPIC]
Learning objective: [OBJECTIVE]
Known prior learning: [PRIOR_LEARNING]
Lesson duration: [DURATION]

TASK
Turn the objective into a coherent lesson sequence. Identify the smallest set of teaching steps pupils need in order to reach the objective successfully.

REQUIREMENTS
- Start with prerequisite knowledge.
- Identify the key concept or skill.
- Sequence explanation, modelling, guided practice and independent application.
- Include one point where understanding should be checked before pupils move on.
- Identify the likely point of difficulty.
- Avoid adding unrelated activities.

OUTPUT FORMAT
Provide a table with: stage, teacher action, pupil action, purpose, time and assessment check.

QUALITY CHECKS
The sequence must be realistic for the year group and duration and must lead directly to the objective.

OPTIONAL CUSTOMISATION
Offer a 30-minute, 45-minute and 60-minute version if the teacher leaves duration blank.
```

**Example input:** Year 3 maths, compare and order numbers to 1,000.

**Example output:** Retrieval of place value, explicit comparison using representations, guided comparison, independent ordering and a hinge check.

**Teacher tip:** Use this before asking AI to create worksheets. Get the teaching sequence right first.

**Related prompts:** 001, 003, 006

---

## Commercial Prompt 003: Build a unit sequence

**Best for:** Turning a broad topic into a logical sequence of lessons.

**Use when:** You need to plan a short unit rather than an isolated lesson.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary curriculum designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Unit topic: [TOPIC]
End goal: [END_GOAL]
Length: [NUMBER_OF_LESSONS] lessons
Known prior learning: [PRIOR_LEARNING]
School sequence or curriculum guidance: [CURRICULUM_GUIDANCE]

TASK
Design a coherent unit sequence showing how knowledge and skills build from the starting point to the end goal.

REQUIREMENTS
- Identify prerequisite knowledge.
- Sequence lessons so new learning builds on earlier learning.
- Include retrieval opportunities across the unit.
- Identify important vocabulary and concepts.
- Identify likely misconceptions and where they should be addressed.
- Include opportunities for application and assessment.
- Avoid treating every lesson as an isolated activity.

OUTPUT FORMAT
Create a lesson-by-lesson table with objective, key knowledge, teaching focus, practice, retrieval, assessment and dependency on previous learning.

QUALITY CHECKS
Check for logical progression, unnecessary repetition and missing prerequisite knowledge. Do not invent statutory curriculum requirements.

OPTIONAL CUSTOMISATION
Add a final end-of-unit assessment or an intervention checkpoint.
```

**Example input:** Year 5 history, Anglo-Saxons, 8 lessons.

**Example output:** A sequence moving from chronology and settlement through evidence, interpretation, daily life and an evidence-based historical conclusion.

**Teacher tip:** Give the AI your existing medium-term plan if you want it to improve rather than replace your sequence.

**Related prompts:** 002, 010, 018

---

## Commercial Prompt 004: Create a retrieval starter

**Best for:** Starting a lesson by bringing essential prior knowledge back to mind.

**Use when:** Pupils need to retrieve previous learning before new teaching begins.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in retrieval practice.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Current topic: [CURRENT_TOPIC]
Previous learning: [PREVIOUS_LEARNING]
Number of questions: [NUMBER]
Time available: [TIME]

TASK
Create a short retrieval starter that checks the knowledge pupils genuinely need for today's learning.

REQUIREMENTS
- Mix recall formats where useful.
- Prioritise essential prerequisite knowledge.
- Avoid trick questions.
- Include answers for the teacher.
- Increase difficulty only where it remains appropriate.
- Keep the task within the stated time.

OUTPUT FORMAT
Provide the pupil questions first, followed by an answer key and a brief note identifying any question that checks particularly important prerequisite knowledge.

QUALITY CHECKS
Check every answer and ensure the questions assess the supplied previous learning rather than unrelated trivia.
```

**Example input:** Year 5 maths, fractions, previous learning equivalent fractions.

**Example output:** Six short questions moving from recall of equivalent fractions to one application question.

**Teacher tip:** Use the result as a starting point, not a test. The purpose is to expose what needs revisiting.

**Related prompts:** 005, 016, 070

---

## Commercial Prompt 005: Plan spaced retrieval across a unit

**Best for:** Preventing important knowledge from disappearing after one lesson.

**Use when:** Planning a unit where pupils need to retain knowledge over several weeks.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as a primary curriculum and retrieval-practice specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Unit: [UNIT]
Duration: [DURATION]
Essential knowledge pupils must retain: [KNOWLEDGE]
Known prior knowledge: [PRIOR_KNOWLEDGE]

TASK
Create a practical spaced retrieval plan across the unit and identify when each important item should be revisited.

REQUIREMENTS
- Distinguish essential knowledge from useful detail.
- Revisit knowledge at increasing intervals where practical.
- Mix old and recent learning.
- Use different retrieval formats rather than repeating identical questions.
- Include answers and teacher checking guidance.
- Keep each retrieval activity proportionate to available lesson time.

OUTPUT FORMAT
Provide a schedule showing lesson point, knowledge retrieved, question format, approximate time and answer/checking guidance.

QUALITY CHECKS
Check that the schedule is realistic and that retrieval supports the unit rather than displacing new teaching.
```

**Example input:** Year 4 science unit lasting 6 weeks with 15 essential knowledge statements.

**Example output:** Short retrieval opportunities distributed across the unit, with later checks mixing several earlier concepts.

**Teacher tip:** Keep the retrieval sets small enough to repeat consistently.

**Related prompts:** 004, 019, 023

---

## Commercial Prompt 006: Identify prerequisite knowledge

**Best for:** Finding what pupils need to know before a new concept can be taught effectively.

**Use when:** A lesson objective looks simple but depends on several earlier ideas.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and curriculum progression specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
New learning objective: [OBJECTIVE]
Current unit: [UNIT]
Known previous learning: [PREVIOUS_LEARNING]

TASK
Identify the prerequisite knowledge and skills pupils are likely to need to access the stated objective.

REQUIREMENTS
- Separate essential prerequisites from helpful background knowledge.
- Explain why each prerequisite matters.
- Identify a quick way to check each one.
- Suggest what to reteach if a prerequisite is insecure.
- Do not assume that an objective has been mastered merely because it appeared in a previous year or unit.

OUTPUT FORMAT
Table with prerequisite, why it matters, quick check and possible response.

QUALITY CHECKS
Avoid inventing curriculum requirements. Distinguish likely prerequisite knowledge from assumptions about individual pupils.
```

**Example input:** Year 6 ratio, pupils have learned multiplication, division and fractions.

**Example output:** A short prerequisite map with checks for multiplicative relationships, fraction equivalence and scaling.

**Teacher tip:** Use this before intervention planning. It helps identify whether the real barrier is earlier knowledge rather than today's objective.

**Related prompts:** 002, 007, 021

---

## Commercial Prompt 007: Create differentiated tasks without lowering the objective

**Best for:** Planning support and challenge for mixed-attainment classes.

**Use when:** One lesson needs multiple access routes while keeping the same core learning intention.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in adaptive teaching.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Learning objective: [OBJECTIVE]
Core task: [TASK]
Known barriers: [BARRIERS]
Likely misconceptions: [MISCONCEPTIONS]
Available resources: [RESOURCES]

TASK
Create practical adaptations that remove unnecessary barriers while preserving the intended learning demand.

REQUIREMENTS
- Keep the same core objective unless the teacher explicitly requests an alternative objective.
- Use scaffolds such as worked examples, vocabulary support, structured steps, visual support or reduced extraneous reading.
- Create genuine challenge through depth, reasoning or transfer rather than simply more work.
- Identify when support can be withdrawn.
- Avoid labelling groups by ability in the pupil-facing material.

OUTPUT FORMAT
Core task; access supports; guided version; independent version; challenge; teacher prompts; fading plan.

QUALITY CHECKS
Check that adaptations do not simply make the task easier by removing the thinking being assessed.
```

**Example input:** Year 4 English, write a persuasive paragraph, mixed attainment, some pupils need vocabulary and sentence support.

**Example output:** One shared objective with sentence stems and vocabulary support for access, plus a challenge requiring deliberate language choices and justification.

**Teacher tip:** Ask for supports that can be removed gradually rather than permanent simplification.

**Related prompts:** 008, 009, 034

---

## Commercial Prompt 008: Build scaffolding for a complex task

**Best for:** Making a demanding task accessible without doing the thinking for pupils.

**Use when:** Pupils understand the objective but struggle to organise the process.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and scaffolding specialist.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Task: [TASK]
Learning objective: [OBJECTIVE]
Observed difficulty: [DIFFICULTY]
Resources: [RESOURCES]

TASK
Design a sequence of temporary scaffolds that help pupils complete the task independently.

REQUIREMENTS
- Identify the barrier rather than assuming lack of ability.
- Break the process into manageable steps.
- Provide a model or worked example where useful.
- Include prompts that make thinking visible.
- Include a point where each scaffold can be reduced or removed.
- Keep the original learning demand intact.

OUTPUT FORMAT
Barrier; scaffold; teacher prompt; pupil action; fading point; independent check.

QUALITY CHECKS
Avoid scaffolds that become permanent substitutes for thinking. Make each support directly connected to the barrier identified.
```

**Teacher tip:** A good scaffold should make the route clearer, not make the destination easier.

**Related prompts:** 007, 009, 034

---

## Commercial Prompt 009: Create a challenge task through depth

**Best for:** Extending pupils who have understood the core objective.

**Use when:** You need meaningful challenge rather than extra questions.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in depth and challenge.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Learning objective: [OBJECTIVE]
Core task: [TASK]
Pupil evidence of understanding: [EVIDENCE]

TASK
Create one or more challenge tasks that deepen the same learning rather than moving pupils onto unrelated content.

REQUIREMENTS
- Preserve the core concept or skill.
- Increase reasoning, explanation, comparison, transfer, justification or ambiguity where appropriate.
- Avoid simply increasing the number of questions.
- Provide a model of what successful depth could look like.
- Keep the task appropriate to the year group.

OUTPUT FORMAT
Challenge task; why it increases depth; teacher prompt; expected evidence; optional extension.

QUALITY CHECKS
The challenge must require deeper thinking, not merely greater workload or larger numbers.
```

**Teacher tip:** Challenge is strongest when pupils must explain, justify, generalise or apply rather than simply finish more work.

**Related prompts:** 007, 010, 021

---

## Commercial Prompt 010: Create success criteria

**Best for:** Making the intended quality of pupil work explicit.

**Use when:** Pupils need to know what successful work looks like.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Learning objective: [OBJECTIVE]
Expected pupil outcome: [OUTCOME]
Existing examples or model: [EXAMPLES]

TASK
Create concise success criteria that pupils can use while working and reviewing their own work.

REQUIREMENTS
- Make criteria observable in the final work or performance.
- Keep the list short enough to use in class.
- Distinguish essential criteria from optional refinement.
- Use pupil-friendly language without losing accuracy.
- Avoid criteria that simply describe compliance or presentation unless presentation is part of the learning objective.

OUTPUT FORMAT
Pupil-facing checklist followed by a teacher version explaining what evidence demonstrates each criterion.

QUALITY CHECKS
Every criterion must relate directly to the objective.
```

**Teacher tip:** If you cannot explain how a criterion will be seen in pupil work, it probably does not belong in the list.

**Related prompts:** 001, 011, 040

---

## Commercial Prompt 011: Create a worked example

**Best for:** Showing pupils what a successful process looks like before independent work.

**Use when:** A task involves a process, sequence or reasoning that pupils need to see modelled.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and instructional designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Learning objective: [OBJECTIVE]
Task pupils will complete: [TASK]
Common error: [COMMON_ERROR]

TASK
Create a worked example that models the process pupils need to use, including the reasoning that should be visible to them.

REQUIREMENTS
- Use accurate subject-specific examples.
- Make important decisions explicit.
- Include a deliberate point where a common error could occur and explain how to avoid it.
- Avoid modelling every possible variation.
- Keep the example proportionate to the lesson.

OUTPUT FORMAT
Model example; teacher narration; key decisions; common error; pupil practice task.

QUALITY CHECKS
Check all facts, calculations, terminology and sequencing.
```

**Teacher tip:** Ask the AI to produce the worked example first, then build the independent task from the same model.

**Related prompts:** 001, 007, 012

---

## Commercial Prompt 012: Plan explicit modelling

**Best for:** Turning a skill or process into a clear teacher modelling sequence.

**Use when:** Pupils need to see how an expert approaches a task.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in explicit instruction.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Skill or process: [SKILL]
Learning objective: [OBJECTIVE]
Prior knowledge: [PRIOR_KNOWLEDGE]

TASK
Plan a short explicit modelling sequence showing what the teacher does, says and makes visible while demonstrating the skill.

REQUIREMENTS
- Start from prerequisite knowledge.
- Break the process into meaningful steps.
- Make expert decisions explicit.
- Include one worked example.
- Identify questions to check understanding during modelling.
- Avoid excessive teacher talk.

OUTPUT FORMAT
Teacher action; teacher language; pupil attention point; check for understanding; next modelling step.

QUALITY CHECKS
The model must demonstrate the actual skill being taught rather than simply describing it.
```

**Teacher tip:** Keep the model short enough that pupils can then practise the same process themselves.

**Related prompts:** 011, 013, 021

---

## Commercial Prompt 013: Plan guided practice

**Best for:** Moving pupils from watching a model to doing the task with support.

**Use when:** Pupils need structured practice before independent work.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Modelled process: [MODELLED_PROCESS]
Common misconceptions: [MISCONCEPTIONS]

TASK
Create a guided-practice sequence in which pupils complete the task with decreasing levels of teacher support.

REQUIREMENTS
- Start with a closely matched example.
- Include teacher prompts that reveal thinking.
- Reduce support progressively.
- Include a quick check before independent practice.
- Identify when to pause and reteach.

OUTPUT FORMAT
Guided example 1; teacher prompt; pupil response; guided example 2; reduced prompt; independent readiness check.

QUALITY CHECKS
The sequence must prepare pupils for the independent task rather than becoming a separate activity.
```

**Related prompts:** 012, 014, 021

---

## Commercial Prompt 014: Create independent practice

**Best for:** Creating purposeful practice after explanation and guided work.

**Use when:** Pupils are ready to apply the learning independently.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Modelled examples: [EXAMPLES]
Prerequisite knowledge: [PREREQUISITES]
Number of tasks: [NUMBER]

TASK
Create an independent practice set that gives pupils enough opportunity to secure the stated objective without unnecessary repetition.

REQUIREMENTS
- Begin with accessible application.
- Increase complexity gradually.
- Include purposeful variation.
- Include answers or teacher checking guidance.
- Include one item that checks whether pupils can transfer the learning.

OUTPUT FORMAT
Pupil task sheet followed by answer key and a short teacher note identifying the most diagnostic item.

QUALITY CHECKS
Every task must assess the intended objective. Check calculations and answer keys independently.
```

**Related prompts:** 013, 015, 022

---

## Commercial Prompt 015: Plan a lesson resource pack

**Best for:** Producing the supporting materials needed for a lesson from one coherent plan.

**Use when:** You have the lesson sequence but still need questions, examples, task sheets or checks.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and resource designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Topic: [TOPIC]
Objective: [OBJECTIVE]
Lesson sequence: [LESSON_SEQUENCE]
Available resources: [RESOURCES]

TASK
Create the minimum useful set of classroom resources required to deliver the lesson sequence.

REQUIREMENTS
- Include only resources that serve a clear teaching purpose.
- Provide teacher modelling examples.
- Provide pupil practice.
- Include answer keys where relevant.
- Include adaptation and challenge options.
- Keep resource language age appropriate.

OUTPUT FORMAT
1. Teacher resource list
2. Modelling examples
3. Pupil activity
4. Answers/checking guidance
5. Adaptations
6. Challenge

QUALITY CHECKS
Check that every resource links directly to the objective and can realistically be used within the lesson.
```

**Teacher tip:** Give the AI the actual lesson plan rather than asking it to invent the lesson and resources separately.

**Related prompts:** 001, 011, 014

---

## Commercial Prompt 016: Plan questioning for a lesson

**Best for:** Improving the quality and timing of teacher questions.

**Use when:** A lesson needs better checks for understanding and deeper questioning.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in classroom questioning.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Lesson sequence: [SEQUENCE]
Known misconceptions: [MISCONCEPTIONS]

TASK
Create a questioning plan for the lesson that checks prerequisite knowledge, understanding during teaching and application at the end.

REQUIREMENTS
- Include a mixture of recall, explanation and reasoning questions where appropriate.
- Identify the purpose of each question.
- Include questions that reveal misconceptions.
- Avoid questions that allow only confident pupils to answer.
- Include a practical whole-class response method where useful.

OUTPUT FORMAT
Question; lesson point; purpose; expected response; likely misconception; follow-up question.

QUALITY CHECKS
Questions must match the objective and be answerable from the learning taught.
```

**Teacher tip:** Ask for follow-up questions, not just a longer list of initial questions.

**Related prompts:** 017, 018, 020

---

## Commercial Prompt 017: Create hinge questions

**Best for:** Deciding whether the class is ready to move on.

**Use when:** A key misconception would make the next stage of the lesson ineffective.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher specialising in formative assessment.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Teaching point immediately before the check: [TEACHING_POINT]
Likely misconception: [MISCONCEPTION]

TASK
Create three possible hinge questions and recommend the strongest one for deciding whether the class should move on.

REQUIREMENTS
- Make the correct answer depend on genuine understanding.
- Include plausible distractors linked to common misconceptions.
- Explain what each response would tell the teacher.
- Include the action the teacher should take for each response pattern.

OUTPUT FORMAT
Hinge question; response options; misconception represented; teacher interpretation; next action.

QUALITY CHECKS
The question must test the intended concept rather than reading speed or superficial recall.
```

**Teacher tip:** A strong hinge question is useful because the wrong answers tell you something about the thinking, not simply because the question is difficult.

**Related prompts:** 016, 020, 036

---

## Commercial Prompt 018: Create a short intervention plan

**Best for:** Turning an identified learning gap into a focused intervention.

**Use when:** A pupil or small group needs targeted support after assessment evidence.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and intervention planner.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Learning objective: [OBJECTIVE]
Evidence of difficulty: [EVIDENCE]
Known prior learning: [PRIOR_LEARNING]
Available time: [TIME]
Group size: [GROUP_SIZE]

TASK
Design a short intervention sequence based on the evidence provided.

REQUIREMENTS
- State the specific skill or knowledge gap.
- Separate observed evidence from possible explanation.
- Begin with a brief diagnostic check.
- Provide explicit teaching and guided practice.
- Include an independent check.
- Define what evidence would indicate that the intervention should continue, change or stop.

OUTPUT FORMAT
Baseline; intervention objective; teaching sequence; practice; check; decision rule; next step.

QUALITY CHECKS
Do not diagnose a learning difficulty from limited evidence. Keep the intervention linked to the identified learning need.
```

**Teacher tip:** Use the evidence you already have. Do not ask AI to infer a pupil's underlying needs from a single wrong answer.

**Related prompts:** 006, 019, 021

---

## Commercial Prompt 019: Turn a lesson into a retrieval plan

**Best for:** Building future retrieval opportunities from today's teaching.

**Use when:** You want important learning to reappear after the lesson rather than disappear into old planning.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as a primary teacher specialising in curriculum sequencing and retrieval.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Lesson content: [LESSON_CONTENT]
Essential knowledge: [ESSENTIAL_KNOWLEDGE]
Upcoming lessons: [UPCOMING_LESSONS]

TASK
Create a short retrieval schedule showing how today's essential learning can be revisited in later lessons.

REQUIREMENTS
- Identify the highest-value knowledge.
- Mix recent and older learning.
- Vary question format.
- Keep each retrieval activity brief.
- Include answers.

OUTPUT FORMAT
Lesson/date; knowledge to retrieve; questions; answers; approximate time.

QUALITY CHECKS
Do not overload future lessons. Retrieval should reinforce important knowledge without displacing essential new teaching.
```

**Related prompts:** 004, 005, 022

---

## Commercial Prompt 020: Audit a lesson plan before teaching

**Best for:** Finding weak points in an existing lesson before it reaches the classroom.

**Use when:** You already have a lesson plan and want a practical quality check rather than a new lesson.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teaching and lesson-quality reviewer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Lesson plan: [PASTE_LESSON_PLAN]
Available resources: [RESOURCES]

TASK
Audit the lesson for coherence, workload, teaching sequence and assessment value. Recommend only changes that materially improve the lesson.

REQUIREMENTS
Check:
- alignment between objective and activities;
- prerequisite knowledge;
- modelling and guided practice;
- questioning;
- cognitive demand;
- differentiation and accessibility;
- timing;
- assessment checks;
- unnecessary activity or resource load.

OUTPUT FORMAT
Keep; change; remove; add; revised sequence; priority level.

QUALITY CHECKS
Do not rewrite the whole lesson unless necessary. Preserve useful teacher decisions and clearly distinguish evidence from recommendation.
```

**Teacher tip:** Ask for a prioritised audit. Ten small suggestions are less useful than the two changes most likely to improve the lesson.

**Related prompts:** 001, 002, 015

---

## Commercial Prompt 021: Build a prerequisite-to-independence sequence

**Best for:** Planning how pupils move from what they already know to independent application.

**Use when:** A new skill depends on several linked pieces of knowledge.

**Difficulty:** Advanced

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and instructional sequence designer.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Objective: [OBJECTIVE]
Prerequisites: [PREREQUISITES]
Common errors: [ERRORS]
Lesson duration: [DURATION]

TASK
Design a progression from prerequisite retrieval to independent application.

REQUIREMENTS
Include:
- prerequisite check;
- explicit explanation;
- worked example;
- guided practice;
- reduced-support practice;
- independent application;
- final check.

For each stage state what evidence tells the teacher whether pupils are ready to move on.

OUTPUT FORMAT
Stage; teacher action; pupil action; evidence; decision to move on or reteach.

QUALITY CHECKS
Keep the sequence realistic and avoid moving pupils to independent work before the necessary knowledge is secure.
```

**Related prompts:** 002, 006, 012, 013

---

## Commercial Prompt 022: Plan a week's retrieval and practice

**Best for:** Connecting daily practice across a teaching week.

**Use when:** You want lessons to reinforce one another rather than operate as isolated sessions.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher and curriculum planner.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Weekly objectives: [OBJECTIVES]
Prior learning to retain: [PRIOR_LEARNING]
Number of lessons: [NUMBER]

TASK
Create a weekly plan showing where retrieval, guided practice, independent practice and application should occur.

REQUIREMENTS
- Keep retrieval short.
- Identify the knowledge that should be revisited.
- Show how practice becomes more independent.
- Include one cumulative check.
- Avoid repeating the same task format unnecessarily.

OUTPUT FORMAT
Day; new learning; retrieval; practice; application; assessment check.

QUALITY CHECKS
Check that the workload is realistic and that retrieval does not replace teaching of new content.
```

**Related prompts:** 005, 019, 023

---

## Commercial Prompt 023: Build a medium-term planning checklist

**Best for:** Quality-checking a medium-term plan before it is used.

**Use when:** You have a sequence of lessons and want to check its coherence.

**Difficulty:** Intermediate

**Copy and paste:**

```text
ROLE
Act as an experienced primary curriculum leader.

CONTEXT
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Unit: [UNIT]
Existing medium-term plan: [PLAN]
Curriculum guidance: [GUIDANCE]

TASK
Audit the plan against progression, prerequisite knowledge, assessment and classroom feasibility.

REQUIREMENTS
Check for:
- clear progression;
- sensible sequencing;
- prerequisite knowledge;
- vocabulary;
- retrieval;
- assessment opportunities;
- misconceptions;
- adaptation;
- realistic workload;
- unnecessary repetition.

OUTPUT FORMAT
Checklist with status, evidence, concern and recommended action.

QUALITY CHECKS
Do not invent curriculum requirements. Identify uncertainty where the supplied guidance is incomplete.
```

**Related prompts:** 003, 020, 024

---

## Commercial Prompt 024: Create a planning checklist for tomorrow's lesson

**Best for:** A fast final preparation check.

**Use when:** The lesson is already planned but you need to make sure the practical details are ready.

**Difficulty:** Beginner

**Copy and paste:**

```text
ROLE
Act as an experienced primary teacher preparing for tomorrow's lesson.

CONTEXT
Lesson plan: [LESSON_PLAN]
Year group: [YEAR_GROUP]
Subject: [SUBJECT]
Resources already available: [RESOURCES]

TASK
Create a concise preparation checklist based on the lesson plan.

REQUIREMENTS
Include only actions that need completing before, during or immediately after the lesson. Identify anything that could cause the lesson to fail if forgotten.

OUTPUT FORMAT
Before pupils arrive; during lesson; after lesson; optional preparation.

QUALITY CHECKS
Do not create unnecessary tasks. Prioritise items that affect teaching, pupil access, resources or assessment.
```

**Teacher tip:** Use this at the end of planning so the AI checks your plan rather than generating another one.

**Related prompts:** 001, 015, 020
