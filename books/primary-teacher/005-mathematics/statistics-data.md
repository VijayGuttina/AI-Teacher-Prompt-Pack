# Statistics and Data Workflows

## SD-01 — Statistics Lesson

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 700–1,000 words  
**Curriculum Tags:** KS1, KS2, Statistics, Data, Lesson Planning

### Editable Variables
`[YEAR_GROUP]` | `[OBJECTIVE]` | `[DATA_SET]` | `[REPRESENTATION]` | `[DURATION]`

### ROLE
Act as an experienced primary mathematics teacher and statistics subject specialist.

### CONTEXT
Plan a lesson for `[YEAR_GROUP]` around `[OBJECTIVE]`, using `[DATA_SET]`, `[REPRESENTATION]` and `[DURATION]`.

### TASK
Create a coherent sequence from prior knowledge through data construction, interpretation and reasoning.

### REQUIREMENTS
Use a mathematically meaningful data context. Include questions requiring pupils to interpret relationships, not merely read values. Keep data, scale and representation appropriate to the year group.

### OUTPUT FORMAT
Objective; prior knowledge; key concept; data set; representation; teacher modelling; guided questions; independent task; answers; reasoning; misconceptions; formative assessment.

### QUALITY CHECKS
Verify every data value, total, calculation, scale and conclusion. Ensure the representation is appropriate for the data type.

### OPTIONAL CUSTOMISATION
Adapt for collecting data, interpreting existing data or comparing representations.

### Example Input
Year 4; objective: interpret data in tables and bar charts; data set: favourite fruits; representation: table and bar chart; 60 minutes.

### Example Output
Move from a reconciled frequency table to a correctly scaled bar chart, then ask comparison, difference and “what can we conclude?” questions rather than limiting pupils to value retrieval.

---

## SD-02 — Tables and Tally Charts

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Statistics, Tables, Tally Charts

### Editable Variables
`[YEAR_GROUP]` | `[DATA_CATEGORIES]` | `[DATA_VALUES]` | `[CONTEXT]` | `[DIFFICULTY]`

### ROLE
Act as a primary mathematics specialist teaching data collection and frequency representation.

### CONTEXT
Create a task for `[YEAR_GROUP]` using `[DATA_CATEGORIES]`, `[DATA_VALUES]` and `[CONTEXT]` at `[DIFFICULTY]` level.

### TASK
Generate or analyse a tally chart and frequency table, then develop questions requiring pupils to use the data meaningfully.

### REQUIREMENTS
Make tally conventions and totals explicit. Ensure categories are mutually appropriate and frequencies reconcile with the source data. Include at least one question requiring comparison or inference.

### OUTPUT FORMAT
Context; raw data; tally/table; questions; answers; reasoning prompts; misconception; extension.

### QUALITY CHECKS
Recalculate all frequencies and totals independently. Check that every raw observation is represented exactly once where the categories require it.

### OPTIONAL CUSTOMISATION
Adapt for pupil-collected data, pre-prepared data or assessment.

### Example Input
Year 3; categories: transport to school; values: 20 pupil responses; context: class survey; medium difficulty.

### Example Output
Provide a raw response list, a completed tally/frequency table and questions that require pupils to verify the total and compare categories.

---

## SD-03 — Bar Charts and Pictograms

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Statistics, Bar Charts, Pictograms

### Editable Variables
`[YEAR_GROUP]` | `[DATA_SET]` | `[SCALE]` | `[CHART_TYPE]` | `[CONTEXT]`

### ROLE
Act as an experienced primary mathematics teacher specialising in accurate data representation.

### CONTEXT
Create a `[CHART_TYPE]` task for `[YEAR_GROUP]` using `[DATA_SET]`, with `[SCALE]` and `[CONTEXT]`.

### TASK
Design construction and interpretation activities requiring pupils to understand the scale, key and correspondence between data and representation.

### REQUIREMENTS
Make the scale or pictogram key explicit. Include questions about comparison, difference and totals where appropriate. Do not use a misleading or unnecessarily complex scale.

### OUTPUT FORMAT
Data; chart specification; construction instructions; interpretation questions; answers; misconception; reasoning; extension.

### QUALITY CHECKS
Verify every scale interval, bar height, symbol value and comparison.

### OPTIONAL CUSTOMISATION
Adapt for pictograms with whole symbols or partial symbols only where curriculum-appropriate.

### Example Input
Year 4; data: books read by five pupils; scale: 2 books per interval; chart type: bar chart; context: reading survey.

### Example Output
Specify the axis, equal intervals and labels, then include a comparison requiring pupils to calculate the difference between two categories rather than simply identify the taller bar.

---

## SD-04 — Line Graphs

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS2, Statistics, Line Graphs, Continuous Data

### Editable Variables
`[YEAR_GROUP]` | `[DATA_CONTEXT]` | `[TIME_INTERVALS]` | `[VALUES]` | `[DIFFICULTY]`

### ROLE
Act as a primary mathematics specialist with expertise in data representation.

### CONTEXT
Create a line-graph activity for `[YEAR_GROUP]` using `[DATA_CONTEXT]`, `[TIME_INTERVALS]`, `[VALUES]` and `[DIFFICULTY]`.

### TASK
Design a line graph only where ordered change over an interval or time makes the representation meaningful, then create interpretation and reasoning tasks.

### REQUIREMENTS
Use an appropriate scale and ordered x-axis. Include questions about trends, differences, changes and interpolation only where justified by the data and curriculum.

### OUTPUT FORMAT
Data; graph specification; construction guidance; interpretation questions; answers; reasoning; misconception; extension.

### QUALITY CHECKS
Verify data ordering, axis labels, intervals, scale and every conclusion. Do not imply continuous values where the data are discrete without justification.

### OPTIONAL CUSTOMISATION
Adapt for temperature, distance, time, rainfall or other curriculum-appropriate contexts.

### Example Input
Year 5; context: temperature across a school day; intervals: hourly; values: supplied; medium difficulty.

### Example Output
Use the ordered measurements to discuss rises, falls and overall change, while avoiding claims that the graph proves what happened between measured points unless interpolation is intended.

---

## SD-05 — Mean or Average Where Curriculum-Appropriate

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS2, Statistics, Average, Data, Reasoning

### Editable Variables
`[YEAR_GROUP]` | `[DATA_SET]` | `[AVERAGE_TYPE]` | `[DIFFICULTY]` | `[OBJECTIVE]`

### ROLE
Act as an experienced primary mathematics teacher who uses statistical terminology precisely.

### CONTEXT
Create an activity for `[YEAR_GROUP]` using `[DATA_SET]`, `[AVERAGE_TYPE]`, `[DIFFICULTY]` and `[OBJECTIVE]`, but only where the supplied curriculum context supports the concept.

### TASK
Teach or practise the intended average concept and connect the calculation to the data's meaning.

### REQUIREMENTS
Define the measure precisely and distinguish it from other summaries where necessary. Include interpretation and reasoning, not calculation alone. If the concept is outside the intended year-group curriculum, flag that and substitute an appropriate curriculum concept.

### OUTPUT FORMAT
Curriculum check; concept; worked example; practice; interpretation; reasoning; answers; misconception; extension.

### QUALITY CHECKS
Verify every calculation and use terminology consistently. Check that the resulting value is interpreted sensibly in context.

### OPTIONAL CUSTOMISATION
Adapt for teacher subject knowledge, pupil practice or assessment.

### Example Input
Year 6; data: five scores; average type: mean; objective: understand mean as a representative value; high difficulty.

### Example Output
Show that the mean balances the data around a central value, then ask pupils to predict how changing one score affects the mean before recalculating.

---

## SD-06 — Interpret Misleading or Incomplete Data

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS2, Statistics, Critical Interpretation, Data Literacy

### Editable Variables
`[YEAR_GROUP]` | `[DATA_REPRESENTATION]` | `[ISSUE_TO_EXPOSE]` | `[CONTEXT]` | `[DIFFICULTY]`

### ROLE
Act as a primary mathematics reasoning teacher developing critical data literacy.

### CONTEXT
Create a data representation for `[YEAR_GROUP]` using `[DATA_REPRESENTATION]`, `[ISSUE_TO_EXPOSE]`, `[CONTEXT]` and `[DIFFICULTY]`.

### TASK
Construct a deliberate but age-appropriate interpretive issue and require pupils to identify, explain and correct or qualify the conclusion.

### REQUIREMENTS
The issue must be mathematically defensible, such as an inappropriate scale, missing category, selective data or unsupported conclusion. Teacher notes must explain precisely why it matters.

### OUTPUT FORMAT
Representation; task; intended issue; expected observations; explanation; corrected interpretation; answers; extension.

### QUALITY CHECKS
Ensure the intended issue is genuinely present and not caused accidentally by incorrect arithmetic or inconsistent data.

### OPTIONAL CUSTOMISATION
Adapt for misleading charts, incomplete samples or over-strong conclusions.

### Example Input
Year 6; representation: bar chart; issue: truncated vertical axis; context: comparing two quantities; high difficulty.

### Example Output
Ask pupils whether the visual difference accurately reflects the numerical difference, then require them to explain how the axis presentation affects the apparent comparison.

---

## SD-07 — Data Investigation

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 700–1,000 words  
**Curriculum Tags:** KS2, Statistics, Data Investigation, Enquiry

### Editable Variables
`[YEAR_GROUP]` | `[QUESTION]` | `[VARIABLES]` | `[COLLECTION_METHOD]` | `[TIME_AVAILABLE]`

### ROLE
Act as an experienced primary mathematics teacher designing pupil-led statistical investigations.

### CONTEXT
Plan an investigation for `[YEAR_GROUP]` around `[QUESTION]`, involving `[VARIABLES]`, `[COLLECTION_METHOD]` and `[TIME_AVAILABLE]`.

### TASK
Guide pupils from a testable question through data collection, organisation, representation, analysis and conclusion.

### REQUIREMENTS
Ensure the data collected can actually answer the question. Address sample size, consistency of collection, categories or measurement units where relevant. Include limitations and a distinction between evidence and speculation.

### OUTPUT FORMAT
Investigation question; variables; collection protocol; raw-data structure; representation; analysis questions; expected findings; limitations; conclusion framework; teacher assessment points.

### QUALITY CHECKS
Check feasibility, fairness and consistency of the collection method and verify that the proposed representation matches the data.

### OPTIONAL CUSTOMISATION
Adapt for individual, paired or whole-class investigations.

### Example Input
Year 5; question: Is the number of minutes pupils read each day related to the number of books they finish in a month?; variables: reading time and books; collection method: pupil log; 1 week.

### Example Output
Clarify that a one-week self-reported sample may provide limited evidence and avoid instructing pupils to claim causation from an observed association.

---

## SD-08 — Statistics Misconception Diagnosis

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Statistics, Diagnosis, Assessment

### Editable Variables
`[YEAR_GROUP]` | `[PUPIL_WORK]` | `[DATA_SET]` | `[OBJECTIVE]` | `[RECENT_TEACHING]`

### ROLE
Act as a primary mathematics diagnostic specialist interpreting statistical evidence cautiously.

### CONTEXT
Analyse `[PUPIL_WORK]` from `[YEAR_GROUP]` using `[DATA_SET]` and `[OBJECTIVE]`; recent teaching is `[RECENT_TEACHING]`.

### TASK
Identify observable errors, generate plausible explanations and design a diagnostic check that distinguishes between them.

### REQUIREMENTS
Separate data-entry errors, calculation errors, representation errors, scale misunderstandings and interpretation errors. Do not infer a stable misconception from a single response when other explanations remain plausible.

### OUTPUT FORMAT
Observed evidence; hypotheses; evidence strength; diagnostic question; expected responses; interpretation; targeted teaching; follow-up assessment.

### QUALITY CHECKS
Verify the source data and calculations before diagnosing the pupil's reasoning.

### OPTIONAL CUSTOMISATION
Adapt for individual conferencing, intervention or whole-class formative assessment.

### Example Input
Year 4; pupil reads a bar chart scale of 2 as 1 and reports a bar representing 8 as 4; objective: interpret scaled charts; recent teaching: bar charts.

### Example Output
Test scale understanding using a short contrasting chart before deciding whether the issue is specific to the representation or a broader difficulty with multiplicative scaling.

---

## SD-09 — Data Reasoning Problems

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 700–1,000 words  
**Curriculum Tags:** KS1, KS2, Statistics, Problem Solving, Reasoning

### Editable Variables
`[YEAR_GROUP]` | `[DATA_SET]` | `[REPRESENTATION]` | `[DIFFICULTY]` | `[NUMBER_OF_PROBLEMS]`

### ROLE
Act as an experienced primary problem-solving teacher specialising in statistical reasoning.

### CONTEXT
Create `[NUMBER_OF_PROBLEMS]` for `[YEAR_GROUP]` from `[DATA_SET]` represented as `[REPRESENTATION]` at `[DIFFICULTY]` level.

### TASK
Generate questions requiring comparison, calculation, interpretation, justification, prediction or evaluation from the supplied data.

### REQUIREMENTS
Avoid questions answerable by reading one displayed value when deeper reasoning is intended. Include at least one question where pupils must explain whether a conclusion is supported by the data.

### OUTPUT FORMAT
Data; representation; questions; answers; reasoning guidance; misconception; extension.

### QUALITY CHECKS
Verify every answer against the source data and ensure each question is answerable without hidden assumptions.

### OPTIONAL CUSTOMISATION
Adapt for retrieval, assessment, collaborative reasoning or challenge work.

### Example Input
Year 6; data set: class survey results; representation: table and bar chart; high difficulty; 8 problems.

### Example Output
Include questions requiring pupils to calculate differences, identify totals, compare proportions where curriculum-appropriate and decide whether a stated conclusion is justified by the evidence.

---

## SD-10 — Adapt Statistics Task

**Prompt Difficulty:** Advanced  
**AI Model Compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected Output Length:** 600–900 words  
**Curriculum Tags:** KS1, KS2, Adaptive Teaching, Inclusion, Statistics

### Editable Variables
`[ORIGINAL_TASK]` | `[YEAR_GROUP]` | `[ACCESS_BARRIER]` | `[OBJECTIVE]` | `[EXISTING_SUPPORT]`

### ROLE
Act as an experienced primary mathematics teacher specialising in adaptive teaching and statistical interpretation.

### CONTEXT
The original task is `[ORIGINAL_TASK]` for `[YEAR_GROUP]`. The objective is `[OBJECTIVE]`; the access barrier is `[ACCESS_BARRIER]`; existing support is `[EXISTING_SUPPORT]`.

### TASK
Adapt the task to remove the identified access barrier while preserving the underlying statistical relationship, interpretation and reasoning demand.

### REQUIREMENTS
Consider layout, visual clarity, vocabulary, data volume, chunking and response format. Do not automatically remove data or simplify relationships if doing so changes the construct. Include a route toward independent completion and scaffold fading.

### OUTPUT FORMAT
Original construct; barrier analysis; adapted task; representation; support; independence route; equivalent evidence; mathematical-demand check; review point.

### QUALITY CHECKS
Confirm that pupils still interpret the same statistical relationship and that support does not perform the statistical reasoning for them.

### OPTIONAL CUSTOMISATION
Adapt for SEND, EAL, working-memory, language, motor or sensory access needs.

### Example Input
Year 5; original task: interpret a scaled bar chart and justify which category changed most; barrier: dense written instructions; objective: compare data and explain change; support: visual vocabulary bank.

### Example Output
Retain the same chart and comparison while restructuring instructions into short steps, clarifying statistical vocabulary and allowing concise written or oral justification before fading the support.