---
name: network-boundary-designer
description: Define deployment network boundaries, ingress, egress, public/private zones, trust boundaries, gateways, DNS, TLS, service-to-service connectivity, external provider access, and network observability.
---

# Network Boundary Designer

## Purpose

Design how traffic enters, moves through, and leaves the deployed system.
Network boundaries should make trust, exposure, control, and support behavior clear.

## Required Inputs

Require:

- runtime topology
- integration surfaces
- security or trust context when available

## Network Concerns

Define:

- public, partner, internal, and operational ingress
- egress to external providers and managed services
- trust zones and boundary crossings
- gateway, load balancer, API gateway, ingress, or edge responsibilities at architecture level
- DNS and TLS ownership expectations
- service-to-service connectivity and allowed directions
- network isolation for stateful dependencies
- rate limiting, abuse control, and egress audit needs
- private connectivity, allowlists, or NAT constraints when relevant
- network logs, metrics, and tracing expectations

## Output

Return:

| Boundary/flow | Source | Destination | Exposure | Control point | Risk |
|---------------|--------|-------------|----------|---------------|------|

Then list:

- ingress decisions
- egress decisions
- trust boundaries
- DNS/TLS ownership
- network observability and support needs
- open network questions
