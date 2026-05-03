# Architecture Integration Designer

Architecture Integration Designer is a Codex plugin for API-first and integration architecture.
It comes after service, data, and load decisions are clear enough to define stable interaction contracts.

## Scope Fit

Use this plugin when the requested outcome is:

- integration surface inventory
- API contract strategy and ownership
- public, partner, internal, and service-to-service interface framing
- sync versus async interaction decisions
- event, webhook, callback, batch, and file integration design
- versioning, compatibility, deprecation, and lifecycle policy
- idempotency, retry, timeout, ordering, and compensation rules
- external provider integration boundaries
- security, authorization, rate limits, observability, and support expectations
- integration context, sequence, or collaboration diagrams

This plugin treats APIs as first-class design artifacts.
APIs are easy to extend when designed carefully, but expensive to change or remove after consumers depend on them.

## Skill Grouping

- `$architecture-integration-designer:architecture-integration-designer`: orchestrates the full integration-design pass.
- `$architecture-integration-designer:integration-surface-inventory`: identifies integration surfaces, consumers, producers, ownership, and lifecycle.
- `$architecture-integration-designer:api-contract-strategist`: designs API contract strategy, extensibility, consumer fit, and lifecycle constraints.
- `$architecture-integration-designer:interaction-style-decider`: chooses sync, async, event, webhook, batch, file, or manual integration style.
- `$architecture-integration-designer:event-webhook-designer`: frames event, webhook, callback, ordering, delivery, and consumer semantics.
- `$architecture-integration-designer:batch-file-integration-planner`: frames batch, import/export, file, reconciliation, and schedule-driven integrations.
- `$architecture-integration-designer:resilience-idempotency-planner`: defines retries, idempotency, timeouts, compensation, rate limits, and backpressure.
- `$architecture-integration-designer:versioning-evolution-planner`: defines compatibility, versioning, deprecation, migration, and consumer-support policy.
- `$architecture-integration-designer:integration-security-support-planner`: defines authn/authz, trust, audit, observability, support, and operational ownership.
- `$architecture-integration-designer:integration-diagrammer`: creates integration context, sequence, and collaboration diagrams.
- `$architecture-integration-designer:integration-review-gate`: reviews integration design for API quality and lifecycle readiness.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output is consumer-aware, contract-explicit, lifecycle-aware, resilient, supportable, and ready for later detailed API/schema design.
It should explain why each interface exists, who depends on it, how it evolves, and how failures are handled.

Reject or revise an integration design when it:

- treats APIs as implementation details
- lacks consumer and producer ownership
- has no compatibility or deprecation plan
- hides idempotency, retry, timeout, ordering, or duplicate-delivery semantics
- chooses sync calls for everything without considering load, resilience, or coupling
- leaks external provider language into the core domain
- omits authentication, authorization, rate limits, audit, observability, or support responsibility
- jumps directly to final endpoint schemas or code before contract strategy is sound

## Required Output Shape

The main output should be an integration-design brief with:

- integration design purpose and source context
- integration surfaces and consumers
- API contract strategy
- interaction style decisions
- event, webhook, callback, batch, and file integration rules
- idempotency, retry, timeout, ordering, and compensation rules
- versioning, compatibility, deprecation, and support policy
- security, access, audit, rate limit, and observability expectations
- integration diagrams
- integration risks and alternatives
- assumptions and open questions
- handoff checklist for detailed API/schema and implementation workflow steps
