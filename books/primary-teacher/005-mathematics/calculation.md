# Calculation and Fluency Workflows

## CF-01 — Calculation Lesson Sequence

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 700–1,000 words  
**Curriculum Tags:** KS1, KS2, Calculation, Fluency, Lesson Planning

### Editable Variables
`[YEAR_GROUP]` | `[OPERATION]` | `[OBJECTIVE]` | `[NUMBER_RANGE]` | `[PRIOR_KNOWLEDGE]` | `[DURATION]`

### ROLE
Act as an experienced primary mathematics teacher and subject specialist.

### CONTEXT
Teach `[OBJECTIVE]` to `[YEAR_GROUP]` using `[OPERATION]` within `[NUMBER_RANGE]`. Pupils bring `[PRIOR_KNOWLEDGE]`; lesson duration is `[DURATION]`.

### TASK
Create a coherent sequence from prerequisite retrieval through explicit modelling, guided practice, reasoning and independent application.

### REQUIREMENTS
Make the mathematical structure and chosen strategy explicit. Distinguish an efficient strategy from one that is merely possible. Include deliberate variation, likely misconceptions and a formative check.

### OUTPUT FORMAT
Objective; prerequisites; key idea; model; guided practice; independent practice; reasoning; misconceptions; assessment; answers.

### QUALITY CHECKS
Verify every calculation and ensure each phase supports the stated objective.

### OPTIONAL CUSTOMISATION
Adapt for mental strategies, informal methods or formal written methods.

### Example Input
Year 4; addition; objective: add two four-digit numbers using partitioning and regrouping; range to 9,999; prior knowledge: place value; 60 minutes.

### Example Output
Model regrouping as an exchange of equivalent place-value units before recording the calculation symbolically, then vary examples so pupils decide when regrouping is required.

---

## CF-02 — Calculation Strategy Comparison

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Calculation, Strategies, Reasoning

### Editable Variables
`[YEAR_GROUP]` | `[CALCULATION_TYPE]` | `[EXAMPLES]` | `[KNOWN_METHODS]` | `[OBJECTIVE]`

### ROLE
Act as a primary mathematics specialist with strong knowledge of calculation strategies.

### CONTEXT
Pupils in `[YEAR_GROUP]` are working on `[CALCULATION_TYPE]`. Compare strategies for `[EXAMPLES]`; known methods are `[KNOWN_METHODS]`; the objective is `[OBJECTIVE]`.

### TASK
Compare mathematically valid methods and explain the reasoning, efficiency and conditions under which each is useful.

### REQUIREMENTS
Do not rank methods universally. Explain how number structure affects efficiency. Include examples where one strategy becomes less suitable and address likely misconceptions.

### OUTPUT FORMAT
Strategy; worked example; mathematical reasoning; strengths; limitations; best use cases; misconception risks; comparison question.

### QUALITY CHECKS
All worked examples and claims about efficiency must be mathematically valid.

### OPTIONAL CUSTOMISATION
Adapt for addition, subtraction, multiplication or division.

### Example Input
Year 5; subtraction; examples: 502−198 and 7,003−2,999; known methods: counting up, compensation, column subtraction; objective: choose efficient methods.

### Example Output
Explain why compensation may exploit proximity to a round number while a general written algorithm remains valid but may not be the most efficient choice for every calculation.

---

## CF-03 — Fluency Practice Generator

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Fluency, Calculation, Deliberate Variation

### Editable Variables
`[YEAR_GROUP]` | `[SKILL]` | `[NUMBER_RANGE]` | `[NUMBER_OF_ITEMS]` | `[DIFFICULTY]`

### ROLE
Act as an experienced primary mathematics teacher designing purposeful fluency practice.

### CONTEXT
Generate `[NUMBER_OF_ITEMS]` items for `[YEAR_GROUP]` on `[SKILL]`, within `[NUMBER_RANGE]`, at `[DIFFICULTY]` level.

### TASK
Create a structured practice set that develops accuracy, efficiency and flexibility.

### REQUIREMENTS
Use mathematical variation rather than cosmetic changes. Sequence items so relationships become visible. Include an intended strategy where useful but permit alternative valid methods.

### OUTPUT FORMAT
Practice sequence; structural rationale; intended strategies; answers; discussion prompts; misconception watchpoints; extension.

### QUALITY CHECKS
Check every answer and ensure all items test the intended skill.

### OPTIONAL CUSTOMISATION
Adapt for retrieval, starter activities, intervention or independent practice.

### Example Input
Year 3; multiplication facts; range: 2, 5 and 10 times tables; 15 items; mixed difficulty.

### Example Output
Group related facts so pupils use known relationships, such as deriving 7×10 from 7×5, rather than practising facts as unrelated recall items.

---

## CF-04 — Arithmetic Misconception Diagnosis

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Calculation, Misconceptions, Assessment

### Editable Variables
`[YEAR_GROUP]` | `[OPERATION]` | `[PUPIL_WORK]` | `[INTENDED_STRATEGY]` | `[PREREQUISITES]`

### ROLE
Act as a primary mathematics assessment specialist diagnosing arithmetic thinking from evidence.

### CONTEXT
A `[YEAR_GROUP]` pupil's work on `[OPERATION]` is `[PUPIL_WORK]`. The intended strategy is `[INTENDED_STRATEGY]`; prerequisites are `[PREREQUISITES]`.

### TASK
Identify observable patterns, generate competing explanations and design a short diagnostic follow-up.

### REQUIREMENTS
Separate observation from inference. Consider slips, notation, place-value insecurity, misunderstood procedures and prerequisite gaps. Do not treat one error as proof of a stable misconception.

### OUTPUT FORMAT
Observed pattern; hypotheses; evidence strength; diagnostic task; response interpretation; targeted teaching; reassessment.

### QUALITY CHECKS
The follow-up must distinguish between plausible explanations.

### OPTIONAL CUSTOMISATION
Adapt for individual conferencing, small-group intervention or whole-class diagnosis.

### Example Input
Year 4; subtraction; pupil records 402−187 as 385; intended strategy: regrouping; prerequisites: tens and ones exchanges.

### Example Output
Test whether the issue is regrouping across a zero, subtraction facts or place-value alignment using carefully chosen contrasting examples.

---

## CF-05 — Mental Calculation Strategy Builder

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Mental Calculation, Number Sense

### Editable Variables
`[YEAR_GROUP]` | `[OPERATION]` | `[NUMBER_RANGE]` | `[KNOWN_STRATEGIES]` | `[TARGET_RELATIONSHIP]`

### ROLE
Act as a primary mathematics fluency specialist.

### CONTEXT
Pupils in `[YEAR_GROUP]` are calculating with `[OPERATION]` within `[NUMBER_RANGE]`. Known strategies are `[KNOWN_STRATEGIES]`; target relationship is `[TARGET_RELATIONSHIP]`.

### TASK
Develop examples and prompts that help pupils select, explain and compare efficient mental strategies.

### REQUIREMENTS
Base strategies on number structure. Include examples that favour different methods so pupils must make choices rather than memorise one trick.

### OUTPUT FORMAT
Strategy options; worked examples; selection cues; teacher prompts; practice; answers; common errors; reflection.

### QUALITY CHECKS
Every strategy must be valid and appropriate to the number range.

### OPTIONAL CUSTOMISATION
Adapt for whole-class discussion or short daily fluency routines.

### Example Input
Year 5; addition; numbers to 10,000; known strategies: compensation and partitioning; target: choosing efficient approaches.

### Example Output
Contrast 3,998+2,407 with 3,451+2,549 so pupils discuss why different number structures may make different approaches efficient.

---

## CF-06 — Written Method Teaching Sequence

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 700–1,000 words  
**Curriculum Tags:** KS2, Written Methods, Place Value, Calculation

### Editable Variables
`[YEAR_GROUP]` | `[OPERATION]` | `[NUMBER_RANGE]` | `[PREREQUISITE_METHODS]` | `[REPRESENTATIONS]`

### ROLE
Act as an experienced primary mathematics teacher teaching formal written calculation methods conceptually.

### CONTEXT
Teach a written method for `[OPERATION]` to `[YEAR_GROUP]` within `[NUMBER_RANGE]`. Prerequisite methods are `[PREREQUISITE_METHODS]`; available representations are `[REPRESENTATIONS]`.

### TASK
Create an explicit sequence linking the written recording to underlying place-value, additive or multiplicative structure.

### REQUIREMENTS
Explain each recorded step mathematically. Include concrete or pictorial support where useful, then deliberately fade support. Address common procedural errors without reducing teaching to rules to memorise.

### OUTPUT FORMAT
Prerequisites; mathematical structure; representation; teacher model; guided practice; independent practice; reasoning check; misconceptions; assessment.

### QUALITY CHECKS
Check alignment, exchanges, regrouping and every worked example.

### OPTIONAL CUSTOMISATION
Adapt for addition, subtraction, multiplication or short/long division where age-appropriate.

### Example Input
Year 5; multiplication; up to 3-digit by 2-digit; prerequisites: distributive partitioning; representations: area model and place-value counters.

### Example Output
Connect partial products in the area model to each line of the written calculation so zero placeholders or place-value shifts are explained rather than memorised.

---

## CF-07 — Calculation Reasoning Problems

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Calculation, Reasoning, Problem Solving

### Editable Variables
`[YEAR_GROUP]` | `[OPERATION]` | `[NUMBER_RANGE]` | `[CONTEXT]` | `[NUMBER_OF_PROBLEMS]`

### ROLE
Act as a primary mathematics reasoning specialist.

### CONTEXT
Create `[NUMBER_OF_PROBLEMS]` for `[YEAR_GROUP]` involving `[OPERATION]` within `[NUMBER_RANGE]`. Use `[CONTEXT]` only where it supports mathematical meaning.

### TASK
Generate problems requiring pupils to choose, explain, estimate or check a calculation rather than merely execute a named operation.

### REQUIREMENTS
Keep contexts mathematically coherent and reading demand proportionate. Include at least one problem with an unnecessary number, multiple possible methods or an error to evaluate.

### OUTPUT FORMAT
Problem; mathematical focus; expected reasoning; possible methods; answer; misconception; extension.

### QUALITY CHECKS
Verify all answers and ensure contexts do not create ambiguity unless intentional.

### OPTIONAL CUSTOMISATION
Adapt for oral reasoning, paired work or written explanation.

### Example Input
Year 6; division; numbers to 10,000; context: planning quantities; 6 problems.

### Example Output
Include a problem where pupils must decide whether to round up a quotient based on the quantity being represented and justify why a remainder cannot simply be ignored.

---

## CF-08 — Calculation Error Analysis

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Error Analysis, Calculation, Teaching

### Editable Variables
`[YEAR_GROUP]` | `[CORRECT_CALCULATION]` | `[PUPIL_ERROR]` | `[KNOWN_METHOD]` | `[RELATED_OBJECTIVE]`

### ROLE
Act as an experienced primary mathematics teacher using errors as diagnostic evidence.

### CONTEXT
The correct calculation is `[CORRECT_CALCULATION]`. A pupil produced `[PUPIL_ERROR]` using `[KNOWN_METHOD]`; the related objective is `[RELATED_OBJECTIVE]`.

### TASK
Analyse the error and create a short teaching response that uses the incorrect example productively.

### REQUIREMENTS
Do not assume the cause. Identify plausible explanations and include a discriminating question or contrasting example. Move from analysis to correction and then similar-but-different practice.

### OUTPUT FORMAT
Observed error; hypotheses; diagnostic question; mathematical explanation; correction; practice sequence; answers; reassessment.

### QUALITY CHECKS
The correction must address the underlying structure, not merely replace an answer.

### OPTIONAL CUSTOMISATION
Adapt for whole-class discussion, conferencing or intervention.

### Example Input
Year 4; 36×4=124; pupil error: multiplied 6×4 and 3×4 then concatenated; known method: partitioning; objective: understand distributive multiplication.

### Example Output
Use an area or partition model to test whether the pupil understands 30×4 as 120, then contrast 36×4 with a similar example that makes concatenation visibly impossible.

---

## CF-09 — Adapt Calculation Practice Without Lowering Demand

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Adaptive Teaching, Inclusion, Calculation

### Editable Variables
`[ORIGINAL_TASK]` | `[YEAR_GROUP]` | `[OBJECTIVE]` | `[ACCESS_BARRIER]` | `[SUPPORT_AVAILABLE]`

### ROLE
Act as an experienced primary mathematics teacher specialising in adaptive teaching.

### CONTEXT
The original task is `[ORIGINAL_TASK]` for `[YEAR_GROUP]`. The intended objective is `[OBJECTIVE]`; the access barrier is `[ACCESS_BARRIER]`; support available is `[SUPPORT_AVAILABLE]`.

### TASK
Adapt presentation, language, recording, scaffolding or quantity while preserving the intended mathematical reasoning.

### REQUIREMENTS
Identify the actual barrier before changing the mathematics. Do not automatically use smaller numbers or easier operations. Include an independence-release or scaffold-fading route.

### OUTPUT FORMAT
Mathematical construct; barrier analysis; adaptation; teacher guidance; adapted task; equivalent evidence; fade-out plan; review point.

### QUALITY CHECKS
The adapted version must still provide evidence of the original objective.

### OPTIONAL CUSTOMISATION
Adapt for SEND, EAL, working-memory, language, motor or sensory access needs.

### Example Input
Year 5; choose efficient multiplication strategies; barrier: extended written recording; support: mini-whiteboard and verbal explanation.

### Example Output
Allow concise annotations or oral reasoning while retaining the requirement to select and justify an efficient strategy for the same mathematical calculations.

---

## CF-10 — Fluency Assessment and Next Steps

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Fluency, Assessment, Calculation

### Editable Variables
`[YEAR_GROUP]` | `[SKILL]` | `[NUMBER_RANGE]` | `[NUMBER_OF_ITEMS]` | `[LIKELY_ERRORS]`

### ROLE
Act as a primary mathematics assessment specialist.

### CONTEXT
Assess `[YEAR_GROUP]` pupils on `[SKILL]` within `[NUMBER_RANGE]` using `[NUMBER_OF_ITEMS]` items. Likely errors are `[LIKELY_ERRORS]`.

### TASK
Create a compact assessment that distinguishes accuracy, efficiency and strategy selection, followed by an interpretation guide and targeted next steps.

### REQUIREMENTS
Do not equate speed alone with fluency. Include items that reveal whether correct answers arise from secure relationships, inefficient procedures or lucky guessing where evidence can distinguish them.

### OUTPUT FORMAT
Assessment; answer key; strategy evidence; response patterns; interpretation guide; next teaching action; extension; follow-up check.

### QUALITY CHECKS
Verify every answer and ensure interpretations are proportionate to the evidence collected.

### OPTIONAL CUSTOMISATION
Adapt for a 5-, 10- or 15-minute assessment.

### Example Input
Year 4; skill: multiply by multiples of 10; range to 9,000; 8 items; likely error: appending zeros without place-value reasoning.

### Example Output
Include calculations, representations and explanation prompts so pupils who obtain correct answers can still demonstrate whether they understand the multiplicative place-value relationship.