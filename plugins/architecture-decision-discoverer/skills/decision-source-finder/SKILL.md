---
name: decision-source-finder
description: Search local files, related repositories, MCP/RAG tools, raw memory, and AI context sources for ADRs, decision notes, accepted architecture decisions, rejected alternatives, and decision logs.
---

# Decision Source Finder

## Purpose

Find where decisions are stored.
ADRs may live outside the current repo, so discovery must include local files and available AI context sources.

## Required Inputs

Require at least one of:

- current repo or path
- architecture task or topic
- related repo, system, service, domain, or context name
- MCP/RAG/memory source available in the session

## Search Order

Search in this order when available:

1. local repo files and docs
2. sibling or related repos suggested by the project context
3. MCP or codebase-memory tools
4. local RAG tools
5. raw memory or AI context sources
6. user-provided notes or exported context

Look for:

- `adr`, `ADR`, `decision`, `decisions`, `architecture-decision`, `records`
- accepted, superseded, proposed, rejected, and draft decisions
- decision notes embedded in roadmaps, design docs, README files, and planning docs

## Output

Return:

| Source | Location/tool | Match reason | Confidence | Access result |
|--------|---------------|--------------|------------|---------------|

Then list:

- sources searched
- sources not available
- likely ADR locations
- source confidence
- next reading targets
