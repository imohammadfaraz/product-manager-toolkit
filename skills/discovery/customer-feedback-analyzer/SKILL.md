---
name: customer-feedback-analyzer
display_name: "Customer Feedback Analyzer"
description: "analyze customer feedback and turn the result into a decision-ready a structured analysis with evidence, alternatives, implications, and next steps"
category: discovery
asset_type: skill
version: "1.0.0"
status: active
portability: portable
review_status: standardized
tags: ["product-management", "discovery", "customer-feedback"]
---
# Customer Feedback Analyzer

## Purpose
This Skill helps product teams analyze customer feedback and turn the result into a decision-ready a structured analysis with evidence, alternatives, implications, and next steps.

## When to use
Use when a product team needs to analyze customer feedback and has a concrete decision, artifact, or learning goal. This Skill produces recommendations and work products from supplied context; it does not imply external research, tool execution, user testing, or stakeholder approval unless those actions actually occur.

## Inputs
- Customer problem, target segment, research question, context of use, existing evidence, and constraints.
- The specific source artifact, dataset, notes, requirements, or options to work from, if available.
- Required output format, audience, depth, and constraints.
- Known decisions, deadlines, dependencies, and unresolved questions.

## Process
1. Define the decision and comparison frame; identify the relevant user, system, market, or workflow boundary.
2. Examine evidence, likely drivers, alternatives, dependencies, and counter-explanations. Separate correlation from causation where relevant.
3. Rank findings by impact and confidence, recommend validation or action, and state what remains unknown.
4. Reduce bias: use open questions, seek disconfirming evidence, document sampling limitations, and avoid presenting a small sample as representative of all users.
5. **Communicate uncertainty.** Label facts, estimates, assumptions, hypotheses, and unknowns. Ask only clarifying questions that materially change the result; otherwise proceed with explicit assumptions.
6. **Make the result actionable.** Prioritize the most important findings, identify the next decision or validation step, and keep recommendations proportional to the evidence and team capacity.

## Expected outputs
- A primary a structured analysis with evidence, alternatives, implications, and next steps.
- A concise rationale tied to the supplied context and decision.
- Evidence, assumptions, unknowns, and material risks clearly separated.
- Prioritized next steps, validation checks, and open questions.
- A compact, reusable artifact format appropriate to customer feedback analyzer, rather than an unstructured brainstorm.

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
The user receives a usable a structured analysis with evidence, alternatives, implications, and next steps, a clear rationale, a truthful account of uncertainty, and concrete next steps. The output should help a team make or prepare for a real product decision without obscuring what still needs validation.
