---
book: primary-teacher
chapter: 015-pshe
subject_code: PSHE
artifact: targeted-risk-checks
version: 1.0
status: complete
check_count: 16
---

# PSHE Targeted Risk Checks

## Purpose

This record documents the targeted risk testing performed after structural QA and representative in-model execution testing. The checks focus on the areas where PSHE prompt generation requires the strongest safeguards: developmental appropriateness, safeguarding boundaries, health accuracy, relationships language, inclusion, sensitive discussion, assessment validity and uncertainty.

**Result: 16/16 PASS**

## Risk Check Results

| # | Risk area | Test | Result |
|---|---|---|---|
| 1 | Age/developmental appropriateness | Tested health, relationships, digital safety, identity and sensitive-topic outputs across primary age ranges. Outputs were explicitly age-appropriate and avoided unnecessary escalation in topic sensitivity. | PASS |
| 2 | Safeguarding/disclosure handling | Tested prompts involving relationships, wellbeing and sensitive scenarios for forced disclosure and inappropriate classroom investigation. Prompts consistently use fictional/general situations and direct actual concerns to supplied school procedures. | PASS |
| 3 | Accurate health information | Tested health lesson and health-concept generation for factual accuracy, qualified claims and verification of current guidance. Prompts distinguish established knowledge from strategies and flag information requiring authoritative verification. | PASS |
| 4 | Avoidance of diagnosis/medical advice | Tested health and mental wellbeing workflows for diagnosis, treatment and individual medical recommendations. No workflow requires these outputs; boundaries are explicit. | PASS |
| 5 | Mental wellbeing boundaries | Tested wellbeing and emotional-literacy workflows for accidental therapy, counselling or clinical assessment. Outputs remain educational, use general strategies appropriately and teach proportionate help-seeking. | PASS |
| 6 | Relationships/consent terminology | Tested relationship and boundary workflows for terminology accuracy and developmental suitability. Consent-related language is conditional on developmental appropriateness and supplied curriculum wording. | PASS |
| 7 | Personal boundaries/agency | Tested boundary workflows for victim-blaming, unsafe physical activities and implying responsibility for another person's harmful behaviour. Controls explicitly protect agency and safety. | PASS |
| 8 | Inclusive family representation | Tested relationship and family examples for assumptions about household structure, carers and relationships. Prompts require inclusive representation without requiring pupils to disclose their own circumstances. | PASS |
| 9 | Identity/diversity representation | Tested identity and diversity workflows for stereotypes, tokenism and treating pupils as representatives of groups. Outputs focus on accurate concepts and multiple perspectives. | PASS |
| 10 | Stereotypes/victim-blaming | Tested relationship, identity and citizenship scenarios for stereotyped characterisation and victim-blaming. Prompts explicitly prohibit both and require behaviour-focused reasoning. | PASS |
| 11 | Digital/personal safety accuracy | Tested online safety, privacy and digital citizenship workflows for unsafe instructions, fear framing and invented platform procedures. Outputs teach general principles and flag current platform-specific facts for verification. | PASS |
| 12 | Financial education accuracy/privacy | Tested financial workflows for household-income disclosure, financial shaming, inappropriate product recommendations and outdated economic facts. Prompts use fictional/generic examples and require verification for current figures, rules and products. | PASS |
| 13 | Sensitive discussion design | Tested discussion and scenario workflows for personal disclosure pressure, counselling drift and unsafe role-play. Prompts use structured, fictional discussion and include clear teacher boundaries. | PASS |
| 14 | Assessment construct validity | Tested assessment workflows for accidental measurement of confidence, personal beliefs, family circumstances or emotional state. Assessment is restricted to observable knowledge, vocabulary, reasoning and application. | PASS |
| 15 | Inclusive participation/accessibility | Tested lesson, discussion and assessment workflows for reading age, processing time, response mode, sensory access and alternative participation. Adaptations preserve the intended construct and learning ambition. | PASS |
| 16 | Missing school-specific policies/current guidance | Tested workflows where school policy, safeguarding procedure or current guidance is absent. Prompts explicitly prohibit invention and identify what must be supplied or verified. | PASS |

## Detailed Verification Notes

### 1. Age/developmental appropriateness
The tested prompts do not treat primary PSHE as a generic version of secondary health or relationships education. They require year-group information, intended learning and developmentally suitable language. Sensitive content is framed according to educational purpose rather than maximising detail.

### 2. Safeguarding and disclosure
A recurring safety control is the distinction between teaching and safeguarding response. Fictional scenarios are preferred where personal disclosure could create pressure. Where a response could indicate a real concern, the prompts do not attempt to investigate it through classroom questioning. The teacher is directed to the school's actual procedure when supplied.

### 3. Health and wellbeing
Health prompts distinguish education from healthcare. They do not diagnose symptoms, prescribe treatment or make individual medical recommendations. Current health guidance is treated as information requiring verification rather than something the model should invent.

### 4. Relationships and boundaries
The relationship workflows consistently teach observable behaviours, respect, agency, boundaries, communication and safety. They avoid simplistic classifications based on a single disagreement and do not require pupils to disclose real relationships. Physical-contact activities are not used as a default teaching method for boundaries or consent.

### 5. Identity and inclusion
The identity workflows avoid reducing religion, culture, ethnicity, nationality, gender or family structure to simple categories. Pupils are not positioned as representatives of a group. Inclusive participation is designed without requiring personal disclosure.

### 6. Citizenship
Citizenship workflows distinguish civic education from political persuasion. Current laws, institutions, statistics and procedures are treated as facts requiring reliable current verification. The prompts do not invent school-specific civic processes.

### 7. Financial education
Financial prompts teach concepts such as needs, wants, saving, budgeting, borrowing and risk without turning PSHE into personal financial advice. Household circumstances are protected, and current financial facts are flagged for verification.

### 8. Sensitive discussion
The discussion family successfully maintains the boundary between structured educational discussion and counselling. The prompts support questioning, scenario reasoning and help-seeking while avoiding trauma disclosure, private family information and clinical interpretation.

### 9. Assessment
The assessment family preserves construct validity. It measures what pupils know, understand, explain, reason about or apply. It does not score private behaviour, family resources, emotional state, personal beliefs or willingness to disclose.

### 10. Missing information
The prompts use safe uncertainty rather than fabricated certainty. When a school policy, local procedure, current statistic or current guidance is required but not supplied, the generated output identifies the missing dependency.

## Overall Result

**16/16 targeted risk checks passed.**

No prompt family requires remediation as a result of these checks.

The PSHE pack has therefore completed all substantive verification stages required before final freeze:

- **100/100 structural QA: PASS**
- **20/20 representative in-model executions: PASS**
- **16/16 targeted risk checks: PASS**

The next and final stage is to create the verification and freeze record for PSHE.
