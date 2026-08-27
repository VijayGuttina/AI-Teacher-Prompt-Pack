# Primary Art & Design Execution Test Plan

**Date:** 27 August 2026  
**Model:** GPT-5.6 Luna  
**Purpose:** Define the representative execution pass before Art & Design can be verified and frozen.

## Testing principle

The 100 workflows will not be individually executed as a substitute for a meaningful QA strategy. Testing will use representative workflows across all ten families plus targeted checks for Art & Design's highest-risk failure modes. Any material systemic defect will trigger remediation and re-testing of the affected family.

## Representative execution matrix

| Family | Representative workflows | Primary test focus |
|---|---|---|
| AE | AE-01, AE-07 | curriculum coherence; evidence-led unit diagnosis |
| DM | DM-01, DM-06 | observation; technique diagnosis |
| CP | CP-01, CP-05 | colour concepts; printmaking method/safety |
| SF | SF-02, SF-06 | construction technique; structural diagnosis |
| TM | TM-02, TM-06 | textile technique; mixed-media diagnosis |
| AC | AC-01, AC-05 | factual context; artistic-intent uncertainty |
| EV | EV-02, EV-08 | critique; criterion-based moderation |
| SK | SK-01, SK-05 | process evidence; progression judgement |
| AMI | AMI-03, AMI-09 | assessment evidence; construct-valid adaptation |
| IA | IA-01, IA-08 | access adaptation; meaningful challenge |
| **Total** | **20 workflows** | **All families represented** |

## Risk-based test scenarios

### 1. Artistic agency
Provide open-ended making tasks and check that the output does not prescribe a single aesthetically correct result where the objective allows legitimate choice.

### 2. Visual evidence discipline
Ask for analysis without supplying an image or reliable artwork description. The model must state the limitation rather than inventing visual details.

### 3. Artist/context accuracy
Use a named artist/context task and inspect whether the model distinguishes supplied/known facts from uncertain claims and avoids fabricated quotations, dates, titles or provenance.

### 4. Observation vs interpretation
Use artwork and pupil-work descriptions containing ambiguous evidence. The output must separate what is observed from what is inferred.

### 5. Technical/material accuracy
Test technique and material recommendations for plausibility, age appropriateness and classroom safety.

### 6. Diagnostic discipline
Provide pupil work evidence that could support several explanations. The workflow must propose a discriminating check rather than asserting motivation, effort or ability.

### 7. Assessment construct validity
Test whether assessment criteria measure the stated art knowledge/skill/decision-making rather than conformity, neatness or personal taste.

### 8. Inclusion and adaptation
Test SEND/EAL adaptations. The workflow should remove access barriers while preserving the intended artistic construct and agency where possible.

### 9. Challenge
Test secure pupils. Increased challenge should involve deeper artistic thinking, refinement, experimentation or justification rather than simply more work.

### 10. Practical implementation
Check resources, setup, tool use, cleanup, timing and safety for classroom feasibility.

## Pass criteria

A representative execution passes only when it is:

- factually and technically defensible;
- faithful to the supplied curriculum intent;
- explicit about uncertainty and missing evidence;
- free of fabricated artwork/contextual details;
- respectful of legitimate artistic variation;
- evidence-led when diagnosing or assessing pupils;
- construct-preserving when adapting tasks;
- practically feasible and appropriately safety-conscious;
- sufficiently specific to be directly useful to a teacher.

## Failure handling

A material failure must be classified as one of:

- factual/contextual error;
- technical/material error;
- fabricated evidence or attribution;
- artistic-agency failure;
- diagnostic/assessment inference failure;
- construct-validity failure;
- inclusion/adaptation failure;
- practical/safety failure;
- output usability failure.

The affected workflow and any common framework rule must be remediated before verification continues.

## Verification boundary

Completion of this plan does not itself establish verification. The execution results must be recorded separately, reviewed, and followed by targeted spot checks before the subject is frozen.
