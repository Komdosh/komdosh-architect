# Acceptance and Delivery Handoff

## Stakeholder acceptance

- Present the architecture in stakeholder language before asking for approval: purpose, scope, main flow, ownership, important decisions, tradeoffs, risks, and operational impact.
- Map material requirements to `covered`, `unclear`, or `missing`. Ask a focused batch of no more than seven questions unless the user requests a full checklist.
- Prefer concrete confirmation or choice questions for decisions and open questions for missing business rules or priorities.
- Use one state: `Accepted`, `Accepted with conditions`, `Needs revision`, or `Blocked`.
- Acceptance requires an explicit decision from an identified role. Silence, vague agreement, or absence of objections is not acceptance.
- Record accepted scope, conditions, required revisions, blockers, open questions, implementation readiness, and the next owner/action.

## Delivery or Jira handoff

- Create delivery work only from sufficiently settled architecture. Unresolved ownership, contract, security, data, or rollout decisions are blockers, not task assumptions.
- Shape work around a coherent outcome and real ownership/release/safety boundaries. Follow the target board's sizing rules; do not impose a universal duration or estimate.
- Discover current project, issue type, workflow, parent, components, labels, required fields, and similar existing issues before creation when tools are available.
- Follow the user's or board's language and format. A useful default body is goal, in scope, out of scope where ambiguity exists, constraints/blockers, observable acceptance criteria, verification evidence, and dependencies.
- Keep the task human-facing. Include code paths, commands, migration steps, or implementation sequencing only when the target team needs them for execution or verification.
- Separate developer/automated evidence from manual QA or operator checks when both apply. Do not invent a manual test section for work that has no manual surface.
- Identify where evidence will live: CI, review, test report, environment, demo, artifact, dashboard, runbook, or linked plan.
- Do not publish placeholders, secrets, personal data, hidden oral agreements, or unsupported metadata.
- A direct request to create or update the issue is authorization for that scoped write. If the user asked only for a draft or review, return a creation-ready payload without mutating Jira.
- After creation or update, return the issue key and URL, final material metadata, and any values the service rejected or normalized.
