---
name: domain-language-mapper
description: Build a domain glossary, clarify ubiquitous language, identify synonyms, overloaded terms, term ownership, forbidden ambiguity, and open vocabulary questions for architecture modeling.
---

# Domain Language Mapper

## Purpose

Clarify the words of the domain before modeling concepts.
Poor vocabulary creates poor architecture boundaries.

## Required Inputs

Require at least one of:

- requirements brief
- scope-boundary brief
- product/domain notes
- user-provided domain description

If terms are missing, infer a first-pass glossary and label inferred terms as assumptions.

## Language Analysis

Identify:

- canonical terms
- synonyms and aliases
- overloaded terms with multiple meanings
- forbidden or misleading terms
- actor-facing versus internal business terms
- terms owned by external systems
- terms that imply source-of-truth ownership
- lifecycle terms such as pending, active, suspended, cancelled, fulfilled, expired, failed
- policy terms such as eligible, verified, approved, blocked, restricted, trusted

## Output

Return:

| Term | Definition | Type | Owner | Synonyms | Ambiguity risk |
|------|------------|------|-------|----------|----------------|

Then list:

- term decisions
- forbidden synonyms
- unresolved vocabulary questions
- architecture implications of ambiguous terms
