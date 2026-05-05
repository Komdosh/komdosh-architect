---
name: integration-designer
description: Design API-first and integration architecture from service, data, load, and external-system context, covering surfaces, contracts, interaction styles, events, webhooks, batch, resilience, idempotency, versioning, security, observability, support, diagrams, assumptions, and handoff readiness.
---

# Architecture Integration Designer

## Purpose

Design interfaces that systems and consumers can safely depend on.
The result must help a system designer define integration surfaces, API contract strategy, collaboration style, resilience semantics, versioning, security, and support expectations before low-level schemas or code are written.

Use this skill when the user asks for API design strategy, integration architecture, external-system integration, service-to-service contracts, event design, webhook design, batch/file integration, versioning, idempotency, retries, or integration diagrams.

## Human Readability Rule

Every output must be easy for humans to read:

- start each section with the main idea or decision in plain words
- keep the document compact and remove decorative explanation
- use short sections, tables, and bullets for scanning
- prefer clear words over professional-sounding complexity
- keep details near the point they explain
- highlight only important decisions, risks, assumptions, open questions, and handoff steps
- explain necessary technical terms in place

## Core Rule

Treat APIs and integration contracts as first-class architecture:

- APIs are easy to extend but hard to change or remove after adoption
- identify consumers, producers, owners, lifecycle, and support responsibility before contract details
- choose interaction style deliberately, not by defaulting to synchronous calls
- design for compatibility, versioning, deprecation, observability, and operational support
- make idempotency, retries, timeouts, ordering, duplicate delivery, and compensation explicit
- protect internal domain language from external provider concepts
- prepare inputs for later detailed API, schema, implementation, and ADR workflow plugins

## Required Inputs

Load the minimum needed context:

- service/component design when available
- data ownership and data contracts when available
- load estimates when available
- external-system landscape and integration expectations when available
- security, privacy, compliance, latency, availability, and support constraints when available
- existing API, event, webhook, or batch contracts when the design must align with a current system

If contract consumers are unknown, infer likely consumer groups and label assumptions.
Ask when unknown consumers or compatibility expectations would make API design misleading.

## Skill Flow

1. Use `$architecture-integration-designer:integration-surface-inventory` to identify surfaces, consumers, producers, owners, and lifecycle.
2. Use `$architecture-integration-designer:api-contract-strategist` to define API contract strategy and extensibility rules.
3. Use `$architecture-integration-designer:interaction-style-decider` to choose sync, async, event, webhook, batch, file, or manual integration style.
4. Use `$architecture-integration-designer:event-webhook-designer` to frame event, webhook, callback, ordering, and delivery semantics.
5. Use `$architecture-integration-designer:batch-file-integration-planner` to frame batch, import/export, reconciliation, and schedule-driven integrations.
6. Use `$architecture-integration-designer:resilience-idempotency-planner` to define retries, idempotency, timeouts, compensation, rate limits, and backpressure.
7. Use `$architecture-integration-designer:versioning-evolution-planner` to define compatibility, versioning, deprecation, and migration policy.
8. Use `$architecture-integration-designer:security-support-planner` to define security, trust, audit, observability, and support ownership.
9. Use `$architecture-integration-designer:integration-diagrammer` when integration diagrams clarify decisions.
10. Use `$architecture-integration-designer:integration-review-gate` before final delivery.

## Output Contract

Return a self-contained integration-design brief with this structure unless the user asks for another format:

1. Integration design purpose
2. Source context
3. Integration surfaces and consumers
4. API contract strategy
5. Interaction style decisions
6. Event, webhook, callback, batch, and file integration rules
7. Idempotency, retry, timeout, ordering, and compensation rules
8. Versioning, compatibility, deprecation, and support policy
9. Security, authorization, audit, rate limit, and trust boundaries
10. Observability and support expectations
11. Integration diagrams
12. Integration risks and alternatives
13. Assumptions
14. Open questions
15. Handoff checklist for detailed API/schema and implementation steps

## API Design Discipline

Do not jump directly to final API implementation:

- do not write full OpenAPI, GraphQL, gRPC, event, or file schemas unless the user asks for the detailed contract stage
- do not choose framework-specific controllers, routes, clients, or serialization libraries
- do not expose internal data models as external contracts
- do not remove or rename public concepts without migration and deprecation strategy
- do not treat versioning as optional when external or long-lived consumers exist

You may state contract-level architecture decisions:

- this public API needs additive evolution only and explicit deprecation windows
- this callback must be idempotent because the provider retries
- this event is a business fact and can be consumed asynchronously
- this partner integration needs an anti-corruption adapter
- this query should be internal only because it exposes unstable domain language

## Stop Conditions

Stop and ask when:

- API consumers are unknown and cannot be safely inferred
- public or partner contract lifecycle expectations are missing
- security or data exposure risk is central but unknown
- event/webhook delivery semantics would affect correctness and are unspecified
- the user asks for final schema/code while contract strategy is unresolved
