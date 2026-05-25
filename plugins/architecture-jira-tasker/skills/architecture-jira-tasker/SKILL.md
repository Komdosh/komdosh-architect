---
name: architecture-jira-tasker
description: Create human-readable, QA-checkable Jira delivery tasks from completed architecture docs, keeping development details out of the task body.
---

# Architecture Jira Tasker

## Purpose

Turn completed architecture documentation into a Jira delivery task that humans can understand, plan, review, and QA.
The task must be large enough to represent a meaningful delivery slice, self-contained enough to avoid architecture follow-up questions, and ready for QA validation after delivery.
The Jira description must not leak development details: no file paths, classes, methods, internal module plans, implementation commands, migration scripts, or coding instructions unless the team explicitly requires that field.

Use this skill when the user asks to create Jira tasks, delivery tasks, board tasks, backlog items, or QA-checkable work from completed architecture docs.

## Core Rule

Create delivery tasks only after architecture is settled.

- if decisions, ownership, API shape, data ownership, security model, or deployment assumptions are still open, do not create a delivery issue yet
- use the relevant architecture plugins or docs first when the source material is not implementation-ready
- do not invent missing architecture decisions to make a Jira task look complete
- surface unresolved architecture questions as blockers, not as task assumptions

## One-Week Delivery Scope Rule

Default to one meaningful delivery task, not a set of tiny technical tickets.

- target size: about one calendar week for the implementation pass
- if the board uses story points, default to a large task such as 8 or 13 points unless local board conventions say otherwise
- merge small related technical changes into one coherent human-visible delivery task
- split only when the work crosses independent ownership, release, review, migration, or safety boundaries
- keep the Jira task focused on outcome, scope, QA validation, release, and review

## Required Inputs

Load the minimum needed context:

- completed architecture docs, ADRs, diagrams, implementation plans, or architecture handoff notes
- product area, service, application, component, release, or QA target when known
- Jira project, board, epic, sprint, issue type, component, and required custom fields when available
- existing roadmap, release, dependency, migration, or operational notes
- local team conventions for labels, priorities, story points, estimates, assignees, reviewers, and QA owners

If Jira target metadata is missing, use Jira tools to discover it when available.
Ask only when a required Jira field cannot be inferred safely or discovered.

## Skill Flow

1. Use `$architecture-jira-tasker:task-scope-planner` to shape one coherent human-visible delivery scope.
2. Use `$architecture-jira-tasker:task-metadata-builder` to fill Jira metadata, delivery ownership, and QA ownership.
3. Use `$architecture-jira-tasker:jira-description-builder` to write the human-readable issue description.
4. Use `$architecture-jira-tasker:task-review-gate` to check readiness before creating anything.
5. Use `$architecture-jira-tasker:jira-task-publisher` to create the issue when Jira tools are available and the user requested creation.

## Jira Creation Rule

Create the Jira issue only when the task is complete enough to avoid placeholder cleanup.

- use available Jira or Atlassian tools when the user wants the issue created on a board
- validate project, issue type, board, epic, sprint, labels, components, estimate, priority, assignee or owner role, reviewer, and required custom fields before creation
- if creation requires a second step for sprint, epic link, labels, estimate, or issue links, perform those updates after issue creation
- return the issue key, URL, final metadata, and any fields that Jira rejected or normalized
- if Jira tools are unavailable, return a creation-ready Jira payload instead of pretending the issue was created

## Metadata Completeness

Fill every useful metadata field.

- project and board
- issue type
- summary
- parent epic or initiative
- sprint or target phase
- priority
- components
- labels, capped at three specific delivery-area labels
- fix version, release train, or target milestone
- delivery owner or team queue
- QA owner, human reviewer, or review group
- estimate or story points
- due target when the board uses it
- dependencies and linked issues
- source architecture docs when the board expects links
- affected product, service, application, release, QA, documentation, or operational areas

Use `Not applicable` only when a field truly does not apply.
Do not leave placeholders such as `TBD`, `TODO`, `unknown`, or `fill later`.

## Human-Only Task Boundary

The Jira task is for humans.

- write only information useful to product owners, delivery leads, QA, reviewers, release managers, and support
- translate architecture decisions into expected behavior, constraints, rollout notes, and QA-visible outcomes
- keep implementation plans in architecture docs, pull requests, or agent-private execution notes, not in the Jira description
- do not include file paths, class names, method names, internal package/module plans, developer commands, database migration instructions, or code-level sequencing
- include technical terms only when QA or operations must use them to verify the work

## Label Policy

Use labels as precise routing and filtering signals for humans.

- use at most three labels
- choose labels from the task's concrete target service, application, platform, bounded context, or capability
- prefer specific labels such as `auth`, `mobile`, `payments`, `observability`, or `search`
- do not add generic process labels such as `architecture-ready`, `ai-agent`, `implementation`, or `human-review`
- if Jira requires generic labels or more than three labels, report that board constraint explicitly before creation

## Task Description Contract

The Jira description must be structured for human execution, review, and QA:

1. Goal
2. Human handoff
3. Business outcome
4. User-visible or operator-visible scope
5. Out of scope
6. Behavior and constraints
7. QA acceptance criteria
8. QA validation checklist
9. QA environment, data, and release context
10. Dependencies and sequencing
11. Documentation and support notes
12. Human review checklist

## Output

When creating the task, return:

```text
Created Jira task: <KEY> <URL>
Summary: <summary>
Scope size: <estimate/story points and why it is one-week delivery scope>
Metadata: <compact field list>
Human review: <reviewer or review group>
Residual risks: <short list or none>
```

When creation is blocked, return:

```text
Jira task not created
Reason: <exact blocker>
Missing required fields: <fields>
Creation-ready payload: <payload if possible>
Next action: <one concrete action>
```

## Stop Conditions

Stop before creating Jira work when:

- architecture source docs are not settled
- required Jira board fields cannot be discovered or inferred safely
- task scope is too small and cannot be merged with adjacent work
- the task description would expose development details instead of human-facing behavior
- QA acceptance criteria cannot be made testable from the available context
