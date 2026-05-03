# Architecture Requirementer

Architecture Requirementer is a Codex plugin for software architecture requirements work.
It turns product goals, domain context, constraints, and early ideas into a comprehensive requirements brief that a software architect can pick up without needing scattered background notes.

## Scope Fit

Use this plugin when the requested outcome is:

- a new software requirements document
- product-goal clarification before architecture design
- functional and non-functional requirements for a system, service, product, platform, or capability
- a requirements review before architecture planning
- explicit assumptions, future expansion expectations, and architecture implications

Do not use it as a solution-design shortcut.
The plugin can describe architecture implications and constraints, but it should not choose a detailed implementation unless the user explicitly asks for architecture design.

## Skill Grouping

- `$architecture-requirementer:architecture-requirementer`: orchestrates the full requirements pass.
- `$architecture-requirementer:product-goal-discovery`: clarifies product goals, users, business outcomes, and domain context.
- `$architecture-requirementer:functional-scope-modeler`: turns goals into functional requirements, workflows, data needs, and scope boundaries.
- `$architecture-requirementer:quality-attribute-requirements`: defines measurable non-functional requirements and quality scenarios.
- `$architecture-requirementer:architecture-assumption-planner`: makes useful assumptions explicit and identifies future expansion paths.
- `$architecture-requirementer:requirements-review-gate`: reviews the finished requirements brief for completeness and architecture readiness.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good result is comprehensive, self-contained, field-aware, and ready for architecture work.
It should include both what the product must do and how well the system must behave.

Reject or revise a requirements brief when it:

- misses the product goal or user outcomes
- only lists features and ignores quality attributes
- mixes confirmed facts, assumptions, and open questions without labels
- hides important constraints, risks, compliance needs, data ownership, or integration boundaries
- designs a detailed solution before requirements are stable
- lacks traceability from goals to requirements
- ignores future operation, support, maintenance, extensibility, migration, and growth

## Required Output Shape

The main output should be an architect-ready requirements brief with:

- purpose and product outcomes
- stakeholders, personas, and user jobs
- glossary and domain context
- scope, out-of-scope items, and release assumptions
- functional requirements with stable IDs
- key workflows and scenarios
- data, integration, security, access, and lifecycle requirements
- measurable non-functional requirements with quality scenarios
- explicit assumptions and open questions
- future expansion and support expectations
- architecture implications and constraints
- traceability from goals to requirements
- readiness checklist for architecture handoff
