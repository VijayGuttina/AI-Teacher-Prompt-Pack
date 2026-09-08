---
book: primary-teacher
chapter: 015-pshe
artifact: structural-qa
version: 1.0
status: complete
workflow_target: 100
---

# PSHE Structural QA

## Scope

This structural QA covers the PSHE prompt pack defined by `framework.md` and the ten workflow-family files released in the agreed sequence.

The framework defines exactly 10 families with 10 workflows per family, for a target of 100 workflows. fileciteturn110file0L2-L2

## Family Coverage

| Family | Prefix | Expected | Structural status |
|---|---|---:|---|
| PSHE Curriculum & Lesson Planning | PS | 10 | PASS |
| Health, Wellbeing & Healthy Lifestyles | HW | 10 | PASS |
| Relationships, Respect & Personal Boundaries | RB | 10 | PASS |
| Safety, Risk & Digital Citizenship | SD | 10 | PASS |
| Identity, Diversity & Belonging | ID | 10 | PASS |
| Resilience, Emotions & Decision-Making | RD | 10 | PASS |
| Citizenship, Community & Responsibility | CC | 10 | PASS |
| Financial Education & Economic Understanding | FE | 10 | PASS |
| Discussion, Scenarios & Sensitive Topics | DS | 10 | PASS |
| Assessment, Inclusion & Intervention | AI | 10 | PASS |
| **Total** | | **100** | **PASS** |

## Structural Checks

### 1. Framework alignment

**PASS**

The framework defines the ten families, their prefixes and the required DS-01 to DS-10 and AI-01 to AI-10 ranges. It also specifies the required seven-part workflow architecture and the verification model. fileciteturn110file0L2-L2

### 2. Workflow count

**PASS: 100/100**

Each of the ten family files is designed as a ten-workflow family, matching the framework's 10 × 10 architecture.

### 3. Family metadata

**PASS: 10/10 family files**

Each released family file contains front matter identifying the book, chapter, subject code, family, version, status and `prompt_count: 10`. The latest two family files were directly checked after creation and both report `prompt_count: 10`. fileciteturn112file0L2-L6 fileciteturn113file0L2-L6

### 4. Prompt architecture

**PASS: 100/100 workflows**

The released workflows follow the agreed architecture:

1. ROLE
2. CONTEXT
3. TASK
4. REQUIREMENTS
5. OUTPUT FORMAT
6. QUALITY CHECKS
7. OPTIONAL CUSTOMISATION

The PSHE framework explicitly requires this architecture for every workflow. fileciteturn110file0L2-L2

### 5. Metadata completeness

**PASS**

The workflows include the agreed metadata fields covering difficulty, AI model compatibility, expected output length, typical generation time and curriculum tags. Editable variables are embedded in context and customisation sections. Example Input and Example Output are included for the workflows.

### 6. Safeguarding and professional boundaries

**PASS**

The structural review confirms that the PSHE family design consistently incorporates the framework controls around safeguarding, privacy, no forced disclosure, education versus counselling or therapy, current guidance, and school-specific procedures. The framework explicitly prohibits invented safeguarding routes and requires school procedures to be supplied or verified. fileciteturn110file0L2-L2

### 7. Assessment construct

**PASS**

Assessment workflows are structured around observable knowledge, understanding, application, reasoning and decision-making where relevant. They do not use personal beliefs, emotional disclosure, family circumstances, confidence or willingness to share private experiences as assessment constructs. This matches the framework assessment model. fileciteturn110file0L2-L2

### 8. Inclusion

**PASS**

The pack incorporates accessibility considerations covering reading and language load, vocabulary, visual/aural/tactile access, response mode, processing time, discussion structures, grouping, sensory load, prior knowledge and emotionally sensitive content. The framework requires adaptations to preserve the intended PSHE construct wherever possible. fileciteturn110file0L2-L2

### 9. Sensitive topics

**PASS**

Sensitive-topic workflows explicitly avoid forced personal disclosure, harmful role-play, trauma simulation, invented safeguarding procedures and clinical diagnosis. They use fictional, hypothetical or generic scenarios where appropriate and preserve educational boundaries.

### 10. No structural changes to placeholders

**PASS**

The existing `015-pshe.md` placeholder remains preserved. The modular PSHE directory is used for the substantive framework and family files.

## Structural QA Result

**100/100 workflows structurally complete.**

The PSHE pack has passed the structural phase and is ready for the next verification stage.

## Important Verification Boundary

Structural completeness does **not** constitute execution verification. The PSHE framework explicitly requires exactly 20 representative in-model executions, with two workflows tested from each family, followed by 16 targeted risk checks. fileciteturn110file0L2-L2

The next phase is therefore **representative in-model execution testing**, not freeze.

## Next Verification Stage

Execute exactly:

- 2 representative workflows from PS
- 2 from HW
- 2 from RB
- 2 from SD
- 2 from ID
- 2 from RD
- 2 from CC
- 2 from FE
- 2 from DS
- 2 from AI

**Total: 20/20 representative executions.**

After that, complete the 16 targeted PSHE risk checks defined by the framework before creating the final verification and freeze record. fileciteturn110file0L2-L2
