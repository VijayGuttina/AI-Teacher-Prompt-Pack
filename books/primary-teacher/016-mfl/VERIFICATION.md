# MFL Workflow Verification Register

**Verification date:** 9 September 2026  
**Verifier:** GPT-5.6 Luna  
**Verification stage:** Structural QA  
**Status:** Structural QA passed. Representative execution testing and targeted risk testing remain outstanding.

## Important distinction

This register records the release-gate stages for the MFL module. Passing structural QA does not mean that all workflows have been execution-verified. Representative in-model execution testing and targeted MFL risk checks must pass before the module can be marked frozen.

## Structural QA criteria

Each workflow must contain:

1. A unique workflow ID within its family.
2. A clear job-to-be-done.
3. The agreed prompt architecture:
   - ROLE
   - CONTEXT
   - TASK
   - REQUIREMENTS
   - OUTPUT FORMAT
   - QUALITY CHECKS
   - OPTIONAL CUSTOMISATION
4. Required metadata.
5. Editable variables appropriate to the workflow.
6. Example Input.
7. Example Output excerpt.
8. MFL-specific accuracy and safety controls appropriate to the workflow.
9. A practical teacher-facing output.
10. No unnecessary dependency on unspecified school or language information.

## Results

| Family | Workflow range | Expected | Structural QA | Status |
|---|---|---:|---:|---|
| MFL Curriculum & Lesson Planning | MF-01 to MF-10 | 10 | 10/10 | Passed |
| Listening, Speaking & Classroom Interaction | LS-01 to LS-10 | 10 | 10/10 | Passed |
| Phonics, Pronunciation & Spelling | PP-01 to PP-10 | 10 | 10/10 | Passed |
| Vocabulary, Retrieval & Language Chunks | VR-01 to VR-10 | 10 | 10/10 | Passed |
| Grammar, Sentence Building & Accuracy | GR-01 to GR-10 | 10 | 10/10 | Passed |
| Reading, Writing, Translation & Mediation | RT-01 to RT-10 | 10 | 10/10 | Passed |
| Culture, Communities & Intercultural Understanding | CC-01 to CC-10 | 10 | 10/10 | Passed |
| Progression, Assessment & Feedback | PA-01 to PA-10 | 10 | 10/10 | Passed |
| Inclusion, SEND, EAL & Adaptive Teaching | IA-01 to IA-10 | 10 | 10/10 | Passed |
| Resources, Authentic Materials & Curriculum Implementation | RA-01 to RA-10 | 10 | 10/10 | Passed |
| **Total** | **MF-01 to RA-10** | **100** | **100/100** | **Passed** |

## Framework integrity checks

- Framework defines exactly 10 workflow families.
- Each family defines exactly 10 workflows.
- Workflow identifiers run consecutively from 01 to 10 within each family.
- No CP family has been introduced.
- The existing `books/primary-teacher/016-mfl.md` placeholder remains preserved.
- The 10 family files remain in the established modular directory.
- Target-language placeholders and missing-information controls are part of the framework and relevant workflow specifications.
- MFL-specific controls cover language accuracy, pronunciation, phonics, vocabulary, grammar, four language skills, translation, mediation, intercultural understanding, inclusion, assessment, resources and safe classroom implementation.

## Structural quality assessment

**100/100 workflows passed structural QA.**

The module is structurally complete and ready for the next release gate. No structural defects were identified that require changes before execution testing.

## Outstanding verification gates

### Representative in-model execution testing

Exactly 20 workflows must be executed in the current GPT-5.6 Luna context, with two workflows selected from each family. Tests must assess whether the prompts actually produce useful, accurate and classroom-ready outputs, rather than merely checking that the prompt text is complete.

### Targeted MFL risk checks

The following 16 checks remain outstanding:

1. Target-language accuracy
2. Pronunciation and phonics accuracy
3. Vocabulary meaning and register
4. Grammar accuracy and progression
5. Listening and speaking construct validity
6. Reading, writing, translation and mediation construct validity
7. Appropriate use of authentic materials
8. Cultural and intercultural accuracy
9. Avoidance of cultural and national stereotypes
10. Distinction between language, nationality, ethnicity and culture
11. Age and developmental appropriateness
12. Inclusion, SEND and EAL accessibility
13. Avoidance of pronunciation fossilisation and poor phonetic respelling
14. Appropriate assessment and feedback
15. Digital/resource safety, copyright and privacy where relevant
16. Safe handling of missing language, syllabus and local-school information

## Publication status

**Structural status: PASS, 100/100.**  
**Representative execution status: Pending.**  
**Targeted risk status: Pending.**  
**Final module freeze: Not yet authorised.**

## Next step

Proceed to exactly 20 representative in-model executions, two workflows per MFL family. After those pass, run the 16 targeted MFL risk checks and then update this register with the final verification and freeze decision.
