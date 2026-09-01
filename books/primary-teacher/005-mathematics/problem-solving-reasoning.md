# Problem Solving and Reasoning Workflows

## PR-01 — Problem-Solving Lesson

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 700–1,000 words  
**Curriculum Tags:** KS1, KS2, Problem Solving, Reasoning, Lesson Planning

### Editable Variables
`[YEAR_GROUP]` | `[MATHEMATICAL_OBJECTIVE]` | `[PROBLEM_TYPE]` | `[PREREQUISITES]` | `[DURATION]`

### ROLE
Act as an experienced primary mathematics teacher specialising in problem solving and mathematical reasoning.

### CONTEXT
Plan a lesson for `[YEAR_GROUP]` on `[MATHEMATICAL_OBJECTIVE]` using `[PROBLEM_TYPE]`. Pupils have `[PREREQUISITES]`; available lesson time is `[DURATION]`.

### TASK
Design a sequence that makes the underlying mathematics explicit while requiring pupils to interpret, choose, reason, solve and evaluate rather than follow a supplied procedure.

### REQUIREMENTS
Include purposeful modelling of thinking, worked examples, guided problems, independent problems and reflection. Keep reading demand proportionate to the mathematical objective. Include deliberate variation and at least one opportunity to compare strategies.

### OUTPUT FORMAT
Objective; prerequisite check; problem structure; modelled reasoning; guided problems; independent problems; teacher questions; misconceptions; answers; reflection.

### QUALITY CHECKS
Verify every problem, answer, numerical condition and stated strategy. Ensure the intended mathematical demand is actually present.

### OPTIONAL CUSTOMISATION
Adapt for whole-class teaching, paired reasoning, intervention or low-floor/high-ceiling tasks.

### Example Input
Year 5; objective: solve multi-step problems involving the four operations; problem type: contextual quantity problems; prerequisites: written methods and estimation; 60 minutes.

### Example Output
Model how to identify known and unknown quantities, decide which operation is justified, estimate the result and check whether the final answer fits the context before moving to independent multi-step problems.

---

## PR-02 — Bar Modelling and Visual Representation

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Problem Solving, Bar Models, Representation

### Editable Variables
`[YEAR_GROUP]` | `[PROBLEM]` | `[KNOWN_QUANTITIES]` | `[UNKNOWN_QUANTITIES]` | `[REPRESENTATION_OPTIONS]`

### ROLE
Act as a primary mathematics specialist skilled in using representations to expose mathematical structure.

### CONTEXT
Analyse `[PROBLEM]` for `[YEAR_GROUP]`. Known quantities are `[KNOWN_QUANTITIES]`; unknown quantities are `[UNKNOWN_QUANTITIES]`; possible representations are `[REPRESENTATION_OPTIONS]`.

### TASK
Select or reject a bar model, diagram, number line, table or other representation based on the mathematical relationships in the problem.

### REQUIREMENTS
Do not force a bar model when another representation is clearer. Explain what each part represents and connect the representation to an equation or calculation. Avoid diagrams that imply relationships not present in the problem.

### OUTPUT FORMAT
Mathematical structure; recommended representation; labelled model description; equation; solution pathway; pupil explanation prompt; alternative representation if useful.

### QUALITY CHECKS
Check that every quantity and relationship in the representation corresponds to the problem and that the equation matches the model.

### OPTIONAL CUSTOMISATION
Adapt for comparison, part-whole, additive, multiplicative or multi-step problems.

### Example Input
Year 4; problem: Sam has 36 cards, which is 12 more than Alex has; how many does Alex have?

### Example Output
Use a comparison bar model showing Sam's quantity as Alex's quantity plus 12, then connect the model directly to 36−12=24.

---

## PR-03 — Multiple-Solution Problem

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Open Problems, Reasoning, Generalisation

### Editable Variables
`[YEAR_GROUP]` | `[TOPIC]` | `[NUMBER_RANGE]` | `[MINIMUM_SOLUTIONS]` | `[DIFFICULTY]`

### ROLE
Act as an experienced primary mathematics problem-solving teacher.

### CONTEXT
Create an open problem for `[YEAR_GROUP]` on `[TOPIC]`, within `[NUMBER_RANGE]`, at `[DIFFICULTY]`, with at least `[MINIMUM_SOLUTIONS]` valid solutions or solution pathways.

### TASK
Design a mathematically meaningful problem in which pupils must explore possibilities, justify choices and identify whether their solution set is complete where appropriate.

### REQUIREMENTS
State constraints clearly. Do not make the task open merely by allowing arbitrary answers. Distinguish multiple answers from multiple methods. Where completeness can reasonably be established, include a route to proving it.

### OUTPUT FORMAT
Problem; mathematical objective; constraints; teacher notes; possible solutions; solution pathways; completeness considerations; discussion prompts; extension.

### QUALITY CHECKS
Test every proposed solution against every constraint and identify accidental extra solutions or contradictions.

### OPTIONAL CUSTOMISATION
Adapt for number, geometry, measure, fractions or mixed-topic reasoning.

### Example Input
Year 5; topic: factors; range: numbers to 100; minimum solutions: 5; difficulty: high.

### Example Output
Create a problem requiring pupils to find several numbers satisfying factor constraints, then investigate whether they have found all possibilities and justify the conclusion.

---

## PR-04 — Always, Sometimes, Never

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Reasoning, Conjecture, Counterexample

### Editable Variables
`[YEAR_GROUP]` | `[TOPIC]` | `[NUMBER_OF_STATEMENTS]` | `[DIFFICULTY]`

### ROLE
Act as a primary mathematics reasoning specialist.

### CONTEXT
Create `[NUMBER_OF_STATEMENTS]` statements for `[YEAR_GROUP]` about `[TOPIC]` at `[DIFFICULTY]` level.

### TASK
Generate statements pupils classify as always, sometimes or never true, requiring justification rather than intuition.

### REQUIREMENTS
Ensure classifications are mathematically defensible. For “sometimes” statements, include examples and counterexamples. For “always” claims, encourage pupils to explain why no counterexample exists within the stated domain.

### OUTPUT FORMAT
Statement; classification; justification; example; counterexample where relevant; teacher prompts; extension.

### QUALITY CHECKS
Test each statement against a broad range of valid cases before assigning a classification. State the domain explicitly.

### OPTIONAL CUSTOMISATION
Adapt for number, fractions, geometry, measures, calculation or algebraic thinking at an appropriate primary level.

### Example Input
Year 6; topic: divisibility; 8 statements; high difficulty.

### Example Output
Include claims such as “A multiple of 4 is even” alongside more subtle claims requiring pupils to distinguish a necessary condition from a sufficient one.

---

## PR-05 — Odd-One-Out Reasoning

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Reasoning, Classification, Mathematical Language

### Editable Variables
`[YEAR_GROUP]` | `[TOPIC]` | `[OBJECTS_OR_NUMBERS]` | `[DIFFICULTY]`

### ROLE
Act as an experienced primary mathematics teacher designing rich classification tasks.

### CONTEXT
Create an odd-one-out task for `[YEAR_GROUP]` about `[TOPIC]`, using `[OBJECTS_OR_NUMBERS]` at `[DIFFICULTY]` level.

### TASK
Create a set in which at least two different mathematically valid justifications can be defended, then provide teacher guidance for discussing alternative classifications.

### REQUIREMENTS
Avoid an unstated “intended” rule. Make the evidence sufficient for each proposed justification. Encourage pupils to identify properties rather than rely on appearance or position.

### OUTPUT FORMAT
Task; possible odd-one-outs; valid justifications; mathematical properties; teacher prompts; alternative interpretations; extension.

### QUALITY CHECKS
Verify every claimed property and ensure alternative justifications genuinely distinguish the selected item.

### OPTIONAL CUSTOMISATION
Adapt for shapes, numbers, calculations, fractions, decimals or measures.

### Example Input
Year 4; topic: multiplication and division; objects: 24, 36, 42, 45; difficulty: mixed.

### Example Output
Allow different valid criteria, such as divisibility or factor structure, and ask pupils to defend the criterion rather than guess the teacher's preferred answer.

---

## PR-06 — Spot the Mistake

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Error Analysis, Reasoning, Misconceptions

### Editable Variables
`[YEAR_GROUP]` | `[TOPIC]` | `[PROBLEM]` | `[INCORRECT_SOLUTION]` | `[TARGET_CONCEPT]`

### ROLE
Act as a primary mathematics teacher using error analysis as a reasoning tool.

### CONTEXT
The problem is `[PROBLEM]`; the supplied incorrect solution is `[INCORRECT_SOLUTION]`; the target concept is `[TARGET_CONCEPT]`; pupils are in `[YEAR_GROUP]`.

### TASK
Create a plausible incorrect solution and a sequence requiring pupils to locate, explain and correct the error.

### REQUIREMENTS
The error should be mathematically plausible. Separate the observable error from any inferred misconception. Require explanation of why the incorrect step fails, not just the corrected answer.

### OUTPUT FORMAT
Problem; incorrect solution; error location; mathematical explanation; corrected solution; diagnostic question; follow-up task; answers.

### QUALITY CHECKS
Verify both the original and corrected solutions and ensure the error is genuinely plausible for the stated age group.

### OPTIONAL CUSTOMISATION
Adapt for calculation, fractions, geometry, measure or data.

### Example Input
Year 5; topic: fractions; problem: compare 3/4 and 5/8; incorrect solution: 5/8 is larger because 5 is larger than 3.

### Example Output
Ask pupils to challenge the numerator-only comparison using equivalent fractions or a common representation and explain why the denominator changes the size of each part.

---

## PR-07 — Reasoning Sentence Stems

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Mathematical Language, Reasoning, Adaptive Teaching

### Editable Variables
`[YEAR_GROUP]` | `[TOPIC]` | `[REASONING_DEMAND]` | `[LANGUAGE_BARRIER]` | `[SUPPORT_LEVEL]`

### ROLE
Act as an experienced primary mathematics teacher specialising in mathematical communication and adaptive teaching.

### CONTEXT
Pupils in `[YEAR_GROUP]` need support with `[REASONING_DEMAND]` in `[TOPIC]`. The relevant language barrier is `[LANGUAGE_BARRIER]`; support level is `[SUPPORT_LEVEL]`.

### TASK
Create concise sentence stems that support explanation, comparison, justification, conjecture or evaluation without supplying the mathematical answer.

### REQUIREMENTS
Provide graduated stems from highly supportive to increasingly independent. Avoid replacing mathematical thinking with fill-in-the-blank scripts. Include teacher guidance on when to fade the stems.

### OUTPUT FORMAT
Reasoning demand; stem bank; graduated support; example use; teacher prompt; fade-out route; warning against over-scaffolding.

### QUALITY CHECKS
Check that each stem supports the intended reasoning and does not reveal the answer or required operation.

### OPTIONAL CUSTOMISATION
Adapt for EAL, SEND, oral rehearsal, paired discussion or written reasoning.

### Example Input
Year 5; topic: fractions; reasoning demand: justify comparison; language barrier: difficulty structuring explanations; support: moderate.

### Example Output
Use stems such as “I know ___ is greater because…” and “This comparison is valid because…” while requiring pupils to supply the mathematical evidence independently.

---

## PR-08 — Problem-Solving Misconception Diagnosis

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Problem Solving, Diagnosis, Assessment

### Editable Variables
`[YEAR_GROUP]` | `[PROBLEM]` | `[PUPIL_WORK]` | `[RECENT_TEACHING]` | `[KNOWN_PREREQUISITES]`

### ROLE
Act as a primary mathematics diagnostic specialist.

### CONTEXT
The problem is `[PROBLEM]`; the pupil work is `[PUPIL_WORK]`; pupils are in `[YEAR_GROUP]`; recent teaching is `[RECENT_TEACHING]`; relevant prerequisites are `[KNOWN_PREREQUISITES]`.

### TASK
Analyse the evidence, distinguish observable behaviour from hypotheses and design diagnostic questions that identify the most useful next teaching step.

### REQUIREMENTS
Consider problem interpretation, representation, operation selection, calculation, reasoning and checking as separate possible points of difficulty. Do not infer fixed ability from limited evidence.

### OUTPUT FORMAT
Observed behaviour; possible explanations; evidence for/against; diagnostic questions; interpretation; targeted teaching response; follow-up check.

### QUALITY CHECKS
Ensure each diagnostic question distinguishes between plausible explanations rather than simply repeating the original problem.

### OPTIONAL CUSTOMISATION
Adapt for pupil conferencing, intervention or whole-class formative assessment.

### Example Input
Year 4; pupil chooses multiplication for every word problem; work shows accurate calculations once an operation is supplied; recent teaching: multiplication strategies.

### Example Output
Test operation selection separately from calculation fluency using short problems with different structures and minimal reading load.

---

## PR-09 — Mixed-Strategy Problem Set

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 700–1,000 words  
**Curriculum Tags:** KS1, KS2, Problem Solving, Strategy Selection, Reasoning

### Editable Variables
`[YEAR_GROUP]` | `[TOPICS]` | `[NUMBER_RANGE]` | `[NUMBER_OF_PROBLEMS]` | `[DIFFICULTY]`

### ROLE
Act as an experienced primary mathematics teacher specialising in strategic problem solving.

### CONTEXT
Create `[NUMBER_OF_PROBLEMS]` problems for `[YEAR_GROUP]` across `[TOPICS]`, within `[NUMBER_RANGE]`, at `[DIFFICULTY]` level.

### TASK
Design a mixed set in which the mathematical strategy or operation is not named in the question and pupils must decide what is appropriate.

### REQUIREMENTS
Include varied problem structures, not merely different contexts wrapped around the same calculation. Require pupils to explain their strategy and check the reasonableness of their answer.

### OUTPUT FORMAT
Problems; answers; appropriate strategy; alternative valid methods; reasoning guidance; common traps; teacher discussion questions; extension.

### QUALITY CHECKS
Verify every calculation, ensure sufficient information and confirm that no item unintentionally requires an out-of-scope method.

### OPTIONAL CUSTOMISATION
Adapt for retrieval-plus-reasoning lessons, assessment, homework or collaborative problem solving.

### Example Input
Year 6; topics: fractions, ratio and four operations; range: primary curriculum scope; 10 problems; high difficulty.

### Example Output
Mix problems so pupils must first identify the mathematical structure, then select a method, estimate or reason about the result and finally justify why their approach is appropriate.

---

## PR-10 — Adapt a Problem-Solving Task

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Adaptive Teaching, Inclusion, Problem Solving

### Editable Variables
`[ORIGINAL_PROBLEM]` | `[YEAR_GROUP]` | `[ACCESS_BARRIER]` | `[MATHEMATICAL_OBJECTIVE]` | `[EXISTING_SUPPORT]`

### ROLE
Act as an experienced primary mathematics teacher specialising in adaptive teaching and inclusive problem solving.

### CONTEXT
The original problem is `[ORIGINAL_PROBLEM]` for `[YEAR_GROUP]`. The objective is `[MATHEMATICAL_OBJECTIVE]`; the identified access barrier is `[ACCESS_BARRIER]`; existing support is `[EXISTING_SUPPORT]`.

### TASK
Adapt the problem to reduce the access barrier while preserving the central mathematical decision, reasoning and level of challenge.

### REQUIREMENTS
Consider vocabulary, layout, chunking, representation, response format and optional scaffolding. Do not assume a diagnosis. Do not automatically reduce numbers or steps if that changes the mathematical construct. Include a route toward independence.

### OUTPUT FORMAT
Original objective; barrier analysis; adapted problem; representation; teacher support; independence route; equivalent evidence; mathematical-demand check; review point.

### QUALITY CHECKS
Confirm that the pupil still has to interpret and solve the same underlying mathematical problem and that support does not perform the reasoning for them.

### OPTIONAL CUSTOMISATION
Adapt for SEND, EAL, working-memory, language, motor or sensory barriers.

### Example Input
Year 5; original problem: multi-step quantity problem; barrier: dense written language; objective: choose and combine appropriate operations; existing support: vocabulary bank.

### Example Output
Retain the quantities and mathematical decisions while restructuring the language, separating essential information visually and providing optional representation prompts that can be faded once the pupil demonstrates independence.