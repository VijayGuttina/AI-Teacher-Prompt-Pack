# Primary Art & Design Framework

## Purpose

This module provides reusable AI-assisted teacher workflows for planning, teaching, assessing and adapting primary Art & Design. It is organised around genuine classroom workflows rather than isolated prompt variations.

## Design principles

Every workflow must:

1. preserve artistic intent and pupil agency;
2. distinguish observation from interpretation and historical/contextual fact;
3. avoid inventing artist quotations, provenance, artwork details or visual evidence;
4. use supplied artwork descriptions, images or verified contextual information where specificity matters;
5. support experimentation rather than prescribing a single 'correct' aesthetic outcome;
6. make success criteria explicit without forcing uniformity of pupil work;
7. adapt access while preserving the intended artistic or design decision-making;
8. separate observed evidence in pupil work from evaluative inference;
9. account for practical materials, equipment and age-appropriate safety;
10. treat generated visual ideas as starting points for teacher review, not unquestionable curriculum content.

## Workflow architecture

The initial release contains 10 workflow families, each with 10 workflows:

| Family | IDs | Core purpose |
|---|---|---|
| Art Enquiry & Curriculum Planning | AE-01–AE-10 | Questions, sequences, objectives and success criteria |
| Drawing, Mark-Making & Observation | DM-01–DM-10 | Observation, technique, modelling and progression |
| Colour, Painting & Printmaking | CP-01–CP-10 | Colour, media exploration and process planning |
| Sculpture, Form & 3D Construction | SF-01–SF-10 | Materials, form, joining and evaluation |
| Textiles, Collage & Mixed Media | TM-01–TM-10 | Surface, texture, combination and experimentation |
| Artists, Craft Makers & Context | AC-01–AC-10 | Contextual study without fabricated attribution |
| Evaluation, Critique & Artistic Vocabulary | EV-01–EV-10 | Reflection, critique, vocabulary and conceptual understanding |
| Sketchbooks, Creative Process & Progression | SK-01–SK-10 | Process evidence, experimentation and development |
| Assessment, Misconceptions & Intervention | AMI-01–AMI-10 | Evidence-led assessment and responsive teaching |
| Inclusion, Adaptation & Classroom Implementation | IA-01–IA-10 | Access, participation, resources and safe implementation |

**Target workflow count: 100.**

## Core quality gates

### Artistic integrity
AI must not present one aesthetic response as objectively correct where the task calls for creative choice. Technical criteria may be explicit, but artistic outcomes should remain open where appropriate.

### Visual evidence discipline
When analysing an artwork or pupil work, conclusions must be grounded in supplied visual evidence. If no image or reliable description is available, the output must state its limitation rather than invent details.

### Contextual accuracy
Artist information, cultural context, quotations, titles, dates and provenance must not be fabricated. Uncertain or unsupplied information should be labelled accordingly.

### Process over imitation
Workflows should prioritise observation, experimentation, decision-making and reflection. They must not reduce artist study to mechanical style copying.

### Assessment discipline
Assessment should distinguish observable evidence from inference and should identify the next useful teaching action rather than simply assigning generic praise or labels.

### Adaptation discipline
Adaptations may change representation, scaffolding, materials or communication routes, but should preserve the intended artistic decision or learning construct wherever possible.

## Verification model

Structural QA, representative execution testing and targeted spot checks are separate stages. Authorship does not constitute model testing. Subject freeze requires recorded representative execution evidence and risk-based spot checks.

## Release sequence

1. Framework
2. Workflow-family architecture
3. Compact workflow modules
4. Structural QA
5. Verification register and execution test plan
6. Worked examples
7. Representative execution and remediation
8. Targeted spot checks
9. Subject freeze
