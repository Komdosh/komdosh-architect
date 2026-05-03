---
name: architecture-domain-modeler
description: Create an architect-level domain model from requirements and bounded scope, covering language, concepts, relationships, lifecycles, rules, invariants, policies, capabilities, commands, events, diagrams, assumptions, and architecture handoff readiness.
---

# Architecture Domain Modeler

## Purpose

Shape the business domain before detailed architecture design starts.
The result must help a system designer understand the domain language, core concepts, lifecycles, invariants, capabilities, and domain signals that later service, data, API, and integration design must respect.

Use this skill when the user asks for domain modeling, domain architecture, DDD-style analysis, concept model, business rules, invariants, lifecycle model, capability model, command/event vocabulary, or domain diagrams.

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

Model the domain, not the implementation:

- clarify domain language and overloaded terms
- identify core business concepts and relationships
- distinguish entities, values, policies, rules, events, actors, and external concepts at an architecture level
- model key lifecycles, transitions, terminal states, and recovery paths
- capture business invariants, policies, validations, and consistency expectations
- identify capabilities, commands, queries, events, and domain signals
- surface source-of-truth and ownership candidates without forcing final service decomposition
- prepare inputs for later architecture workflow plugins, not a full service/data/API design

## Required Inputs

Load the minimum needed context:

- requirements brief when available
- scope-boundary brief when available
- product area, capability, bounded context, feature, or domain problem statement
- known actors, external systems, business rules, constraints, and lifecycle facts
- existing architecture docs, ADRs, schemas, or service docs when the domain model must align with a current system

If scope is too broad, choose the bounded system part already established by `$architecture-scope-bounder:architecture-scope-bounder` or label a proposed focus.
Ask only when missing domain context would make the model misleading.

## Skill Flow

1. Use `$architecture-domain-modeler:domain-language-mapper` to define glossary, synonyms, ambiguous terms, and term ownership.
2. Use `$architecture-domain-modeler:concept-relationship-modeler` to identify core concepts, relationships, and source-of-truth candidates.
3. Use `$architecture-domain-modeler:lifecycle-state-modeler` to map key lifecycles, transitions, triggers, and terminal states.
4. Use `$architecture-domain-modeler:rule-invariant-cataloger` to capture business rules, policies, invariants, and consistency constraints.
5. Use `$architecture-domain-modeler:capability-command-event-modeler` to identify capabilities, commands, queries, events, and domain signals.
6. Use `$architecture-domain-modeler:domain-diagrammer` to produce concept, lifecycle, or capability diagrams when useful.
7. Use `$architecture-domain-modeler:domain-review-gate` before final delivery.

## Output Contract

Return a self-contained domain-modeling brief with this structure unless the user asks for another format:

1. Domain purpose
2. Bounded scope reference
3. Glossary and term decisions
4. Ambiguous or overloaded terms
5. Core domain concepts
6. Concept relationships
7. Source-of-truth and ownership candidates
8. State lifecycles and transitions
9. Business rules and policies
10. Invariants and consistency expectations
11. Capabilities
12. Commands, queries, and events
13. Domain diagrams
14. Domain risks and unstable concepts
15. Assumptions
16. Open questions
17. Handoff checklist for later architecture steps

## Domain Discipline

Do not turn this step into implementation design:

- do not create code-level class diagrams
- do not choose tables, collections, topics, queues, APIs, or storage engines
- do not decompose into microservices
- do not define final API schemas or database schemas
- do not hide unclear domain language behind technical names

You may state architecture implications:

- one concept likely needs a clear source of truth
- one lifecycle requires explicit transition ownership
- one event may become important for downstream integrations
- one invariant may require transactional or process-level consistency later
- one overloaded term blocks safe service decomposition

## Domain Additions To Consider

To build first-class system design context, consider:

- canonical terms and forbidden synonyms
- core concepts versus supporting concepts
- entities with continuity over time
- values that describe but do not own lifecycle
- policies and rules that may change independently
- aggregate-like consistency clusters without forcing code structure
- lifecycle ownership and state transition authority
- events that mean business facts, not technical notifications
- commands that request business change
- queries that reveal domain information
- projections or read concerns that may exist later
- source-of-truth candidates and duplicated data risks
- ambiguity, unstable vocabulary, and business exceptions

## Stop Conditions

Stop and ask when:

- domain language is too ambiguous to model honestly
- requirements and scope contradict each other
- lifecycle or source-of-truth assumptions would hide a high-risk decision
- the user asks for detailed implementation while the domain model is still unclear
