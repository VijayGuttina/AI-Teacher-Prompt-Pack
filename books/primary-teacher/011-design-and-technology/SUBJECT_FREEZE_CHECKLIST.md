# Primary Design & Technology Subject Freeze Checklist

## 1. Architecture

- [ ] Framework is complete and reflects the intended subject scope.
- [ ] All workflow families have a distinct purpose.
- [ ] No duplicate or legacy modules remain.
- [ ] Workflow IDs are unique and sequential within each family.
- [ ] Total workflow inventory matches the verification register.

## 2. Structural QA

- [x] All 100 workflows have passed formal structural QA.
- [ ] Any post-QA changes have been rechecked.
- [ ] Subject-specific safeguards remain consistent across modules.

## 3. Worked examples and fixtures

- [x] Twenty representative fixtures exist.
- [x] Two representative workflows are selected from each family.
- [ ] Fixtures reflect the current workflow wording.

## 4. Execution verification

- [ ] All 20 representative workflows have actual execution records.
- [ ] AI tool, model/model family and date are recorded.
- [ ] Observed outputs are assessed against expected behaviour.
- [ ] Material failures are remediated.
- [ ] Remediated workflows have been retested.
- [ ] Systemic failures triggered expanded family testing.
- [ ] Verification statuses are current in the register.

## 5. Publication integrity

- [ ] No workflow is described as model-verified without execution evidence.
- [ ] Structural QA and execution verification claims are clearly separated.
- [ ] Safety, curriculum and model-review boundaries are stated accurately.
- [ ] Prompt metadata and global specification inheritance are documented.

## 6. Final freeze decision

**Subject status:** `Not Frozen`

**Decision:**

- [ ] Freeze approved
- [ ] Freeze blocked pending remediation

**Blocking issues:**

[Record any unresolved issue.]

**Approved by:**

**Approval date:**

**Frozen workflow version/commit:**

## Reopening rule

A frozen subject moves to `Re-verify` if a workflow is materially changed, a systemic defect is identified, the underlying model behaviour changes materially, or a curriculum/safety change affects workflow validity.
