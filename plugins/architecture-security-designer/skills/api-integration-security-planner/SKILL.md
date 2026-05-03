---
name: api-integration-security-planner
description: Define architecture-level security controls for public, partner, internal, admin, service-to-service, event, webhook, callback, batch, file, and external provider integrations.
---

# API Integration Security Planner

## Purpose

Protect system interfaces.
APIs and integrations are durable attack surfaces, so their security controls must be clear before detailed schemas and implementation are written.

## Required Inputs

Require:

- integration or API design
- trust boundary map
- identity and authorization context when available

## Interface Security Concerns

Define:

- public, partner, internal, admin, and service-to-service API controls
- event, webhook, callback, batch, file, and external provider controls
- authentication and authorization expectations per interface
- input validation and output exposure expectations at architecture level
- replay, spoofing, tampering, and duplicate-message risk
- rate limits, quotas, abuse controls, and backpressure
- idempotency and signature requirements when relevant
- versioning and deprecation security implications
- audit, monitoring, and incident support for interfaces

## Output

Return:

| Interface | Exposure | Required controls | Abuse risk | Audit/monitoring | Owner |
|-----------|----------|-------------------|------------|------------------|-------|

Then list:

- high-risk interfaces
- replay/spoofing protections
- abuse and quota controls
- security expectations for external systems
- open interface-security questions
