---
name: architecture-acceptance-review-gate
description: Review whether a presented architecture and interview record are ready for stakeholder acceptance or must be revised or blocked.
---

# Architecture Acceptance Review Gate

## Purpose

Review the acceptance interview result before claiming the architecture is approved.
The gate protects implementation handoff from vague approval, missing requirements, unresolved decisions, and hidden conditions.

## Required Inputs

Require:

- architecture presentation
- requirements coverage summary
- interview questions and answers
- acceptance record
- decision maker or stakeholder role

## Review Checklist

Reject or revise when any item fails:

- architecture was not presented clearly enough for informed approval
- known requirements are missing, unclear, or only partially covered without conditions
- stakeholder answers contradict the architecture
- required decisions or ownership boundaries are unresolved
- acceptance is inferred instead of explicitly confirmed
- conditions or required revisions are not listed separately
- risks, assumptions, rollout constraints, or operational expectations are hidden
- implementation handoff readiness is claimed while acceptance is conditional or blocked
- no decision maker or accepting role is recorded

## Output

Return:

```text
Review decision: Pass | Revise | Block
Reason: <short reason>
Acceptance state: Accepted | Accepted with conditions | Needs revision | Blocked
Required fixes:
- <fix or None>
Requirements coverage: pass | fail | partial
Stakeholder confirmation: explicit | missing | insufficient
Implementation handoff readiness: ready | not ready
```

## Pass Criteria

Pass only when:

- the architecture was presented in stakeholder-facing language
- requirements coverage is clear
- acceptance or conditions are explicit
- required revisions and blockers are absent or intentionally tracked as conditions
- implementation agents can rely on the acceptance record without guessing stakeholder intent
