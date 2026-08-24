# AI Compatibility and Verification Standard

## Purpose

The library must not imply that a prompt is permanently compatible with every AI model. Model behaviour changes. Compatibility is therefore treated as a **testable publication attribute** and maintained separately from the core workflow text.

## Required metadata

Every published workflow should have a verification record containing:

| Field | Requirement |
|---|---|
| Workflow ID | Required |
| AI tool | ChatGPT, Claude, Gemini, Copilot or other named tool |
| Exact model / model family | Required where the platform exposes it |
| Test date | Required |
| Verification status | Verified / Review Required / Not Tested |
| Test scenario | Representative input or test case |
| Quality result | Pass / Partial / Fail |
| Reviewer notes | Required for Partial or Fail |
| Next review date | Required for published workflows |

## Verification principle

A workflow is not marked `Verified` merely because the AI produced an answer. The output must satisfy the workflow's quality gates and any subject-specific constraints.

## Quarterly review

Published workflows should be re-tested at least quarterly. A major model release, significant platform behaviour change or reported failure can trigger an earlier review.

## Cross-model strategy

The primary workflow should remain model-neutral wherever possible. Tool-specific instructions should only be introduced when they materially improve reliability.

Recommended compatibility categories:

- **Verified** — tested against the recorded model and passed the defined quality gates.
- **Compatible, not tested** — no known blocker, but no verification claim is made.
- **Review Required** — a previous verification has expired or a material model change has occurred.
- **Not Recommended** — known limitations make the workflow unsuitable for the stated use.

## Test pack

Each subject should eventually have a small regression test set covering:

1. Normal input
2. Ambiguous input
3. Incomplete input
4. Edge case
5. Safety / privacy-sensitive classroom context where relevant
6. Output-format compliance

The test set should be short and repeatable. It is not necessary to run hundreds of examples for every quarterly review.

## Worked-output evidence

For each workflow category, retain at least one representative worked example showing:

**Teacher input → workflow → AI output → teacher quality check**

The example should be representative rather than presented as a guarantee of identical output on every model.

## Commercial claim standard

Use language such as:

> Tested against the model and date shown in the workflow's verification record.

Avoid claims such as:

> Works perfectly on every AI model.

or

> Future-proof prompt.

## Product design implication

The published PDF should expose compatibility through a searchable/filterable index or compact metadata panel. It should not clutter the main workflow with repeated model instructions.
