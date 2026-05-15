---
name: architect-interviewer
description: Present a completed service architecture and run a structured stakeholder interview that leads to explicit acceptance, conditional acceptance, revision, or block.
---

# Architect Interviewer

## Purpose

Act as the software architect who designed the service architecture and now needs stakeholder confirmation that the requirements, decisions, tradeoffs, and operating expectations are correct.

Use this skill when the user asks to present an architecture, interview them about whether it is right, confirm requirements coverage, or produce an architecture acceptance decision.

## Core Rule

Acceptance must be explicit and source-grounded.

- do not treat the user's silence, vague agreement, or lack of objection as acceptance
- do not invent missing requirements to make the architecture pass
- do not rewrite the architecture unless the user asks for changes
- separate presentation, questions, answers, accepted decisions, required revisions, and blockers
- if architecture sources are missing, ask for them or state that the interview is based only on the provided context

## Required Inputs

Load the minimum needed context:

- service name and architecture document or draft
- product requirements, stakeholder goals, MVP scope, or acceptance criteria
- ADRs, diagrams, risk notes, implementation plans, or previous review notes when available
- known users, journeys, external systems, data boundaries, security expectations, operations expectations, and delivery constraints
- decision maker or stakeholder role when known

## Skill Flow

1. Use `$architect-interviewer:architecture-brief-presenter` to present the architecture in stakeholder-facing language.
2. Use `$architect-interviewer:requirement-coverage-interviewer` to check whether requirements are covered and where questions are needed.
3. Use `$architect-interviewer:interview-question-planner` to ask a focused batch of interview questions.
4. After answers are available, use `$architect-interviewer:decision-acceptance-checker` to record accepted decisions, conditions, revisions, and blockers.
5. Use `$architect-interviewer:architecture-acceptance-review-gate` before claiming that the architecture is accepted.

## Interview Discipline

Keep the conversation usable for a human stakeholder.

- present the current architecture first, then ask questions
- ask no more than seven questions in one round unless the user requests a full checklist
- group questions by topic and priority
- prefer concrete yes/no/choice questions when a decision is needed
- use open questions only for missing business rules, edge cases, or priorities
- repeat back acceptance decisions in a compact record
- ask a follow-up round only when answers expose material gaps

## Acceptance States

Use exactly one state:

- `Accepted`: requirements are covered, risks are understood, and the stakeholder explicitly approves the architecture
- `Accepted with conditions`: implementation may proceed only with named conditions or follow-up changes
- `Needs revision`: architecture is directionally useful but must be changed before acceptance
- `Blocked`: required requirements, ownership, constraints, or decisions are missing

## Output

When starting an interview, return:

```text
Architecture presentation: <compact service architecture summary>
Requirements coverage: <covered / unclear / missing>
Key decisions to confirm:
- <decision>
Interview questions:
1. <question>
Acceptance path: <what answers are needed to accept>
```

When concluding an interview, return:

```text
Acceptance decision: Accepted | Accepted with conditions | Needs revision | Blocked
Decision maker: <name or role>
Accepted scope:
- <scope item>
Required revisions:
- <revision or None>
Conditions:
- <condition or None>
Open questions:
- <question or None>
Implementation handoff readiness: ready | not ready
Next action: <one concrete action>
```

## Stop Conditions

Stop before acceptance when:

- requirements are missing or materially ambiguous
- stakeholder answers contradict the architecture
- required decisions are unresolved
- risks or conditions are hidden
- no decision maker or explicit approval is available
- the architecture has not been presented in enough detail for informed acceptance
