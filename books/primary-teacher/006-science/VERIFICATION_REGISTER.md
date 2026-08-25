# Primary Science Verification Register

**Subject:** Primary Science
**Initial workflow count:** 80
**Current verification status:** Representative execution QA passed; targeted workflow spot checks pending

## Status definitions

- `Not Yet Tested` — authored and structurally reviewed, but no representative execution recorded.
- `Structural QA Pass` — workflow architecture and required fields have been checked.
- `Tested - Fix Required` — representative execution identified a blocking or material issue.
- `Verified` — representative execution passed and factual/enquiry quality checks were completed.
- `Re-verify` — previously verified workflow requires testing again after a material change, model change or identified issue.

## Required verification metadata

Every verified workflow must record:

- AI tool
- Exact model / model family
- Test date
- Representative test input
- Result
- Reviewer notes
- Next scheduled review

## Current status

| Strand | Workflows | Structural status | Representative execution |
|---|---:|---|---|
| Working scientifically | 10 | Pass | Covered by representative tests |
| Living things, plants, animals and humans | 10 | Pass | Covered by representative tests |
| Materials and changes | 10 | Pass | Covered by representative tests |
| Forces and motion | 10 | Pass | Covered by representative tests |
| Light, sound, electricity and energy | 10 | Pass | Covered by representative tests |
| Earth, space and environmental science | 10 | Pass | Covered by representative tests |
| Classification, habitats and adaptation | 10 | Pass | Covered by representative tests |
| Assessment, diagnosis and intervention | 10 | Pass | Covered by representative tests |
| **Total** | **80** | **80/80 structural pass** | **18/18 representative tests passed** |

## Execution QA record

`EXECUTION_RESULTS_2026-08-25.md` records the representative execution results.

**AI tool:** ChatGPT  
**Model:** GPT-5.6 Luna  
**Test date:** 25 August 2026  
**Representative executions:** 18  
**Passed:** 18  
**Fix required:** 0

The representative tests cover the principal scientific, pedagogical and output-risk patterns across all eight workflow families.

## Important verification boundary

The 18 passed representative executions do **not** justify marking all 80 workflows individually as execution-verified. The remaining workflows require targeted spot checks before the complete subject is described as fully execution-verified.

Any workflow with materially different behaviour or risk must receive its own execution test.

## Verification method

Execution checks cover:

1. Scientific factual accuracy
2. Curriculum/year-group appropriateness
3. Enquiry validity
4. Accuracy of data, units and conclusions
5. Misconception/evidence discipline
6. Practical feasibility and sensible safety guidance
7. Preservation of scientific demand during adaptation
8. Completeness and usability of the requested output

Verification is qualitative execution evidence for the recorded model and test date. It is not a claim of universal reliability, multi-platform compatibility or API-level performance.

## Review cycle

Default review interval: quarterly. Re-verify sooner if the workflow changes materially, the underlying model changes materially, a repeated user failure is identified, curriculum requirements change, or a factual/scientific issue is discovered.
