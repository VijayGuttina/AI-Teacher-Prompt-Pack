# English Workflow Verification Register

**Verification date:** 24 August 2026  
**Verifier:** GPT-5.6 Luna  
**Verification type:** In-model qualitative execution and specification review  
**Status:** Verified for current model behaviour; external API/product regression testing still recommended before commercial publication.

## Important distinction

`Verified` means the workflow specification was reviewed and qualitatively executed against representative inputs in the current ChatGPT model context. It does not mean an automated API regression test has been run across OpenAI, Anthropic, Google and Microsoft endpoints.

Before publication, the production verification layer should additionally test each workflow in the exact customer-facing environment and record the production model identifier, interface, date, output sample and reviewer approval.

## Verification criteria

Each workflow was checked for:

1. Clear job-to-be-done.
2. Sufficient editable inputs.
3. Correct inheritance from the English framework.
4. No unnecessary duplication of global instructions.
5. A deterministic enough output structure to be useful as a reusable workflow.
6. Age-appropriate and educationally plausible task design.
7. Explicit quality gates where factual or pedagogical errors could occur.
8. No unsupported certainty in diagnostic workflows.
9. Appropriate adaptive-teaching safeguards.
10. A practical teacher-facing output.

## Results

| ID range | Coverage | Model | Tested | Status |
|---|---|---|---|---|
| RD-01 to RD-12 | Reading | GPT-5.6 Luna | 2026-08-24 | Verified |
| WR-01 to WR-12 | Writing | GPT-5.6 Luna | 2026-08-24 | Verified |
| GPS-01 to GPS-12 | Grammar, punctuation and spelling | GPT-5.6 Luna | 2026-08-24 | Verified |
| VO-01 to VO-12 | Vocabulary and oracy | GPT-5.6 Luna | 2026-08-24 | Verified |
| PH-01 to PH-08 | Phonics | GPT-5.6 Luna | 2026-08-24 | Verified |
| HW-01 to HW-06 | Handwriting | GPT-5.6 Luna | 2026-08-24 | Verified |

## Strand-level checks

### Reading
The twelve workflows were checked for distinct job-to-be-done boundaries, evidence-based reasoning, age appropriateness, diagnostic caution and practical classroom outputs.

### Writing
The twelve workflows were checked for alignment between writing purpose, audience, modelling, composition, editing, assessment and adaptive support.

### Grammar, punctuation and spelling
The twelve workflows were checked for explicit teaching, practice, retrieval, diagnosis, assessment and editing use cases without unnecessary overlap.

### Vocabulary and oracy
The twelve workflows were checked for contextual vocabulary instruction, retrieval, purposeful classroom talk, discussion, oral rehearsal, questioning and observable assessment.

### Phonics
The eight workflows were checked for GPC accuracy, blending/segmenting, decodability, assessment, diagnostic reasoning and intervention. The decodable-text workflow requires an explicit audit against supplied phonics knowledge.

### Handwriting
The six workflows were checked for formation, fluency, diagnosis, practice-sheet generation and adaptive teaching.

## Publication status

**62/62 workflows: Verified for current GPT-5.6 Luna in-model qualitative testing.**

**External multi-platform regression status: Not yet tested.**

Do not market external multi-platform verification as completed until production tests have been run against the exact customer-facing models and interfaces.

## Next verification

Scheduled: **24 November 2026** or earlier if a major model/platform change materially affects workflow behaviour.
