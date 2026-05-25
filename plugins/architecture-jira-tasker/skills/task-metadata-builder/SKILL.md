---
name: task-metadata-builder
description: Fill human-facing Jira metadata for architecture-derived delivery tasks, avoiding placeholders, unsafe guesses, and implementation detail leaks.
---

# Task Metadata Builder

## Purpose

Build the Jira metadata set for a delivery task created from completed architecture docs.
The metadata must be rich enough for board planning, filtering, ownership, review, and release tracking.
Labels must stay specific and sparse enough to be useful for human filtering and QA routing.

## Required Inputs

Use:

- scope contract from `$architecture-jira-tasker:task-scope-planner`
- Jira project, board, epic, sprint, issue type, and custom field conventions
- source architecture docs and human-visible delivery targets
- known team labels, components, priorities, versions, owners, and reviewers

Use Jira tools to inspect valid projects, boards, epics, components, versions, statuses, priorities, and required fields when available.

## Metadata Rules

Fill fields with concrete values.

- do not emit `TBD`, `TODO`, `unknown`, `later`, or empty placeholders
- use `Not applicable` only when the field truly does not apply
- prefer existing Jira values over invented labels, components, epics, or versions
- if a required Jira field cannot be discovered or inferred safely, block creation and list the missing field
- keep assignee, reviewer, and QA owner fields human-facing
- use at most three labels, and make each one specific to the service, application, platform, bounded context, or capability
- prefer labels such as `auth` for authorization service work or `mobile` for mobile application work
- do not use broad process labels such as `architecture-ready`, `ai-agent`, `implementation`, or `human-review`
- do not expose file paths, class names, internal module names, implementation commands, or private execution notes in metadata fields

## Default Metadata Policy

When local board rules are not more specific:

- issue type: `Task`
- priority: `Medium`, or `High` when it blocks a committed roadmap or release
- estimate: `1w` or the closest Jira estimate field value
- story points: `8` or `13` for a large delivery task, depending on board convention
- labels: choose up to three specific labels from the target service, application, platform, bounded context, or capability
- assignee: delivery owner, team queue, or automation user supported by the board
- reviewer: human technical owner or review group
- QA owner: QA owner or review group when the board supports it
- components: derive from service, bounded context, platform area, product area, or application
- source docs: include architecture docs, ADRs, diagrams, and approved handoff notes only when the board expects source references

## Output

Return a metadata block:

```text
Jira metadata:
- Project: <key/name>
- Board: <board>
- Issue type: <type>
- Summary: <summary>
- Epic or parent: <epic or Not applicable>
- Sprint or target phase: <sprint/phase or Not applicable>
- Priority: <priority>
- Components: <components>
- Labels: <up to three specific labels>
- Fix version or milestone: <version/milestone or Not applicable>
- Estimate: <time estimate>
- Story points: <points or Not applicable>
- Delivery owner or queue: <team/owner/queue>
- Human reviewer: <reviewer/group>
- QA owner: <QA owner/group or Not applicable>
- Linked issues: <links or Not applicable>
- Dependencies: <dependencies or Not applicable>
- Source docs: <paths/URLs or Not applicable>
- Human-visible target: <product/service/application area>
- QA/release context: <environment/build/feature flag/release train or Not applicable>
Blocked fields:
- <none or exact missing Jira-required fields>
```

## Review

Before handing off metadata:

- confirm every Jira-required field is present
- confirm labels and components exist or are acceptable on the board
- confirm labels are no more than three items and are specific enough for human routing
- confirm estimate matches one-week delivery scope
- confirm assignee, reviewer, and QA owner are human-facing
- confirm source docs are linked precisely enough for review when they are included
- confirm metadata does not leak implementation details
