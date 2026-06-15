---
name: task-review-gate
description: Review an architecture-derived Jira task for human readability, QA-checkable criteria, metadata completeness, and absence of leaked development details.
---

# Task Review Gate

## Purpose

Review the Jira task before publishing.
The gate protects the board from tiny, vague, under-specified, or placeholder-heavy tickets.
It also checks that the task is convenient for human review and QA validation without exposing implementation details.

## Required Inputs

Require:

- architecture source references
- scope contract
- Jira metadata block
- Jira description
- intended Jira project or board

## Review Checklist

Reject or revise when any item fails:

- architecture docs are not complete enough for delivery
- task is smaller than a meaningful one-week delivery slice
- task scope crosses unrelated review, release, or ownership boundaries
- summary is vague or not outcome-oriented
- Jira description body is not written in Russian
- description fails the 30-second rule or is longer than one screen without a strong reason
- metadata contains placeholders, empty fields, or unsafe guesses
- required Jira fields are unknown
- estimates, story points, or hours are present when the target format says the team lead sets them
- labels exceed three items
- labels are generic process markers instead of specific service, application, platform, bounded-context, or capability labels
- description is not structured for human scanning and QA validation
- architecture decisions are copied as internal design detail instead of translated into behavior or constraints
- development details leak into the Jira task, including file paths, classes, methods, internal modules, local commands, migration scripts, or implementation sequencing
- out-of-scope boundaries are missing
- dependencies, migration, release, or operational risks are hidden
- acceptance criteria are not split into `DEV` and `QA`
- `DEV` acceptance criteria contain implementation sequencing, file paths, class names, local commands, or other unnecessary internals instead of developer-accepted quality gates
- `QA` acceptance criteria are not understandable or manually testable by QA
- Testing section is missing a one-line verification or a separate QA test-plan reference
- separate QA test plan is missing when the task result can be verified in a running app, database, networked environment, or is a bug
- QA validation context is missing environment, test data, build, feature-flag, negative-path, or regression context where expected
- the task asks humans to infer implementation details instead of stating expected behavior
- Jira creation or update is attempted before the user explicitly approves the final proposal
- duplicate search was skipped before creating new Jira work

## Output

Return:

```text
Review decision: Pass | Revise | Block
Reason: <short reason>
Required fixes:
- <fix or None>
One-week delivery scope check: <pass/fail and rationale>
Metadata completeness: <pass/fail and missing fields>
Label quality: <pass/fail and rationale>
Human readability: <pass/fail and gap>
Russian description: <pass/fail and gap>
DEV acceptance: <pass/fail and gap>
QA checkability: <pass/fail and gap>
Development-detail leakage: <pass/fail and examples or None>
Creation safety: <pass/fail for explicit approval and duplicate search>
Publish readiness: <ready/not ready>
```

## Pass Criteria

Pass only when:

- the task is ready to create in Jira without placeholder cleanup
- humans can understand the outcome, scope, release context, and review expectations
- the Jira description body is written in Russian
- acceptance criteria are split into `DEV` and `QA`
- `DEV` criteria cover developer-accepted quality gates such as code completion, compilation, lint/static checks, type checks, and automated/unit tests without leaking unnecessary internals
- QA can manually validate the `QA` criteria without reading implementation details
- the Testing section is appropriate for the task and points to a separate test plan when needed
- the task contains no developer-only instructions, file paths, internal modules, local commands, or code-level sequencing
- the task has no more than three specific labels
- creation or update has explicit user approval and duplicate search is complete
- all blocked fields are resolved
