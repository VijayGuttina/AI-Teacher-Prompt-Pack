---
title: "Primary Teacher Prompt Pack: MFL Culture, Communities & Intercultural Understanding"
book: "Primary Teacher Prompt Pack"
chapter: "016 MFL"
subject_code: "MFL"
family: "Culture, Communities & Intercultural Understanding"
status: "draft"
version: "1.0"
---

# MFL Family 7: Culture, Communities & Intercultural Understanding

This family contains ten copy/paste-ready workflows for teaching culture and intercultural understanding through primary modern foreign languages. The workflows are designed to develop curiosity, comparison, contextual understanding and respectful interpretation without turning culture into stereotypes or treating one community, country or speaker as representative of everyone.

## Family Principles

Use these controls in every workflow:

- Treat culture as diverse, dynamic and contextual rather than a fixed list of national characteristics.
- Distinguish language, nationality, ethnicity, religion, heritage, geography and culture.
- Avoid claims such as "people from X are..." unless a carefully evidenced, appropriately bounded claim is genuinely required.
- Do not reduce cultural learning to food, festivals, flags, famous people or tourist facts.
- Where a cultural practice varies by region, generation, community, family or context, say so.
- Do not invent cultural practices, quotations, statistics, traditions, community opinions or historical claims.
- Do not present generated material as authentic unless the source has actually been supplied or verified.
- Use current reliable sources for contemporary claims that could have changed.
- Use `[VERIFY]` where a language-specific, cultural, historical or contemporary claim requires teacher verification.
- If the target language is unspecified, use `[TARGET LANGUAGE]` rather than assuming French or another particular language.
- Build intercultural understanding through evidence, comparison and interpretation, not through forced imitation or personal disclosure.
- Do not require pupils to disclose family heritage, nationality, religion, migration history or personal beliefs.
- Avoid asking pupils to perform, parody or role-play people from another culture in ways that could caricature identity.
- Make comparisons between contexts rather than ranking cultures.
- Preserve age appropriateness, reading accessibility and curriculum intent.
- Adapt access for SEND and EAL needs without removing the intended cultural or language construct.
- Respect copyright when using authentic texts, images, recordings or other cultural materials.

---

## RT/CC Workflow Architecture

Each workflow follows the standard prompt architecture:

1. ROLE
2. CONTEXT
3. TASK
4. REQUIREMENTS
5. OUTPUT FORMAT
6. QUALITY CHECKS
7. OPTIONAL CUSTOMISATION

Each prompt also includes metadata and an example input/output so that a teacher can use it without requiring a separate prompt-engineering step.

---

# CC-01 Plan a Culture and Intercultural Understanding Lesson

**Prompt ID:** CC-01  
**Difficulty:** Beginner  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 700–1,000 words  
**Typical generation time:** 30–60 seconds  
**Curriculum tags:** Primary MFL, KS2, Culture, Intercultural Understanding, Comparison, [TARGET LANGUAGE]

### Editable variables

| Variable | Replace with |
|---|---|
| `[YEAR GROUP]` | Year 3, Year 4, Year 5 or Year 6 |
| `[TARGET LANGUAGE]` | French, Spanish, German, etc. |
| `[LANGUAGE TOPIC]` | Food, school, family, weather, travel, hobbies, etc. |
| `[CULTURAL CONTEXT]` | Specific country, region, community or comparison supplied by the teacher |
| `[LESSON LENGTH]` | e.g. 45 minutes |
| `[KNOWN PRIOR LEARNING]` | Vocabulary, structures and cultural knowledge already taught |

### Copy/paste prompt

```text
ROLE
You are an expert primary MFL teacher and intercultural education specialist.

CONTEXT
I teach [YEAR GROUP]. The target language is [TARGET LANGUAGE]. The language topic is [LANGUAGE TOPIC]. I want pupils to develop both language knowledge and carefully evidenced intercultural understanding through [CULTURAL CONTEXT]. The lesson length is [LESSON LENGTH]. Known prior learning is [KNOWN PRIOR LEARNING].

TASK
Design a complete, classroom-ready lesson that connects meaningful [TARGET LANGUAGE] learning with evidence-based intercultural understanding.

REQUIREMENTS
1. Begin with a precise learning intention covering the intended language learning and the intended intercultural learning.
2. State the prerequisite vocabulary, structures and cultural knowledge.
3. Use a specific cultural context rather than vague statements about a whole country or population.
4. Include 5–10 carefully selected target-language words, phrases or sentence frames only where they are genuinely relevant. Do not invent forms. Mark anything needing teacher verification as [VERIFY].
5. Build the cultural learning around evidence, examples, comparison and interpretation.
6. Explain what pupils should notice and what they should not infer from the evidence.
7. Include teacher explanation, pupil activity, structured comparison and reflection.
8. Avoid stereotypes, tokenism, caricature and claims that everyone in a country or community behaves in the same way.
9. Distinguish nationality, ethnicity, religion, language, geography and culture where relevant.
10. Do not require pupils to disclose personal family or cultural experiences.
11. Include scaffolding for pupils who need additional language support and extension for pupils ready for greater independence.
12. Include an observable assessment method.
13. Identify any cultural, historical, contemporary or language-specific claims that should be checked before teaching.
14. Do not invent school-specific policies, safeguarding procedures or local arrangements.

OUTPUT FORMAT
Produce:
- lesson title
- learning intentions
- success criteria
- prior knowledge
- key vocabulary and sentence frames
- cultural evidence/context
- misconception and stereotype safeguards
- resources
- timed lesson sequence
- teacher explanations
- pupil tasks
- comparison questions
- differentiation and accessibility
- assessment
- likely misconceptions
- teacher verification notes
- exit ticket

QUALITY CHECKS
Before finalising, check that the lesson teaches a real language construct, uses bounded and evidenced cultural claims, avoids overgeneralisation, distinguishes evidence from interpretation, avoids personal disclosure, and is realistic for [YEAR GROUP].

OPTIONAL CUSTOMISATION
If I provide a syllabus objective, textbook extract, authentic source or school policy, use it as the controlling source and do not contradict it.
```

**Example input:** Year 5 Spanish, school life, compare a supplied Spanish school timetable with the pupils' own timetable, 50 minutes.

**Example output excerpt:** The lesson begins by examining the supplied timetable as evidence, then pupils identify familiar language, infer carefully bounded differences and similarities, and justify one comparison using sentence frames. The prompt explicitly avoids claiming that the timetable represents every Spanish school.

---

# CC-02 Create an Evidence-Based Cultural Case Study

**Prompt ID:** CC-02  
**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 900–1,300 words  
**Typical generation time:** 45–75 seconds  
**Curriculum tags:** Primary MFL, KS2, Culture, Case Study, Intercultural Understanding

### Editable variables

| Variable | Replace with |
|---|---|
| `[YEAR GROUP]` | Year group |
| `[TARGET LANGUAGE]` | Target language |
| `[CASE STUDY TOPIC]` | Specific cultural topic |
| `[LOCATION OR COMMUNITY]` | Specific bounded context |
| `[SOURCE MATERIAL]` | Supplied authentic material or source description |

### Copy/paste prompt

```text
ROLE
You are a primary MFL curriculum specialist with expertise in evidence-based intercultural education.

CONTEXT
Create a case study for [YEAR GROUP] learning [TARGET LANGUAGE]. The case study topic is [CASE STUDY TOPIC], focused specifically on [LOCATION OR COMMUNITY]. The source material is [SOURCE MATERIAL].

TASK
Create a classroom-ready cultural case study that develops language knowledge, contextual knowledge and intercultural interpretation without stereotyping or pretending that one example represents an entire culture.

REQUIREMENTS
1. Establish the exact scope of the case study.
2. Explain why this particular example is useful for primary MFL.
3. Separate sourced facts from interpretation and pupil enquiry.
4. Do not invent cultural details. If the supplied source is insufficient, identify what needs verification.
5. Include appropriate [TARGET LANGUAGE] vocabulary and sentence frames only where accurate and relevant.
6. Explain internal diversity where it matters.
7. Distinguish local practice from national generalisation.
8. Include at least three comparison questions that require evidence rather than opinion.
9. Include one activity that asks pupils to identify what can and cannot reasonably be concluded from the evidence.
10. Avoid stereotypes involving nationality, ethnicity, religion, family structure, gender or socioeconomic status.
11. Do not ask pupils to reveal personal heritage or family circumstances.
12. Include SEND/EAL accessibility adaptations that preserve the intended construct.
13. Include assessment criteria for factual understanding, vocabulary and intercultural reasoning separately.

OUTPUT FORMAT
Produce a teacher briefing, pupil-friendly case study, vocabulary box, evidence table, enquiry questions, comparison activity, misconception safeguards, differentiated tasks, assessment rubric and verification list.

QUALITY CHECKS
Check source integrity, cultural specificity, internal diversity, target-language accuracy, age suitability, evidence/interpretation distinction and absence of stereotypes.

OPTIONAL CUSTOMISATION
If I provide a verified source, quote or image, refer only to what it actually supports and label any additional information as requiring verification.
```

**Example input:** Year 6 French, a supplied photograph and school website extract about a school in Lyon.

**Example output excerpt:** The case study treats the Lyon school as one specific example, not as evidence about all French schools, and asks pupils to distinguish observations from conclusions.

---

# CC-03 Compare Everyday Life Across Contexts Without Stereotyping

**Prompt ID:** CC-03  
**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 800–1,200 words  
**Typical generation time:** 45–75 seconds  
**Curriculum tags:** Primary MFL, KS2, Culture, Comparison, Everyday Life

### Editable variables

`[YEAR GROUP]`, `[TARGET LANGUAGE]`, `[EVERYDAY LIFE TOPIC]`, `[CONTEXT A]`, `[CONTEXT B]`, `[SUPPLIED EVIDENCE]`

### Copy/paste prompt

```text
ROLE
You are an expert primary MFL teacher specialising in comparative and intercultural learning.

CONTEXT
I teach [YEAR GROUP] through [TARGET LANGUAGE]. I want pupils to compare [EVERYDAY LIFE TOPIC] across [CONTEXT A] and [CONTEXT B]. My available evidence is [SUPPLIED EVIDENCE].

TASK
Design a comparison sequence that develops language and intercultural reasoning without turning either context into a stereotyped picture.

REQUIREMENTS
1. Define exactly what is being compared.
2. Use evidence that is specific enough to support the comparison.
3. Distinguish observed practice from assumptions about people.
4. Identify variation within each context where relevant.
5. Avoid "us versus them" framing.
6. Use [TARGET LANGUAGE] for meaningful comparison sentence frames where accurate.
7. Include vocabulary retrieval, guided comparison and independent explanation.
8. Include questions such as "What evidence supports this?", "Could this vary?" and "What can we not conclude?".
9. Do not rank either context as better, more normal or more advanced.
10. Do not require personal disclosure.
11. Include accessibility adaptations and extension.
12. Include an assessment that measures evidence-based comparison rather than personal opinion.

OUTPUT FORMAT
Provide learning objectives, vocabulary, evidence table, modelling, guided task, independent task, misconceptions, differentiation, assessment and reflection.

QUALITY CHECKS
Verify that similarities and differences are balanced, evidence is not overextended, cultural claims are bounded, and target-language material is accurate or marked [VERIFY].

OPTIONAL CUSTOMISATION
If an authentic source is supplied, use it as the primary evidence rather than replacing it with generic generated examples.
```

**Example input:** Year 4 German, school lunches, supplied menu from one school in Germany and one UK school menu.

**Example output excerpt:** Pupils compare the supplied menus and explain what the menus show, while explicitly avoiding claims about what all German or British children eat.

---

# CC-04 Teach Festivals, Celebrations and Traditions With Context

**Prompt ID:** CC-04  
**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 900–1,300 words  
**Typical generation time:** 45–75 seconds  
**Curriculum tags:** Primary MFL, KS2, Festivals, Traditions, Culture, Context

### Editable variables

`[YEAR GROUP]`, `[TARGET LANGUAGE]`, `[CELEBRATION]`, `[LOCATION/COMMUNITY]`, `[SOURCE]`, `[LANGUAGE OBJECTIVE]`

### Copy/paste prompt

```text
ROLE
You are a primary MFL and intercultural education specialist.

CONTEXT
Design learning for [YEAR GROUP] in [TARGET LANGUAGE] about [CELEBRATION] in [LOCATION/COMMUNITY]. The language objective is [LANGUAGE OBJECTIVE]. The available source is [SOURCE].

TASK
Create an accurate, age-appropriate learning sequence that explains the celebration in context and avoids reducing it to a colourful collection of stereotypes or tourist facts.

REQUIREMENTS
1. Explain the specific historical, religious, regional, community or contemporary context only where relevant and evidenced.
2. Acknowledge variation in participation and practice.
3. Do not imply that everyone in the location celebrates it in the same way.
4. Do not invent rituals, foods, clothing, songs, quotations or beliefs.
5. Separate factual information from interpretation.
6. Include meaningful target-language vocabulary and communication.
7. Avoid asking pupils to imitate sacred or sensitive practices inappropriately.
8. Do not require personal religious or family disclosure.
9. Include misconceptions and stereotype safeguards.
10. Include accessible pupil activities, assessment and teacher verification notes.

OUTPUT FORMAT
Provide teacher background, pupil-friendly explanation, key vocabulary, source/evidence activity, language practice, enquiry questions, comparison task, differentiation, assessment, misconceptions and verification notes.

QUALITY CHECKS
Check historical/contextual accuracy, internal diversity, respectful treatment, target-language accuracy and construct validity.

OPTIONAL CUSTOMISATION
If the source is incomplete, state what requires verification instead of filling gaps with invented details.
```

**Example input:** Year 5 Spanish, Las Fallas, Valencia, using a supplied local tourism museum source and a language objective on descriptive adjectives.

**Example output excerpt:** The lesson explains that Las Fallas is a specific Valencian festival with varied participation and historical context, rather than presenting it as a generic "Spanish tradition".

---

# CC-05 Explore Language, Identity and Belonging

**Prompt ID:** CC-05  
**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 900–1,400 words  
**Typical generation time:** 60–90 seconds  
**Curriculum tags:** Primary MFL, KS2, Language, Identity, Belonging, Intercultural Understanding

### Editable variables

`[YEAR GROUP]`, `[TARGET LANGUAGE]`, `[LANGUAGE/IDENTITY TOPIC]`, `[SOURCE]`, `[PRIOR KNOWLEDGE]`

### Copy/paste prompt

```text
ROLE
You are an expert primary MFL teacher with specialist knowledge of sociolinguistics and inclusive intercultural education.

CONTEXT
I teach [YEAR GROUP] using [TARGET LANGUAGE]. The topic is [LANGUAGE/IDENTITY TOPIC]. Relevant prior knowledge is [PRIOR KNOWLEDGE]. The source material is [SOURCE].

TASK
Design a safe and age-appropriate learning sequence exploring how language can connect with identity and belonging while making clear that language does not determine a person's nationality, ethnicity, religion or identity.

REQUIREMENTS
1. Keep the lesson educational rather than asking pupils to disclose personal identity.
2. Explain that individuals and communities may use language in different ways and for different reasons.
3. Distinguish target-language learning from assumptions about who "belongs" to a language.
4. Include examples of multilingualism, language choice, regional variation or heritage language where relevant and evidenced.
5. Do not invent community attitudes or claim that a language is inherently associated with one ethnic or national group.
6. Include accurate target-language examples, using [VERIFY] where needed.
7. Use evidence and structured enquiry.
8. Include discussion protocols that allow pupils to participate without personal disclosure.
9. Include SEND/EAL adaptations.
10. Assess conceptual understanding and language learning separately.

OUTPUT FORMAT
Produce learning intentions, key concepts, teacher briefing, source activity, language tasks, discussion questions, misconception safeguards, accessibility, assessment and reflection.

QUALITY CHECKS
Check that identity is not essentialised, language/nationality/ethnicity are distinguished, personal disclosure is optional, and all language and factual claims are accurate or marked [VERIFY].

OPTIONAL CUSTOMISATION
If the supplied source includes a community member's perspective, present it as that person's perspective rather than as the view of everyone in the community.
```

**Example input:** Year 6 French, multilingual signs and language choice in a supplied photograph set.

**Example output excerpt:** Pupils identify languages and discuss why different languages may appear in one setting without being asked to reveal their own linguistic background.

---

# CC-06 Build Intercultural Questioning and Enquiry

**Prompt ID:** CC-06  
**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 800–1,200 words  
**Typical generation time:** 45–75 seconds  
**Curriculum tags:** Primary MFL, KS2, Enquiry, Questioning, Critical Thinking, Culture

### Editable variables

`[YEAR GROUP]`, `[TARGET LANGUAGE]`, `[CULTURAL QUESTION]`, `[AVAILABLE EVIDENCE]`, `[LANGUAGE KNOWLEDGE]`

### Copy/paste prompt

```text
ROLE
You are a primary MFL curriculum and enquiry specialist.

CONTEXT
I teach [YEAR GROUP] through [TARGET LANGUAGE]. I want pupils to investigate [CULTURAL QUESTION]. Available evidence is [AVAILABLE EVIDENCE]. Relevant language knowledge is [LANGUAGE KNOWLEDGE].

TASK
Build a complete intercultural enquiry in which pupils ask questions, inspect evidence, interpret cautiously, compare contexts and justify conclusions.

REQUIREMENTS
1. Turn the topic into an age-appropriate enquiry question that can actually be investigated.
2. Generate a sequence of sub-questions from observation to interpretation and evaluation.
3. Distinguish questions answerable from the evidence from questions requiring additional research.
4. Include target-language use appropriate to [YEAR GROUP].
5. Prevent premature generalisation.
6. Include an explicit "What does the evidence not tell us?" stage.
7. Include alternative interpretations where reasonable.
8. Avoid stereotypes and ranking.
9. Do not require personal disclosure.
10. Include a final evidence-based pupil explanation.
11. Include differentiation and assessment.

OUTPUT FORMAT
Provide enquiry question, sub-questions, evidence plan, vocabulary, modelling, pupil enquiry steps, discussion structures, written outcome, assessment rubric, misconceptions and verification notes.

QUALITY CHECKS
Check enquiry quality, evidence sufficiency, language accuracy, cultural neutrality and age suitability.

OPTIONAL CUSTOMISATION
If evidence is insufficient to answer the enquiry question, explicitly recommend narrowing the question or obtaining an additional reliable source.
```

**Example input:** Year 5 Spanish, "How might school routines vary between different Spanish-speaking contexts?", with two supplied school sources.

**Example output excerpt:** The enquiry asks pupils to compare the two sources and explicitly prevents them from treating either source as representative of every Spanish-speaking school.

---

# CC-07 Use Authentic Cultural Materials Responsibly

**Prompt ID:** CC-07  
**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 900–1,300 words  
**Typical generation time:** 45–75 seconds  
**Curriculum tags:** Primary MFL, KS2, Authentic Materials, Copyright, Culture, Media Literacy

### Editable variables

`[YEAR GROUP]`, `[TARGET LANGUAGE]`, `[AUTHENTIC MATERIAL]`, `[SOURCE INFORMATION]`, `[LEARNING OBJECTIVE]`

### Copy/paste prompt

```text
ROLE
You are a primary MFL teacher and curriculum resource specialist experienced in responsible use of authentic cultural materials.

CONTEXT
I teach [YEAR GROUP] in [TARGET LANGUAGE]. The authentic material is [AUTHENTIC MATERIAL]. Source information is [SOURCE INFORMATION]. The learning objective is [LEARNING OBJECTIVE].

TASK
Create a classroom sequence using the supplied authentic material while preserving source integrity, age appropriateness and copyright awareness.

REQUIREMENTS
1. Use only information actually supported by the supplied material.
2. Do not invent missing source details.
3. Explain what the material is, who created it where known, its context and what pupils can reasonably learn from it.
4. Do not call a generated adaptation "authentic".
5. If copyright or permission status is unknown, flag it for teacher checking rather than asserting that reproduction is permitted.
6. Select short extracts only where appropriate and encourage use of lawful links or teacher-provided materials where necessary.
7. Include target-language comprehension and cultural interpretation.
8. Distinguish observation, source information and pupil inference.
9. Identify possible stereotypes, bias, outdated assumptions or limited representativeness in the material.
10. Include accessibility adaptations without changing the core learning objective.
11. Provide an assessment method.

OUTPUT FORMAT
Provide source briefing, teacher preparation, pupil-facing activity, language tasks, source-analysis questions, cultural interpretation, copyright/source notes, differentiation, assessment and verification checklist.

QUALITY CHECKS
Check source integrity, representativeness, target-language accuracy, age suitability, copyright caution and evidence/interpretation distinction.

OPTIONAL CUSTOMISATION
If I provide a URL, image, text or transcript, work from that exact material and identify anything you cannot verify.
```

**Example input:** Year 6 German, a supplied children's museum webpage excerpt and photograph.

**Example output excerpt:** The prompt asks pupils to identify what the museum source shows and what it cannot establish about wider German culture, while preserving the source attribution.

---

# CC-08 Teach Regional and Internal Cultural Diversity

**Prompt ID:** CC-08  
**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 900–1,300 words  
**Typical generation time:** 45–75 seconds  
**Curriculum tags:** Primary MFL, KS2, Regional Variation, Internal Diversity, Culture

### Editable variables

`[YEAR GROUP]`, `[TARGET LANGUAGE]`, `[REGIONAL/COMMUNITY TOPIC]`, `[CONTEXTS]`, `[SOURCES]`

### Copy/paste prompt

```text
ROLE
You are a primary MFL specialist with expertise in regional and internal cultural diversity.

CONTEXT
I teach [YEAR GROUP] in [TARGET LANGUAGE]. The topic is [REGIONAL/COMMUNITY TOPIC]. The contexts are [CONTEXTS], supported by [SOURCES].

TASK
Design a lesson or short sequence showing pupils that cultures and language communities contain meaningful internal diversity.

REQUIREMENTS
1. Define the specific regions, communities or contexts being considered.
2. Use evidence rather than unsupported claims.
3. Make clear that examples illustrate variation rather than defining every individual.
4. Distinguish regional language variation from errors.
5. Where pronunciation, vocabulary or grammar varies regionally, do not label legitimate variation as incorrect without evidence.
6. Include meaningful target-language learning.
7. Avoid presenting regional differences as exotic or inferior.
8. Do not equate region with ethnicity, religion or nationality.
9. Include comparison and reflection.
10. Include accessibility and assessment.
11. Mark uncertain claims [VERIFY].

OUTPUT FORMAT
Provide teacher background, pupil explanation, evidence examples, language activity, comparison task, misconception safeguards, differentiation, assessment and verification notes.

QUALITY CHECKS
Check regional accuracy, language accuracy, internal diversity, respectful representation and age suitability.

OPTIONAL CUSTOMISATION
If the school teaches a particular target-language variety, use that as the classroom norm while explaining variation accurately and respectfully.
```

**Example input:** Year 6 Spanish, compare selected vocabulary or cultural practices across two supplied Spanish-speaking regions.

**Example output excerpt:** Pupils identify differences between the supplied contexts and learn that regional variation does not make one form universally correct and another universally wrong.

---

# CC-09 Design an Intercultural Reflection and Discussion Task

**Prompt ID:** CC-09  
**Difficulty:** Intermediate  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 700–1,000 words  
**Typical generation time:** 30–60 seconds  
**Curriculum tags:** Primary MFL, KS2, Reflection, Discussion, Intercultural Understanding, Oracy

### Editable variables

`[YEAR GROUP]`, `[TARGET LANGUAGE]`, `[CULTURAL TOPIC]`, `[SOURCE/EVIDENCE]`, `[LANGUAGE LEVEL]`

### Copy/paste prompt

```text
ROLE
You are an expert primary MFL teacher and structured discussion designer.

CONTEXT
I teach [YEAR GROUP] in [TARGET LANGUAGE]. The cultural topic is [CULTURAL TOPIC]. Pupils have examined [SOURCE/EVIDENCE]. Their current language level is [LANGUAGE LEVEL].

TASK
Create a structured reflection and discussion task that requires pupils to use evidence, listen carefully and explain their thinking without requiring personal cultural disclosure.

REQUIREMENTS
1. Start with individual thinking before discussion.
2. Include sentence frames appropriate to [LANGUAGE LEVEL].
3. Use prompts that distinguish fact, observation, interpretation and opinion.
4. Include at least one question requiring evidence.
5. Include at least one question about uncertainty or limits of the evidence.
6. Prevent stereotyping and ranking.
7. Do not require pupils to compare with their own family or heritage.
8. Allow non-verbal, written or supported participation where appropriate.
9. Include teacher prompts for correcting inaccurate generalisations respectfully.
10. Include an observable assessment rubric.

OUTPUT FORMAT
Provide teacher setup, pupil instructions, discussion protocol, sentence frames, question sequence, misconception responses, accessibility, assessment rubric and reflection exit task.

QUALITY CHECKS
Check that the task assesses intercultural reasoning and language use rather than personality, confidence or willingness to disclose personal experiences.

OPTIONAL CUSTOMISATION
If I provide a particular source or language structure, integrate it exactly and identify any verification needs.
```

**Example input:** Year 4 French, school routine, using a supplied timetable, with sentence frames for "In the source..." and "This suggests...".

**Example output excerpt:** Pupils make evidence-based statements and can participate through writing or paired discussion without having to discuss their own family experience.

---

# CC-10 Build a Complete Culture and Intercultural Understanding Unit

**Prompt ID:** CC-10  
**Difficulty:** Advanced  
**AI model compatibility:** ChatGPT, Claude, Gemini, Copilot  
**Expected output length:** 1,500–2,200 words  
**Typical generation time:** 60–120 seconds  
**Curriculum tags:** Primary MFL, KS2, Culture, Intercultural Understanding, Unit Planning, Progression

### Editable variables

| Variable | Replace with |
|---|---|
| `[YEAR GROUP]` | Year group |
| `[TARGET LANGUAGE]` | Target language |
| `[UNIT THEME]` | Cultural/language theme |
| `[UNIT LENGTH]` | Number of lessons |
| `[LANGUAGE OBJECTIVES]` | Vocabulary, structures and skills |
| `[CULTURAL OBJECTIVES]` | Intercultural knowledge/reasoning objectives |
| `[SUPPLIED SOURCES]` | Authentic or verified materials |
| `[PRIOR LEARNING]` | Existing language/cultural knowledge |

### Copy/paste prompt

```text
ROLE
You are a senior primary MFL curriculum designer specialising in language progression and evidence-based intercultural education.

CONTEXT
Design a [UNIT LENGTH]-lesson unit for [YEAR GROUP] in [TARGET LANGUAGE]. The unit theme is [UNIT THEME]. Language objectives are [LANGUAGE OBJECTIVES]. Cultural/intercultural objectives are [CULTURAL OBJECTIVES]. Prior learning is [PRIOR LEARNING]. Supplied sources are [SUPPLIED SOURCES].

TASK
Build a complete, cumulative unit in which language learning and intercultural understanding reinforce one another without stereotypes, tokenism or unsupported cultural claims.

REQUIREMENTS
1. Sequence the unit from prior knowledge through input, noticing, guided practice, enquiry, comparison, communication, reflection and assessment.
2. Define a small number of high-value cultural concepts rather than an overloaded list of facts.
3. Use specific, bounded cultural contexts and explain internal diversity where relevant.
4. Do not treat one source, person, region or school as representative of an entire country or language community.
5. Distinguish language, nationality, ethnicity, religion, geography and culture.
6. Do not invent authentic texts, quotations, songs, statistics, practices or community opinions.
7. Use [VERIFY] for language-specific or cultural claims requiring teacher checking.
8. Include target-language vocabulary and sentence structures that are accurate, cumulative and communicatively useful.
9. Include listening, speaking, reading and writing where appropriate.
10. Include source analysis and evidence-based comparison.
11. Include explicit anti-stereotype teaching points.
12. Do not require pupils to disclose personal identity, heritage, religion or family circumstances.
13. Do not require pupils to imitate or role-play cultural practices inappropriately.
14. Include SEND/EAL adaptations that preserve the intended language and intercultural constructs.
15. Include formative assessment throughout and a final assessment with separate criteria for language learning and intercultural understanding.
16. Include retrieval and reuse across lessons.
17. Identify all source, copyright, current-information and teacher-verification considerations.
18. Do not invent school-specific policies or procedures.

OUTPUT FORMAT
Produce:
- unit rationale
- language objectives
- intercultural objectives
- prior knowledge
- vocabulary and structures
- cultural concepts and contexts
- source/evidence plan
- lesson-by-lesson sequence
- teacher explanations
- pupil activities
- enquiry questions
- comparison tasks
- retrieval plan
- speaking/listening/reading/writing opportunities
- misconceptions and stereotype safeguards
- SEND/EAL adaptations
- formative assessment
- final assessment rubric
- resource list
- source/copyright notes
- verification checklist
- unit reflection and next-step recommendations

QUALITY CHECKS
Before finalising, check cumulative language progression, target-language accuracy, evidence integrity, cultural specificity, internal diversity, balanced comparison, source/interpretation distinction, age appropriateness, accessibility and assessment construct validity.

OPTIONAL CUSTOMISATION
If I supply a curriculum specification, authentic sources, textbook materials or school policy, treat them as controlling inputs. Do not replace supplied evidence with invented material. If critical information is missing, flag it clearly rather than guessing.
```

**Example input:** Year 6 French, 6 lessons, theme "Everyday life and communities", language objectives on describing routines and places, cultural objectives on comparing selected everyday contexts using supplied sources.

**Example output excerpt:** The unit moves from language retrieval into source-based cultural enquiry, then structured comparison and an independent evidence-based explanation. The final assessment scores language knowledge and intercultural reasoning separately.

---

# Family-Level Quality Control Checklist

Before releasing this family, verify every workflow against the following controls:

- [ ] Exactly 10 workflows are present: CC-01 to CC-10.
- [ ] Every workflow follows ROLE → CONTEXT → TASK → REQUIREMENTS → OUTPUT FORMAT → QUALITY CHECKS → OPTIONAL CUSTOMISATION.
- [ ] Every workflow contains required metadata.
- [ ] Target language is explicit or represented by `[TARGET LANGUAGE]`.
- [ ] No target-language vocabulary, grammar or pronunciation is invented.
- [ ] Language-specific uncertainty is marked `[VERIFY]`.
- [ ] Cultural claims are specific, bounded and evidence-led.
- [ ] One person, source, region, school or community is never presented as representative of everyone.
- [ ] Internal cultural diversity is acknowledged where relevant.
- [ ] Language, nationality, ethnicity, religion, geography, heritage and culture are not conflated.
- [ ] Stereotypes, tokenism, caricature and ranking are actively prevented.
- [ ] Festivals and traditions are taught with context rather than as generic national facts.
- [ ] Authentic materials are not falsely claimed when generated.
- [ ] Source integrity and copyright considerations are explicit where relevant.
- [ ] Contemporary claims are flagged for reliable current-source checking.
- [ ] Pupils are not required to disclose personal identity, heritage, religion or family circumstances.
- [ ] Pupils are not required to imitate or parody cultural practices.
- [ ] Comparison tasks distinguish evidence, observation, interpretation and opinion.
- [ ] Assessment measures language learning and intercultural understanding as distinct constructs.
- [ ] Confidence, personality or willingness to speak is not used as a proxy for intercultural understanding.
- [ ] SEND and EAL adaptations preserve the intended construct.
- [ ] Reading age and language load are appropriate to the year group.
- [ ] Generated resources are copy/paste-ready and do not require iterative prompt engineering.
- [ ] Missing syllabus, source, local-policy or current-information details are handled explicitly rather than guessed.
