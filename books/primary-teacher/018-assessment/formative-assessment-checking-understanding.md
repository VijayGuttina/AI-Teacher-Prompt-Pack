---
title: "Primary Teacher Prompt Pack: Formative Assessment & Checking Understanding"
book: "Primary Teacher Prompt Pack"
chapter: "018 Assessment"
family: "Formative Assessment & Checking Understanding"
subject_code: "ASSESSMENT"
status: "workflows"
version: "1.0"
---

# Formative Assessment & Checking Understanding

This family contains ten copy/paste-ready workflows for eliciting useful evidence during teaching and converting it into proportionate instructional decisions.

## Assessment-specific controls

Use these controls throughout the family:

- Start with the learning intention and the decision the evidence will support.
- Use the smallest useful check rather than adding assessment for its own sake.
- Distinguish evidence of learning from evidence of confidence, compliance, speed or participation.
- Treat one response as evidence to interpret, not proof of a fixed misconception or ability level.
- Make teaching responses explicit where the workflow is intended to inform responsive teaching.
- Preserve the intended construct when adapting access.
- Avoid unnecessary pupil data and avoid asking pupils to disclose sensitive personal information.
- Do not invent school assessment policy, statutory requirements or pupil characteristics.
- Use current authoritative sources where current requirements matter.
- Use UK English and no em dash character in generated output.

## AS-11: Design a Hinge Question

**Difficulty:** Beginner  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** Short, under 700 words  
**Typical generation time:** Under 1 minute  
**Curriculum tags:** formative assessment, hinge question, checking understanding

### Purpose
Create one high-value hinge question that reveals whether pupils are ready to move on, need further explanation or need a different teaching response.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Learning Objective: [LEARNING_OBJECTIVE]
- Current Teaching Point: [TEACHING_POINT]
- Likely Errors: [LIKELY_ERRORS]
- Response Method: [RESPONSE_METHOD]

### ROLE
Act as an experienced primary teacher skilled in formative assessment and responsive teaching.

### CONTEXT
The question will be used during teaching, not as a formal graded assessment. Use the supplied learning objective and likely errors. If likely errors are unknown, generate plausible distractors but label them as hypotheses to verify.

### TASK
Create one hinge question with answer options that discriminate between secure understanding, common errors and partial understanding.

### REQUIREMENTS
- Keep the question focused on one important teaching decision.
- Make every option plausible for a real pupil.
- Explain what each response may indicate.
- Provide the teacher action for each response pattern.
- Include a quick recheck after the response.

### OUTPUT FORMAT
Provide: Hinge question; options; intended answer; what each response may indicate; teaching response; quick recheck.

### QUALITY CHECKS
Check that the question assesses the stated learning point rather than reading fluency, confidence or test-taking skill.

### OPTIONAL CUSTOMISATION
Add [MISCONCEPTION_EVIDENCE] if the teacher has previous pupil work.

**Example Input:** Year 4 maths; objective: identify equivalent fractions; teaching point: recognising that 2/4 and 1/2 represent the same quantity.

**Example Output:** The options include common denominator and numerator errors and require pupils to justify the equivalence rather than guess.

**Teacher Tip:** A good hinge question changes what you do next. If every answer leads to the same action, it may not be functioning as a hinge.

**Related Workflows:** AS-12, AS-14, AS-18

---

## AS-12: Build a Mini-Whiteboard Check Sequence

**Difficulty:** Beginner  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** Short, under 700 words  
**Typical generation time:** Under 1 minute  
**Curriculum tags:** formative assessment, mini-whiteboards, checking understanding

### Purpose
Create a short sequence of mini-whiteboard checks that reveals understanding across a teaching episode without becoming a low-value quiz.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Learning Objective: [OBJECTIVE]
- Teaching Sequence: [TEACHING_SEQUENCE]
- Common Errors: [COMMON_ERRORS]

### ROLE
Act as a primary teacher using whole-class formative assessment to make immediate teaching decisions.

### CONTEXT
Use mini-whiteboards as rapid evidence. Keep the number of checks manageable and make the response to evidence explicit.

### TASK
Create 4 to 6 checks that progress from basic understanding to application where appropriate.

### REQUIREMENTS
For each check include prompt, expected response, what to scan for, likely interpretation and next teacher action.

### OUTPUT FORMAT
Use a table with columns: Check, Prompt, Expected Evidence, Watch For, Teacher Decision, Recheck.

### QUALITY CHECKS
Ensure checks are answerable quickly and assess the intended construct. Avoid using handwriting quality as evidence unless handwriting is itself the objective.

### OPTIONAL CUSTOMISATION
Add [AVAILABLE_TIME] and [RESPONSE_CONVENTIONS].

**Example Input:** Year 2 English; objective: identify nouns and verbs; 20-minute explicit teaching sequence.

**Example Output:** Checks move from single-word identification to choosing the correct category in short sentences.

**Teacher Tip:** Scan patterns across the class rather than reacting to the loudest or fastest pupils.

**Related Workflows:** AS-11, AS-13, AS-15

---

## AS-13: Create a Think-Pair-Share Assessment Routine

**Difficulty:** Beginner  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** Short, under 700 words  
**Typical generation time:** Under 1 minute  
**Curriculum tags:** formative assessment, discussion, pupil explanation, checking understanding

### Purpose
Turn structured pupil discussion into useful evidence about understanding while avoiding the assumption that confident speaking equals secure learning.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Objective: [OBJECTIVE]
- Question: [QUESTION]
- Discussion Time: [DISCUSSION_TIME]
- Known Access Needs: [ACCESS_NEEDS]

### ROLE
Act as a primary teacher designing an inclusive discussion-based formative assessment.

### CONTEXT
Use the supplied question and objective. Provide alternative response routes where needed without changing the intended construct.

### TASK
Create a Think-Pair-Share routine that elicits reasoning and gives the teacher usable evidence.

### REQUIREMENTS
Include individual thinking time, paired rehearsal, a clear listening focus, teacher sampling method and a follow-up check. Distinguish verbal fluency from the quality of reasoning.

### OUTPUT FORMAT
Provide: Teacher prompt; think phase; pair phase; share phase; evidence to listen for; misconceptions; follow-up check.

### QUALITY CHECKS
Do not require personal disclosure or assume that pupils who speak less have weaker understanding.

### OPTIONAL CUSTOMISATION
Add [ALTERNATIVE_RESPONSE_MODE].

**Example Input:** Year 5 geography; objective: explain why some places experience more rainfall than others.

**Example Output:** Pupils first formulate one causal explanation, rehearse it with a partner and then the teacher samples explanations against the stated success criteria.

**Teacher Tip:** Listen for the reasoning link between ideas, not simply the presence of correct vocabulary.

**Related Workflows:** AS-11, AS-16, AS-18

---

## AS-14: Design an Exit Ticket That Drives the Next Lesson

**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 600 to 900 words  
**Typical generation time:** Under 1 minute  
**Curriculum tags:** formative assessment, exit ticket, next-step planning

### Purpose
Create a brief end-of-lesson check that produces evidence useful for planning the next teaching step.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Objective: [OBJECTIVE]
- Lesson Content: [LESSON_CONTENT]
- Next Lesson: [NEXT_LESSON]

### ROLE
Act as a primary teacher who uses exit tickets as decision-support rather than routine data collection.

### CONTEXT
The exit ticket should take approximately [TIME_LIMIT] and should sample the most important evidence from the lesson.

### TASK
Create a compact exit ticket with interpretation rules and three possible next-lesson responses.

### REQUIREMENTS
Include one core item and, where useful, one explanation or application item. Define what secure, partial and insecure evidence looks like.

### OUTPUT FORMAT
Provide: Exit ticket; expected evidence; interpretation guide; next lesson response for each evidence pattern; recheck question.

### QUALITY CHECKS
Avoid creating a mini-test that takes disproportionate time to complete or mark.

### OPTIONAL CUSTOMISATION
Add [MARKING_METHOD] such as whole-class scan, self-check or teacher sampling.

**Example Input:** Year 3 maths; objective: subtract two three-digit numbers with exchange; five minutes available.

**Example Output:** The ticket includes one calculation and one short explanation, then maps response patterns to reteaching or progression decisions.

**Teacher Tip:** If the exit ticket cannot change tomorrow's teaching, reduce it or remove it.

**Related Workflows:** AS-04, AS-15, AS-19

---

## AS-15: Create a Live Questioning Plan for a Lesson

**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 900 to 1,300 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** questioning, formative assessment, responsive teaching

### Purpose
Plan purposeful questioning across a lesson so the teacher can elicit prior knowledge, check understanding, expose reasoning and decide when to adapt instruction.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Objective: [OBJECTIVE]
- Lesson Sequence: [LESSON_SEQUENCE]
- Likely Misconceptions: [LIKELY_MISCONCEPTIONS]
- Discussion Constraints: [DISCUSSION_CONSTRAINTS]

### ROLE
Act as an experienced primary teacher and formative assessment specialist.

### CONTEXT
Build questions into the supplied lesson sequence rather than producing a disconnected question bank.

### TASK
Create a questioning plan with questions placed at useful decision points.

### REQUIREMENTS
Include a purposeful mix of retrieval, checking, explanation, comparison, reasoning and application questions where relevant. For each, state what evidence the teacher is looking for and what action follows.

### OUTPUT FORMAT
Use a lesson-stage table with: Stage, Question, Intended Evidence, Follow-up, Teacher Decision.

### QUALITY CHECKS
Avoid excessive questioning. Ensure questions assess the objective and do not confuse rapid response with secure understanding.

### OPTIONAL CUSTOMISATION
Add [TARGET_PUPIL_GROUPS] or [QUESTIONING_ROUTINES].

**Example Input:** Year 6 English; objective: explain how an author creates tension; lesson includes model analysis, guided annotation and independent paragraph writing.

**Example Output:** Questions progress from retrieving textual details to explaining how language choices contribute to tension, with follow-up prompts based on evidence.

**Teacher Tip:** Plan the follow-up question as carefully as the first question. That is where much of the formative value sits.

**Related Workflows:** AS-12, AS-13, AS-18

---

## AS-16: Build a Self-Assessment and Reflection Check

**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 600 to 900 words  
**Typical generation time:** Under 1 minute  
**Curriculum tags:** self-assessment, metacognition, formative assessment, reflection

### Purpose
Create a self-assessment routine that helps pupils compare their work with explicit success criteria and identify a useful next action.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Objective: [OBJECTIVE]
- Success Criteria: [SUCCESS_CRITERIA]
- Pupil Work: [PUPIL_WORK]
- Reflection Time: [REFLECTION_TIME]

### ROLE
Act as a primary teacher designing structured self-assessment linked to learning rather than confidence or compliance.

### CONTEXT
Self-assessment should use clear criteria and evidence. It should not ask pupils to make unsupported judgements about their ability.

### TASK
Create a pupil-friendly self-assessment and reflection process.

### REQUIREMENTS
Include criteria in pupil-friendly language, an evidence prompt for each criterion, one next-step choice and a teacher follow-up where useful.

### OUTPUT FORMAT
Provide: pupil checklist; evidence prompts; reflection sentence stems; next-step choices; teacher interpretation notes.

### QUALITY CHECKS
Ensure pupils are assessing work against learning criteria, not rating themselves as a person or labelling their ability.

### OPTIONAL CUSTOMISATION
Add [VISUAL_SCALE] if appropriate, but do not let a traffic-light colour replace evidence.

**Example Input:** Year 4 writing; objective: use paragraphs to organise ideas; success criteria supplied.

**Example Output:** Pupils identify one paragraphing choice they can evidence and one specific improvement they will make.

**Teacher Tip:** “Show me where” is often more useful than “How confident are you?”

**Related Workflows:** AS-13, AS-17, AS-41

---

## AS-17: Design Peer Assessment Safely and Usefully

**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 800 to 1,200 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** peer assessment, feedback, formative assessment, pupil dignity

### Purpose
Create a structured peer-assessment routine that produces useful learning evidence without turning pupils into informal graders or creating unnecessary comparison and embarrassment.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Objective: [OBJECTIVE]
- Success Criteria: [SUCCESS_CRITERIA]
- Work to Review: [WORK]
- Discussion Time: [TIME]

### ROLE
Act as a primary teacher designing a safe, constructive peer-assessment process.

### CONTEXT
Peer assessment must be tightly linked to supplied success criteria. Pupils should comment on work and next steps, not assign unsupported ability judgements.

### TASK
Create the peer-assessment process, including modelling, sentence stems, evidence prompts and teacher oversight.

### REQUIREMENTS
- Model one example first.
- Require evidence from the work.
- Use respectful, specific language.
- Avoid public ranking or ability labelling.
- Include a teacher moderation or sampling step where appropriate.

### OUTPUT FORMAT
Provide: teacher model; pupil instructions; review checklist; feedback stems; escalation point; teacher sampling method; reflection.

### QUALITY CHECKS
Check that pupils can realistically judge the stated criteria and that peer comments do not become high-stakes judgements.

### OPTIONAL CUSTOMISATION
Add [PAIRING_OR_GROUPING_RULES] and [ANONYMOUS_WORK_OPTION].

**Example Input:** Year 5 art; objective: use contrast deliberately; pupils review one another's work using three supplied criteria.

**Example Output:** Pupils identify visible evidence of contrast and suggest one purposeful adjustment rather than rating artistic ability.

**Teacher Tip:** Peer assessment works best when the criteria are narrower than “Is this good?”

**Related Workflows:** AS-16, AS-18, AS-41

---

## AS-18: Diagnose Whole-Class Understanding From Multiple Responses

**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 900 to 1,300 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** formative assessment, response analysis, misconception diagnosis, responsive teaching

### Purpose
Analyse a set of pupil responses and identify patterns that should influence the next teaching move without over-interpreting limited evidence.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Objective: [OBJECTIVE]
- Assessment Prompt: [PROMPT]
- Pupil Responses: [PUPIL_RESPONSES]
- Context: [LESSON_CONTEXT]

### ROLE
Act as an experienced primary assessment lead analysing classroom evidence conservatively and constructively.

### CONTEXT
Treat the responses as evidence, not as definitive diagnoses. Where the response set is too small or ambiguous, state what further evidence is needed.

### TASK
Identify response patterns, plausible explanations, confidence level and the most proportionate next teaching response.

### REQUIREMENTS
Separate observable error patterns from explanations. Distinguish conceptual, procedural, language, reading, memory, representation and task-interpretation possibilities where relevant.

### OUTPUT FORMAT
Provide: observed patterns; possible explanations; confidence; evidence still needed; teaching response; recheck; pupils or groups requiring further attention only where evidence supports this.

### QUALITY CHECKS
Do not diagnose pupils or assign fixed labels. Do not claim that one response proves a misconception.

### OPTIONAL CUSTOMISATION
Add [PREVIOUS_EVIDENCE] to improve interpretation where appropriate.

**Example Input:** Year 4 fractions; 24 short pupil responses to “Which is greater, 3/8 or 1/2? Explain.”

**Example Output:** The analysis distinguishes denominator comparison errors from incomplete explanation and recommends a short representation-based check before concluding what pupils understand.

**Teacher Tip:** Always separate “what I can see” from “why I think it happened”.

**Related Workflows:** AS-11, AS-31, AS-61

---

## AS-19: Create a Responsive Teaching Decision Tree

**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 800 to 1,200 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** responsive teaching, formative assessment, decision rules, adaptive teaching

### Purpose
Convert formative evidence into a simple decision tree showing when to proceed, revisit, model differently, practise further or gather more evidence.

### Editable Variables
- Year Group: [YEAR_GROUP]
- Subject: [SUBJECT]
- Objective: [OBJECTIVE]
- Evidence Sources: [EVIDENCE_SOURCES]
- Likely Response Patterns: [RESPONSE_PATTERNS]
- Lesson Time Remaining: [TIME_REMAINING]

### ROLE
Act as a primary teacher designing practical responsive-teaching rules from classroom evidence.

### CONTEXT
Use the supplied evidence sources and time constraints. Avoid pretending that thresholds are universally valid unless the teacher supplies them.

### TASK
Create a decision tree for the teacher to use after formative checks.

### REQUIREMENTS
Include branches for secure evidence, partial evidence, widespread uncertainty, isolated difficulty and ambiguous evidence. For each branch specify the next teaching action and a quick way to check impact.

### OUTPUT FORMAT
Provide a decision tree followed by a compact classroom version suitable for printing or displaying.

### QUALITY CHECKS
Ensure the decision rules are proportionate and do not convert rough classroom evidence into unsupported grades or labels.

### OPTIONAL CUSTOMISATION
Add [TEACHER_DEFINED_THRESHOLD] if the school already uses a threshold.

**Example Input:** Year 6 science; pupils have completed a hinge question on electrical circuits; 70% secure, 20% partial, 10% ambiguous.

**Example Output:** The plan recommends targeted clarification and a short recheck rather than reteaching the entire lesson solely because a minority response is insecure.

**Teacher Tip:** Build a recheck into every branch. Otherwise the decision tree ends with an assumption.

**Related Workflows:** AS-11, AS-14, AS-18

---

## AS-20: Plan a Formative Assessment Review Meeting

**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT and comparable general-purpose models  
**Expected output length:** 900 to 1,300 words  
**Typical generation time:** 40 to 70 seconds  
**Curriculum tags:** formative assessment, professional dialogue, assessment review, teacher workload

### Purpose
Structure a short teacher or phase-team review of formative evidence so discussion results in concrete teaching actions rather than broad pupil labels or unnecessary data collection.

### Editable Variables
- Year Group / Phase: [YEAR_GROUP_OR_PHASE]
- Subject: [SUBJECT]
- Learning Priorities: [LEARNING_PRIORITIES]
- Evidence Available: [EVIDENCE_AVAILABLE]
- Meeting Length: [MEETING_LENGTH]
- Existing Actions: [EXISTING_ACTIONS]

### ROLE
Act as a primary assessment lead facilitating a focused professional review of formative evidence.

### CONTEXT
The meeting should use only relevant evidence. Avoid sharing unnecessary personal pupil information. School-specific assessment processes should be followed where supplied.

### TASK
Create a meeting agenda and evidence-review protocol that ends with agreed teaching actions, rechecks and ownership.

### REQUIREMENTS
Include: purpose; evidence selection; key questions; pattern analysis; pupils or groups requiring further evidence only where justified; teaching actions; intervention or revisit decisions; recheck date; recording method; workload safeguard.

### OUTPUT FORMAT
Provide a timed agenda, discussion prompts, action table and short record template.

### QUALITY CHECKS
The meeting must not become a ranking exercise, diagnosis exercise or data-production exercise. Every recorded action should have a clear purpose.

### OPTIONAL CUSTOMISATION
Add [SCHOOL_DATA_SYSTEM] and [PHASE_TEAM_ROLES] where supplied.

**Example Input:** Year 3 phase team; mathematics; 30-minute meeting; evidence from hinge questions and exit tickets; goal is to plan the next week's reteaching.

**Example Output:** The meeting prioritises two common learning gaps, assigns a short reteach response and schedules a recheck rather than producing a long pupil spreadsheet.

**Teacher Tip:** End every discussion with “What will we teach differently, and how will we know it helped?”

**Related Workflows:** AS-18, AS-19, AS-61
