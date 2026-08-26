# Geography Verification Register

**Subject:** Primary Geography  
**Library:** AI Teacher Prompt Pack  
**Workflow count:** 100  
**Status:** Representative execution QA passed; targeted spot checks pending

## Verification status

| Module | IDs | Count | Structural QA | Execution status |
|---|---|---:|---|---|
| Locational & Place Knowledge | LP-01–LP-10 | 10 | Pass | Representative QA passed |
| Map Skills | MS-01–MS-10 | 10 | Pass | Representative QA passed |
| Physical Geography | PG-01–PG-10 | 10 | Pass | Representative QA passed |
| Human Geography | HG-01–HG-10 | 10 | Pass | Representative QA passed |
| Geographical Data & Fieldwork | GF-01–GF-10 | 10 | Pass | Representative QA passed |
| Climate, Weather & Environmental Change | CW-01–CW-10 | 10 | Pass | Representative QA passed |
| Settlements, Land Use & Resources | SR-01–SR-10 | 10 | Pass | Representative QA passed |
| Interdependence, Sustainability & Global Issues | IS-01–IS-10 | 10 | Pass | Representative QA passed |
| Geographical Vocabulary & Explanation | GV-01–GV-10 | 10 | Pass | Representative QA passed |
| Assessment, Diagnosis & Intervention | GA-01–GA-10 | 10 | Pass | Representative QA passed |
| **Total** | | **100** | **Pass** | **20/20 representative tests passed; targeted spot checks pending** |

## Execution evidence

The 20-test representative execution suite was completed against **GPT-5.6 Luna** on **26 August 2026**. Full results are recorded in `EXECUTION_RESULTS_2026-08-26.md`.

The representative tests covered the major workflow families and Geography-specific risk gates. All 20 tests passed with no material defect requiring remediation.

## Evidence standard

A workflow is **Individually Verified** only after that workflow has itself been executed and assessed on the stated model, with the input, output assessment, reviewer notes and any remediation recorded. Representative execution does not count as individual verification of every untested workflow.

## Geography-specific gates

- Do not invent places, local facts, maps, datasets or fieldwork observations.
- Preserve map scale, direction, distance and units when supplied.
- Separate observation from inference.
- Separate evidence from explanation and value judgement.
- Do not fabricate quotations, stakeholder views or source provenance.
- Environmental and sustainability claims must be appropriately qualified.
- Adaptation must preserve geographical knowledge and disciplinary reasoning.
- Assessment diagnosis must distinguish conceptual, vocabulary, data-handling and access issues.

## Review metadata

**Execution model:** GPT-5.6 Luna  
**Execution date:** 26 August 2026  
**Next scheduled review:** 26 November 2026, or sooner following a material model change

## Next gate

Complete targeted spot checks across the remaining workflows. If no material defects are identified, update this register to **Verified / Frozen** and proceed to Computing.
