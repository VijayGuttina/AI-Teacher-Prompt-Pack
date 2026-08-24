# Primary Mathematics Framework

This framework is the subject-specific operating layer for the Primary Mathematics Workflow Library. It inherits from the Global Prompt Standard, Master Prompt Framework and Primary Teacher Framework.

## Purpose

Generate practical, curriculum-aware mathematics workflows that help primary teachers plan, teach, assess, diagnose misconceptions, adapt instruction and develop mathematical reasoning.

## Core principles

1. **Mathematical intent before activity** — every workflow starts with the intended mathematical knowledge, skill or reasoning outcome.
2. **Representation matters** — use concrete, pictorial and abstract representations where they genuinely improve understanding.
3. **Fluency, reasoning and problem solving are connected** — do not treat them as isolated lesson types.
4. **Precision matters** — mathematical notation, terminology, calculations and examples must be checked.
5. **Misconceptions are evidence-led** — distinguish what a pupil has actually demonstrated from a hypothesis about why an error occurred.
6. **Variation should be purposeful** — vary examples to expose mathematical structure, not simply to create more questions.
7. **Cognitive demand should be preserved during adaptation** — accessibility support should remove unnecessary barriers without automatically reducing mathematical thinking.
8. **Age and prior knowledge matter** — outputs must be appropriate to the stated year group and prerequisite knowledge.
9. **British curriculum context** — where a curriculum is specified, align with the National Curriculum for England or the supplied school sequence rather than inventing curriculum requirements.
10. **No false precision** — if the input does not establish a curriculum expectation, model or pupil misconception, state the limitation rather than inventing evidence.

## Mathematical workflow categories

The library is organised by teacher job-to-be-done:

- Number and place value
- Calculation and fluency
- Fractions, decimals and percentages
- Geometry and measure
- Problem solving and reasoning
- Statistics and data
- Assessment and diagnosis
- Intervention and adaptive teaching

## Required workflow behaviour

Every mathematics workflow should, where relevant:

- identify the mathematical objective;
- identify prerequisite knowledge;
- use mathematically accurate examples;
- distinguish answer accuracy from reasoning quality;
- include representations where useful;
- expose likely misconceptions where relevant;
- provide answer keys or teacher checking guidance for generated practice;
- avoid ambiguous questions unless ambiguity is the deliberate teaching point;
- verify calculations before presenting them;
- distinguish procedural fluency from conceptual understanding;
- include challenge through mathematical depth rather than merely larger numbers.

## Quality gate

Before returning an output, check:

1. Is every calculation correct?
2. Are units and notation consistent?
3. Is the terminology mathematically accurate?
4. Are examples valid for the stated objective?
5. Are representations consistent with the mathematics?
6. Could a pupil reasonably interpret an item in more than one way?
7. Does the task test the intended mathematics rather than reading complexity or irrelevant context?
8. If diagnosing an error, is the proposed cause supported by the supplied evidence?
9. If adapting the task, has the intended mathematical demand been preserved?
10. Are answer keys complete and independently checked?

## AI verification

Mathematics workflows must be tested against the recorded model before publication. Verification must include at least one representative input, calculation checking and output-quality review. Published metadata should record the exact model, test date, result and next review date.

## Worked examples

The published Mathematics book should include worked examples by workflow category showing:

1. Teacher input
2. Workflow used
3. Representative AI output
4. Why the output is useful
5. What the teacher must check or customise

Worked examples should demonstrate quality rather than inflate the page count.
