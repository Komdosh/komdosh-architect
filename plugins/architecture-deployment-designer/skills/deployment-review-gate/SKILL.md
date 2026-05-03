---
name: deployment-review-gate
description: Review deployment architecture for topology clarity, environment readiness, network boundaries, stateful dependency ownership, scaling, rollout, reliability, DR, operations, and stage discipline.
---

# Deployment Review Gate

## Purpose

Review deployment design before platform, IaC, CI/CD, SRE, or implementation work.
Find unresolved runtime assumptions, unsafe topology, hidden network exposure, weak recovery posture, and premature platform implementation.

## Required Inputs

Require:

- deployment-design brief or exact diff
- service/data/load/integration context when available
- diagrams when produced

If only a deployment brief is provided, review internal coherence and state that source alignment was not verified.

## DEPLOY Review

Use `DEPLOY`:

| Check | Question |
|-------|----------|
| `D` Deployment units | Are runtime units, stateless/stateful roles, owners, and scaling boundaries clear? |
| `E` Environments | Are environments, regions, AZs, tenants, data boundaries, and promotion paths defined? |
| `P` Perimeter | Are ingress, egress, DNS, TLS, trust zones, and network controls explicit? |
| `L` Lifecycle | Are rollout, rollback, migration, compatibility, and release gates defined? |
| `O` Operations | Are config, secrets, observability, alerts, runbooks, and support owners covered? |
| `Y` Yield under failure | Are availability, failover, backup, restore, RPO, RTO, and DR expectations clear? |

Also check:

- stateful dependencies have placement, ownership, backup, restore, and recovery expectations
- scaling strategy is grounded in load signals, quotas, bottlenecks, and cost guardrails
- diagrams match written topology and boundary decisions
- platform/IaC details are deferred when topology decisions are still the goal

## Blockers

Treat these as blockers:

- production topology lacks deployment units or owners
- public ingress or external egress is undefined
- stateful dependency has no owner, backup, restore, or failover posture
- region, AZ, data-residency, compliance, or tenant placement is missing when relevant
- scaling has no signals, limits, protected dependencies, or cost guardrails
- rollout has no rollback, migration, compatibility, or validation strategy
- RPO, RTO, failover, or DR expectations are missing for critical state
- secrets, configuration, observability, alerting, or support ownership is omitted
- output jumps to Terraform, Kubernetes, Helm, CI scripts, or cloud resource definitions before topology decisions are sound
- diagrams contradict written placement, traffic direction, or ownership

## Output

Return either:

```text
DEPLOY: pass
Deployment readiness: pass
```

or:

```text
DEPLOY: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the deployment design, provide the corrected section or full revised deployment-design brief.
