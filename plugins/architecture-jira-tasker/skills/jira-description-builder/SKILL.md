---
name: jira-description-builder
description: Write a self-contained Jira issue description for an AI implementation agent from architecture docs, metadata, and acceptance criteria.
---

# Jira Description Builder

## Purpose

Write the Jira description for an architecture-derived implementation task.
The description must be complete enough for an AI agent to implement the work and for a human to review it.

## Required Inputs

Require:

- scope contract
- filled Jira metadata
- architecture docs, ADRs, diagrams, and implementation notes
- implementation repository, service, module, package, API, data, security, deployment, and observability context when applicable

## Description Rules

Write in Jira-friendly Markdown or the format required by the Jira tool.

- start with the outcome, not background
- include source document links before implementation detail
- keep architecture decisions tied to their source
- make scope and out-of-scope boundaries explicit
- include acceptance criteria that are testable or reviewable
- include validation commands, manual checks, and negative paths when relevant
- include documentation updates and release notes when the change is user-facing or operator-facing
- keep human work in the review checklist

## Required Description Shape

Use this structure:

```markdown
## Goal
<one paragraph>

## Architecture sources
- <doc/ADR/diagram/link>

## Business outcome
- <outcome>

## Implementation scope
- <deliverable>

## Out of scope
- <non-goal>

## Architecture decisions and constraints
- <decision or constraint with source>

## Required implementation changes
- <repo/module/API/data/test/doc change>

## Data, API, security, observability, and deployment notes
- Data: <requirement or Not applicable>
- API: <requirement or Not applicable>
- Security: <requirement or Not applicable>
- Observability: <requirement or Not applicable>
- Deployment: <requirement or Not applicable>

## Dependencies and sequencing
- <dependency or Not applicable>

## Acceptance criteria
- [ ] <testable criterion>

## Validation plan
- <command/check>

## Documentation updates
- <doc update or Not applicable>

## AI-agent execution notes
- Implement, test, document, and prepare for review in one delivery pass.
- Do not change architecture decisions; stop and escalate if a listed decision is impossible to implement.

## Human review checklist
- [ ] Architecture decisions were followed.
- [ ] Acceptance criteria are met.
- [ ] Tests and validation evidence are attached.
- [ ] Security, data, observability, and release impacts were reviewed.
```

## Acceptance Criteria Rules

Acceptance criteria must:

- be observable from code, tests, docs, API behavior, UI behavior, deployment output, or review evidence
- include success and failure paths when behavior has branching logic
- cover documentation and operational validation when relevant
- avoid vague criteria such as `works correctly`, `is scalable`, or `is secure`

## Output

Return the final Jira description and mention any formatting constraints required by the target Jira tool.
