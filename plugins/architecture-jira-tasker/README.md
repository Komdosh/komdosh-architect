# Architecture Jira Tasker

Architecture Jira Tasker is a Codex plugin for creating Jira implementation tasks after architecture documentation is complete.
It turns architecture docs into large, self-contained delivery tasks for fast AI agents.

## Scope Fit

Use this plugin when the requested outcome is:

- read completed architecture docs and create an implementation task
- convert architecture decisions, constraints, diagrams, ADRs, and implementation notes into Jira work
- produce one large task sized around one AI-agent delivery week
- fill Jira metadata, including project, issue type, priority, labels, component, epic, sprint, estimate, owner, reviewer, dependencies, source docs, and release context
- write a task description that an implementation agent can execute without asking for architectural context
- create the task on a Jira board when Jira tools are available

Do not use it for unsettled architecture work.
If the architecture is not done, send the work back to the relevant architecture plugin or workflow before creating Jira delivery tasks.

## Delivery Model

The task is for an AI implementation agent, not a human developer.

- default issue size is one coherent implementation slice of about one calendar week
- small tickets should be merged into a larger, reviewable delivery task
- split only when independent review, ownership, release, or risk boundaries require separate tasks
- human participation belongs in review, approval, and merge sections only
- the issue must include enough context for the AI agent to implement, test, document, and prepare for human review

## Skill Grouping

- `$architecture-jira-tasker:architecture-jira-tasker`: orchestrates the full architecture-docs-to-Jira flow.
- `$architecture-jira-tasker:task-scope-planner`: shapes the implementation scope and confirms one-week sizing.
- `$architecture-jira-tasker:task-metadata-builder`: fills Jira metadata and delivery ownership fields.
- `$architecture-jira-tasker:jira-description-builder`: writes the self-contained Jira issue description.
- `$architecture-jira-tasker:jira-task-publisher`: creates the Jira issue or returns a creation-ready payload.
- `$architecture-jira-tasker:task-review-gate`: reviews the draft task before creation.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good task lets an AI agent start implementation immediately.
It should include:

- architecture source links and important decisions
- implementation goal and business outcome
- exact scope and out-of-scope boundaries
- repo, package, module, service, API, data, security, observability, and deployment expectations when applicable
- dependencies and sequencing
- acceptance criteria, negative paths, and validation commands
- documentation updates
- human review checklist
- Jira metadata filled from board context or explicit assumptions

Reject or revise a task when it:

- is smaller than a meaningful AI-agent delivery slice
- depends on undocumented architecture decisions
- leaves metadata as placeholders
- hides dependencies or migration/release risk
- gives a human developer implementation work outside review
- contains only prose without acceptance criteria and validation steps
- creates a Jira issue before required board fields are known
