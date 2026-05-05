---
name: security-support-planner
description: Define integration authentication, authorization, trust boundaries, data exposure, audit, rate limits, observability, diagnostics, support ownership, and operational runbook expectations.
---

# Integration Security Support Planner

## Purpose

Make integrations safe and supportable.
An interface is not production-ready if nobody can secure, observe, diagnose, or support it.

## Required Inputs

Require:

- integration surfaces
- consumer and producer list
- data exposure or trust context when available

## Coverage

For each integration, identify:

- authentication method at architecture level
- authorization owner
- trust boundary
- data exposure and privacy concern
- audit requirement
- rate limit or quota need
- abuse or misuse concern
- correlation ID or tracing expectation
- logs and metrics needed
- support owner
- diagnostic data available to support
- runbook or escalation path

## Output

Return:

| Surface | Auth/trust | Data exposure | Audit/observability | Rate limit | Support owner |
|---------|------------|---------------|---------------------|------------|---------------|

Then list:

- security risks
- support and diagnostics requirements
- operational ownership assumptions
- open security/support questions
