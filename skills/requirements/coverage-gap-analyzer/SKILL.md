---
name: coverage-gap-analyzer
description: "Acceptance Criteria Coverage Gap Analyzer. Find missing, partial, blocked, duplicated, ambiguous, or orphaned coverage."
---

# Acceptance Criteria Coverage Gap Analyzer

## Purpose
Find missing, partial, blocked, duplicated, ambiguous, or orphaned coverage.

## Inputs
- Relevant PRD, feature brief, requirement register, story, business rules, test artifacts, or change record.
- Source IDs and version/date information where available.
- Desired deliverable and constraints.
- Approved decisions and related artifacts, if supplied.

## Process
1. Compare requirements with criteria and scenarios.
2. Check stated actors, rules, states, constraints, and outcomes.
3. Classify gaps with source evidence.
4. Prioritize with stated rationale.
5. Recommend next artifact or decision.

## Expected outputs
- Gap register
- Coverage table
- Priority rationale
- Blockers
- Next actions

## Quality checklist
- [ ] Material outputs have source references or clearly labeled generated IDs.
- [ ] Facts are distinguished from interpretations, assumptions, unknowns, conflicts, and proposals.
- [ ] Missing information has not been silently converted into product behavior.
- [ ] Recommendations include rationale and uncertainty where relevant.
- [ ] Output matches the requested format and supports the next reviewer.

## Guardrails
- Do not call coverage complete because every requirement has one criterion.
- Do not invent criteria for unknown behavior.
- Do not claim tool execution, automated checks, stakeholder approvals, or tests unless they occurred.

## Definition of done
The artifact is delivered with traceability, quality checks, and unresolved decisions clearly represented. Any blocker is explicit.
