---
name: config-secrets-operations-planner
description: Define runtime configuration, secrets ownership, rotation, observability, logging, metrics, tracing, alerts, dashboards, runbooks, support ownership, and operational readiness.
---

# Config Secrets Operations Planner

## Purpose

Make the deployment operable after it is running.
Runtime architecture is incomplete without configuration, secrets, observability, alerting, and support ownership.

## Required Inputs

Require:

- runtime topology
- environment strategy
- network and stateful dependency decisions when available

## Operational Concerns

Define:

- runtime configuration ownership and environment overrides
- secrets ownership, access model, and rotation expectation
- certificate and key lifecycle assumptions
- logs, metrics, traces, and correlation expectations
- dashboards, alerts, and SLO indicators
- health checks and readiness signals
- diagnostic data available to support
- runbooks and escalation paths
- operational access boundaries
- audit and compliance evidence needs

## Output

Return:

| Area | Runtime decision | Owner | Rotation/change rule | Observability/support signal | Risk |
|------|------------------|-------|----------------------|------------------------------|------|

Then list:

- critical configuration rules
- secrets and certificate lifecycle expectations
- required logs, metrics, traces, and alerts
- runbook and escalation needs
- open operations questions
