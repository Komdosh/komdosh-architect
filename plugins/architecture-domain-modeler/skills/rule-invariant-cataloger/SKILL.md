---
name: rule-invariant-cataloger
description: Catalog business rules, policies, validations, invariants, consistency expectations, exception rules, and change-prone rule areas for architecture modeling.
---

# Rule Invariant Cataloger

## Purpose

Capture the rules the architecture must preserve.
Rules and invariants define where consistency, ownership, audit, and policy flexibility matter.

## Required Inputs

Require:

- domain concepts or requirements
- known workflows, policies, constraints, or lifecycle facts

## Rule Types

Consider:

- eligibility rules
- permission and authorization rules
- state transition guards
- validation rules
- uniqueness rules
- pricing, ranking, routing, assignment, or matching policies
- quota, limit, threshold, or rate rules
- compliance, retention, audit, and consent rules
- exception and override rules
- consistency and atomicity expectations
- rules likely to change by market, tenant, plan, role, or time

## Invariant Rules

Write invariants as durable statements:

- `An order cannot be fulfilled before it is paid.`
- `A verified identity claim must have an issuer and verification time.`
- `A cancelled reservation cannot be consumed.`

Avoid implementation-specific statements:

- not `The database must have a unique index.`
- not `The service should call Kafka.`

## Output

Return:

| ID | Rule/invariant | Applies to | Enforcement moment | Change likelihood | Architecture impact |
|----|----------------|------------|--------------------|-------------------|---------------------|

Then list:

- high-risk invariants
- policy areas likely to become configurable
- consistency assumptions
- unresolved rule questions
