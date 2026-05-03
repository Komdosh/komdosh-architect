---
name: architecture-service-designer
description: Design top-level service, component, or module structure from requirements, scope, and domain models, covering responsibility boundaries, contracts, collaboration, consistency, dependencies, adapters, diagrams, assumptions, and handoff readiness.
---

# Architecture Service Designer

## Purpose

Turn a bounded domain model into a top-level service, component, or module structure.
The result must help a system designer understand what structural units should exist, why each boundary exists, what each unit owns, and how units collaborate.

Use this skill when the user asks for service design, component design, module boundaries, service decomposition, container diagram, collaboration design, contract boundaries, dependency rules, or top-level system structure.

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

Design structure, not implementation detail:

- derive boundaries from requirements, scope, domain concepts, capabilities, rules, and lifecycles
- identify service, component, or module candidates conservatively
- assign responsibilities and source-of-truth ownership explicitly
- define high-level public and internal contract boundaries
- choose sync, async, event, command, query, or batch collaboration style where it matters
- identify consistency, transaction, idempotency, and process boundaries
- define dependency direction rules and forbidden coupling shortcuts
- frame adapters and anti-corruption layers for external systems
- prepare inputs for later data, API, integration, infrastructure, and ADR workflow plugins

## Required Inputs

Load the minimum needed context:

- requirements brief when available
- scope-boundary brief when available
- domain model when available
- known external systems and integration expectations
- quality attributes that affect structure, such as availability, latency, scale, security, audit, maintainability, and operability
- existing architecture docs, ADRs, service docs, or code when the design must align with a current system

If the domain model is missing, infer a conservative first-pass structure only when the system is simple and label assumptions.
Ask when missing domain ownership or lifecycle facts would make decomposition misleading.

## Skill Flow

1. Use `$architecture-service-designer:service-candidate-modeler` to identify service, component, or module candidates.
2. Use `$architecture-service-designer:responsibility-boundary-designer` to assign responsibilities, ownership, and source-of-truth boundaries.
3. Use `$architecture-service-designer:contract-collaboration-designer` to frame contracts and collaboration styles.
4. Use `$architecture-service-designer:consistency-transaction-bounder` to identify consistency, transaction, idempotency, and process boundaries.
5. Use `$architecture-service-designer:dependency-rule-planner` to define dependency direction and coupling rules.
6. Use `$architecture-service-designer:adapter-anti-corruption-planner` to frame external adapters and anti-corruption boundaries.
7. Use `$architecture-service-designer:service-diagrammer` to create component or collaboration diagrams when useful.
8. Use `$architecture-service-designer:service-review-gate` before final delivery.

## Output Contract

Return a self-contained service-design brief with this structure unless the user asks for another format:

1. Design purpose
2. Source context
3. Service/component/module candidates
4. Responsibility boundaries
5. Source-of-truth ownership
6. Public and internal contract boundaries
7. Collaboration matrix
8. Sync/async decisions
9. Transaction and consistency boundaries
10. Dependency direction rules
11. External adapters and anti-corruption layers
12. Operational ownership and support notes
13. Diagrams
14. Decomposition risks and alternatives
15. Assumptions
16. Open questions
17. Handoff checklist for later architecture steps

## Design Discipline

Do not turn this step into low-level implementation design:

- do not write detailed REST, GraphQL, gRPC, event, or database schemas
- do not choose database engines, queue products, cloud resources, or deployment topology
- do not create code package plans unless the user explicitly asks for implementation planning
- do not split into microservices only because multiple concepts exist
- do not normalize shared database access as service integration

You may state architecture decisions at the structural level:

- this capability can stay inside one deployable module until scale or ownership changes
- this component should own a specific lifecycle state
- this integration should go through an adapter to protect domain language
- this relationship should be async because the downstream system is not authoritative
- this command needs idempotency because it crosses an external boundary

## Stop Conditions

Stop and ask when:

- the source domain model is too unclear for meaningful boundaries
- multiple unrelated scopes are being decomposed together
- source-of-truth ownership is unknown for central state
- quality attributes conflict and the tradeoff cannot be assumed safely
- the user asks for detailed implementation while structural boundaries are unresolved
