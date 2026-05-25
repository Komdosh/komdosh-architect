---
name: architecture-jira-tasker
description: Create human-readable, QA-checkable Jira delivery tasks from completed architecture docs, keeping development details out of the task body.
---

# Architecture Jira Tasker

## Purpose

Turn completed architecture documentation into a Jira delivery task that humans can understand, plan, review, and QA.
The task must be large enough to represent a meaningful delivery slice, self-contained enough to avoid architecture follow-up questions, and ready for QA validation after delivery.
The Jira description must not leak development details: no file paths, classes, methods, internal module plans, implementation commands, migration scripts, or coding instructions unless the team explicitly requires that field.
The description must pass the 30-second rule: a team lead or colleague should understand the task in about 30 seconds without scrolling through a long implementation specification.

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
- do not add estimates, story points, or hours unless the target board requires them or the user explicitly asks for them
- merge small related technical changes into one coherent human-visible delivery task
- split only when the work crosses independent ownership, release, review, migration, or safety boundaries
- keep the Jira task focused on outcome, scope, QA validation, release, and review

## Required Inputs

Load the minimum needed context:

- completed architecture docs, ADRs, diagrams, implementation plans, or architecture handoff notes
- Jira format/profile docs when provided, including project key, cloud/workspace, issue types, priority mapping, epic/parent rules, description format, workflow, and testing rules
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
5. Use `$architecture-jira-tasker:jira-task-publisher` only after the user has explicitly approved the final task text for creation or update.

## Jira Creation Rule

Create the Jira issue only when the task is complete enough to avoid placeholder cleanup.

- use available Jira or Atlassian tools when the user wants the issue created on a board
- validate project, issue type, board, epic or parent, sprint or phase, labels, components, priority, assignee or owner role, reviewer, QA owner, and required custom fields before creation
- search for similar existing Jira issues before creating new work
- propose the full task in chat and wait for explicit approval before creating a Jira issue
- for issue updates, show the proposed description/field diff and wait for explicit approval before updating Jira
- if creation requires a second step for sprint, epic link, labels, required estimate fields, or issue links, perform those updates after issue creation
- return the issue key, URL, final metadata, and any fields that Jira rejected or normalized
- if Jira tools are unavailable, return a creation-ready Jira payload instead of pretending the issue was created

## Jira Format Profile Rule

When the user provides a Jira format/profile document, treat it as the target board contract.

- use its project key, workspace/cloud ID, issue types, priority mapping, parent/epic mapping, labels, workflow, and creation rules
- choose `Story` for user-facing functionality, `Task` for technical or coordination work with no direct user-facing behavior, and `Bug` for broken behavior
- do not use unavailable issue types; if `Spike` does not exist, use `Task` with a specific `spike` label when acceptable
- attach child tasks to the parent/epic required by the format profile; only leave parent empty when the profile explicitly allows it
- if the profile says estimates are set by the team lead, omit estimates and story points from creation payloads
- if the profile defines priority mapping such as P0/P1/P2, translate it into the board's Jira priority values

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
- estimate or story points only when required by the board
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
- keep the description short enough to fit on one screen; if it cannot, split the task or move detailed checks to a separate test plan

## Label Policy

Use labels as precise routing and filtering signals for humans.

- use at most three labels
- choose labels from the task's concrete target service, application, platform, bounded context, or capability
- prefer specific labels such as `auth`, `mobile`, `payments`, `observability`, or `search`
- do not add generic process labels such as `architecture-ready`, `ai-agent`, `implementation`, or `human-review`
- if Jira requires generic labels or more than three labels, report that board constraint explicitly before creation

## Task Description Contract

The Jira description must use 5-7 short sections for human execution, review, and QA:

1. Goal
2. Context, when useful
3. What's included
4. Out of scope, when useful
5. Known limitations, when useful
6. Acceptance criteria
7. Testing
8. Dependencies, when useful

For bugs, use a bug-specific shape: Description, Reproduction steps, Expected, Actual, Environment.
Do not add time estimates, long justifications, device/OS specifics, or implementation-detail inventories to the Description.

## Output

When creating the task, return:

```text
Created Jira task: <KEY> <URL>
Summary: <summary>
Scope rationale: <why it is one coherent delivery task>
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
- the task has not been explicitly approved for Jira creation or update
- the task description would expose development details instead of human-facing behavior
- QA acceptance criteria cannot be made testable from the available context
