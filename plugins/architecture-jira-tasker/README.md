# Architecture Jira Tasker

Architecture Jira Tasker is a Codex plugin for creating Jira delivery tasks after architecture documentation is complete.
It turns architecture docs into large, self-contained Jira delivery tasks for humans, with QA-checkable criteria and no leaked development details.
Each task is treated as a working contract: what must be done, why, where the boundaries are, and how the result will be verified.

## Scope Fit

Use this plugin when the requested outcome is:

- read completed architecture docs and create a delivery task
- convert architecture decisions, constraints, diagrams, ADRs, and implementation notes into Jira work
- produce one large task sized around one delivery week
- apply a provided Jira format profile for project, issue type, priority, parent/epic, workflow, description shape, and testing rules
- fill Jira metadata, including project, issue type, priority, up to three specific labels, component, parent/epic, sprint or phase, owner, reviewer, QA owner, dependencies, source docs, and release context
- write a structured Jira summary and task description in Russian that product, QA, reviewers, release managers, and support can understand
- keep the description short enough for a team lead to understand in about 30 seconds
- capture important agreements, constraints, risks, blockers, evidence locations, and required links in the task instead of private messages or comments
- keep file paths, classes, internal modules, developer commands, migration scripts, and code-level sequencing out of the Jira issue
- keep confidential data, secrets, tokens, private incident details, personal data, and hidden requirements out of the Jira issue
- omit estimates, story points, and hours unless the board requires them or the user explicitly asks for them
- propose the full task first, wait for explicit approval, and search for duplicates before creating Jira work
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
- detailed QA steps belong in a separate test plan when the result can be checked in a running app, database, or networked environment
- during updates, status, assignee, blockers, important questions, scope, acceptance criteria, MR/design/API/test-plan/release links, and evidence references must stay current

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
- human handoff summary with product/service/application area, owner, reviewer, QA owner, and labels
- exact human-visible scope and out-of-scope boundaries
- behavior, business rules, security/privacy constraints, rollout constraints, and operational expectations when applicable
- dependencies and sequencing
- acceptance criteria split into `Проверяет разработчик` and `Проверяет ручной тестировщик`, or board-required equivalent headings with the same developer/manual QA separation
- developer checks covering code/build/lint/test/schema/contract/MR evidence, and manual tester checks covering UI, UX, actions, animations, functionality, negative paths, permissions, documentation, and release checks
- a `Проверка` section with the evidence location: CI job, MR, test report, QA note, demo, environment, build, artifact, or linked test plan
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
- leaks confidential data, secrets, tokens, private incident details, personal data, or hidden requirements
- is not written in Russian
- lacks split developer/manual tester acceptance criteria
- lacks manually testable QA acceptance criteria and validation context
- is too long to understand in about 30 seconds
- includes estimates when the target format says the team lead owns estimates
- skips duplicate search or creates/updates Jira before explicit approval
- hides dependencies or migration/release risk
- contains only prose without acceptance criteria and verification evidence
- creates a Jira issue before required board fields are known
