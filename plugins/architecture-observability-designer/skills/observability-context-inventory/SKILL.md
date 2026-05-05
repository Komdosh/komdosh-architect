---
name: context-inventory
description: Identify user journeys, components, dependencies, integrations, jobs, failure modes, owners, support needs, compliance constraints, and existing observability assumptions.
---

# Observability Context Inventory

## Purpose

Collect the facts that shape observability.
Observability starts with what users do, what can fail, and who must understand the failure.

## Required Inputs

Require at least one of:

- requirements or user journeys
- service, integration, deployment, or security design
- load estimate or SLO context
- incident, support, or operational notes

## Inventory Coverage

Consider:

- critical user journeys and business workflows
- services, APIs, workers, jobs, data stores, queues, external systems, and operational tools
- sync and async flow boundaries
- failure modes, degradation paths, and retry/timeout behavior
- user-visible impact and support impact
- owners, support teams, and escalation paths
- privacy, compliance, retention, and cost constraints for telemetry
- existing metrics, logs, traces, dashboards, alerts, and incident gaps

## Output

Return:

| Item | Type | Owner | User/support impact | Observability need | Open question |
|------|------|-------|---------------------|--------------------|---------------|

Then list:

- critical journeys
- high-risk dependencies
- unknown failure modes
- support and incident needs
- missing source context
