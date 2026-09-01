# Working Scientifically Workflows

## WS-01 — Scientific Question Builder

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Science, Working Scientifically, Scientific Questions, Enquiry

### Editable Variables
`[YEAR_GROUP]` | `[TOPIC]` | `[STARTING_OBSERVATION]` | `[EQUIPMENT]` | `[CONSTRAINTS]`

### ROLE
Act as an experienced primary science teacher and scientific-enquiry specialist.

### CONTEXT
Pupils in `[YEAR_GROUP]` are exploring `[TOPIC]`. Their starting observation is `[STARTING_OBSERVATION]`; available equipment is `[EQUIPMENT]`; relevant constraints are `[CONSTRAINTS]`.

### TASK
Turn the broad curiosity into several increasingly precise, scientifically meaningful questions and identify the strongest question for the stated age group and available evidence.

### REQUIREMENTS
Distinguish questions suitable for observing over time, pattern seeking, classification, comparative/fair testing and secondary research. Keep the question answerable with the available evidence. Do not force a causal question where the enquiry cannot establish causation.

### OUTPUT FORMAT
Starting idea; question options; enquiry type for each; recommended question; rationale; evidence required; feasibility check; teacher prompts.

### QUALITY CHECKS
Check that the recommended question is scientifically meaningful, age-appropriate, practically answerable and aligned with the available equipment and time.

### OPTIONAL CUSTOMISATION
Adapt for a short lesson, extended investigation, pupil-generated questions or mixed-attainment groups.

### Example Input
Year 4; topic: forces; observation: toy cars travel different distances; equipment: cars, ramps and rulers; constraints: 45 minutes.

### Example Output
Generate questions about ramp height, surface or another measurable factor, then select a question whose variables can realistically be controlled and measured within the lesson.

---

## WS-02 — Enquiry Type Selector

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Science, Working Scientifically, Enquiry Types

### Editable Variables
`[YEAR_GROUP]` | `[QUESTION]` | `[TOPIC]` | `[CONSTRAINTS]`

### ROLE
Act as a primary science enquiry specialist.

### CONTEXT
The proposed science question is `[QUESTION]` for `[YEAR_GROUP]` pupils studying `[TOPIC]`, within `[CONSTRAINTS]`.

### TASK
Determine which enquiry type best answers the question: observing over time, pattern seeking, classification and identification, comparative/fair testing, or secondary research.

### REQUIREMENTS
Explain why the selected enquiry matches the question. Identify what pupils would observe, measure, classify or research. Provide an alternative only where a realistic change in the question or constraints would justify it.

### OUTPUT FORMAT
Question; recommended enquiry; rationale; evidence; suitable method; alternative enquiry; teacher explanation.

### QUALITY CHECKS
Do not label an investigation a fair test simply because variables can be changed. Verify that the chosen enquiry can answer the actual question.

### OPTIONAL CUSTOMISATION
Adapt for KS1, KS2, limited equipment, outdoor work or cross-curricular research.

### Example Input
Year 3; question: How does a plant change over four weeks?; topic: plants; constraints: one lesson per week.

### Example Output
Select observing over time because the question concerns change across a period rather than the effect of a deliberately manipulated variable.

---

## WS-03 — Fair Test Planner

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 700–1,000 words  
**Curriculum Tags:** KS2, Science, Working Scientifically, Fair Testing, Variables

### Editable Variables
`[YEAR_GROUP]` | `[QUESTION]` | `[VARIABLE_TO_CHANGE]` | `[OUTCOME_TO_MEASURE]` | `[EQUIPMENT]` | `[TIME]`

### ROLE
Act as an experienced primary science teacher and practical-enquiry planner.

### CONTEXT
Design an investigation for `[YEAR_GROUP]` to answer `[QUESTION]`. The intended variable to change is `[VARIABLE_TO_CHANGE]`; the outcome to measure is `[OUTCOME_TO_MEASURE]`; equipment is `[EQUIPMENT]`; available time is `[TIME]`.

### TASK
Design a feasible comparative or fair test that makes the changed variable, measured outcome and relevant controls explicit.

### REQUIREMENTS
Include prediction, variables, equipment, method, measurement, recording, safety, conclusion and evaluation. Identify controls that are realistic and relevant rather than producing an unnecessarily long list. Explain how repeated measurements or trials could improve reliability where appropriate.

### OUTPUT FORMAT
Question; prediction; independent variable; dependent variable; control variables; equipment; method; safety; results table; conclusion prompt; evaluation; teacher notes.

### QUALITY CHECKS
Check that the measurement actually answers the question, the controls are practical, the method is repeatable and the conclusion will be limited to what the evidence supports.

### OPTIONAL CUSTOMISATION
Adapt for simple KS2 comparative tests, group investigations or constrained equipment.

### Example Input
Year 5; question: Which material makes the best parachute?; variable: canopy material; outcome: descent time; equipment: equal-sized canopies, string and weights; time: 60 minutes.

### Example Output
Keep weight, canopy size, drop height and procedure consistent while changing only the selected material and recording repeated descent times.

---

## WS-04 — Observation-Over-Time Planner

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Science, Working Scientifically, Observation Over Time

### Editable Variables
`[YEAR_GROUP]` | `[PHENOMENON]` | `[OBSERVATION_PERIOD]` | `[INTERVAL]` | `[EQUIPMENT]`

### ROLE
Act as a primary science specialist experienced in longitudinal observation enquiries.

### CONTEXT
Plan an observation enquiry for `[YEAR_GROUP]` pupils investigating `[PHENOMENON]` over `[OBSERVATION_PERIOD]`, with observations at `[INTERVAL]` using `[EQUIPMENT]`.

### TASK
Create a schedule that captures meaningful change over time and produces evidence pupils can compare and interpret.

### REQUIREMENTS
Specify what should be observed or measured, how consistency will be maintained, how observations will be recorded and what pupils should look for. Do not invent expected results; distinguish predictions from actual observations.

### OUTPUT FORMAT
Question; prediction; schedule; observation criteria; recording template; vocabulary; analysis prompts; conclusion criteria; practical notes.

### QUALITY CHECKS
Ensure every observation is feasible at the stated intervals and that the recording method can reveal meaningful change.

### OPTIONAL CUSTOMISATION
Adapt for germination, seasonal change, shadows, weather, decomposition or other curriculum-appropriate phenomena.

### Example Input
Year 2; phenomenon: seed germination; period: 14 days; interval: every two days; equipment: seeds, containers and ruler.

### Example Output
Use consistent observation intervals and record visible changes such as root or shoot emergence without presenting a predicted sequence as if it were observed fact.

---

## WS-05 — Pattern-Seeking Investigation

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS2, Science, Working Scientifically, Pattern Seeking, Data

### Editable Variables
`[YEAR_GROUP]` | `[TOPIC]` | `[VARIABLES]` | `[AVAILABLE_DATA]` | `[CONSTRAINTS]`

### ROLE
Act as an experienced primary science teacher specialising in evidence-based data interpretation.

### CONTEXT
Create a pattern-seeking investigation for `[YEAR_GROUP]` on `[TOPIC]` using `[VARIABLES]`, `[AVAILABLE_DATA]` and `[CONSTRAINTS]`.

### TASK
Design an investigation that helps pupils identify, describe and test patterns in observations or measurements.

### REQUIREMENTS
Define the data to collect or analyse, an appropriate table or graph, pattern prompts and limitations. Distinguish a pattern or association from a causal claim. Where useful, include anomalous or incomplete data for discussion.

### OUTPUT FORMAT
Question; data requirements; method; table/graph; pattern prompts; interpretation; limitations; teacher questions; answers.

### QUALITY CHECKS
Verify the data structure and any supplied values. Ensure pupils are not led to infer causation from correlation alone.

### OPTIONAL CUSTOMISATION
Adapt for temperature, shadows, materials, forces, habitats or other suitable primary science contexts.

### Example Input
Year 6; topic: shadows; variables: time and shadow length; available data: measurements taken hourly; constraints: 30-minute analysis lesson.

### Example Output
Plot time against shadow length, ask pupils to describe the observed pattern and require them to distinguish that pattern from a claim about why the pattern occurs.

---

## WS-06 — Classification Investigation

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Science, Working Scientifically, Classification, Identification

### Editable Variables
`[YEAR_GROUP]` | `[OBJECTS_OR_LIVING_THINGS]` | `[OBSERVABLE_CHARACTERISTICS]` | `[CLASSIFICATION_PURPOSE]`

### ROLE
Act as a primary science teacher specialising in classification and identification.

### CONTEXT
Create a classification activity for `[YEAR_GROUP]` using `[OBJECTS_OR_LIVING_THINGS]` and `[OBSERVABLE_CHARACTERISTICS]` for `[CLASSIFICATION_PURPOSE]`.

### TASK
Design a classification investigation in which pupils identify useful characteristics, group examples and, where appropriate, construct or use a simple identification key.

### REQUIREMENTS
Make classification criteria explicit. Require pupils to justify grouping decisions and revise the classification if new evidence challenges the original grouping. Avoid appearance-only criteria where they do not reliably distinguish groups.

### OUTPUT FORMAT
Starting set; characteristics; classification criteria; groups; key; pupil task; answers; discussion questions; extension.

### QUALITY CHECKS
Every classification decision must follow the stated characteristics and terminology. Check that the key leads consistently to the intended identification.

### OPTIONAL CUSTOMISATION
Adapt for rocks, materials, plants, animals, habitats or classroom objects.

### Example Input
Year 4; living things: frog, eagle, dolphin, lizard, beetle; characteristics: body features; purpose: identify broad animal groups.

### Example Output
Construct a branching key using relevant characteristics and ask pupils to explain why each organism follows its particular route.

---

## WS-07 — Secondary-Source Research Planner

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS2, Science, Working Scientifically, Research, Information Literacy

### Editable Variables
`[YEAR_GROUP]` | `[SCIENCE_QUESTION]` | `[SOURCE_TYPES]` | `[LESSON_TIME]` | `[ACCESS_NEEDS]`

### ROLE
Act as a primary science and information-literacy specialist.

### CONTEXT
Plan a research activity for `[YEAR_GROUP]` answering `[SCIENCE_QUESTION]`, using `[SOURCE_TYPES]` within `[LESSON_TIME]` and considering `[ACCESS_NEEDS]`.

### TASK
Create a research workflow that helps pupils locate relevant information, assess sources, record evidence and synthesise findings without confusing source claims with their own inference.

### REQUIREMENTS
Provide search terms, source-selection criteria, note-taking structure, comparison questions and age-appropriate citation guidance. Do not invent source findings, quotations or citations. Distinguish what pupils can verify from what requires teacher review.

### OUTPUT FORMAT
Question; search terms; source checklist; note-taking template; evidence table; synthesis questions; citation guidance; teacher checks.

### QUALITY CHECKS
Ensure proposed sources are appropriate for the age group and question. Do not fabricate references or claim that a source says something unless its content has actually been checked.

### OPTIONAL CUSTOMISATION
Adapt for independent research, paired research, guided source packs or EAL/SEND access needs.

### Example Input
Year 6; question: How has human activity affected a local habitat?; sources: council, museum and environmental organisation websites; time: 60 minutes.

### Example Output
Give pupils focused search terms and a source-evidence table requiring them to record the claim, source and evidence before drawing a conclusion.

---

## WS-08 — Data Recording Template

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 500–800 words  
**Curriculum Tags:** KS1, KS2, Science, Working Scientifically, Data Recording

### Editable Variables
`[YEAR_GROUP]` | `[ENQUIRY]` | `[MEASUREMENTS]` | `[DATA_VOLUME]` | `[UNITS]`

### ROLE
Act as a primary science teacher specialising in clear evidence recording.

### CONTEXT
Create a recording structure for `[YEAR_GROUP]` pupils investigating `[ENQUIRY]`, with `[MEASUREMENTS]`, approximately `[DATA_VOLUME]` observations and units of `[UNITS]`.

### TASK
Design a table, tally, annotated observation record or other appropriate format that makes the evidence easy to record accurately and analyse.

### REQUIREMENTS
Use meaningful headings, appropriate units, enough rows or categories and a clear distinction between qualitative observations and quantitative measurements. Include one worked example entry without fabricating investigation results.

### OUTPUT FORMAT
Teacher instructions; pupil template; headings; units; example entry; recording guidance; analysis prompts; common recording errors.

### QUALITY CHECKS
Check headings, units, categories and number of columns against the actual enquiry. Ensure the example does not accidentally imply a predetermined result.

### OPTIONAL CUSTOMISATION
Adapt for KS1 pictorial recording, KS2 tables, repeated trials or group data collection.

### Example Input
Year 5; enquiry: parachute descent; measurements: canopy material and descent time; data volume: five trials per material; units: seconds.

### Example Output
Create columns for material and trials 1–5, followed by an appropriate summary field if justified, with seconds clearly stated and space for relevant observations.

---

## WS-09 — Conclusion and Evidence Builder

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Science, Working Scientifically, Conclusions, Evidence

### Editable Variables
`[YEAR_GROUP]` | `[QUESTION]` | `[DATA]` | `[PREDICTION]` | `[KNOWN_LIMITATIONS]`

### ROLE
Act as a primary science assessment specialist who teaches evidence-based conclusions.

### CONTEXT
Help `[YEAR_GROUP]` pupils interpret `[DATA]` in relation to `[QUESTION]` and `[PREDICTION]`, considering `[KNOWN_LIMITATIONS]`.

### TASK
Guide pupils from the supplied evidence to a conclusion while clearly separating what the data show from explanations or claims that go beyond the evidence.

### REQUIREMENTS
Identify relevant trends, comparisons or observations; select specific evidence; evaluate the prediction; identify a limitation where justified; and propose a useful next question. Do not manufacture missing values.

### OUTPUT FORMAT
What the data show; evidence statements; conclusion; relation to prediction; limitation; confidence/uncertainty; next question; teacher prompts.

### QUALITY CHECKS
Every conclusion must be supported by the supplied data. Flag where the evidence is insufficient to answer the question confidently.

### OPTIONAL CUSTOMISATION
Adapt for KS1 oral conclusions, KS2 written conclusions, tables, charts or comparative investigations.

### Example Input
Year 5; question: Which material absorbed the most water?; data: three repeated measurements per material; prediction: cotton; known limitation: inconsistent sample sizes.

### Example Output
Require pupils to cite the relevant measurements, state whether the evidence supports the prediction and recognise that unequal sample sizes weaken the comparison.

---

## WS-10 — Enquiry Evaluation and Improvement

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS2, Science, Working Scientifically, Evaluation, Reliability

### Editable Variables
`[YEAR_GROUP]` | `[QUESTION]` | `[METHOD]` | `[RESULTS]` | `[LIMITATIONS]`

### ROLE
Act as an experienced primary science teacher specialising in enquiry evaluation.

### CONTEXT
Evaluate a completed investigation for `[YEAR_GROUP]`. The question is `[QUESTION]`; method is `[METHOD]`; results are `[RESULTS]`; known limitations are `[LIMITATIONS]`.

### TASK
Identify strengths and limitations in the enquiry and recommend one or more feasible improvements that would improve the quality, reliability or validity of the evidence.

### REQUIREMENTS
Base evaluation on the actual method and results. Distinguish improvements to measurement, consistency, sample size, controls, timing or recording from changes that create a different investigation. Explain the expected effect of each improvement.

### OUTPUT FORMAT
Question; strengths; limitations; evidence; priority improvement; rationale; expected effect; further question; pupil reflection prompts.

### QUALITY CHECKS
Do not recommend changes that alter the research question unless explicitly identified as a new investigation. Ensure each improvement is practical and connected to a real limitation.

### OPTIONAL CUSTOMISATION
Adapt for pupil self-evaluation, group critique, teacher-led discussion or written scientific evaluation.

### Example Input
Year 6; question: Does ramp height affect car travel distance?; method: three ramp heights, one trial each; results: recorded distances; limitation: only one trial per height.

### Example Output
Prioritise repeated trials at each height, explain that this provides more evidence about consistency, and distinguish this from changing the variable or question.