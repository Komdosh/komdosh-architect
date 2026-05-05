# Architecture Deployment Designer

Architecture Deployment Designer is a Codex plugin for deployment-stage software architecture.
It comes after requirements, scope, domain, service, data, load, and integration decisions are clear enough to place the system into real runtime environments.

## Scope Fit

Use this plugin when the requested outcome is:

- deployment units and runtime topology
- environment strategy for dev, test, staging, production, sandbox, and disaster recovery
- cloud, region, availability-zone, tenant, and data-residency placement
- network boundaries, ingress, egress, trust zones, gateways, DNS, and TLS
- compute/runtime choices at architecture level
- database, cache, queue, broker, object store, search, and file storage placement
- scaling model, autoscaling signals, headroom, quotas, and cost guardrails
- rollout, rollback, migration, compatibility, and release strategy
- backup, restore, failover, RPO, RTO, and disaster recovery expectations
- configuration, secrets, observability, alerting, runbooks, and support ownership
- deployment topology, network, reliability, and rollout diagrams

This plugin designs the runtime architecture.
It should not jump into Terraform, Kubernetes manifests, Helm charts, CI scripts, or cloud-specific resource definitions unless a later implementation workflow asks for them.

## Human-Readable Output

Prefer readability over professional complexity.
Outputs should be compact, self-contained, and easy to scan.

- put the main idea or decision first
- use plain words before specialist terms
- highlight only important decisions, risks, assumptions, open questions, and next steps
- keep details close to the point they explain
- avoid long paragraphs and decorative wording
- explain necessary technical terms in place

## Skill Grouping

- `$architecture-deployment-designer:deployment-designer`: orchestrates the full deployment-design pass.
- `$architecture-deployment-designer:deployment-context-inventory`: identifies runtime constraints, environments, dependencies, and operational assumptions.
- `$architecture-deployment-designer:runtime-topology-designer`: defines deployment units, process/runtime boundaries, and topology.
- `$architecture-deployment-designer:environment-strategy-planner`: defines environment, region, AZ, tenant, data, and promotion strategy.
- `$architecture-deployment-designer:network-boundary-designer`: defines ingress, egress, trust zones, network boundaries, DNS, TLS, and gateway placement.
- `$architecture-deployment-designer:stateful-placement-planner`: places databases, caches, queues, brokers, object stores, search, and files.
- `$architecture-deployment-designer:scaling-capacity-planner`: defines scaling units, autoscaling signals, quotas, headroom, and cost constraints.
- `$architecture-deployment-designer:rollout-release-planner`: defines rollout, rollback, compatibility, migration, and release strategy.
- `$architecture-deployment-designer:reliability-dr-planner`: defines availability, failover, backup, restore, RPO, RTO, and DR posture.
- `$architecture-deployment-designer:config-secrets-ops-planner`: defines config, secrets, observability, alerting, runbooks, and support ownership.
- `$architecture-deployment-designer:deployment-diagrammer`: creates deployment topology, environment, network, reliability, or rollout diagrams.
- `$architecture-deployment-designer:deployment-review-gate`: reviews deployment design for runtime readiness and stage discipline.

Use the namespaced skill form above in Codex prompts.
Directory names are source layout only; runtime skill names come from `SKILL.md` frontmatter.

## Quality Bar

A good output is deployment-realistic, operationally supportable, and implementation-ready for a later platform/IaC workflow.
It should explain what runs where, what owns state, how traffic enters and leaves, how the system scales, how releases move safely, and how failures are recovered.

Reject or revise a deployment design when it:

- treats deployment as an afterthought after logical design
- lacks environment, region, AZ, tenant, or data-residency assumptions
- hides network boundaries, ingress, egress, TLS, or trust relationships
- places stateful dependencies without backup, restore, ownership, or failover expectations
- defines scaling without load signals, bottlenecks, quotas, or cost constraints
- omits rollout, rollback, migration, or compatibility strategy
- ignores configuration, secrets, observability, alerting, runbooks, or support ownership
- jumps directly to Terraform, Kubernetes, Helm, or CI implementation before topology decisions are sound

## Required Output Shape

The main output should be a deployment-design brief with:

- deployment design purpose and source context
- runtime topology and deployment units
- environment, region, AZ, tenant, and data placement strategy
- network boundaries, ingress, egress, DNS, TLS, and trust zones
- stateful dependency placement and ownership
- scaling, capacity, quotas, and cost guardrails
- rollout, rollback, migration, and release strategy
- reliability, backup, restore, failover, RPO, RTO, and DR expectations
- configuration, secrets, observability, alerting, runbooks, and support model
- deployment diagrams
- risks, alternatives, assumptions, and open questions
- handoff checklist for platform, IaC, CI/CD, SRE, and implementation workflow steps
