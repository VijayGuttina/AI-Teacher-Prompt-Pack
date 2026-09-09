---
book: primary-teacher
chapter: 016-mfl
status: execution-verification
version: 1.0
verification_date: 2026-09-09
verifier: GPT-5.6 Luna
---

# MFL Representative Execution Verification

## Purpose

This record documents representative in-model execution of the MFL prompt library after structural QA. The test set deliberately samples two workflows from each of the ten MFL families, giving coverage of planning, language accuracy, communication, phonics, vocabulary, grammar, literacy, culture, assessment, inclusion and resource implementation.

`Verified` here means the workflow was executed qualitatively in the current model context against the representative input shown below. It does not constitute automated regression testing against external APIs or every supported AI platform.

## Test standard

Each representative execution was checked for:

1. Clear job-to-be-done.
2. Correct use of supplied editable variables.
3. Appropriate primary MFL pedagogy.
4. Target-language accuracy safeguards.
5. Age-appropriate language load.
6. A usable teacher-facing output.
7. Construct-valid assessment where assessment was requested.
8. Appropriate scaffolding and progression.
9. Inclusion and access without unjustified reduction of ambition.
10. No invented school-specific procedures, policies or current facts.

## Results summary

| Family | Workflows tested | Result |
|---|---|---|
| MFL Curriculum & Lesson Planning | MF-01, MF-10 | 2/2 Verified |
| Listening, Speaking & Classroom Interaction | LS-01, LS-10 | 2/2 Verified |
| Phonics, Pronunciation & Spelling | PP-01, PP-10 | 2/2 Verified |
| Vocabulary, Retrieval & Language Chunks | VR-01, VR-10 | 2/2 Verified |
| Grammar, Sentence Building & Accuracy | GR-01, GR-10 | 2/2 Verified |
| Reading, Writing, Translation & Mediation | RT-01, RT-10 | 2/2 Verified |
| Culture, Communities & Intercultural Understanding | CC-01, CC-10 | 2/2 Verified |
| Progression, Assessment & Feedback | PA-01, PA-10 | 2/2 Verified |
| Inclusion, SEND, EAL & Adaptive Teaching | IA-01, IA-10 | 2/2 Verified |
| Resources, Authentic Materials & Curriculum Implementation | RA-01, RA-10 | 2/2 Verified |
| **Total** | **20 workflows** | **20/20 Verified** |

## Representative execution records

### MF-01: Plan an MFL Lesson From a Curriculum Objective

**Input:** Year 4 Spanish; 30 minutes; pupils know greetings and numbers; objective is to ask and answer age; speaking and listening emphasis.

**Execution check:** The workflow produced a coherent lesson sequence beginning with retrieval, followed by teacher modelling, supported listening and speaking practice, communicative pair work, assessment and corrective feedback. The output preserved the distinction between language performance and confidence. Target-language examples were treated as language-specific content rather than generic English substitutions.

**Result:** Verified.

### MF-10: Build a Complete MFL Unit Planning Pack

**Input:** Year 5 French; six lessons; food and preferences; pupils know basic opinions and classroom instructions; weekly 45-minute lessons.

**Execution check:** The workflow produced a unit-level planning structure covering outcomes, vocabulary and chunks, grammar, phonics, four skills, retrieval, cultural context, formative assessment, final assessment, inclusion and preparation. The sequence increased independence rather than simply changing activities each lesson.

**Result:** Verified.

### LS-01: Plan a Listening Comprehension Lesson

**Input:** Year 3 German; 25 minutes; classroom objects; pupils know greetings and numbers; mixed listening confidence.

**Execution check:** The workflow generated picture-supported listening discrimination and comprehension tasks, with repeated exposure and staged support. It did not treat repeating heard language as equivalent to demonstrating listening comprehension. The assessment sampled meaning recognition.

**Result:** Verified.

### LS-10: Build a Complete Listening, Speaking & Classroom Interaction Unit

**Input:** Year 5 Spanish; eight lessons; topic weather and activities; pupils know days, numbers and basic opinions.

**Execution check:** The output linked listening input to structured interaction, information-gap work, supported speaking, retrieval and assessment. Participation routes were varied, and speaking assessment focused on language use and intelligibility rather than accent conformity or personality.

**Result:** Verified.

### PP-01: Plan an MFL Phonics Lesson

**Input:** Year 4 French; pupils know basic greetings; focus on a supplied sound-spelling relationship; 30 minutes.

**Execution check:** The workflow correctly required the language-specific sound-spelling relationship to be supplied or verified before generating teaching examples. It sequenced noticing and discrimination before controlled production and avoided misleading English phonetic respelling.

**Result:** Verified.

### PP-10: Build a Complete Phonics, Pronunciation & Spelling Unit

**Input:** Year 5 Spanish; six lessons; focus on a verified target-language vowel pattern; pupils need reinforcement of spelling and pronunciation.

**Execution check:** The generated sequence connected sound discrimination, pronunciation, spelling, decoding and meaningful language use. It did not collapse spelling difficulty, pronunciation difficulty and general language knowledge into one diagnosis.

**Result:** Verified.

### VR-01: Select High-Value Vocabulary for a Primary MFL Unit

**Input:** Year 4 Italian; topic school and classroom; six lessons; objective is simple descriptions and requests.

**Execution check:** The workflow prioritised useful, reusable vocabulary and language chunks linked to the communicative objective. It avoided producing a large unfiltered noun list and identified where vocabulary should be verified in the target language.

**Result:** Verified.

### VR-10: Build a Complete Vocabulary, Retrieval & Language Chunks Unit

**Input:** Year 5 French; eight lessons; topic hobbies; pupils know basic opinions and days.

**Execution check:** The output used spaced and varied retrieval, moved from word recognition to sentence use, connected vocabulary to communication and included assessment and intervention. It did not treat copying or isolated list recall as sufficient evidence of language use.

**Result:** Verified.

### GR-01: Identify the Grammar Needed for a Primary MFL Unit

**Input:** Year 6 Spanish; topic daily routines; existing knowledge includes basic present-tense sentence patterns.

**Execution check:** The workflow identified only grammar needed to support the stated communication objective, rather than generating an unnecessarily broad grammar syllabus. It separated grammar from vocabulary and pronunciation and flagged language-specific forms for verification.

**Result:** Verified.

### GR-10: Build a Complete Grammar, Sentence Building & Accuracy Unit

**Input:** Year 5 French; six lessons; topic describing people; supplied grammar focus includes adjective agreement.

**Execution check:** The generated unit progressed from modelling and controlled sentence construction to independent use. Agreement examples were treated as language-specific and subject to verification. Assessment focused on meaningful sentence accuracy rather than handwriting or confidence.

**Result:** Verified.

### RT-01: Plan a Primary MFL Reading Comprehension Sequence

**Input:** Year 4 German; short teacher-supplied text about pets; pupils know common animals and simple opinions.

**Execution check:** The workflow distinguished decoding, vocabulary recognition, literal comprehension and simple inference. It used the supplied text rather than falsely presenting generated material as authentic and included an appropriate progression from supported to less-supported reading.

**Result:** Verified.

### RT-10: Build a Complete Reading, Writing, Translation & Mediation Unit

**Input:** Year 6 Spanish; eight lessons; topic travel; pupils know basic questions, opinions and place vocabulary.

**Execution check:** The output integrated reading, short-form writing, age-appropriate translation and purposeful mediation. Translation was treated as meaning and equivalence rather than mechanical word substitution. Mediation involved transferring relevant meaning between languages for a purpose.

**Result:** Verified.

### CC-01: Plan a Culture and Intercultural Understanding Lesson

**Input:** Year 5 French; topic school life; teacher wants pupils to compare two supplied school-life sources without stereotypes.

**Execution check:** The workflow framed culture through evidence and contextualised comparison. It avoided claims that all people in a country behave identically and distinguished language, nationality, region, culture and individual experience.

**Result:** Verified.

### CC-10: Build a Complete Culture and Intercultural Understanding Unit

**Input:** Year 6 Spanish; six lessons; topic regional diversity in Spain; supplied sources from two regions.

**Execution check:** The output used internal diversity as a central organising principle and avoided reducing the country to tourist facts or a single cultural identity. It required source provenance and verification for factual claims and avoided invented quotations or practices.

**Result:** Verified.

### PA-01: Map MFL Progression Across a Year Group

**Input:** Year 3 to Year 6 French; school has supplied end-of-year vocabulary and grammar expectations; weekly lessons.

**Execution check:** The workflow created a cumulative progression map based on increasing ability to recognise, recall, produce, combine, interact, read, write and apply language. It avoided treating completion of topics as equivalent to progression.

**Result:** Verified.

### PA-10: Build a Complete MFL Progression, Assessment & Feedback Cycle

**Input:** Year 5 German; current assessment evidence shows stronger vocabulary recognition than independent sentence production.

**Execution check:** The output used the evidence to identify a specific gap, proposed targeted practice, generated actionable feedback, included reassessment and avoided using confidence or personality as proxies for language attainment.

**Result:** Verified.

### IA-01: Adapt an MFL Lesson for SEND/EAL Access

**Input:** Year 4 Spanish; lesson objective is listening comprehension; supplied access information indicates pupils benefit from visual support, additional processing time and structured response options.

**Execution check:** The workflow preserved the listening construct while adapting access through visual cues, chunking, processing time and response structure. It did not diagnose needs or assume that EAL status indicates lower MFL aptitude.

**Result:** Verified.

### IA-10: Build an Inclusion, SEND, EAL & Adaptive Teaching Unit Plan

**Input:** Year 5 French; mixed prior knowledge; supplied pupil information includes varied reading fluency and one pupil requiring an alternative response route for extended writing.

**Execution check:** The output provided access adaptations while retaining the intended language-learning ambition. It distinguished reading, writing, vocabulary and language-production barriers and did not invent EHCP, SEND or school policy requirements.

**Result:** Verified.

### RA-01: Select Resources for a Primary MFL Learning Objective

**Input:** Year 5 Spanish; objective is listening comprehension of simple descriptions; available resources include teacher-created slides, a supplied textbook extract and a school-approved audio platform.

**Execution check:** The workflow evaluated resources against the objective and construct before recommending them. It distinguished genuinely authentic, teacher-created, adapted and AI-generated material and did not falsely label generated material authentic.

**Result:** Verified.

### RA-10: Build a Complete MFL Resource, Authentic Materials & Curriculum Implementation Toolkit

**Input:** Year 6 French; eight lessons; limited printing; school-approved digital platform; supplied authentic video clip; pupils need repeated retrieval and accessible resources.

**Execution check:** The output created a resource and implementation plan with low-tech fallbacks, provenance checks, copyright awareness, privacy considerations, accessibility, repeated reuse and teacher preparation. It did not invent external links, school permissions or platform restrictions.

**Result:** Verified.

## Overall execution conclusion

**20/20 representative workflows passed qualitative in-model execution testing.**

Coverage is exactly two workflows from each of the ten MFL families. The tests demonstrate that the workflow specifications produce practical outputs while retaining the framework's key safeguards around language accuracy, progression, communication, assessment validity, cultural representation, inclusion and safe uncertainty.

This is not yet the final release freeze. The next required stage is the **16 targeted MFL risk checks**, followed by the final verification record and freeze.

**External multi-platform regression testing:** Not completed.
