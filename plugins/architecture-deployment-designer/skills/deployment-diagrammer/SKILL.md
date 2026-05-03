---
name: deployment-diagrammer
description: Create architecture-level deployment topology, environment, network, stateful dependency, scaling, rollout, reliability, and disaster recovery diagrams from source-backed deployment decisions.
---

# Deployment Diagrammer

## Purpose

Visualize deployment architecture.
Diagrams should show runtime placement, boundaries, traffic paths, stateful dependencies, scaling points, and recovery posture without becoming infrastructure manifests.

## Required Inputs

Require:

- runtime topology
- environments and placement decisions
- network boundaries
- stateful dependencies
- reliability or rollout decisions when relevant
- requested format when the user needs Mermaid, DrawIO, or another output

If deployment inputs are missing, route back to `$architecture-deployment-designer:architecture-deployment-designer`.

## Diagram Types

Use a deployment topology diagram when the goal is:

- deployment units, runtime roles, and dependencies
- stateless versus stateful placement
- scaling groups

Use an environment or region diagram when the goal is:

- dev/stage/prod/DR boundaries
- region, AZ, tenant, or data-residency placement

Use a network diagram when the goal is:

- ingress, egress, gateways, public/private boundaries, and trust zones

Use a reliability or DR diagram when the goal is:

- failover, backup, restore, recovery anchors, and degradation paths

Use a rollout diagram when the goal is:

- deployment order, canary/blue-green flow, migration steps, and rollback points

## Diagram Rules

- Label nodes with deployment role, not implementation class names.
- Label edges with traffic direction, protocol category, or operational meaning when relevant.
- Mark external systems and managed dependencies outside the owned deployment boundary.
- Show public/private/trust boundaries clearly.
- Show stateful dependencies and recovery anchors explicitly.
- Do not show Terraform resources, Kubernetes YAML fields, Helm templates, CI jobs, or cloud resource IDs.

## Output

Return:

- diagram purpose
- deployment topology, environment, network, reliability, DR, or rollout diagram
- source-assumption note
- diagram limitations for later platform/IaC design
