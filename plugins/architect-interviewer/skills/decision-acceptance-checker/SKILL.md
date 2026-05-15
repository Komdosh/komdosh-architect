---
name: decision-acceptance-checker
description: Convert stakeholder answers into accepted decisions, conditional acceptance, required revisions, blockers, and implementation handoff readiness.
---

# Decision Acceptance Checker

## Purpose

Turn stakeholder interview answers into a clear architecture acceptance record.

## Required Inputs

Require:

- architecture presentation or source summary
- requirements coverage status
- interview questions and stakeholder answers
- known decision maker or stakeholder role

## Decision Rules

Use these rules consistently:

- `Accepted` only when the stakeholder explicitly approves the covered architecture scope
- `Accepted with conditions` when implementation may proceed but named conditions must be tracked
- `Needs revision` when architecture changes are required before acceptance
- `Blocked` when required requirements, ownership, authority, or answers are missing

Do not hide conditions inside general notes.
Every required revision needs a scope and owner or next action.

## Output

Return:

```text
Acceptance decision: Accepted | Accepted with conditions | Needs revision | Blocked
Decision maker: <name or role>
Accepted architecture scope:
- <scope item>
Accepted decisions:
- <decision>
Conditions:
- <condition or None>
Required revisions:
- <revision or None>
Blocked topics:
- <topic or None>
Implementation handoff readiness: ready | not ready
Reason: <short reason>
```

## Quality Bar

- tie each condition or revision to a stakeholder answer, requirement, risk, or architecture decision
- keep accepted scope narrower than the total architecture when only part was approved
- surface contradictions instead of smoothing them over
- do not produce implementation handoff readiness when acceptance is blocked
