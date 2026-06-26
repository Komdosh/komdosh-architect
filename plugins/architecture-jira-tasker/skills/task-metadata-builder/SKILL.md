---
name: task-metadata-builder
description: Fill human-facing Jira metadata for architecture-derived delivery tasks, avoiding placeholders, unsafe guesses, and implementation detail leaks.
---

# Task Metadata Builder

## Purpose

Build the Jira metadata set for a delivery task created from completed architecture docs.
The metadata must be rich enough for board planning, filtering, ownership, review, and release tracking.
Labels must stay specific and sparse enough to be useful for human filtering and QA routing.
The metadata must keep the task on the actual Jira board with current ownership, priority, status, parent/epic, related issues, blockers, and evidence links.

## Required Inputs

Use:

- scope contract from `$architecture-jira-tasker:task-scope-planner`
- Jira project, board, epic, sprint, issue type, and custom field conventions
- Jira format/profile docs when provided
- source architecture docs and human-visible delivery targets
- known team labels, components, priorities, versions, owners, and reviewers
- required product, design, API, test-plan, release-note, environment, access, and related-issue links
- known assumptions, risks, blockers, and evidence locations

Use Jira tools to inspect valid projects, boards, epics, components, versions, statuses, priorities, and required fields when available.

## Metadata Rules

Fill fields with concrete values.

- do not emit `TBD`, `TODO`, `unknown`, `later`, or empty placeholders
- use `Not applicable` only when the field truly does not apply
- if a required fact is missing, record it as an open question with an owner or as a blocker; do not hide it behind `Not applicable`
- prefer existing Jira values over invented labels, components, epics, or versions
- if a required Jira field cannot be discovered or inferred safely, block creation and list the missing field
- keep assignee, reviewer, QA owner, and owner-role fields human-facing and current
- ensure status reflects the real state for updates; do not leave stale statuses when scope or blockers changed
- choose `Story` for user-facing functionality, `Task` for technical or coordination work without direct user-facing behavior, and `Bug` for broken behavior
- do not create child work as `Epic`; use existing epics/parents from the format profile
- do not use unavailable issue types; if research/spike work has no `Spike` type, use `Task` plus a specific `spike` label when acceptable
- attach each task to the parent/epic required by the format profile, except cross-cutting work that the profile explicitly allows without a parent
- map priority through the target board's profile, such as P0 to `High`, P1 to `Medium`, and P2/P3 to `Low`
- omit estimates, story points, and hours unless the target board requires them or the user explicitly requests them
- use at most three labels, and make each one specific to the service, application, platform, bounded context, or capability
- prefer labels such as `auth` for authorization service work or `mobile` for mobile application work
- do not use broad process labels such as `architecture-ready`, `ai-agent`, `implementation`, or `human-review`
- include source links only when they are required for execution, review, QA, release, or support
- do not expose file paths, class names, internal module names, implementation commands, private execution notes, confidential data, secrets, tokens, private incident details, or personal data in metadata fields

## Default Metadata Policy

When local board rules are not more specific:

- issue type: `Task`
- priority: `Medium`, or `High` when it blocks a committed roadmap or release
- status: the board's initial/backlog status for new tasks, or the current real delivery state for updates
- estimate: omit unless required by the board
- story points: omit unless required by the board
- labels: choose up to three specific labels from the target service, application, platform, bounded context, or capability
- assignee: delivery owner, team queue, or automation user supported by the board
- reviewer: human technical owner or review group
- QA owner: QA owner or review group when the board supports it
- components: derive from service, bounded context, platform area, product area, or application
- source docs: include architecture docs, ADRs, diagrams, and approved handoff notes only when the board expects source references
- evidence links: include MR, CI job, test report, QA note, demo, environment, artifact, or test-plan links when they already exist or are required by the task lifecycle

## Output

Return a metadata block:

```text
Jira metadata:
- Project: <key/name>
- Board: <board>
- Issue type: <type>
- Summary: <summary>
- Status: <status>
- Epic or parent: <epic or Not applicable>
- Sprint or target phase: <sprint/phase or Not applicable>
- Priority: <priority>
- Components: <components>
- Labels: <up to three specific labels>
- Fix version or milestone: <version/milestone or Not applicable>
- Estimate: <required board value or Not applicable>
- Story points: <required board value or Not applicable>
- Delivery owner or queue: <team/owner/queue>
- Human reviewer: <reviewer/group>
- QA owner: <QA owner/group or Not applicable>
- Linked issues: <links or Not applicable>
- Dependencies: <dependencies or Not applicable>
- Source docs: <paths/URLs or Not applicable>
- Required materials: <design/API/product/test-plan/release links or Not applicable>
- Evidence location: <MR/CI/test report/QA note/demo/environment/artifact/test plan or Not applicable>
- Human-visible target: <product/service/application area>
- QA/release context: <environment/build/feature flag/release train or Not applicable>
Blocked fields:
- <none or exact missing Jira-required fields>
```

## Review

Before handing off metadata:

- confirm every Jira-required field is present
- confirm status, assignee, priority, parent/epic, related issues, blockers, and evidence links are current for updates
- confirm labels and components exist or are acceptable on the board
- confirm labels are no more than three items and are specific enough for human routing
- confirm estimates, story points, and hours are omitted unless required by the board or explicitly requested
- confirm assignee, reviewer, and QA owner are human-facing
- confirm source docs are linked precisely enough for review when they are included
- confirm missing critical materials are blockers or owned open questions, not placeholders
- confirm metadata does not leak implementation details
