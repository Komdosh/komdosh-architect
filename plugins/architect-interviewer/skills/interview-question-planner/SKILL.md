---
name: interview-question-planner
description: Plan a focused stakeholder interview round for confirming architecture requirements, decisions, assumptions, risks, and acceptance criteria.
---

# Interview Question Planner

## Purpose

Create the next focused set of stakeholder questions for an architecture acceptance interview.

## Required Inputs

Require:

- architecture presentation or source summary
- requirements coverage status
- known decisions, assumptions, risks, and open questions
- stakeholder role or decision authority when available

## Question Types

Use the smallest set that can move acceptance forward:

- acceptance questions for core behavior
- priority questions for tradeoffs
- exception-path questions for important edge cases
- non-functional questions for measurable targets
- ownership questions for unclear responsibility
- rollout questions for migration, release, or coexistence
- risk questions for known assumptions or unresolved constraints

## Output

Return:

```text
Interview round goal: <what this round must confirm>
Questions:
1. <question>
   Why it matters: <requirement, decision, or risk>
   Expected answer type: yes/no | choice | short explanation
Acceptance impact: <what can be accepted if answered>
```

## Guardrails

- ask no more than seven questions in one round by default
- order questions by acceptance impact
- do not ask questions already answered unless the answer conflicts with source material
- do not use vague questions such as "is everything fine?"
- when a yes/no question has consequences, state the consequence
