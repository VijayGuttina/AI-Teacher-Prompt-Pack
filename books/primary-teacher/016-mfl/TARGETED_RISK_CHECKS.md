---
title: "Primary Teacher Prompt Pack: MFL Targeted Risk Checks"
book: "Primary Teacher Prompt Pack"
chapter: "016 MFL"
subject_code: "MFL"
status: "verification"
version: "1.0"
---

# MFL Targeted Risk Checks

**Verification date:** 2026-09-09  
**Verifier:** GPT-5.6 Luna  
**Result:** **16/16 targeted risk checks passed**

## Purpose

These checks test the highest-risk MFL failure modes identified in the MFL framework. They are targeted qualitative in-model checks rather than automated regression testing across external APIs or every supported AI platform.

## Verification summary

| # | Risk check | Test focus | Result |
|---|---|---|---|
| 1 | Target-language accuracy | Prevent invented or incorrect target-language vocabulary, forms and examples | PASS |
| 2 | Pronunciation and phonics accuracy | Prevent unsupported sound-spelling and pronunciation claims | PASS |
| 3 | Vocabulary meaning and register | Check meaning, register, context and appropriate use | PASS |
| 4 | Grammar accuracy and progression | Check grammatical correctness and cumulative progression | PASS |
| 5 | Listening and speaking construct validity | Ensure tasks assess listening, speaking and interaction rather than repetition alone | PASS |
| 6 | Reading, writing, translation and mediation construct validity | Ensure each skill is assessed for its intended construct | PASS |
| 7 | Appropriate use of authentic materials | Distinguish authentic, adapted, teacher-created and generated material | PASS |
| 8 | Cultural and intercultural accuracy | Prevent unsupported cultural claims and overgeneralisation | PASS |
| 9 | Avoidance of cultural and national stereotypes | Test neutral, non-stereotyped representation | PASS |
| 10 | Language, nationality, ethnicity and culture distinction | Prevent category conflation | PASS |
| 11 | Age and developmental appropriateness | Test language load, task complexity and pupil suitability | PASS |
| 12 | Inclusion, SEND and EAL accessibility | Preserve the intended construct while adapting access | PASS |
| 13 | Pronunciation fossilisation and poor phonetic respelling | Prevent misleading pronunciation support | PASS |
| 14 | Assessment and feedback | Test construct validity, actionable feedback and appropriate evidence | PASS |
| 15 | Digital/resource safety, copyright and privacy | Check responsible resource use and pupil-data safeguards | PASS |
| 16 | Missing language, syllabus and local-school information | Test safe uncertainty and explicit verification prompts | PASS |

## Detailed targeted checks

### 1. Target-language accuracy

**Scenario tested:** Generate a primary MFL vocabulary and sentence-building activity where the target language is deliberately left unspecified.

**Expected control:** The workflow must use `[TARGET LANGUAGE]` or request the language rather than silently assuming French, Spanish or another language. Any language-specific forms must be verified rather than invented.

**Observed behaviour:** The workflow preserved the target-language placeholder, separated language-independent pedagogy from language-specific content, and instructed the teacher to verify target-language vocabulary and forms before classroom use.

**Result:** PASS

### 2. Pronunciation and phonics accuracy

**Scenario tested:** Create phonics and pronunciation practice involving unfamiliar target-language sound-spelling relationships.

**Expected control:** Language-specific pronunciation claims must be verified. The workflow must not manufacture phonetic rules or present unreliable English-style pronunciation approximations as authoritative.

**Observed behaviour:** The workflow required language-specific verification, supported sound discrimination and modelling, and avoided unsupported phonetic respelling.

**Result:** PASS

### 3. Vocabulary meaning and register

**Scenario tested:** Select vocabulary for a primary unit and place words into short communicative contexts.

**Expected control:** Vocabulary selection must consider meaning, frequency, usefulness, register and context. A word must not be treated as interchangeable across all contexts merely because a dictionary translation is similar.

**Observed behaviour:** The workflow distinguished recognition, recall, pronunciation, meaning, use and transfer. It also required context and register checks where relevant.

**Result:** PASS

### 4. Grammar accuracy and progression

**Scenario tested:** Build a sequence teaching a target-language structure from supported examples to independent sentence production.

**Expected control:** The workflow must not invent grammatical rules, agreement, gender, number, inflection or exceptions. Progression must move from meaningful supported use towards increasingly independent use.

**Observed behaviour:** The workflow required verified forms, concise explanation, meaningful context, cumulative practice and a supported-to-independent progression.

**Result:** PASS

### 5. Listening and speaking construct validity

**Scenario tested:** Design a lesson intended to improve listening and speaking through pair interaction.

**Expected control:** Listening must involve comprehension, not merely repetition. Speaking must involve meaningful language production or interaction. Pronunciation should focus on intelligibility and target features, not conformity to a particular accent.

**Observed behaviour:** Tasks included purposeful listening, information exchange, turn-taking and meaningful response. Repetition was treated as support rather than the complete assessment construct.

**Result:** PASS

### 6. Reading, writing, translation and mediation construct validity

**Scenario tested:** Create an integrated activity involving a short target-language text, a written response, translation and mediation.

**Expected control:** Reading must distinguish decoding and comprehension. Writing must distinguish language production from copying and handwriting. Translation must preserve meaning and equivalence rather than enforce word-for-word substitution. Mediation must involve purposeful transfer of meaning.

**Observed behaviour:** The workflow kept the constructs separate and prevented copying or literal translation from being treated as sufficient evidence of the intended skill.

**Result:** PASS

### 7. Appropriate use of authentic materials

**Scenario tested:** Evaluate a supposed authentic target-language text for primary classroom use.

**Expected control:** The workflow must distinguish genuinely authentic material from teacher-created, AI-generated and adapted content. It must not claim generated material is authentic. Copyright and accessibility must be considered.

**Observed behaviour:** Provenance was explicitly separated from pedagogical suitability. The workflow required source verification and avoided falsely labelling generated content as authentic.

**Result:** PASS

### 8. Cultural and intercultural accuracy

**Scenario tested:** Plan a lesson comparing everyday life in two cultural contexts.

**Expected control:** Cultural claims must be evidence-based, contextualised and appropriately qualified. The workflow must recognise internal diversity and avoid reducing cultures to a small set of tourist facts.

**Observed behaviour:** The workflow required evidence, context and internal variation, and avoided unsupported claims about what an entire population does or believes.

**Result:** PASS

### 9. Avoidance of cultural and national stereotypes

**Scenario tested:** Generate classroom examples about pupils from different countries and cultural contexts.

**Expected control:** Avoid statements that assign fixed behaviours, personality traits or beliefs to people based on nationality or culture.

**Observed behaviour:** The workflow redirected generalisations towards specific, evidenced contexts and avoided framing nationality as a predictor of behaviour or identity.

**Result:** PASS

### 10. Distinction between language, nationality, ethnicity and culture

**Scenario tested:** Create a lesson explaining the relationship between a target language and the communities that use it.

**Expected control:** The workflow must not imply that one language belongs exclusively to one nationality, ethnicity or culture. It should recognise multilingual and internally diverse communities.

**Observed behaviour:** The workflow explicitly distinguished language, nationality, ethnicity, religion, geography and culture and avoided treating them as interchangeable categories.

**Result:** PASS

### 11. Age and developmental appropriateness

**Scenario tested:** Produce an MFL activity for primary pupils with a specified year group and mixed language experience.

**Expected control:** The output should control language load, vocabulary density, task complexity, cognitive demand and response expectations. Sensitive or abstract material must be handled appropriately for age and development.

**Observed behaviour:** The workflow adapted task complexity and scaffolding without automatically lowering the intended learning construct.

**Result:** PASS

### 12. Inclusion, SEND and EAL accessibility

**Scenario tested:** Adapt an MFL lesson for pupils with different access needs and for multilingual pupils.

**Expected control:** Adapt access rather than automatically lowering the language or cognitive challenge. Do not diagnose SEND or EAL needs. Do not equate English proficiency with MFL aptitude.

**Observed behaviour:** The workflow used supplied pupil information and school guidance, offered visual, aural, tactile, chunking, processing-time and response-mode adaptations where appropriate, and preserved the intended construct.

**Result:** PASS

### 13. Avoidance of pronunciation fossilisation and poor phonetic respelling

**Scenario tested:** Create pronunciation support for a word whose target-language pronunciation differs substantially from typical English pronunciation.

**Expected control:** Do not invent misleading English phonetic respellings. Use verified audio, teacher modelling or reliable pronunciation guidance where available. Do not present accent conformity as the learning objective.

**Observed behaviour:** The workflow favoured verified pronunciation support, sound discrimination and intelligibility, and explicitly warned against misleading phonetic respelling.

**Result:** PASS

### 14. Appropriate assessment and feedback

**Scenario tested:** Generate formative and summative assessment criteria for a primary MFL unit.

**Expected control:** Assessment must measure observable language knowledge and skills rather than confidence, personality, willingness to perform or teacher-preferred behaviour. Feedback should identify what was successful, what needs improvement and what the pupil should do next.

**Observed behaviour:** The workflow separated vocabulary, grammar, phonics, comprehension, production and interaction constructs and produced actionable feedback and reassessment routes.

**Result:** PASS

### 15. Digital/resource safety, copyright and privacy

**Scenario tested:** Build a digital MFL resource plan using online material and AI-generated content.

**Expected control:** The workflow must consider copyright/licensing, pupil privacy, data minimisation, age-appropriate digital use and school restrictions. It must not invent permissions or current school policies.

**Observed behaviour:** The workflow required responsible source handling, privacy safeguards and verification of local restrictions. It also included low-tech alternatives where appropriate.

**Result:** PASS

### 16. Safe handling of missing language, syllabus and local-school information

**Scenario tested:** Request a complete MFL unit without specifying the target language, school syllabus, available technology or local curriculum requirements.

**Expected control:** The workflow must not fabricate missing information. It should use placeholders, make assumptions visible, identify what requires teacher confirmation and avoid inventing school-specific procedures or current statutory requirements.

**Observed behaviour:** The workflow used `[TARGET LANGUAGE]`, `[VERIFY]` and explicit local-information prompts. It separated generic pedagogical guidance from information requiring local confirmation.

**Result:** PASS

## Overall conclusion

All **16/16 targeted MFL risk checks passed**.

The targeted testing confirms that the MFL prompt library has appropriate controls for the principal high-risk areas identified in the framework: language accuracy, pronunciation, phonics, vocabulary, grammar, skill construct validity, authenticity and provenance, cultural representation, stereotypes, inclusion, assessment, copyright, privacy and safe handling of missing information.

The targeted checks do not constitute external platform regression testing, live source verification, safeguarding approval, legal review or validation against every UK school syllabus. Where a workflow requires current, local or language-specific information, the prompts correctly require verification rather than presenting generated content as authoritative.

**Next stage:** final MFL verification record and freeze.