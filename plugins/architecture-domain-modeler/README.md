# Architecture Domain Modeler

Architecture Domain Modeler is a Codex plugin for the domain-shaping step of software architecture work.
It comes after requirements and scope bounding, and before detailed service, API, data, integration, and deployment design.

## Scope Fit

Use this plugin when the requested outcome is:

- domain glossary and ubiquitous language
- architect-level domain concept model
- entity, value, policy, rule, and lifecycle discovery
- business invariants and constraints
- capability, command, query, and event vocabulary
- source-of-truth and ownership candidates
- domain concept map, lifecycle diagram, or capability map
- ambiguity and open questions that block service decomposition

This plugin should model the business domain, not the final code model.
It may state architecture implications, but it must not choose service boundaries, database schemas, framework types, or deployment topology unless the user explicitly asks for later-stage design.

## Human-Readable Output

Prefer readability over professional complexity.
Outputs should be compact, self-contained, and easy to scan.

- put the main idea or decision first
- use plain words before specialist terms
- highlight only important decisions, risks, assumptions, open questions, and next steps
- keep details close to the point they explain
- avoid long paragraphs and decorative wording
- explain necessary technical terms in place

## Skill Grouping

- `$architecture-domain-modeler:architecture-domain-modeler`: orchestrates the full domain-modeling pass.
- `$architecture-domain-modeler:domain-language-mapper`: builds the glossary, term ownership, synonyms, and ambiguous terms.
- `$architecture-domain-modeler:concept-relationship-modeler`: identifies domain concepts, relationships, ownership candidates, and source-of-truth candidates.
- `$architecture-domain-modeler:lifecycle-state-modeler`: models key state lifecycles, transitions, triggers, and terminal states.
- `$architecture-domain-modeler:rule-invariant-cataloger`: catalogs business rules, invariants, policies, validations, and consistency constraints.
- `$architecture-domain-modeler:capability-command-event-modeler`: maps capabilities, commands, queries, events, and domain signals.
- `$architecture-domain-modeler:domain-diagrammer`: creates concept maps, lifecycle diagrams, and capability maps.
- `$architecture-domain-modeler:domain-review-gate`: reviews the result for domain readiness and design-stage discipline.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output is language-clear, invariant-aware, lifecycle-aware, and ready for later architecture decisions.
It should explain the shape of the business problem before anyone chooses services or storage.

Reject or revise a domain model when it:

- is just a database schema or class diagram
- mixes confirmed domain facts with assumptions
- hides overloaded or ambiguous terms
- misses important state transitions or terminal states
- ignores business rules, policies, and invariants
- jumps directly to microservices, tables, queues, or APIs
- cannot trace concepts back to requirements, scope, or assumptions

## Required Output Shape

The main output should be a domain-modeling brief with:

- domain purpose and bounded scope reference
- glossary and ambiguous terms
- core concepts and relationships
- source-of-truth and ownership candidates
- state lifecycles and transitions
- business rules, policies, and invariants
- capabilities, commands, queries, and events
- domain risks and unstable concepts
- concept map
- lifecycle diagram when useful
- capability map when useful
- assumptions and open questions
- handoff checklist for later architecture workflow steps
