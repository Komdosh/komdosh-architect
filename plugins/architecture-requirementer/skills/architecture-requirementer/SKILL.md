---
name: architecture-requirementer
description: Create comprehensive, self-contained software architecture requirements from product goals, covering functional requirements, non-functional requirements, assumptions, future expansion, and architecture handoff readiness.
---

# Architecture Requirementer

## Purpose

Turn product intent into an architect-ready requirements brief.
The result must help a software architect understand what needs to be built, why it matters, how it must behave, and which assumptions or open questions affect architecture.

Use this skill when the user asks for requirements, software requirements, functional requirements, non-functional requirements, product-to-architecture handoff, architect-ready specification, or deep product requirement analysis.

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

Understand the product before writing requirements:

- identify product goals, target users, business outcomes, and success criteria
- cover both functional and non-functional requirements
- make the document self-contained enough for an architect to pick up without external context
- think deeply about the domain, likely edge cases, operating model, support model, and future expansion
- make helpful assumptions when needed, but label them clearly as assumptions
- separate requirements from architecture decisions unless the user explicitly asks for solution design

## Required Inputs

Load the minimum needed context:

- product idea, feature brief, ticket, domain notes, or user-provided goal
- target users, stakeholders, and business constraints when available
- existing product, architecture, roadmap, ADR, or service docs when the work must align with a current system
- known compliance, security, data, integration, deployment, budget, timeline, or support constraints
- expected output path when the user asks to write a file

If critical context is missing, make a reasonable assumption only when it helps move the work forward and is low risk.
Mark every assumption explicitly.
Ask only when a missing fact would make the requirements misleading or unsafe.

## Skill Flow

1. Use `$architecture-requirementer:product-goal-discovery` to identify goals, users, outcomes, domain context, and constraints.
2. Use `$architecture-requirementer:functional-scope-modeler` to define functional requirements, workflows, data needs, and boundaries.
3. Use `$architecture-requirementer:quality-attribute-requirements` to define measurable non-functional requirements.
4. Use `$architecture-requirementer:architecture-assumption-planner` to surface assumptions, future expansion, support concerns, and architecture implications.
5. Use `$architecture-requirementer:requirements-review-gate` before final delivery.

## Output Contract

Return a self-contained requirements brief with this structure unless the user asks for another format:

1. Product purpose
2. Target users and stakeholders
3. Business goals and success metrics
4. Domain context and glossary
5. Scope and out of scope
6. Functional requirements
7. Key workflows and scenarios
8. Data and lifecycle requirements
9. Integration requirements
10. Security, privacy, and access requirements
11. Non-functional requirements
12. Assumptions
13. Open questions
14. Future expansion and support expectations
15. Architecture implications and constraints
16. Traceability matrix
17. Architecture handoff checklist

## Requirement Style

Write requirements so they can be used:

- use stable IDs such as `GOAL-001`, `FR-001`, `NFR-001`, `ASSUMP-001`, and `Q-001`
- make each requirement testable or reviewable
- use `Must`, `Should`, and `Could` intentionally
- include acceptance or validation notes for important requirements
- include negative and failure paths, not only happy paths
- state unresolved decisions as open questions, not hidden assumptions
- avoid vague words such as fast, scalable, secure, reliable, intuitive, or enterprise-ready without measurable meaning

## Architecture Boundary

Do not prematurely choose:

- concrete database, queue, framework, cloud provider, or vendor
- service split, deployment topology, or internal module structure
- detailed API schema
- final data model

You may state architecture implications such as:

- data ownership must be explicit
- the system needs auditability
- the workflow requires idempotent external callbacks
- high read volume suggests separate read concerns
- future marketplace expansion implies extensible policy/rule modeling

## Stop Conditions

Stop and ask when:

- the product goal is contradictory or absent
- legal, safety, financial, medical, privacy, or compliance requirements are central but unknown
- the user asks for assumptions that would hide a high-risk decision
- the requested output would look complete while missing a core business or user goal
