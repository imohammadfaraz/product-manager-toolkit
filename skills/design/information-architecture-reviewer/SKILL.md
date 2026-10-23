---
name: information-architecture-reviewer
display_name: "Information Architecture Reviewer"
description: "evaluate the quality and completeness of information architecture and turn the result into a decision-ready a prioritized review with evidence, severity, recommendations, and unresolved risks"
category: design
asset_type: skill
version: "1.0.0"
status: active
portability: portable
review_status: standardized
tags: ["product-management", "design", "information-architecture"]
---
# Information Architecture Reviewer

## Purpose
This Skill helps product teams evaluate the quality and completeness of information architecture and turn the result into a decision-ready a prioritized review with evidence, severity, recommendations, and unresolved risks.

## When to use
Use when a product team needs to evaluate the quality and completeness of information architecture and has a concrete decision, artifact, or learning goal. This Skill produces recommendations and work products from supplied context; it does not imply external research, tool execution, user testing, or stakeholder approval unless those actions actually occur.

## Inputs
- Screens, flows, prototypes, content, target users, task context, accessibility needs, and research or product evidence.
- The specific source artifact, dataset, notes, requirements, or options to work from, if available.
- Required output format, audience, depth, and constraints.
- Known decisions, deadlines, dependencies, and unresolved questions.

## Process
1. Inspect the supplied artifact against a fit-for-purpose rubric and the intended user or decision.
2. Record each finding with evidence or location, consequence, severity, confidence, and a specific recommended change.
3. Separate blocking issues from improvements; identify what cannot be assessed from the available material and define validation steps.
4. Include inclusive and failure paths: assess accessibility, comprehension, empty/error/loading states, recovery, and task completion.
5. **Communicate uncertainty.** Label facts, estimates, assumptions, hypotheses, and unknowns. Ask only clarifying questions that materially change the result; otherwise proceed with explicit assumptions.
6. **Make the result actionable.** Prioritize the most important findings, identify the next decision or validation step, and keep recommendations proportional to the evidence and team capacity.

## Expected outputs
- A primary a prioritized review with evidence, severity, recommendations, and unresolved risks.
- A concise rationale tied to the supplied context and decision.
- Evidence, assumptions, unknowns, and material risks clearly separated.
- Prioritized next steps, validation checks, and open questions.
- A compact, reusable artifact format appropriate to information architecture reviewer, rather than an unstructured brainstorm.

## Quality checklist
- The output directly addresses the stated objective and intended audience.
- Every important recommendation is connected to evidence, a clearly labeled assumption, or an explicit hypothesis.
- Alternatives, trade-offs, limitations, and material failure modes are considered.
- Priorities are explained; false precision and unsupported claims are avoided.
- The artifact is clear enough for another teammate to review, challenge, and use.
- Recommendations are concrete and prioritized; usability claims are not inferred as measured behavior; validation methods are specified.

## Guardrails
- Do not invent source evidence, customer quotes, statistics, benchmarks, policies, approvals, owners, dates, or system capabilities.
- Do not claim to have browsed, run code, queried a database, tested a prototype, or verified an implementation unless that action actually occurred.
- If information is missing, identify the gap and either ask a focused question or proceed with clearly labeled assumptions.
- Tie findings to specific elements and tasks; separate observation from hypothesis; treat accessibility and error recovery as core quality.

## Definition of done
The user receives a usable a prioritized review with evidence, severity, recommendations, and unresolved risks, a clear rationale, a truthful account of uncertainty, and concrete next steps. The output should help a team make or prepare for a real product decision without obscuring what still needs validation.
