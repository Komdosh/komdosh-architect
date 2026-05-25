---
name: task-scope-planner
description: Shape completed architecture docs into one coherent, human-visible delivery scope suitable for about one delivery week.
---

# Task Scope Planner

## Purpose

Define the human-visible delivery scope for a Jira task created from architecture docs.
The scope must be large enough for a meaningful delivery pass and small enough for one human review and QA cycle.

## Required Inputs

Require:

- source architecture docs or excerpts
- target product capability, service, application, integration, or release area
- known implementation boundaries and out-of-scope decisions
- expected release, epic, milestone, or roadmap phase when available

## Scope Rules

Use one task for one coherent delivery slice.

- target about one calendar week for the delivery pass
- combine small related changes into one task when they share the same review boundary
- include human-visible behavior, QA validation, docs, release, and review in the same issue
- include migration, observability, security, or operational impact only as QA/release-visible expectations
- split only for independent ownership, release, migration, data-safety, or review boundaries

Do not create tasks whose Jira description is only an internal technical change, such as:

- add one endpoint
- add one DTO
- write one migration
- add one test file
- update one README

Those belong inside a larger human-visible delivery issue unless they are separately releasable and QA-checkable.

## Scope Contract

Return:

```text
Task name: <clear delivery task name>
Delivery size: <one-week rationale>
Primary outcome: <what must be true after delivery>
Human-visible scope:
- <user-visible, operator-visible, QA-visible, or release-visible deliverable>
Out of scope:
- <explicit non-goal>
Architecture sources:
- <path or URL>
Dependencies:
- <dependency or Not applicable>
Split decision:
- <why this is one Jira task or where it must split>
Review boundary:
- <what a human reviewer and QA must verify>
```

## Quality Bar

The scope is ready when:

- a human reader can understand the target outcome without reading implementation details
- the task has a single primary outcome
- review can happen in one coherent change set
- architecture decisions are translated into behavior and constraints
- risks and dependencies are visible before delivery starts
