---
name: trust-boundary-mapper
description: Map trust zones, boundary crossings, threat surfaces, exposed entry points, privileged paths, data movement, external dependencies, and required control points.
---

# Trust Boundary Mapper

## Purpose

Show where trust changes.
Most security decisions come from understanding who crosses a boundary, what they can reach, and what control point must exist there.

## Required Inputs

Require:

- security context inventory
- scope or deployment/integration context when available

## Boundary Concerns

Define:

- public, partner, internal, admin, operational, and data trust zones
- users, services, jobs, and external systems crossing each boundary
- ingress, egress, callbacks, events, batch, files, and admin paths
- data entering, leaving, or changing sensitivity
- control points: authentication, authorization, validation, rate limits, audit, monitoring
- trust assumptions that need proof or monitoring
- attack surface and misuse surface at architecture level

## Output

Return:

| Boundary | Source | Destination | Trust change | Main risk | Required control |
|----------|--------|-------------|--------------|-----------|------------------|

Then list:

- highest-risk boundary crossings
- exposed entry points
- privileged paths
- assumptions that need validation
- controls to carry into later design steps
