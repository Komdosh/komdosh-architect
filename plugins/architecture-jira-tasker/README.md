# Architecture Jira Tasker

Architecture Jira Tasker is a Codex plugin for creating Jira delivery tasks after architecture documentation is complete.
It turns architecture docs into large, self-contained Jira delivery tasks for humans, with QA-checkable criteria and no leaked development details.

## Scope Fit

Use this plugin when the requested outcome is:

- read completed architecture docs and create a delivery task
- convert architecture decisions, constraints, diagrams, ADRs, and implementation notes into Jira work
- produce one large task sized around one delivery week
- fill Jira metadata, including project, issue type, priority, up to three specific labels, component, epic, sprint, estimate, owner, reviewer, dependencies, source docs, and release context
- write a structured task description that product, QA, reviewers, release managers, and support can understand
- keep file paths, classes, internal modules, developer commands, migration scripts, and code-level sequencing out of the Jira issue
- create the task on a Jira board when Jira tools are available

Do not use it for unsettled architecture work.
If the architecture is not done, send the work back to the relevant architecture plugin or workflow before creating Jira delivery tasks.

## Delivery Model

The Jira task is for humans, even when implementation is later performed by an AI agent or automation.

- default issue size is one coherent delivery slice of about one calendar week
- small tickets should be merged into a larger, reviewable delivery task
- split only when independent review, ownership, release, or risk boundaries require separate tasks
- the issue must include enough context for humans to understand outcome, scope, QA validation, release impact, and review evidence
- implementation plans belong in architecture docs, pull requests, or private execution notes, not in the Jira task body

## Skill Grouping

- `$architecture-jira-tasker:architecture-jira-tasker`: orchestrates the full architecture-docs-to-Jira flow.
- `$architecture-jira-tasker:task-scope-planner`: shapes the human-visible delivery scope and confirms one-week sizing.
- `$architecture-jira-tasker:task-metadata-builder`: fills Jira metadata, delivery ownership, and QA ownership fields.
- `$architecture-jira-tasker:jira-description-builder`: writes the human-readable, QA-checkable Jira issue description.
- `$architecture-jira-tasker:jira-task-publisher`: creates the Jira issue or returns a creation-ready payload.
- `$architecture-jira-tasker:task-review-gate`: reviews the draft task before creation.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good task lets humans understand what is being delivered and how QA can check it.
It should include:

- goal and business outcome
- human handoff summary with product/service/application area, owner, reviewer, QA owner, labels, and estimate
- exact human-visible scope and out-of-scope boundaries
- behavior, business rules, security/privacy constraints, rollout constraints, and operational expectations when applicable
- dependencies and sequencing
- QA acceptance criteria, negative paths, test data, environment/build context, and regression checks
- documentation, release, support, or operator updates
- human review checklist
- Jira metadata filled from board context or explicit assumptions
- no more than three specific labels, such as `auth` for authorization service work or `mobile` for mobile application work

Reject or revise a task when it:

- is smaller than a meaningful delivery slice
- depends on undocumented architecture decisions
- leaves metadata as placeholders
- uses more than three labels or generic labels such as `architecture-ready`, `ai-agent`, `implementation`, or `human-review`
- leaks development details such as file paths, internal modules, classes, developer commands, migration scripts, or code-level sequencing
- lacks QA-checkable acceptance criteria and validation context
- hides dependencies or migration/release risk
- contains only prose without acceptance criteria and validation steps
- creates a Jira issue before required board fields are known
