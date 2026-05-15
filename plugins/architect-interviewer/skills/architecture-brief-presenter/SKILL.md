---
name: architecture-brief-presenter
description: Prepare a concise stakeholder-facing architecture presentation from source docs before an acceptance interview.
---

# Architecture Brief Presenter

## Purpose

Turn the available architecture sources into a compact presentation that a stakeholder can review before answering acceptance questions.

## Required Inputs

Require:

- service name or system name
- architecture source or draft
- known requirements or MVP scope
- relevant decisions, diagrams, risks, assumptions, and constraints when available

## Presentation Checklist

Cover only what is needed for informed acceptance:

- service purpose and business outcome
- users, actors, and external systems
- main responsibilities and boundaries
- important user journeys or system flows
- data ownership and lifecycle expectations
- APIs, events, integrations, or contracts
- security, privacy, and authorization expectations
- observability, operations, reliability, and deployment expectations
- key decisions and tradeoffs
- known risks, assumptions, and open questions
- what is explicitly out of scope

## Output

Return:

```text
Architecture presentation: <service name>
Purpose: <one or two sentences>
How it works:
- <main flow or responsibility>
Requirement coverage highlights:
- <covered requirement>
Important decisions:
- <decision and rationale>
Known risks or assumptions:
- <risk or assumption>
Out of scope:
- <boundary>
Questions that need stakeholder confirmation:
- <question topic>
```

## Quality Bar

The presentation must be:

- compact enough to read before an interview round
- understandable without implementation details unless the detail affects acceptance
- clear about what is fact, assumption, decision, and open question
- source-grounded when source references are available

Do not turn the presentation into a full architecture rewrite.
