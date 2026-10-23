---
name: research-insight-prioritizer
display_name: "Research Insight Prioritizer"
description: "rank options for research insight and turn the result into a decision-ready a ranked set of options with criteria, trade-offs, and sensitivity notes"
category: discovery
asset_type: skill
version: "1.0.0"
status: active
portability: portable
review_status: standardized
tags: ["product-management", "discovery", "research-insight"]
---
# Research Insight Prioritizer

## Purpose
This Skill helps product teams rank options for research insight and turn the result into a decision-ready a ranked set of options with criteria, trade-offs, and sensitivity notes.

## When to use
Use when a product team needs to rank options for research insight and has a concrete decision, artifact, or learning goal. This Skill produces recommendations and work products from supplied context; it does not imply external research, tool execution, user testing, or stakeholder approval unless those actions actually occur.

## Inputs
- Customer problem, target segment, research question, context of use, existing evidence, and constraints.
- The specific source artifact, dataset, notes, requirements, or options to work from, if available.
- Required output format, audience, depth, and constraints.
- Known decisions, deadlines, dependencies, and unresolved questions.

## Process
1. Agree on the outcome, eligibility criteria, and constraints before ranking candidates.
2. Apply a transparent method. Explain scoring scales and weights; keep raw evidence separate from subjective estimates.
3. Show the ranking, rationale, trade-offs, confidence, and how the result changes if a key assumption or weight changes.
4. Reduce bias: use open questions, seek disconfirming evidence, document sampling limitations, and avoid presenting a small sample as representative of all users.
5. **Communicate uncertainty.** Label facts, estimates, assumptions, hypotheses, and unknowns. Ask only clarifying questions that materially change the result; otherwise proceed with explicit assumptions.
6. **Make the result actionable.** Prioritize the most important findings, identify the next decision or validation step, and keep recommendations proportional to the evidence and team capacity.

## Expected outputs
- A primary a ranked set of options with criteria, trade-offs, and sensitivity notes.
- A concise rationale tied to the supplied context and decision.
- Evidence, assumptions, unknowns, and material risks clearly separated.
- Prioritized next steps, validation checks, and open questions.
- A compact, reusable artifact format appropriate to research insight prioritizer, rather than an unstructured brainstorm.

## Quality checklist
- The output directly addresses the stated objective and intended audience.
- Every important recommendation is connected to evidence, a clearly labeled assumption, or an explicit hypothesis.
- Alternatives, trade-offs, limitations, and material failure modes are considered.
- Priorities are explained; false precision and unsupported claims are avoided.
- The artifact is clear enough for another teammate to review, challenge, and use.
- Insights are traceable to supplied evidence; counterexamples and uncertainty remain visible; recommendations do not presume the preferred solution.

## Guardrails
- Do not invent source evidence, customer quotes, statistics, benchmarks, policies, approvals, owners, dates, or system capabilities.
- Do not claim to have browsed, run code, queried a database, tested a prototype, or verified an implementation unless that action actually occurred.
- If information is missing, identify the gap and either ask a focused question or proceed with clearly labeled assumptions.
- Use neutral language, protect participant privacy, distinguish direct evidence from interpretation, and never invent quotes or research findings.

## Definition of done
The user receives a usable a ranked set of options with criteria, trade-offs, and sensitivity notes, a clear rationale, a truthful account of uncertainty, and concrete next steps. The output should help a team make or prepare for a real product decision without obscuring what still needs validation.
