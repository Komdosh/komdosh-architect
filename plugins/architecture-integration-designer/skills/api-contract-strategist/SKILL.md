---
name: api-contract-strategist
description: Design API contract strategy, consumer fit, resource/action boundaries, extensibility rules, compatibility constraints, contract ownership, and public/internal API lifecycle without final schemas.
---

# API Contract Strategist

## Purpose

Make APIs first-class design artifacts.
An API should be easy to extend, but changes and removals must be treated as high-cost lifecycle decisions.

## Required Inputs

Require:

- integration surface inventory
- consumers and producers
- domain/service/data context

## API Strategy Questions

Answer:

- Who is the consumer and what job does the API support?
- Is the API public, partner, internal, or operational?
- What domain language should be stable in the contract?
- Which concepts are safe to expose and which must remain internal?
- What is the extension model?
- Which fields, operations, or meanings are likely to change?
- What is additive versus breaking?
- Who owns documentation, examples, support, and lifecycle?
- What should be intentionally omitted to avoid locking unstable design?

## API Design Rules

- Prefer consumer tasks and stable domain concepts over internal data structures.
- Keep public and partner APIs additive by default.
- Avoid exposing internal enum values that are likely to change without an extension strategy.
- Reserve room for future fields, filters, states, pagination, localization, and partial failures when relevant.
- Treat delete, rename, semantic narrowing, and required-field additions as breaking changes.
- Distinguish command APIs from query APIs.
- Keep error model, idempotency, and correlation expectations visible.

## Output

Return:

| API surface | Consumer | Contract strategy | Extension rule | Breaking-change risk | Owner |
|-------------|----------|-------------------|----------------|----------------------|-------|

Then list:

- stable contract concepts
- intentionally hidden internal concepts
- extension points
- lifecycle and documentation responsibilities
- deferred schema decisions
