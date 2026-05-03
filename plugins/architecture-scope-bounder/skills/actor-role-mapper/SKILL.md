---
name: actor-role-mapper
description: Identify user roles, system actors, operators, administrators, external actors, trust positions, permissions, and actor-driven architecture concerns.
---

# Actor Role Mapper

## Purpose

Start scope thinking from actors.
Architecture boundaries are clearer when human and non-human actors are explicit.

## Required Inputs

Require:

- system of interest or product area
- any known user roles, stakeholders, or external systems

If roles are unknown, infer likely roles from the domain and label them as assumptions.

## Actor Types

Consider:

- primary end users
- secondary users
- administrators and back-office users
- support, moderation, operations, finance, compliance, or legal actors
- partner users and tenant administrators
- external systems acting through APIs or events
- scheduled jobs, automation, import/export tools, and agents
- attackers, abusive users, or accidental misuse actors when relevant

## Actor Analysis

For each actor, identify:

- goal or job to be done
- interaction channel
- authority and permission level
- trust level
- data visibility
- boundary crossed
- failure or misuse concern
- support or audit expectation

## Output

Return an actor table:

| Actor | Type | Goal | Boundary crossed | Trust level | Architecture concern |
|-------|------|------|------------------|-------------|----------------------|

Then list role assumptions and open actor questions.
