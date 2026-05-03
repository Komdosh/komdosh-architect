---
name: architecture-assumption-planner
description: Identify explicit assumptions, future expansion needs, support expectations, risks, and architecture implications without prematurely designing the solution.
---

# Architecture Assumption Planner

## Purpose

Make the useful thinking around requirements explicit.
Good assumptions help architecture move forward; hidden assumptions create bad architecture.

## Required Inputs

Require:

- product goal or requirements draft
- known facts and open questions
- any user-provided constraints

## Assumption Rules

- Label assumptions with stable IDs.
- Prefer assumptions that are reversible or cheap to validate.
- Do not make assumptions that hide legal, safety, security, privacy, or financial risk.
- State how an assumption affects architecture.
- Turn high-risk assumptions into open questions or validation tasks.

## Future Expansion Thinking

Identify likely expansion across:

- user segments and roles
- geographic markets, localization, currencies, language, and regulation
- volume, traffic, data growth, and tenant count
- new channels, devices, clients, APIs, or partner integrations
- workflow variants, rule engines, approval policies, and configuration
- analytics, reporting, experimentation, and personalization
- support tooling, admin operations, audit, disputes, and investigations
- migration from MVP to durable product architecture

## Architecture Implication Rules

State implications without over-designing:

- acceptable: `Requirements imply explicit data ownership for account state.`
- acceptable: `Requirements imply idempotency for payment callbacks.`
- acceptable: `Future partner integrations imply versioned external contracts.`
- avoid: `Use PostgreSQL, Kafka, Kubernetes, and microservices.`

## Output

Return:

- assumption table with impact and validation path
- open question table with architecture impact
- future expansion requirements
- support, maintenance, and operations expectations
- architecture implications and constraints
- risks that must be resolved before architecture design
