---
name: architecture-jira-tasker
description: Create rich, self-contained Jira implementation tasks from completed architecture docs, sized around one AI-agent delivery week, with humans involved only at review.
---

# Architecture Jira Tasker

## Purpose

Turn completed architecture documentation into a Jira implementation task that an AI agent can execute quickly and independently.
The task must be large enough to justify an AI delivery pass, self-contained enough to avoid architecture follow-up questions, and ready for human review after implementation.

Use this skill when the user asks to create Jira tasks, implementation tickets, delivery tasks, board tasks, backlog items, or AI-agent work from completed architecture docs.

## Core Rule

Create delivery tasks only after architecture is settled.

- if decisions, ownership, API shape, data ownership, security model, or deployment assumptions are still open, do not create a delivery issue yet
- use the relevant architecture plugins or docs first when the source material is not implementation-ready
- do not invent missing architecture decisions to make a Jira task look complete
- surface unresolved architecture questions as blockers, not as task assumptions

## One-Week AI-Agent Scope Rule

Default to one large task, not a set of small human-sized tickets.

- target size: about one calendar week for a fast AI implementation agent
- if the board uses story points, default to a large task such as 8 or 13 points unless local board conventions say otherwise
- merge small related changes into one coherent implementation task
- split only when the work crosses independent ownership, release, review, migration, or safety boundaries
- keep human work limited to review, approval, merge, and release acceptance

## Required Inputs

Load the minimum needed context:

- completed architecture docs, ADRs, diagrams, implementation plans, or architecture handoff notes
- implementation repository, service, module, or package target when known
- Jira project, board, epic, sprint, issue type, component, and required custom fields when available
- existing roadmap, release, dependency, migration, or operational notes
- local team conventions for labels, priorities, story points, estimates, assignees, and reviewers

If Jira target metadata is missing, use Jira tools to discover it when available.
Ask only when a required Jira field cannot be inferred safely or discovered.

## Skill Flow

1. Use `$architecture-jira-tasker:task-scope-planner` to shape one coherent AI-agent implementation scope.
2. Use `$architecture-jira-tasker:task-metadata-builder` to fill Jira metadata and delivery ownership.
3. Use `$architecture-jira-tasker:jira-description-builder` to write the issue description.
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
- labels
- fix version, release train, or target milestone
- assignee or AI-agent owner role
- human reviewer or review group
- estimate or story points
- due target when the board uses it
- dependencies and linked issues
- source architecture docs
- implementation repo and module
- affected API, data, security, observability, deployment, and documentation areas

Use `Not applicable` only when a field truly does not apply.
Do not leave placeholders such as `TBD`, `TODO`, `unknown`, or `fill later`.

## Task Description Contract

The Jira description must include:

1. Goal
2. Architecture sources
3. Business outcome
4. Implementation scope
5. Out of scope
6. Architecture decisions and constraints
7. Required implementation changes
8. Data, API, integration, security, observability, and deployment notes
9. Dependencies and sequencing
10. Acceptance criteria
11. Validation plan
12. Documentation updates
13. AI-agent execution notes
14. Human review checklist

## Output

When creating the task, return:

```text
Created Jira task: <KEY> <URL>
Summary: <summary>
Scope size: <estimate/story points and why it is one-week AI-agent scope>
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
- the task would require a human developer to design or implement instead of only review
- acceptance criteria cannot be made testable from the available context
