---
name: requirement-coverage-interviewer
description: Check architecture coverage against known requirements and ask focused stakeholder questions for missing, ambiguous, or risky requirements.
---

# Requirement Coverage Interviewer

## Purpose

Check whether the architecture covers every known requirement well enough for stakeholder acceptance.
Use the result to ask targeted questions rather than broad approval questions.

## Required Inputs

Require:

- architecture source or summary
- known requirements, MVP scope, product goals, or acceptance criteria
- stakeholder answers from earlier interview rounds when available

## Coverage Categories

Classify each requirement as:

- `Covered`: the architecture clearly supports it
- `Partially covered`: the architecture supports it but has unresolved detail, risk, or condition
- `Unclear`: source material is insufficient to judge
- `Missing`: the architecture does not address it
- `Out of scope`: the requirement is explicitly outside this architecture

## Interview Focus

Ask questions when:

- a requirement is missing or unclear
- the architecture changes user behavior or operational responsibility
- a non-functional requirement lacks a measurable target
- a decision depends on stakeholder priority
- an edge case, failure mode, or exception path is not confirmed
- acceptance depends on a business rule, compliance constraint, or rollout condition

## Output

Return:

```text
Requirements coverage:
| Requirement | Status | Evidence | Question or action |
|-------------|--------|----------|--------------------|
| <requirement> | Covered | <source or summary> | None |

Questions for stakeholder:
1. <focused question tied to one requirement>

Coverage decision: pass | needs answers | blocked
Reason: <short reason>
```

## Quality Bar

- do not claim coverage without evidence
- do not require implementation-level detail unless the requirement depends on it
- keep questions tied to specific requirements
- prefer fewer high-value questions over a long generic checklist
