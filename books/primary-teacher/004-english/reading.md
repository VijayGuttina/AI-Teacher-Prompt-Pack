# English Reading Workflows

This module contains compact, reusable workflows for primary English reading. It inherits the global, primary-teacher and English frameworks.

## Workflow index

| ID | Workflow | Primary use |
|---|---|---|
| ENG-R-01 | Whole-class reading lesson | Plan a complete text-centred reading lesson |
| ENG-R-02 | Guided reading sequence | Structure guided reading around a text |
| ENG-R-03 | Retrieval questions | Generate text-grounded retrieval questions |
| ENG-R-04 | Inference questions | Generate evidence-based inference questions |
| ENG-R-05 | Vocabulary in context | Teach and assess vocabulary from a text |
| ENG-R-06 | Prediction questions | Develop prediction using textual evidence |
| ENG-R-07 | Explanation questions | Develop explanation of ideas, events or choices |
| ENG-R-08 | Summarise a text | Generate age-appropriate summarising tasks |
| ENG-R-09 | Compare texts or characters | Structure comparative reading |
| ENG-R-10 | Evaluate author choices | Explore language, structure and effect |
| ENG-R-11 | Diagnose reading misconceptions | Analyse pupil responses and identify misconceptions |
| ENG-R-12 | Reading intervention activity | Create targeted short intervention |

---

## ENG-R-03 — Retrieval Questions

**Purpose:** Create short, text-grounded retrieval questions that check whether pupils can locate and recall explicitly stated information.

**Prompt Difficulty:** Beginner

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Short to medium

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS1/KS2; English; Reading; Retrieval

### Editable Variables

- Year Group
- Text / extract
- Number of questions
- Question difficulty
- Optional focus vocabulary
- Whether answers should include quotations or paragraph references

### CONTEXT

Use the supplied text and the teacher's variables. Do not invent information that is not stated or clearly supported by the text.

### TASK

Create retrieval questions that require pupils to find and recall explicit information from the supplied text.

### REQUIREMENTS

- Include the requested number of questions.
- Vary where information appears in the text.
- Keep questions appropriate to the year group.
- Avoid turning straightforward retrieval into inference.
- Provide accurate answers.
- If the teacher requests evidence locations, identify the relevant sentence or paragraph without inventing quotations.

### OUTPUT FORMAT

| Question | Answer | Evidence location |
|---|---|---|

Then provide one optional teacher note identifying any question that may be unusually difficult because of vocabulary or text structure.

### QUALITY CHECKS

- Every answer must be supported by the supplied text.
- No question should require unsupported inference unless explicitly requested.
- Questions should measure retrieval rather than general knowledge.

### OPTIONAL CUSTOMISATION

Add a mix of multiple-choice, short-answer and oral questions, or restrict all questions to one format.

### Teacher Tip

Use retrieval questions early in a reading lesson to establish what pupils know before moving to inference or evaluation.

---

## ENG-R-04 — Inference Questions

**Purpose:** Create questions that require pupils to combine textual evidence with reasoning to infer meaning, feelings, motives or events.

**Prompt Difficulty:** Intermediate

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Medium

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS1/KS2; English; Reading; Inference

### Editable Variables

- Year Group
- Text / extract
- Number of questions
- Inference focus
- Difficulty
- Expected evidence requirement

### CONTEXT

Use only the supplied text as the evidence base. Where more than one interpretation is defensible, identify this rather than pretending that one answer is uniquely correct.

### TASK

Create inference questions that require pupils to identify what can reasonably be inferred and explain which textual clues support the inference.

### REQUIREMENTS

- Include questions requiring reasoning, not simple retrieval.
- Provide model answers and acceptable alternative answers where appropriate.
- Identify the relevant textual evidence.
- Distinguish evidence from inference.
- Include at least one question requiring an explanation of how the evidence supports the inference.

### OUTPUT FORMAT

For each question provide:

1. Question
2. Skill tested
3. Model answer
4. Evidence
5. Reasoning explanation
6. Acceptable alternatives, where relevant

### QUALITY CHECKS

- The inference must be logically supported by the text.
- Evidence must not be invented.
- The question must not depend on specialist background knowledge unless supplied.
- Alternative defensible interpretations must not be incorrectly marked wrong.

### Teacher Tip

Ask pupils to complete the chain: **What do you infer? What evidence supports it? How does the evidence support your inference?**

---

## ENG-R-05 — Vocabulary in Context

**Purpose:** Identify important vocabulary in a supplied text and create a short teaching sequence that helps pupils understand and use it in context.

**Prompt Difficulty:** Intermediate

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Medium

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS1/KS2; English; Reading; Vocabulary

### Editable Variables

- Year Group
- Text / extract
- Number of words
- Vocabulary focus
- Existing pupil knowledge
- Desired application task

### CONTEXT

Select words that are genuinely useful for understanding the text, building vocabulary or discussing the author's meaning. Use the surrounding context rather than dictionary definitions alone.

### TASK

Select the most useful vocabulary and create a concise teach-practise-apply sequence.

### REQUIREMENTS

For each selected word provide:

- word;
- contextual meaning;
- pupil-friendly explanation;
- text context;
- useful synonym or contrast where appropriate;
- example sentence;
- short application task.

### OUTPUT FORMAT

Start with a prioritised vocabulary table, followed by a short teaching sequence and application activity.

### QUALITY CHECKS

- Meanings must fit the supplied context.
- Definitions must be age appropriate.
- Do not select words merely because they look difficult.
- Do not teach an inaccurate synonym as an exact equivalent.

### Teacher Tip

Prioritise a small number of high-value words that pupils can encounter repeatedly rather than attempting to teach every unfamiliar word.

---

## ENG-R-06 — Prediction Questions

**Purpose:** Generate prediction questions that require pupils to use evidence from a text to anticipate what may happen next or what a text may reveal.

**Prompt Difficulty:** Beginner

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Short

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS1/KS2; English; Reading; Prediction

### Editable Variables

- Year Group
- Text / extract
- Number of questions
- Prediction point
- Difficulty

### TASK

Create prediction questions grounded in the information available at the specified point in the text.

### REQUIREMENTS

- Ask pupils to justify predictions using evidence.
- Avoid questions that require knowledge of the rest of a known published story unless the teacher explicitly supplies it.
- Provide example predictions and evidence.
- Accept multiple plausible predictions where appropriate.

### OUTPUT FORMAT

| Question | Possible prediction | Evidence pupils could use |
|---|---|---|

### QUALITY CHECKS

Predictions must be plausible but should not be presented as certain when the text does not establish certainty.

---

## ENG-R-07 — Explanation Questions

**Purpose:** Create questions requiring pupils to explain ideas, events, character behaviour or author choices using evidence from a text.

**Prompt Difficulty:** Intermediate

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Medium

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS1/KS2; English; Reading; Explanation

### Editable Variables

- Year Group
- Text / extract
- Focus
- Number of questions
- Expected response length

### TASK

Create explanation questions that require pupils to connect evidence with a reasoned explanation.

### REQUIREMENTS

- Avoid questions answerable with a single copied phrase.
- Provide model answers.
- Identify evidence and reasoning separately.
- Include sentence stems where useful for the specified year group.

### OUTPUT FORMAT

For each question provide the question, expected evidence, model answer and optional scaffold.

### QUALITY CHECKS

The answer must demonstrate explanation rather than merely repetition.

---

## ENG-R-08 — Summarise a Text

**Purpose:** Create a summary task that requires pupils to identify and combine the most important information from a text.

**Prompt Difficulty:** Intermediate

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Medium

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS1/KS2; English; Reading; Summarising

### Editable Variables

- Year Group
- Text / extract
- Summary length
- Focus
- Scaffold level

### TASK

Identify the essential information and create an age-appropriate summarising activity.

### REQUIREMENTS

- Distinguish main ideas from interesting but non-essential details.
- Provide a model summary appropriate to the year group.
- Include a simple success checklist.
- Where appropriate, provide a planning grid or key-point extraction step.

### QUALITY CHECKS

The model summary must preserve the meaning of the source without adding unsupported information.

---

## ENG-R-09 — Compare Texts or Characters

**Purpose:** Create a structured comparison task for two supplied texts, characters, viewpoints or representations.

**Prompt Difficulty:** Intermediate

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Medium

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS2; English; Reading; Comparison

### Editable Variables

- Year Group
- Text A
- Text B
- Comparison focus
- Number of questions
- Expected response format

### TASK

Generate comparison questions and a structured response activity requiring evidence from both sources.

### REQUIREMENTS

- Make the comparison dimension explicit.
- Require evidence from both sources where appropriate.
- Distinguish similarity from difference.
- Provide a model comparative response.

### QUALITY CHECKS

Do not claim a similarity or difference that the supplied texts do not support.

---

## ENG-R-10 — Evaluate Author Choices

**Purpose:** Create higher-order reading tasks exploring how an author uses language, structure or viewpoint to create an effect.

**Prompt Difficulty:** Advanced

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Medium to long

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS2; English; Reading; Language; Structure; Evaluation

### Editable Variables

- Year Group
- Text / extract
- Focus: language / structure / viewpoint
- Number of questions
- Desired depth

### TASK

Create evaluation questions requiring pupils to identify an authorial choice, explain its effect and support their view with evidence.

### REQUIREMENTS

- Avoid presenting subjective interpretation as fact.
- Distinguish observation, interpretation and evaluation.
- Provide model responses that show evidence and reasoning.
- Include one question where more than one defensible interpretation is possible.

### QUALITY CHECKS

Do not attribute authorial intention unless the text or supplied context supports it. Use phrasing such as "may suggest" or "could make the reader" where appropriate.

---

## ENG-R-11 — Diagnose Reading Misconceptions

**Purpose:** Analyse supplied pupil responses and identify likely misconceptions in reading comprehension.

**Prompt Difficulty:** Advanced

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Medium

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS1/KS2; English; Reading; Assessment

### Editable Variables

- Year Group
- Source text
- Questions
- Pupil responses
- Mark scheme, if available
- Teacher concern

### TASK

Analyse the responses and identify patterns that may indicate misunderstanding of vocabulary, retrieval, inference, evidence, explanation or question interpretation.

### REQUIREMENTS

- Separate evidence from hypothesis.
- Quote or reference the pupil response when explaining the finding.
- Suggest one targeted next step per meaningful misconception.
- Do not diagnose a learning difficulty from a small sample.

### OUTPUT FORMAT

| Pupil / group | Observed response pattern | Likely misunderstanding | Evidence | Targeted next step |
|---|---|---|---|---|

Finish with the two or three highest-priority teaching actions.

### QUALITY CHECKS

Do not make medical, SEND or diagnostic claims. Clearly label interpretations as hypotheses requiring teacher judgement.

---

## ENG-R-12 — Reading Intervention Activity

**Purpose:** Create a short, targeted intervention activity from a specified reading need.

**Prompt Difficulty:** Advanced

**AI Model Compatibility:** ChatGPT, Claude, Gemini and Microsoft Copilot

**Expected Output Length:** Medium

**Typical Generation Time:** Under 1 minute

**Curriculum Tags:** KS1/KS2; English; Reading; Intervention

### Editable Variables

- Year Group
- Identified reading need
- Text / extract
- Duration
- Group size
- Current attainment information
- Desired outcome

### TASK

Create a short intervention sequence focused on the stated reading need.

### REQUIREMENTS

- Define the precise skill being targeted.
- Begin with a brief diagnostic check.
- Include explicit teaching and guided practice.
- Include a short independent check.
- Provide success criteria and next-step guidance.
- Keep the intervention tightly focused rather than recreating a full lesson.

### QUALITY CHECKS

The activity must address the stated need rather than simply providing easier reading work. Avoid unsupported diagnostic conclusions.

### Teacher Tip

Repeat the short diagnostic check after several sessions to determine whether the targeted skill is improving before changing the intervention focus.
