---
name: architecture-scope-bounder
description: Define a focused architecture scope and system boundary, including actors, roles, external systems, integrations, high-level use cases, exception paths, top-level design frame, and context or system landscape diagrams.
---

# Architecture Scope Bounder

## Purpose

Frame one system part before detailed architecture design starts.
The result must help a system designer understand the system of interest, who interacts with it, what stays outside it, how it relates to external systems, and which top-level scenarios shape the architecture.

Use this skill when the user asks for architecture scope, system boundary, context diagram, system landscape, external-system map, top-level design framing, actors, roles, or high-level use cases.

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

Focus on one bounded part:

- define the system of interest and keep attention there
- make in-scope, out-of-scope, and adjacent responsibilities explicit
- start from user roles, actors, operators, and external systems
- describe high-level use cases, alternate paths, and exception paths
- identify integration surfaces without choosing detailed implementation
- produce context or landscape diagrams when they clarify the boundary
- prepare inputs for later architecture workflow plugins, not a full detailed design

## Required Inputs

Load the minimum needed context:

- product area, capability, feature, service, bounded context, or problem statement to scope
- requirements brief when available
- known users, actors, external systems, constraints, and business rules
- existing architecture docs, diagrams, ADRs, or service docs when the scope must align with a current system
- requested diagram format or target artifact path when the user asks for a file

If the user asks for an entire product, choose one system-of-interest slice when possible and label that focus.
Ask only when the requested boundary is too ambiguous to avoid misleading architecture work.

## Skill Flow

1. Use `$architecture-scope-bounder:scope-focus-framer` to define the system of interest and boundary.
2. Use `$architecture-scope-bounder:actor-role-mapper` to identify roles, actors, operators, and trust positions.
3. Use `$architecture-scope-bounder:external-system-landscape` to identify external systems and integration surfaces.
4. Use `$architecture-scope-bounder:use-case-exception-mapper` to capture top-level use cases, alternate paths, and exception paths.
5. Use `$architecture-scope-bounder:context-landscape-diagrammer` to produce context and landscape diagrams when useful.
6. Use `$architecture-scope-bounder:scope-review-gate` before final delivery.

## Output Contract

Return a self-contained scope-boundary brief with this structure unless the user asks for another format:

1. Scope purpose
2. System of interest
3. In scope
4. Out of scope
5. Adjacent responsibilities
6. Actors and roles
7. External systems
8. Integration expectations
9. High-level use cases
10. Alternate and exception paths
11. Boundary events and information flows
12. Top-level design frame
13. Context diagram
14. System landscape diagram when useful
15. Assumptions
16. Open questions
17. Handoff checklist for later architecture steps

## Boundary Discipline

Do not turn this step into detailed architecture design:

- do not choose concrete databases, queues, frameworks, cloud services, or deployment topology
- do not decompose the whole product into microservices
- do not write detailed API schemas
- do not define final data models
- do not solve every downstream architecture decision

You may state top-level design implications:

- the system needs a clear ownership boundary for specific domain state
- one external integration requires idempotent command handling
- one actor crosses a trust boundary and needs explicit authorization
- one exception path requires human operator recovery
- one adjacent system should remain outside this scope

## Scope Additions To Consider

To build first-class system design context, consider:

- ownership and source-of-truth boundaries
- trust boundaries and actor authentication level
- operational actors such as support, moderators, back-office users, and administrators
- non-human actors such as schedulers, partner systems, event consumers, and automation
- upstream and downstream systems
- data flows, command flows, event flows, and control flows at a high level
- failure ownership, retries, idempotency, and compensation responsibility
- configuration, policy, and rule ownership
- audit, observability, and support handoff boundaries
- migration and coexistence with legacy systems
- future product expansion that could move the boundary

## Stop Conditions

Stop and ask when:

- the system of interest cannot be identified
- multiple unrelated system parts are mixed into one requested scope
- a missing ownership, trust, compliance, or external-system fact would make the boundary misleading
- the user asks for detailed implementation while the scope boundary is still unclear
