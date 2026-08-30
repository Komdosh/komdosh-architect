---
name: architecture
description: Design or review software architecture, including requirements, boundaries, domain, services, data, integrations, runtime qualities, ADR alignment, risks, diagrams, stakeholder acceptance, and delivery handoffs. Use for architecture decisions and artifacts, not ordinary implementation work.
---

# Architecture

Work at the seam the user named. Do not force a full lifecycle or produce a large architecture document when a focused decision, review, diagram, or handoff is enough.

## Evidence

- For an existing system, inspect executable code and runtime configuration before describing current behavior. Treat requirements and accepted decisions as intended constraints; report any drift instead of reconciling it silently.
- Prefer the repository's indexed code-navigation tools when available. Use text search for prose, configuration values, and literals.
- Distinguish confirmed facts, observed implementation, inference, assumptions, and open questions. Cite concrete sources in reviews.
- Make low-risk assumptions explicit. Ask only when a missing fact would materially change the result or make an external write unsafe.

## Route to the needed detail

Read only the references required for the request:

| Work | Reference |
|---|---|
| Requirements, scope, domain language, lifecycles, invariants | [foundations.md](references/foundations.md) |
| Service/module boundaries, data ownership, APIs, events, webhooks, batch | [structure-data.md](references/structure-data.md) |
| Load, deployment, reliability, operations, observability | [runtime-quality.md](references/runtime-quality.md) |
| Security architecture, abuse cases, risk and readiness | [security-risk.md](references/security-risk.md) |
| ADR discovery, drift, architecture or code-backed review | [decisions-review.md](references/decisions-review.md) |
| Architecture diagrams or diagram review | [diagrams.md](references/diagrams.md) |
| Stakeholder acceptance or Jira/delivery handoff | [acceptance-delivery.md](references/acceptance-delivery.md) |

For an end-to-end design, read the relevant design references; the table is a menu, not a mandatory sequence.

## Working rules

- Preserve the user's scope, terminology, chosen technology, and requested artifact format.
- When asked to review or diagnose, report evidence-backed findings; do not redesign or edit unless requested.
- When asked to design, make ownership, boundaries, data movement, failure handling, and operational responsibility explicit.
- Choose products, schemas, deployment manifests, or code only when the requested decision needs that detail. Do not use abstraction-stage rules to withhold detail the user explicitly requested.
- Evaluate alternatives by requirements and tradeoffs. Do not invent options or sections merely to make the output look complete.
- Keep outputs compact and human-readable. Lead with the verdict or decision, then give the evidence, consequences, risks, assumptions, and next action that matter.
- Treat external creation or updates as authorized only when the user's request covers them. Otherwise return a review or creation-ready draft.

## Completion bar

Before claiming readiness, acceptance, or completion, check that:

- each material requirement maps to a responsibility, flow, decision, validation, or explicit gap;
- authoritative owners and trust boundaries are unambiguous;
- important failure, recovery, migration, and lifecycle paths are covered;
- quality targets are measurable where they drive design;
- risks have evidence, consequence, mitigation or acceptance, and an owner when action is required;
- the delivered artifact matches its sources and requested scope.

Do not claim readiness while a material blocker is merely listed as an open question.
