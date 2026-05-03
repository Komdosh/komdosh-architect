---
name: identity-access-modeler
description: Define security architecture for human, service, admin, operator, support, job, and external-system identities, authentication posture, sessions, tokens, credential flow, and access entry points.
---

# Identity Access Modeler

## Purpose

Define who or what can prove identity to the system.
Identity design must include humans, services, jobs, admins, operators, and external systems.

## Required Inputs

Require:

- actor and role context
- trust boundary map
- integration or deployment context when available

## Identity Concerns

Define:

- identity types: user, admin, operator, support, service, job, external provider
- authentication posture at architecture level
- session and token lifecycle expectations
- machine-to-machine and workload identity expectations
- external identity provider or federation assumptions
- account recovery and credential reset risk when relevant
- device, client, or channel trust assumptions
- access entry points and authentication handoff boundaries
- authentication audit and anomaly signals

## Output

Return:

| Identity | Used by | Entry point | Authentication posture | Token/session concern | Risk |
|----------|---------|-------------|------------------------|-----------------------|------|

Then list:

- identity boundaries
- session and token lifecycle rules
- machine identity needs
- high-risk authentication paths
- open identity questions
