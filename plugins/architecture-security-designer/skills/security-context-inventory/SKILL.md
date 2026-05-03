---
name: security-context-inventory
description: Identify security assets, actors, trust assumptions, sensitive data, privileged paths, external dependencies, compliance constraints, support needs, and unresolved security risks.
---

# Security Context Inventory

## Purpose

Collect the facts that shape security architecture.
Security design starts by knowing what needs protection, who interacts with it, and which assumptions are risky.

## Required Inputs

Require at least one of:

- requirements or scope brief
- actor and role map
- service, data, integration, or deployment design
- existing security, compliance, or privacy constraints

## Inventory Coverage

Consider:

- users, admins, operators, support agents, services, jobs, and external systems
- assets and sensitive data
- privileged operations and operational access
- public, partner, internal, admin, and machine entry points
- trust assumptions and boundary crossings
- tenant, organization, account, or workspace separation
- compliance, privacy, legal, audit, and retention constraints
- known abuse, fraud, misuse, or operational-risk concerns
- incident support and evidence needs

## Output

Return:

| Item | Type | Sensitivity | Actor/owner | Security concern | Open question |
|------|------|-------------|-------------|------------------|---------------|

Then list:

- most important assets
- high-risk actors or privileged paths
- sensitive data and exposure points
- hard security constraints
- missing source context
