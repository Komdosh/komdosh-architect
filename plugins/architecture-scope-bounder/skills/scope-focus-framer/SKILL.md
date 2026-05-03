---
name: scope-focus-framer
description: Define the system of interest, one-part focus, ownership boundary, adjacent responsibilities, and scope exclusions for top-level architecture work.
---

# Scope Focus Framer

## Purpose

Choose and describe the system part that architecture work should focus on.
The scope boundary must be clear enough that later architecture steps do not drift into unrelated product areas.

## Required Inputs

Require at least one of:

- product area or capability
- requirements brief
- current system description
- user-provided architecture question

If the requested scope is broad, propose a focused system-of-interest slice and label excluded areas.

## Boundary Questions

Answer:

- What is the system of interest?
- What user or business problem does this system part solve?
- Which responsibilities belong inside this boundary?
- Which responsibilities are adjacent but outside?
- Which responsibilities are explicitly out of scope?
- What is the source-of-truth state inside the boundary, if known?
- What external decisions must not be hidden inside this scope?
- What future expansion might change the boundary later?

## Boundary Types

Consider:

- product capability boundary
- bounded context or domain responsibility boundary
- trust boundary
- ownership and team boundary
- data ownership boundary
- operational support boundary
- integration boundary
- migration or legacy-coexistence boundary

## Output

Return:

- system-of-interest statement
- in-scope responsibilities
- out-of-scope responsibilities
- adjacent systems and responsibilities
- likely ownership and source-of-truth notes
- boundary assumptions
- open boundary questions
