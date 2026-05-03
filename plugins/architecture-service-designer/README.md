# Architecture Service Designer

Architecture Service Designer is a Codex plugin for the service and component structure step of software architecture work.
It comes after requirements, scope bounding, and domain modeling, and before detailed data, API, infrastructure, and implementation design.

## Scope Fit

Use this plugin when the requested outcome is:

- service, component, or module candidates
- responsibility and ownership boundaries
- source-of-truth decisions at a high level
- collaboration style between components
- public and internal contract boundaries
- sync versus async interaction framing
- transaction and consistency boundary decisions
- dependency direction rules
- adapter and anti-corruption layer needs
- component, container, or service collaboration diagrams

This plugin should design the system structure, not implementation details.
It may state architecture implications and contract responsibilities, but it must not write final API schemas, database schemas, deployment topology, cloud resource plans, or framework-specific module code.

## Skill Grouping

- `$architecture-service-designer:architecture-service-designer`: orchestrates the full service-design pass.
- `$architecture-service-designer:service-candidate-modeler`: identifies service, component, and module candidates from capabilities and domain boundaries.
- `$architecture-service-designer:responsibility-boundary-designer`: assigns responsibilities, ownership, and source-of-truth boundaries.
- `$architecture-service-designer:contract-collaboration-designer`: frames public/internal contracts and collaboration styles.
- `$architecture-service-designer:consistency-transaction-bounder`: identifies transaction, consistency, idempotency, and process boundaries.
- `$architecture-service-designer:dependency-rule-planner`: defines dependency direction, allowed coupling, and forbidden shortcuts.
- `$architecture-service-designer:adapter-anti-corruption-planner`: frames adapters, external boundaries, and anti-corruption layers.
- `$architecture-service-designer:service-diagrammer`: creates component, container, and service collaboration diagrams.
- `$architecture-service-designer:service-review-gate`: reviews the structure for architectural readiness and decomposition risks.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output is cohesive, domain-aligned, ownership-explicit, and ready for later data/API/infrastructure design.
It should explain why each service or component boundary exists and what collaboration rules keep the system maintainable.

Reject or revise a service design when it:

- splits by technology layer instead of domain responsibility
- creates microservices without operational or domain justification
- hides source-of-truth ownership
- allows shared database coupling as a default
- omits transaction and consistency boundaries
- leaves external system adapters undefined
- makes every relationship synchronous without reason
- ignores deployability, observability, support ownership, and failure isolation
- jumps to low-level endpoint, schema, or cloud design

## Required Output Shape

The main output should be a service-design brief with:

- design purpose and source context
- service/component/module candidates
- responsibility and ownership table
- source-of-truth boundaries
- public and internal contracts at high level
- collaboration and interaction matrix
- sync/async decisions and rationale
- consistency and transaction boundaries
- dependency direction rules
- adapter and anti-corruption needs
- operational ownership notes
- decomposition risks and alternatives
- service/component diagrams
- assumptions and open questions
- handoff checklist for later architecture workflow steps
