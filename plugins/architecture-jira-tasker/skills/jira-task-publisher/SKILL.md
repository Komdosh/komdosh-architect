---
name: jira-task-publisher
description: Create the Jira task from a reviewed architecture-derived issue payload, or return a creation-ready payload when Jira tools are unavailable.
---

# Jira Task Publisher

## Purpose

Publish the reviewed task to Jira.
This skill creates the issue only when the payload is complete and the required Jira tools are available.
The published Jira issue must remain human-facing and QA-checkable.

## Required Inputs

Require:

- reviewed task scope
- filled metadata
- final Jira description
- target Jira project, board, issue type, and required custom fields
- user intent to create or update Jira work

## Publishing Rules

Create the Jira issue only after preflight validation.

- use available Jira or Atlassian tools to create the issue
- verify the project, issue type, priority, components, labels, parent epic, sprint, estimate, story points, and required custom fields
- verify labels are no more than three specific service, application, platform, bounded-context, or capability labels
- verify the description does not expose development details such as file paths, classes, methods, internal modules, local commands, migration scripts, or implementation sequencing
- verify QA acceptance criteria and QA validation checks are understandable without reading code or architecture internals
- do not create placeholder issues
- do not create multiple issues unless the user explicitly approves the split
- if Jira requires post-create updates for sprint, epic, estimate, labels, links, or custom fields, perform those updates immediately after creation
- if a field is rejected, fix it using valid Jira values when safe; otherwise stop and report the exact rejected field

## Creation Payload

Prepare a payload with:

```text
Project: <key>
Issue type: Task
Summary: <clear summary>
Description: <self-contained description>
Priority: <priority>
Labels: <up to three specific labels>
Components: <components>
Epic or parent: <epic>
Sprint or target phase: <sprint/phase>
Fix version or milestone: <version/milestone>
Estimate: <1w or board equivalent>
Story points: <large-task value or Not applicable>
Delivery owner or queue: <team/owner/queue>
Human reviewer: <reviewer/group>
QA owner: <QA owner/group or Not applicable>
Linked issues: <dependencies>
Source docs: <paths/URLs or Not applicable>
```

## Output On Success

Return:

```text
Created Jira task: <KEY> <URL>
Board: <board>
Epic or parent: <epic or Not applicable>
Estimate: <estimate/story points>
Delivery owner or queue: <team/owner/queue>
Human reviewer: <reviewer/group>
QA owner: <QA owner/group or Not applicable>
Labels: <up to three specific labels>
Components: <components>
Residual risks: <none or concise list>
```

## Output When Jira Tools Are Unavailable

Return:

```text
Jira task not created because Jira tools are unavailable in this session.
Creation-ready payload:
<payload>
```

## Output When Creation Is Blocked

Return:

```text
Jira task not created.
Blocking field: <field>
Reason: <why creation would produce an incomplete or invalid Jira issue>
Next action: <exact lookup or user input needed>
```
