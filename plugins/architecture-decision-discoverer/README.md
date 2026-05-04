# Architecture Decision Discoverer

Architecture Decision Discoverer is a Codex plugin for finding and using existing architecture decisions.
It reads ADRs and decision notes as context for architecture work.

## Scope Fit

Use this plugin when the requested outcome is:

- discover ADRs and architecture decision notes
- search local files, related repos, MCP/RAG tools, raw memory, and AI context sources
- read ADR notes before requirements, scope, domain, service, data, integration, deployment, security, or observability work
- extract accepted decisions, rejected alternatives, assumptions, consequences, and revisit triggers
- identify architecture constraints that current work must follow
- detect drift or conflict between a new design and existing ADRs
- find decisions that probably need a future ADR
- produce a compact decision-context brief for an architect

This plugin is read-first.
It may write short temporary working notes only to absorb and organize discovered context.
It must not write, update, rename, supersede, or approve ADRs.

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

- `$architecture-decision-discoverer:architecture-decision-discoverer`: orchestrates the full decision-discovery pass.
- `$architecture-decision-discoverer:decision-source-finder`: searches local files, related repos, MCP/RAG, memory, and AI context sources for ADRs and decision notes.
- `$architecture-decision-discoverer:adr-reader-summarizer`: reads ADRs and extracts status, context, decision, alternatives, consequences, notes, and links.
- `$architecture-decision-discoverer:decision-constraint-extractor`: turns ADR content into constraints, defaults, forbidden choices, assumptions, and revisit triggers.
- `$architecture-decision-discoverer:decision-drift-detector`: checks current architecture work for conflict, drift, or missing alignment with discovered decisions.
- `$architecture-decision-discoverer:future-adr-question-planner`: identifies decisions that need future ADR attention without writing the ADR.
- `$architecture-decision-discoverer:temporary-decision-note-builder`: creates short temporary working notes when needed for context absorption.
- `$architecture-decision-discoverer:decision-context-brief-builder`: produces the compact decision-context brief.
- `$architecture-decision-discoverer:decision-source-map-diagrammer`: creates simple maps of decision sources and constraints when useful.
- `$architecture-decision-discoverer:decision-discovery-review-gate`: reviews discovery coverage, readability, and scope discipline.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output tells the architect what decisions already exist and how they constrain the current work.
It should cite where decisions came from and separate confirmed decisions from assumptions.

Reject or revise a decision-context brief when it:

- ignores ADRs or decision notes that are likely available nearby
- searches only the current folder when related repos, MCP/RAG, or memory are available
- treats remembered or inferred decisions as confirmed ADR facts
- loses ADR status, consequences, rejected alternatives, or revisit triggers
- hides conflict between current work and existing decisions
- writes or edits ADRs instead of only discovering context
- becomes a long ADR catalog instead of a compact architecture-useful brief

## Required Output Shape

The main output should be a decision-context brief with:

- discovery purpose and current architecture task
- searched sources and coverage limits
- relevant ADRs and decision notes with locations
- decisions that constrain the current work
- rejected alternatives and forbidden paths
- consequences and architecture implications
- assumptions and open questions from discovered decisions
- conflicts, drift risks, and follow-up checks
- decisions that may need a future ADR
- short handoff notes for the architect
