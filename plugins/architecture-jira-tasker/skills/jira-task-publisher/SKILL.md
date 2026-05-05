---
name: jira-task-publisher
description: Create the Jira task from a reviewed architecture-derived issue payload, or return a creation-ready payload when Jira tools are unavailable.
---

# Jira Task Publisher

## Purpose

Publish the reviewed task to Jira.
This skill creates the issue only when the payload is complete and the required Jira tools are available.

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
Labels: <labels>
Components: <components>
Epic or parent: <epic>
Sprint or target phase: <sprint/phase>
Fix version or milestone: <version/milestone>
Estimate: <1w or board equivalent>
Story points: <large-task value or Not applicable>
Assignee or owner: <AI-agent owner/queue>
Human reviewer: <reviewer/group>
Linked issues: <dependencies>
Source docs: <paths/URLs>
```

## Output On Success

Return:

```text
Created Jira task: <KEY> <URL>
Board: <board>
Epic or parent: <epic or Not applicable>
Estimate: <estimate/story points>
Assignee or owner: <AI-agent owner/queue>
Human reviewer: <reviewer/group>
Labels: <labels>
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
