---
name: decision-discoverer
description: Discover existing ADRs and architecture decisions from local files, related repos, MCP/RAG tools, raw memory, and AI context sources, then extract constraints, assumptions, consequences, drift risks, and compact decision context without writing ADRs.
---

# Architecture Decision Discoverer

## Purpose

Find the architecture decisions that already exist.
The result must help an architect understand which ADRs and decision notes constrain current work before new design decisions are made.

Use this skill when the user asks to discover ADRs, reveal decision context, check architecture work against existing decisions, find related decisions in local or external AI context, or prepare an ADR-aware design pass.

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

Read decisions; do not write them:

- search local files first, then related repos, MCP/RAG, raw memory, and other available AI context sources when ADRs may live elsewhere
- treat ADRs and decision notes as source-of-truth context only after their location and status are clear
- extract accepted decisions, rejected alternatives, consequences, assumptions, constraints, and revisit triggers
- distinguish confirmed ADR facts from inferred or memory-derived context
- identify conflict or drift between current architecture work and existing decisions
- create only short temporary working notes when needed to absorb context
- do not write, update, rename, supersede, approve, or delete ADRs

## Required Inputs

Load the minimum needed context:

- current architecture task, scope, repo, or design brief
- local ADR or docs paths when the user provides them
- related repo names, MCP/RAG tools, memory locations, or raw AI context when available
- existing architecture-stage outputs when checking drift

If related decisions may be outside the current repo, search available local context sources before concluding no ADR exists.
Ask when access to a named repo, MCP, RAG, or memory source is unavailable and the missing source is central.

## Skill Flow

1. Use `$architecture-decision-discoverer:decision-source-finder` to find ADRs and decision notes in local files, related repos, MCP/RAG, memory, and AI context sources.
2. Use `$architecture-decision-discoverer:adr-reader-summarizer` to read ADRs and extract status, context, decision, alternatives, consequences, notes, and links.
3. Use `$architecture-decision-discoverer:decision-constraint-extractor` to turn decisions into architecture constraints, defaults, assumptions, and revisit triggers.
4. Use `$architecture-decision-discoverer:decision-drift-detector` to compare discovered decisions with current architecture work when a current design exists.
5. Use `$architecture-decision-discoverer:future-adr-question-planner` to identify decisions that may need future ADR attention.
6. Use `$architecture-decision-discoverer:temporary-decision-note-builder` only when short working notes help absorb context.
7. Use `$architecture-decision-discoverer:decision-context-brief-builder` to produce the final compact brief.
8. Use `$architecture-decision-discoverer:decision-source-map-diagrammer` when a source/constraint map clarifies the result.
9. Use `$architecture-decision-discoverer:decision-discovery-review-gate` before final delivery.

## Output Contract

Return a self-contained decision-context brief with this structure unless the user asks for another format:

1. Discovery purpose
2. Current architecture task
3. Searched sources and coverage limits
4. Relevant ADRs and decision notes with locations
5. Decisions that constrain current work
6. Rejected alternatives and forbidden paths
7. Consequences and architecture implications
8. Assumptions and open questions from decisions
9. Conflicts and drift risks
10. Decisions that may need a future ADR
11. Short handoff notes for the architect

## Source Search Discipline

Search broadly but label confidence:

- local repo ADR folders, docs, README files, architecture folders, decision logs, issue notes, and planning docs
- sibling or related repos when project context suggests decisions may live outside the current checkout
- MCP/codebase-memory/RAG tools when available
- raw memory or AI context sources when available
- user-provided files, summaries, transcripts, or exported context

Never present memory-derived or inferred context as a confirmed ADR unless the source can be identified.

## Temporary Note Discipline

Temporary notes are allowed only for comprehension:

- keep them short
- mark them as temporary working notes
- do not commit them
- do not treat them as official architecture records
- do not use them as a substitute for source citations

## Stop Conditions

Stop and ask when:

- a named ADR repo, MCP, RAG, or memory source is unavailable and likely contains the needed decision
- ADR status is unclear and would change the architecture constraint
- current design conflicts with an accepted ADR and the user asked for implementation, not decision review
- the user asks this plugin to write, edit, approve, or supersede an ADR
