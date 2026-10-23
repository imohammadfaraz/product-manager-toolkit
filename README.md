# Product Manager Toolkit

A modular, AI-powered toolkit for Product Managers. It collects reusable Skills, specialist agents, workflows, prompts, templates, integrations, and evaluation resources for work from discovery and strategy through requirements, delivery, growth, and learning.

> **Principle:** Product artifacts should be grounded in source evidence, traceable, testable where applicable, and explicit about unresolved decisions. Never invent product rules just to make an output look complete.

## Start here

Pick a Skill for the task, read its instructions, provide the relevant source material, and review the output against its quality checklist. Workflows are guides unless the target runtime is configured to execute them.

## Skills

This repository currently contains 28 Skills.

1. [Metrics Analytics Designer](skills/analytics/metrics-analytics-designer/SKILL.md)
2. [Ux Reviewer](skills/design/ux-reviewer/SKILL.md)
3. [Problem Definition Expert](skills/discovery/problem-definition-expert/SKILL.md)
4. [Ab Testing Expert](skills/experimentation/ab-testing-expert/SKILL.md)
5. [Monetization Strategist](skills/growth/monetization-strategist/SKILL.md)
6. [Gtm Planner](skills/launch/gtm-planner/SKILL.md)
7. [Risk And Edge Case Analyzer](skills/quality/risk-and-edge-case-analyzer/SKILL.md)
8. [Acceptance Criteria Generator](skills/requirements/acceptance-criteria-generator/SKILL.md)
9. [Business Rule Builder](skills/requirements/business-rule-builder/SKILL.md)
10. [Change Impact Analyzer](skills/requirements/change-impact-analyzer/SKILL.md)
11. [Clarification Builder](skills/requirements/clarification-builder/SKILL.md)
12. [Coverage Gap Analyzer](skills/requirements/coverage-gap-analyzer/SKILL.md)
13. [Edge Case Generator](skills/requirements/edge-case-generator/SKILL.md)
14. [Gherkin Quality Reviewer](skills/requirements/gherkin-quality-reviewer/SKILL.md)
15. [Non Functional Reviewer](skills/requirements/non-functional-reviewer/SKILL.md)
16. [Prd Analyzer](skills/requirements/prd-analyzer/SKILL.md)
17. [Prd Generator](skills/requirements/prd-generator/SKILL.md)
18. [Prd Intake](skills/requirements/prd-intake/SKILL.md)
19. [Prd To Gherkin](skills/requirements/prd-to-gherkin/SKILL.md)
20. [Qa Handoff](skills/requirements/qa-handoff/SKILL.md)
21. [Requirement Decomposer](skills/requirements/requirement-decomposer/SKILL.md)
22. [Scenario Coverage Planner](skills/requirements/scenario-coverage-planner/SKILL.md)
23. [Test Data Builder](skills/requirements/test-data-builder/SKILL.md)
24. [Traceability Matrix](skills/requirements/traceability-matrix/SKILL.md)
25. [User Story Generator](skills/requirements/user-story-generator/SKILL.md)
26. [Workflow Orchestrator](skills/requirements/workflow-orchestrator/SKILL.md)
27. [Competitive Analysis Expert](skills/strategy/competitive-analysis-expert/SKILL.md)
28. [Product Strategy Builder](skills/strategy/product-strategy-builder/SKILL.md)

### Existing Product Management Skills

These ten Skills were migrated from [Claude Skills for Product Manager](https://github.com/imohammadfaraz/claude-skills-for-product-manager). Their original instruction content is preserved, with source references retained. Review runtime-specific phrasing before using them on other agent platforms.

- [Metrics Analytics Designer](skills/analytics/metrics-analytics-designer/SKILL.md)
- [Ux Reviewer](skills/design/ux-reviewer/SKILL.md)
- [Problem Definition Expert](skills/discovery/problem-definition-expert/SKILL.md)
- [Ab Testing Expert](skills/experimentation/ab-testing-expert/SKILL.md)
- [Monetization Strategist](skills/growth/monetization-strategist/SKILL.md)
- [Gtm Planner](skills/launch/gtm-planner/SKILL.md)
- [Risk And Edge Case Analyzer](skills/quality/risk-and-edge-case-analyzer/SKILL.md)
- [Prd Generator](skills/requirements/prd-generator/SKILL.md)
- [Competitive Analysis Expert](skills/strategy/competitive-analysis-expert/SKILL.md)
- [Product Strategy Builder](skills/strategy/product-strategy-builder/SKILL.md)

### Requirements & Acceptance Criteria Skills

This collection supports the path from PRD intake to quality-reviewed QA handoff.

- [Acceptance Criteria Generator](skills/requirements/acceptance-criteria-generator/SKILL.md)
- [Business Rule Builder](skills/requirements/business-rule-builder/SKILL.md)
- [Change Impact Analyzer](skills/requirements/change-impact-analyzer/SKILL.md)
- [Clarification Builder](skills/requirements/clarification-builder/SKILL.md)
- [Coverage Gap Analyzer](skills/requirements/coverage-gap-analyzer/SKILL.md)
- [Edge Case Generator](skills/requirements/edge-case-generator/SKILL.md)
- [Gherkin Quality Reviewer](skills/requirements/gherkin-quality-reviewer/SKILL.md)
- [Non Functional Reviewer](skills/requirements/non-functional-reviewer/SKILL.md)
- [Prd Analyzer](skills/requirements/prd-analyzer/SKILL.md)
- [Prd Generator](skills/requirements/prd-generator/SKILL.md)
- [Prd Intake](skills/requirements/prd-intake/SKILL.md)
- [Prd To Gherkin](skills/requirements/prd-to-gherkin/SKILL.md)
- [Qa Handoff](skills/requirements/qa-handoff/SKILL.md)
- [Requirement Decomposer](skills/requirements/requirement-decomposer/SKILL.md)
- [Scenario Coverage Planner](skills/requirements/scenario-coverage-planner/SKILL.md)
- [Test Data Builder](skills/requirements/test-data-builder/SKILL.md)
- [Traceability Matrix](skills/requirements/traceability-matrix/SKILL.md)
- [User Story Generator](skills/requirements/user-story-generator/SKILL.md)
- [Workflow Orchestrator](skills/requirements/workflow-orchestrator/SKILL.md)

## Suggested workflows

**PRD to scenarios:** PRD Intake → PRD Analyzer → Requirement Decomposer → Clarification Builder → User Story / Acceptance Criteria Generator → PRD-to-Gherkin.

**Scenarios to QA handoff:** Scenario Coverage Planner → Edge Case Generator → Gherkin Quality Reviewer → Traceability Matrix → Coverage Gap Analyzer → QA Handoff.

**Requirement change:** Change Impact Analyzer → focused requirement review → update impacted criteria/scenarios → refresh traceability → QA handoff.

## Shared quality rules

- Preserve original source references and stable identifiers.
- Distinguish facts, interpretations, assumptions, unknowns, conflicts, and proposals.
- Make criteria observable and testable.
- Never invent thresholds, permissions, calculations, defaults, retry counts, error behavior, or performance targets.
- Classify coverage honestly as covered, partial, missing, blocked, duplicate, or not applicable.
- Do not claim testing, linting, integration, or approval unless it actually happened.
- Keep vendor-specific instructions and adapters separate from reusable capability definitions.

## Adding a new Skill

Create a unique kebab-case folder under the appropriate category in `skills/`, and use `SKILL.md` with: purpose, inputs, process, expected outputs, quality checklist, guardrails, and definition of done. Add the path and metadata to `catalog/skills.yaml`, then update the README and relevant workflows.

## More repository guides

- [Contributing](CONTRIBUTING.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)
- [Asset types](docs/asset-types.md)
- [Requirements & Acceptance Criteria Toolkit](toolkits/acceptance-criteria/TOOLKIT.md)
- [PRD to Acceptance Criteria Workflow](workflows/prd-to-acceptance-criteria/WORKFLOW.md)
- [Requirements Change Review Workflow](workflows/requirements-change-review/WORKFLOW.md)
- [QA Handoff Workflow](workflows/qa-handoff/WORKFLOW.md)

## License

A license has not yet been selected. Add a `LICENSE` file before explicitly granting reuse or redistribution rights.
