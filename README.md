# Product Manager Toolkit

**A modular, AI-powered toolkit for Product Managers.**

Reusable Skills, specialist agents, workflows, prompts, templates, integrations, and evaluation resources for product work from discovery and strategy through requirements, delivery, growth, and learning.

> **Core principle:** Keep product artifacts grounded in source evidence, traceable to requirements, testable where applicable, and explicit about unresolved decisions. Never invent business rules to make an output look complete.

## Start here

Choose a Skill that matches the task, read its instructions, provide relevant source material, then review the output against its quality checklist. Resolve blocking questions before treating generated behavior as approved.

## Existing product-management Skills

These ten Skills were migrated from the [Claude Skills for Product Manager repository](https://github.com/imohammadfaraz/claude-skills-for-product-manager). Original instructions are preserved; review runtime-specific wording before using them elsewhere.

- [A/B Testing Expert](skills/experimentation/ab-testing-expert/SKILL.md)
- [Competitive Analysis Expert](skills/strategy/competitive-analysis-expert/SKILL.md)
- [GTM Planner](skills/launch/gtm-planner/SKILL.md)
- [Metrics & Analytics Designer](skills/analytics/metrics-analytics-designer/SKILL.md)
- [Monetization Strategist](skills/growth/monetization-strategist/SKILL.md)
- [PRD Generator](skills/requirements/prd-generator/SKILL.md)
- [Problem Definition Expert](skills/discovery/problem-definition-expert/SKILL.md)
- [Product Strategy Builder](skills/strategy/product-strategy-builder/SKILL.md)
- [Risk & Edge Case Analyzer](skills/quality/risk-and-edge-case-analyzer/SKILL.md)
- [UX Reviewer](skills/design/ux-reviewer/SKILL.md)

## Requirements & Acceptance Criteria Toolkit

This collection contains 18 focused Skills. Each can be used independently; chained execution depends on runtime configuration.

1. [PRD Intake & Normalizer](skills/requirements/prd-intake/SKILL.md)
2. [PRD Analyzer](skills/requirements/prd-analyzer/SKILL.md)
3. [Requirement Decomposer](skills/requirements/requirement-decomposer/SKILL.md)
4. [Clarification & Decision Builder](skills/requirements/clarification-builder/SKILL.md)
5. [User Story Generator](skills/requirements/user-story-generator/SKILL.md)
6. [Acceptance Criteria Generator](skills/requirements/acceptance-criteria-generator/SKILL.md)
7. [Business Rules & Decision Table Builder](skills/requirements/business-rule-builder/SKILL.md)
8. [PRD-to-Gherkin Converter](skills/requirements/prd-to-gherkin/SKILL.md)
9. [Scenario Coverage Planner](skills/requirements/scenario-coverage-planner/SKILL.md)
10. [Edge Case & Negative Path Generator](skills/requirements/edge-case-generator/SKILL.md)
11. [Test Data & Boundary Value Builder](skills/requirements/test-data-builder/SKILL.md)
12. [Non-Functional Acceptance Criteria Reviewer](skills/requirements/non-functional-reviewer/SKILL.md)
13. [Gherkin Quality Reviewer](skills/requirements/gherkin-quality-reviewer/SKILL.md)
14. [Requirements Traceability Matrix Builder](skills/requirements/traceability-matrix/SKILL.md)
15. [Acceptance Criteria Coverage Gap Analyzer](skills/requirements/coverage-gap-analyzer/SKILL.md)
16. [Requirements Change Impact Analyzer](skills/requirements/change-impact-analyzer/SKILL.md)
17. [QA Handoff & Automation Readiness Reviewer](skills/requirements/qa-handoff/SKILL.md)
18. [Acceptance Criteria Workflow Orchestrator](skills/requirements/workflow-orchestrator/SKILL.md)

## Suggested workflows

**Rough PRD to scenarios:** PRD Intake → PRD Analyzer → Requirement Decomposer → Clarification Builder → User Story / Acceptance Criteria Generator → PRD-to-Gherkin.

**Mature requirements to QA:** PRD-to-Gherkin → Scenario Coverage Planner → Edge Case Generator → Gherkin Quality Reviewer → Traceability Matrix → QA Handoff.

**Requirement change:** Change Impact Analyzer → focused review → Coverage Gap Analyzer → update impacted criteria/scenarios → traceability review → QA handoff.

These are workflow guides, not claims of automatic execution.

## Shared quality principles

- Preserve source references and stable IDs.
- Distinguish facts, interpretations, assumptions, unknowns, conflicts, and proposals.
- Keep criteria observable and testable.
- Never invent thresholds, permissions, calculations, defaults, retries, error behavior, or targets.
- Classify coverage honestly as covered, partial, missing, blocked, duplicate, or not applicable.
- Do not claim execution, validation, integration, or stakeholder approval unless it occurred.
- Keep platform-specific configuration separate from reusable source instructions.

## Repository structure

```text
product-manager-toolkit/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── ROADMAP.md
├── catalog/
├── skills/
├── agents/
├── workflows/
├── toolkits/
├── commands/
├── prompts/
├── templates/
├── integrations/
├── evals/
├── examples/
├── schemas/
├── docs/
└── scripts/
```

## Adding a Skill

Use a unique kebab-case directory and a `SKILL.md` with purpose, inputs, ordered process, outputs, quality checks, examples, guardrails, and definition of done. Update the catalog and README, and review licenses before reusing third-party material.

## License

No license has been selected yet. Add a `LICENSE` file before granting explicit reuse or redistribution rights.
