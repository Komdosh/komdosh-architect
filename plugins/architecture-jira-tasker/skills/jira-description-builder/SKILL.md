---
name: jira-description-builder
description: Write a human-readable Jira issue description with QA-checkable acceptance criteria and no leaked development details.
---

# Jira Description Builder

## Purpose

Write the Jira description for an architecture-derived delivery task.
The description must be complete enough for humans to understand the outcome, scope, QA expectations, release context, and review requirements.
It must not expose development details that belong in architecture docs, pull requests, or private execution notes.

## Required Inputs

Require:

- scope contract
- filled Jira metadata
- architecture docs, ADRs, diagrams, and implementation notes
- product area, service, application, component, release, QA, security, deployment, and observability context when applicable

## Description Rules

Write in Jira-friendly Markdown or the format required by the Jira tool.

- start with the outcome, not background
- keep the section order stable so human readers and QA can scan the same fields across tasks
- include source document links only when useful for human review
- translate architecture decisions into human-readable behavior, constraints, and verification expectations
- make scope and out-of-scope boundaries explicit
- include acceptance criteria that QA can test or review directly
- include QA validation steps, test data, environments, build or feature-flag context, and negative paths when relevant
- include documentation updates and release notes when the change is user-facing or operator-facing
- keep human work in the review checklist
- do not include file paths, class names, method names, internal package/module plans, developer commands, database migration instructions, or code-level sequencing
- mention APIs, logs, dashboards, or operational tools only when they are approved QA or operations verification surfaces

## Required Description Shape

Use this structure:

```markdown
## Goal
<one paragraph>

## Human handoff
- Area: <product/service/application area>
- Delivery owner or queue: <team/owner>
- Human reviewer: <reviewer/group>
- QA owner: <QA owner/group or Not applicable>
- Labels: <up to three specific labels>
- Estimate: <estimate/story points>

## Business outcome
- <outcome>

## User-visible or operator-visible scope
- <human-visible deliverable or behavior>

## Out of scope
- <non-goal>

## Behavior and constraints
- <expected behavior, business rule, security/privacy constraint, rollout constraint, or Not applicable>

## QA acceptance criteria
- [ ] <testable criterion>

## QA validation checklist
- <manual check, approved QA tool check, negative path, regression check, or release/build check>

## QA environment, data, and release context
- Environment/build: <environment, build number, feature flag, or Not applicable>
- Test data/accounts: <data setup QA can use or Not applicable>
- Rollout/release notes: <release context or Not applicable>

## Dependencies and sequencing
- <dependency or Not applicable>

## Documentation and support notes
- <user-facing, QA-facing, support-facing, or operator-facing doc/update or Not applicable>

## Human review checklist
- [ ] Scope and out-of-scope boundaries are clear.
- [ ] QA acceptance criteria are checkable without reading implementation details.
- [ ] QA validation evidence is attached or linked.
- [ ] Security, privacy, operational, and release impacts were reviewed.
```

## Acceptance Criteria Rules

Acceptance criteria must:

- be understandable by QA without reading code, implementation plans, pull requests, or architecture internals
- be observable through UI behavior, approved API behavior, user-visible output, operator-visible output, documentation, support workflow, build/release state, or agreed QA tools
- include success and failure paths when behavior has branching logic
- cover documentation, regression, release, and operational validation when relevant
- avoid vague criteria such as `works correctly`, `is scalable`, or `is secure`
- avoid developer-only checks such as unit test names, source files, migration scripts, class names, internal package names, or local commands

## Output

Return the final Jira description and mention any formatting constraints required by the target Jira tool.
