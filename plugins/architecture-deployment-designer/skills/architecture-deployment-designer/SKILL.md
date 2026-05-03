---
name: architecture-deployment-designer
description: Design deployment architecture from service, data, load, and integration context, covering runtime topology, environments, network boundaries, stateful dependencies, scaling, rollout, reliability, DR, configuration, secrets, operations, diagrams, assumptions, and handoff readiness.
---

# Architecture Deployment Designer

## Purpose

Design how a software system runs in real environments.
The result must help a system designer translate logical architecture into runtime topology, deployment units, network boundaries, scaling model, rollout strategy, reliability posture, disaster recovery, and operational support expectations before platform-specific implementation starts.

Use this skill when the user asks for deployment architecture, runtime topology, environment strategy, cloud placement, network boundaries, scaling model, rollout strategy, backup/DR, operational readiness, or deployment diagrams.

## Human Readability Rule

Every output must be easy for humans to read:

- start each section with the main idea or decision in plain words
- keep the document compact and remove decorative explanation
- use short sections, tables, and bullets for scanning
- prefer clear words over professional-sounding complexity
- keep details near the point they explain
- highlight only important decisions, risks, assumptions, open questions, and handoff steps
- explain necessary technical terms in place

## Core Rule

Treat deployment architecture as a first-class design stage:

- deployment choices shape availability, security, cost, support, and future operability
- define what runs where before writing Terraform, Kubernetes, Helm, CI, or cloud resource code
- connect runtime topology to service, data, load, and integration decisions
- make environment, region, AZ, tenant, data-residency, and external dependency assumptions explicit
- distinguish stateless deployment units from stateful dependencies and operational control planes
- define ingress, egress, DNS, TLS, gateways, trust zones, and network boundaries
- plan rollout, rollback, compatibility, migrations, failover, backup, restore, observability, and support ownership
- prepare inputs for later platform, IaC, CI/CD, SRE, and implementation workflow plugins

## Required Inputs

Load the minimum needed context:

- service/component design when available
- data ownership and stateful dependency decisions when available
- load estimates and SLO expectations when available
- API and integration surfaces when available
- security, privacy, compliance, data residency, latency, and availability constraints when available
- existing hosting, cloud, platform, CI/CD, or operational constraints when the design must align with a current system

If runtime constraints are unknown, infer conservative assumptions and label them.
Ask when region, data residency, availability, or compliance constraints would materially change deployment topology.

## Skill Flow

1. Use `$architecture-deployment-designer:deployment-context-inventory` to identify runtime constraints, environments, dependencies, and operational assumptions.
2. Use `$architecture-deployment-designer:runtime-topology-designer` to define deployment units, process/runtime boundaries, and topology.
3. Use `$architecture-deployment-designer:environment-strategy-planner` to define environment, region, AZ, tenant, data, and promotion strategy.
4. Use `$architecture-deployment-designer:network-boundary-designer` to define ingress, egress, trust zones, gateways, DNS, and TLS.
5. Use `$architecture-deployment-designer:stateful-dependency-placement-planner` to place databases, caches, queues, brokers, object stores, search, and files.
6. Use `$architecture-deployment-designer:scaling-capacity-planner` to define scaling units, autoscaling signals, quotas, headroom, and cost constraints.
7. Use `$architecture-deployment-designer:rollout-release-planner` to define rollout, rollback, migration, compatibility, and release strategy.
8. Use `$architecture-deployment-designer:reliability-dr-planner` to define availability, failover, backup, restore, RPO, RTO, and DR posture.
9. Use `$architecture-deployment-designer:config-secrets-operations-planner` to define config, secrets, observability, alerting, runbooks, and support ownership.
10. Use `$architecture-deployment-designer:deployment-diagrammer` when deployment diagrams clarify decisions.
11. Use `$architecture-deployment-designer:deployment-review-gate` before final delivery.

## Output Contract

Return a self-contained deployment-design brief with this structure unless the user asks for another format:

1. Deployment design purpose
2. Source context
3. Runtime topology and deployment units
4. Environment, region, AZ, tenant, and data placement strategy
5. Network boundaries, ingress, egress, DNS, TLS, and trust zones
6. Stateful dependency placement and ownership
7. Scaling, capacity, quotas, and cost guardrails
8. Rollout, rollback, migration, and release strategy
9. Reliability, backup, restore, failover, RPO, RTO, and DR expectations
10. Configuration, secrets, observability, alerting, runbooks, and support model
11. Deployment diagrams
12. Deployment risks and alternatives
13. Assumptions
14. Open questions
15. Handoff checklist for platform, IaC, CI/CD, SRE, and implementation steps

## Deployment Discipline

Do not jump directly to platform implementation:

- do not write Terraform, Kubernetes, Helm, CI/CD, Docker Compose, or cloud resource manifests unless the user asks for the implementation stage
- do not pick a managed service by vendor name unless the architecture context requires or already constrains it
- do not hide unresolved availability, residency, compliance, or cost assumptions
- do not place stateful systems without backup, restore, failover, retention, and ownership expectations
- do not define autoscaling without signals, limits, saturation behavior, and cost implications
- do not treat production and non-production environments as identical without explaining why

You may state deployment-level architecture decisions:

- this service should run as stateless horizontal replicas behind an ingress boundary
- this worker pool scales on queue depth and must have a concurrency cap to protect the database
- this database is the recovery anchor and needs point-in-time restore with an explicit RPO/RTO
- this external provider call should leave through controlled egress with audit and rate controls
- this release path needs canary plus rollback because the public API contract is long-lived

## Stop Conditions

Stop and ask when:

- region, data residency, or compliance constraints are central and unknown
- availability target, RPO, or RTO would materially change topology
- production platform constraints are unknown and would make the design misleading
- stateful dependency ownership or backup responsibility is unclear
- the user asks for infrastructure code while topology and operations decisions are unresolved
