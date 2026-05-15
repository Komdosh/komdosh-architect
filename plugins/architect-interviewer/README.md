# Architect Interviewer

Architect Interviewer is a Codex plugin for architecture acceptance conversations.
It presents a completed service architecture, interviews stakeholders against the requirements, and records whether the architecture is accepted or needs revision.

## Scope Fit

Use this plugin when the requested outcome is:

- present a completed architecture to a stakeholder for review
- verify that every known requirement is covered by the architecture
- interview the user about missing requirements, unclear tradeoffs, risks, and acceptance criteria
- distinguish accepted decisions from conditional acceptance and required revisions
- produce a concise acceptance record that later implementation or Jira handoff can trust

Do not use it to invent the architecture from scratch.
If the architecture is not ready to present, send the work back to the relevant architecture design plugin first.

## Interview Model

The plugin acts as the architect who designed the service and now needs stakeholder confirmation.

- present the architecture in plain language before asking for approval
- ask focused questions instead of a generic "is this okay?"
- keep each interview round short enough for a human to answer
- trace questions back to requirements, assumptions, decisions, risks, or user journeys
- record explicit acceptance, conditional acceptance, requested changes, and blocked decisions
- do not mark architecture accepted while unresolved required requirements remain

## Skill Grouping

- `$architect-interviewer:architect-interviewer`: orchestrates the full presentation and acceptance interview.
- `$architect-interviewer:architecture-brief-presenter`: prepares a concise stakeholder-facing architecture presentation.
- `$architect-interviewer:requirement-coverage-interviewer`: checks requirements coverage and asks gap-focused questions.
- `$architect-interviewer:interview-question-planner`: prepares the next focused question set for the stakeholder.
- `$architect-interviewer:decision-acceptance-checker`: records accepted decisions, conditional decisions, required revisions, and blockers.
- `$architect-interviewer:architecture-acceptance-review-gate`: reviews whether the architecture can be accepted.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good acceptance interview produces:

- a short architecture presentation the stakeholder can understand
- a requirements coverage summary with explicit gaps
- targeted questions grouped by business behavior, users, integrations, data, security, operations, and delivery impact
- clear decisions: accepted, accepted with conditions, needs revision, or blocked
- follow-up changes with owners and source references
- an acceptance record that implementation agents can treat as reviewed context

Reject or revise the acceptance record when it:

- asks only broad confirmation questions
- hides uncovered requirements or assumptions
- treats silence as approval
- mixes new architecture design with stakeholder acceptance
- claims acceptance without a named decision maker or clear confirmation
- leaves required revisions without owner, scope, or next action
