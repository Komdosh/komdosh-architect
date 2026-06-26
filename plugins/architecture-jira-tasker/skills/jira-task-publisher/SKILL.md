---
name: jira-task-publisher
description: Create the Jira task from a reviewed architecture-derived issue payload, or return a creation-ready payload when Jira tools are unavailable.
---

# Jira Task Publisher

## Purpose

Publish the reviewed task to Jira.
This skill creates the issue only when the payload is complete and the required Jira tools are available.
The published Jira issue must remain human-facing and QA-checkable.
The published or updated Jira issue must be the current working contract, not a placeholder that depends on oral context or private notes.

## Required Inputs

Require:

- reviewed task scope
- filled metadata
- final Jira description
- target Jira project, board, issue type, and required custom fields
- user intent to create or update Jira work
- required product, design, API, architecture, test-plan, environment, release, and related-issue links
- known blockers, assumptions, owners, and evidence locations

## Publishing Rules

Create the Jira issue only after preflight validation.

- use available Jira or Atlassian tools to create the issue
- verify the task targets the actual Jira board
- verify the project, issue type, status, priority, assignee or owner, components, labels, parent epic, related issues, sprint or phase, and required custom fields
- verify estimates, story points, or hours are omitted unless required by the board or explicitly requested by the user
- verify labels are no more than three specific service, application, platform, bounded-context, or capability labels
- verify summary and Jira description body are written in Russian
- verify the description does not expose development details such as file paths, classes, methods, internal modules, local commands, migration scripts, or implementation sequencing
- verify the description does not expose confidential data, secrets, tokens, private incident details, personal data, or hidden requirements
- verify acceptance criteria are split into `Проверяет разработчик` and `Проверяет ручной тестировщик`, or board-required equivalent headings with the same meaning
- verify developer acceptance criteria describe developer/reviewer evidence, and manual tester criteria plus QA validation checks are manually testable without reading code or architecture internals
- verify the `Проверка` section states where evidence will live: CI job, MR, test report, QA note, demo, environment, build, artifact, or linked test plan
- verify required source links are present, or missing materials are explicit blockers or owned open questions
- search for similar existing Jira issues before creating to avoid duplicates
- show the final creation payload in chat and wait for explicit user approval before creating the Jira issue
- for Jira updates, show the field/description diff in chat and wait for explicit user approval before updating
- for Jira updates, keep status, assignee, blockers, important questions, scope, acceptance criteria, MR/design/API/test-plan/release links, and evidence references current
- do not create placeholder issues
- do not create multiple issues unless the user explicitly approves the split
- if Jira requires post-create updates for sprint, epic, required estimate fields, labels, links, or custom fields, perform those updates immediately after creation
- if a field is rejected, fix it using valid Jira values when safe; otherwise stop and report the exact rejected field

## Creation Payload

Prepare a payload with:

```text
Project: <key>
Issue type: <Story|Task|Bug or board-specific type>
Summary: <clear summary>
Description: <self-contained description>
Status: <status>
Priority: <priority>
Labels: <up to three specific labels>
Components: <components>
Epic or parent: <epic>
Sprint or target phase: <sprint/phase>
Fix version or milestone: <version/milestone>
Estimate: <required board value or Not applicable>
Story points: <required board value or Not applicable>
Delivery owner or queue: <team/owner/queue>
Human reviewer: <reviewer/group>
QA owner: <QA owner/group or Not applicable>
Linked issues: <dependencies>
Source docs: <paths/URLs or Not applicable>
Required materials: <design/API/product/test-plan/release links or Not applicable>
Evidence location: <MR/CI/test report/QA note/demo/environment/artifact/test plan or Not applicable>
```

## Output On Success

Return:

```text
Created Jira task: <KEY> <URL>
Board: <board>
Epic or parent: <epic or Not applicable>
Status: <status>
Planning fields: <estimate/story points if required by board, otherwise Not applicable>
Delivery owner or queue: <team/owner/queue>
Human reviewer: <reviewer/group>
QA owner: <QA owner/group or Not applicable>
Labels: <up to three specific labels>
Components: <components>
Evidence location: <MR/CI/test report/QA note/demo/environment/artifact/test plan or Not applicable>
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
