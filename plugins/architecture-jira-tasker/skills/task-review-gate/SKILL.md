---
name: task-review-gate
description: Review an architecture-derived Jira task for scope size, self-contained delivery context, metadata completeness, and human-review-only operating model.
---

# Task Review Gate

## Purpose

Review the Jira task before publishing.
The gate protects the board from tiny, vague, under-specified, or placeholder-heavy tickets.

## Required Inputs

Require:

- architecture source references
- scope contract
- Jira metadata block
- Jira description
- intended Jira project or board

## Review Checklist

Reject or revise when any item fails:

- architecture docs are not complete enough for implementation
- task is smaller than a meaningful one-week AI-agent delivery slice
- task scope crosses unrelated review, release, or ownership boundaries
- summary is vague or not outcome-oriented
- metadata contains placeholders, empty fields, or unsafe guesses
- required Jira fields are unknown
- architecture decisions are not linked to sources
- out-of-scope boundaries are missing
- dependencies, migration, release, or operational risks are hidden
- acceptance criteria are not testable
- validation plan is missing commands or checks where they are expected
- human work appears in implementation steps instead of review steps
- the task could not be executed by an AI agent without asking for architecture context

## Output

Return:

```text
Review decision: Pass | Revise | Block
Reason: <short reason>
Required fixes:
- <fix or None>
One-week scope check: <pass/fail and rationale>
Metadata completeness: <pass/fail and missing fields>
Self-contained context: <pass/fail and gap>
Human review model: <pass/fail>
Publish readiness: <ready/not ready>
```

## Pass Criteria

Pass only when:

- the task is ready to create in Jira without placeholder cleanup
- the AI agent can execute the work in one delivery pass
- the human reviewer has a clear checklist and validation evidence expectations
- all blocked fields are resolved
