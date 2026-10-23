---
name: dependency-mapper
display_name: "Dependency Mapper"
description: "create a structured artifact for dependency mapper and turn the result into a decision-ready a usable artifact with explicit structure, rationale, and open questions"
category: execution
asset_type: skill
version: "1.0.0"
status: active
portability: portable
review_status: standardized
tags: ["product-management", "execution", "dependency-mapper"]
---
# Dependency Mapper

## Purpose
This Skill helps product teams create a structured artifact for dependency mapper and turn the result into a decision-ready a usable artifact with explicit structure, rationale, and open questions.

## When to use
Use when a product team needs to create a structured artifact for dependency mapper and has a concrete decision, artifact, or learning goal. This Skill produces recommendations and work products from supplied context; it does not imply external research, tool execution, user testing, or stakeholder approval unless those actions actually occur.

## Inputs
- Product goals, candidate work, team capacity, dependencies, constraints, planning horizon, and stakeholder context.
- The specific source artifact, dataset, notes, requirements, or options to work from, if available.
- Required output format, audience, depth, and constraints.
- Known decisions, deadlines, dependencies, and unresolved questions.

## Process
1. Choose a structure that fits the decision and the maturity of the product; do not force a large template when a compact artifact is sufficient.
2. Populate each section using source-backed facts and explicit assumptions. Preserve traceability between inputs, analysis, and recommendations.
3. Check internal consistency, missing sections, dependencies, and whether the artifact can be used without undocumented context.
4. Make execution realistic: expose dependencies, capacity limits, decision owners, risks, and proposed versus confirmed dates.
5. **Communicate uncertainty.** Label facts, estimates, assumptions, hypotheses, and unknowns. Ask only clarifying questions that materially change the result; otherwise proceed with explicit assumptions.
6. **Make the result actionable.** Prioritize the most important findings, identify the next decision or validation step, and keep recommendations proportional to the evidence and team capacity.

## Expected outputs
- A primary a usable artifact with explicit structure, rationale, and open questions.
- A concise rationale tied to the supplied context and decision.
- Evidence, assumptions, unknowns, and material risks clearly separated.
- Prioritized next steps, validation checks, and open questions.
- A compact, reusable artifact format appropriate to dependency mapper, rather than an unstructured brainstorm.

## Quality checklist
- The output directly addresses the stated objective and intended audience.
- Every important recommendation is connected to evidence, a clearly labeled assumption, or an explicit hypothesis.
- Alternatives, trade-offs, limitations, and material failure modes are considered.
- Priorities are explained; false precision and unsupported claims are avoided.
- The artifact is clear enough for another teammate to review, challenge, and use.
- Priorities connect to outcomes; dependencies and risks are visible; capacity assumptions are stated; decisions and follow-ups are actionable.

## Guardrails
- Do not invent source evidence, customer quotes, statistics, benchmarks, policies, approvals, owners, dates, or system capabilities.
- Do not claim to have browsed, run code, queried a database, tested a prototype, or verified an implementation unless that action actually occurred.
- If information is missing, identify the gap and either ask a focused question or proceed with clearly labeled assumptions.
- Distinguish committed facts from proposals; do not invent owners, delivery dates, capacity, or approvals.

## Definition of done
The user receives a usable a usable artifact with explicit structure, rationale, and open questions, a clear rationale, a truthful account of uncertainty, and concrete next steps. The output should help a team make or prepare for a real product decision without obscuring what still needs validation.
