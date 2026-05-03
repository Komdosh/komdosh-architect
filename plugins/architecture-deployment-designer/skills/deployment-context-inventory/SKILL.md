---
name: deployment-context-inventory
description: Identify deployment inputs, runtime constraints, environments, platform assumptions, stateful dependencies, external dependencies, SLOs, compliance, support ownership, and unresolved topology risks.
---

# Deployment Context Inventory

## Purpose

Collect the deployment facts that shape runtime topology.
Deployment design starts by knowing what must run, where it may run, what state it owns, and what operational constraints apply.

## Required Inputs

Require at least one of:

- service/component design
- data and stateful dependency design
- load estimate or SLO target
- integration/external-system design
- existing deployment or platform constraints

## Inventory Coverage

Consider:

- deployment units and runtime processes
- APIs, workers, schedulers, consumers, jobs, and admin tools
- databases, caches, queues, brokers, object stores, search, and file storage
- public, partner, internal, and operational entry points
- environments and promotion path
- regions, AZs, tenants, residency, and compliance constraints
- expected load, peak behavior, latency, availability, RPO, and RTO
- external providers and network egress
- secrets, configuration, observability, and support ownership

## Output

Return:

| Item | Type | Owner | Runtime constraint | Operational risk | Open question |
|------|------|-------|--------------------|------------------|---------------|

Then list:

- hard deployment constraints
- assumptions that affect topology
- missing source context
- high-risk unknowns
- context needed before platform/IaC work
