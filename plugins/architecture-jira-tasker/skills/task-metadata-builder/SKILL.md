---
name: task-metadata-builder
description: Fill rich Jira metadata for architecture-derived AI-agent implementation tasks, avoiding placeholders and unsafe guesses.
---

# Task Metadata Builder

## Purpose

Build the Jira metadata set for an implementation task created from completed architecture docs.
The metadata must be rich enough for board planning, filtering, ownership, review, and release tracking.

## Required Inputs

Use:

- scope contract from `$architecture-jira-tasker:task-scope-planner`
- Jira project, board, epic, sprint, issue type, and custom field conventions
- source architecture docs and implementation targets
- known team labels, components, priorities, versions, owners, and reviewers

Use Jira tools to inspect valid projects, boards, epics, components, versions, statuses, priorities, and required fields when available.

## Metadata Rules

Fill fields with concrete values.

- do not emit `TBD`, `TODO`, `unknown`, `later`, or empty placeholders
- use `Not applicable` only when the field truly does not apply
- prefer existing Jira values over invented labels, components, epics, or versions
- if a required Jira field cannot be discovered or inferred safely, block creation and list the missing field
- keep human identity in reviewer fields, not implementation ownership, unless the board requires a human assignee

## Default Metadata Policy

When local board rules are not more specific:

- issue type: `Task`
- priority: `Medium`, or `High` when it blocks a committed roadmap or release
- estimate: `1w` or the closest Jira estimate field value
- story points: `8` or `13` for a large AI-agent task, depending on board convention
- labels: include `architecture-ready`, `ai-agent`, `implementation`, and `human-review`
- assignee: AI-agent owner role, automation user, or implementation queue supported by the board
- reviewer: human technical owner or review group
- components: derive from service, bounded context, platform area, or repo module
- source docs: include architecture docs, ADRs, diagrams, and implementation plan links

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
- Labels: <labels>
- Fix version or milestone: <version/milestone or Not applicable>
- Estimate: <time estimate>
- Story points: <points or Not applicable>
- Assignee or owner: <AI-agent owner/queue>
- Human reviewer: <reviewer/group>
- Linked issues: <links or Not applicable>
- Dependencies: <dependencies or Not applicable>
- Source docs: <paths/URLs>
- Implementation target: <repo/service/module/package>
- Affected areas: <API/data/security/observability/deployment/docs>
Blocked fields:
- <none or exact missing Jira-required fields>
```

## Review

Before handing off metadata:

- confirm every Jira-required field is present
- confirm labels and components exist or are acceptable on the board
- confirm estimate matches one-week AI-agent scope
- confirm reviewer is human-facing and implementation owner is AI-agent-facing
- confirm source docs are linked precisely enough for review
