---
name: jira-description-builder
description: Write a human-readable Jira issue description with QA-checkable acceptance criteria and no leaked development details.
---

# Jira Description Builder

## Purpose

Write the Jira description for an architecture-derived delivery task.
The description must be complete enough for humans to understand the outcome, scope, QA expectations, release context, and review requirements.
It must not expose development details that belong in architecture docs, pull requests, or private execution notes.
It must satisfy the 30-second rule: a team lead or colleague should understand the task quickly, without reading a long implementation specification.

## Required Inputs

Require:

- scope contract
- filled Jira metadata
- architecture docs, ADRs, diagrams, and implementation notes
- Jira format/profile docs when provided
- product area, service, application, component, release, QA, security, deployment, and observability context when applicable

## Description Rules

Write in Jira-friendly Markdown or the format required by the Jira tool.

- start with the outcome, not background
- keep the description compact, usually 5-7 short sections and no longer than one screen
- use the section order required by the target Jira format profile when one is provided
- include source document links only when useful for human review
- translate architecture decisions into human-readable behavior, constraints, and verification expectations
- make scope and out-of-scope boundaries explicit
- include acceptance criteria that QA can test or review directly
- include testing guidance that is either a one-line verification or a link/path to a separate QA test plan
- include documentation updates and release notes when the change is user-facing or operator-facing
- keep human work in the review checklist
- do not include file paths, class names, method names, internal package/module plans, developer commands, database migration instructions, or code-level sequencing
- mention APIs, logs, dashboards, or operational tools only when they are approved QA or operations verification surfaces
- do not include estimates, story points, hours, long justifications, filler, or detailed inventories of existing code
- avoid specific OS/device versions in Jira; use general phrasing such as `older devices`, `low-end devices`, or `slow network` unless the format profile requires exact values

## Required Description Shape

Use this compact structure for normal Story/Task issues:

```markdown
**Goal**

<one or two sentences: what the user, operator, or team gets after the task is closed.>

**Context**

<where this comes from, what it unblocks, or what blocks it. Omit when not useful.>

**What's included**

- <human-visible deliverable or behavior>
- <human-visible deliverable or behavior>

**Out of scope**

- <non-goal, when useful>

**Known limitations (not a blocker)**

<short limitation with blocker classification and follow-up destination. Omit when none.>

**Acceptance criteria**

- <verifiable condition>
- <verifiable condition>

**Testing**

Verification: <single manual/build/QA check>.
Or: See `<test-plan-path>` when a separate QA test plan is needed.

**Dependencies**

- <dependency or None>
```

For Bug issues, use this structure:

```markdown
**Description**

<what is broken, in one sentence.>

**Reproduction steps**

1. <step>
2. <step>

**Expected**

<what should happen.>

**Actual**

<what happens now.>

**Environment**

- Platform: <platform>
- App version / commit: <version or commit>
- Device / emulator: <general class or exact value only when the bug report requires it>
- Special conditions: <network/offline/slow network/etc. or None>
```

## Acceptance Criteria Rules

Acceptance criteria must:

- be understandable by QA without reading code, implementation plans, pull requests, or architecture internals
- be observable through UI behavior, approved API behavior, user-visible output, operator-visible output, documentation, support workflow, build/release state, or agreed QA tools
- include success and failure paths when behavior has branching logic
- cover documentation, regression, release, and operational validation when relevant
- avoid vague criteria such as `works correctly`, `is scalable`, or `is secure`
- avoid developer-only checks such as unit test names, source files, migration scripts, class names, internal package names, or local commands

## Testing Section Rules

Decide whether the task needs a separate QA test plan.

- use a one-line `Verification:` entry for simple technical tasks that cannot be meaningfully verified in a running app, database, or networked environment
- point to a separate test plan when the result can be touched or verified in a running app, database, or networked environment
- always require a separate test plan for bugs, because reproduction and regression checks must be explicit
- when a separate test plan is needed, keep detailed steps out of Jira and reference the plan from the `Testing` section
- when a format profile defines test-plan templates or paths, follow that path convention

## Known Limitations Rules

Use `Known limitations (not a blocker)` inside the Description for long-lived task facts.

- keep each limitation to 3-5 sentences
- classify it as `not a blocker`, `blocker until <date/event>`, or `MVP blocker`
- state where the follow-up belongs, such as a separate ticket or epic
- do not use Jira comments to document stable task limitations; comments are for process discussion

## Output

Return the final Jira description and mention any formatting constraints required by the target Jira tool.
