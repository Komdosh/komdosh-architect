---
name: task-scope-planner
description: Shape completed architecture docs into one coherent, large AI-agent implementation scope suitable for about one delivery week.
---

# Task Scope Planner

## Purpose

Define the implementation scope for a Jira task created from architecture docs.
The scope must be large enough for a fast AI agent and small enough for one human review cycle.

## Required Inputs

Require:

- source architecture docs or excerpts
- target product capability, service, module, integration, or package
- known implementation boundaries and out-of-scope decisions
- expected release, epic, milestone, or roadmap phase when available

## Scope Rules

Use one task for one coherent delivery slice.

- target about one calendar week for an AI implementation agent
- combine small related changes into one task when they share the same review boundary
- include implementation, tests, docs, and validation in the same issue
- include migration, observability, security, or operational work when it is part of making the feature shippable
- split only for independent ownership, release, migration, data-safety, or review boundaries

Do not create small human-sized tasks such as:

- add one endpoint
- add one DTO
- write one migration
- add one test file
- update one README

Those belong inside a larger AI-agent implementation issue unless they are separately releasable and reviewable.

## Scope Contract

Return:

```text
Task name: <clear implementation task name>
AI-agent size: <one-week rationale>
Primary outcome: <what must be true after implementation>
Implementation scope:
- <concrete deliverable>
Out of scope:
- <explicit non-goal>
Architecture sources:
- <path or URL>
Dependencies:
- <dependency or Not applicable>
Split decision:
- <why this is one Jira task or where it must split>
Review boundary:
- <what a human reviewer must verify>
```

## Quality Bar

The scope is ready when:

- the AI agent can understand the target deliverable without rereading unrelated architecture docs
- the task has a single primary outcome
- review can happen in one coherent pull request or change set
- architecture decisions are cited instead of repeated vaguely
- risks and dependencies are visible before implementation starts
