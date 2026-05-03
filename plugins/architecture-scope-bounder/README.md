# Architecture Scope Bounder

Architecture Scope Bounder is a Codex plugin for the boundary-framing step of software architecture work.
It focuses on one system part at a time and prepares top-level context for later architecture workflow plugins.

## Scope Fit

Use this plugin when the requested outcome is:

- a clear system-of-interest boundary
- actor, role, and external system discovery
- high-level use cases and exception paths
- integration surface framing
- context diagrams or system landscape diagrams
- top-level design context before detailed architecture work

This plugin is only one top-level step in the full architecture workflow.
It should frame the boundary and context, not produce detailed service decomposition, database design, deployment topology, or final API schemas.

## Skill Grouping

- `$architecture-scope-bounder:architecture-scope-bounder`: orchestrates the full scope-boundary pass.
- `$architecture-scope-bounder:scope-focus-framer`: defines the system of interest, ownership boundary, and one-part focus.
- `$architecture-scope-bounder:actor-role-mapper`: identifies human roles, system actors, operators, and trust positions.
- `$architecture-scope-bounder:external-system-landscape`: maps external systems, integration surfaces, ownership, and interaction styles.
- `$architecture-scope-bounder:use-case-exception-mapper`: captures top-level use cases, alternate paths, exception paths, and boundary events.
- `$architecture-scope-bounder:context-landscape-diagrammer`: creates context and system landscape diagrams from the bounded scope.
- `$architecture-scope-bounder:scope-review-gate`: reviews the result for boundary clarity and design-stage discipline.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output is focused, boundary-explicit, actor-aware, and ready for the next architecture step.
It should make clear what is inside the system, what is outside, who uses it, which external systems matter, and which top-level scenarios drive architecture.

Reject or revise a scope brief when it:

- tries to design the whole product instead of one focused part
- hides ownership or trust boundaries
- omits external systems, operators, or non-human actors
- only covers happy-path use cases
- presents assumptions as facts
- chooses detailed implementation technology too early
- produces diagrams that do not match the written boundary

## Required Output Shape

The main output should be a scope-boundary brief with:

- system of interest and purpose
- explicit in-scope and out-of-scope boundaries
- actors, roles, operators, and system actors
- external systems and integration expectations
- high-level use cases
- alternate and exception paths
- boundary events and information flows
- top-level design frame and architecture implications
- assumptions and open questions
- context diagram
- system landscape diagram when useful
- handoff checklist for later architecture workflow steps
