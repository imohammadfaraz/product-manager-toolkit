# Product Manager Toolkit

**A modular, AI-powered toolkit for Product Managers.**

Reusable Skills, specialist agents, workflows, prompts, templates, integrations, and evaluation resources for work from product discovery and strategy through requirements, execution, growth, and learning.

> **Design principle:** Keep product artifacts grounded in source evidence, traceable, testable where applicable, and explicit about unresolved decisions. Never invent product rules to make an output look complete.

## Browse Skills

This repository currently contains **28 standalone Skills**, each in its own `SKILL.md` file.

### Existing Product Management Skills

These 10 Skills were migrated from [Claude Skills for Product Manager](https://github.com/imohammadfaraz/claude-skills-for-product-manager). Their metadata and top-level operating structure are standardized, while the original detailed instructions remain preserved. Each is marked `migrated-source-preserved` and `standardized-wrapper-content-review-needed`; treat platform-specific wording as unverified until its content review is completed.

#### Analytics & Metrics

- [Metrics & Analytics Designer](skills/analytics/metrics-analytics-designer/SKILL.md)

#### UX & Design

- [UX Reviewer](skills/design/ux-reviewer/SKILL.md)

#### Discovery

- [Problem Definition Expert](skills/discovery/problem-definition-expert/SKILL.md)

#### Experimentation

- [A/B Testing Expert](skills/experimentation/ab-testing-expert/SKILL.md)

#### Growth & Monetization

- [Monetization Strategist](skills/growth/monetization-strategist/SKILL.md)

#### Launch & GTM

- [GTM Planner](skills/launch/gtm-planner/SKILL.md)

#### Quality & Risk

- [Risk & Edge Case Analyzer](skills/quality/risk-and-edge-case-analyzer/SKILL.md)

#### Requirements & Acceptance Criteria

- [PRD Generator](skills/requirements/prd-generator/SKILL.md)

#### Strategy

- [Competitive Analysis Expert](skills/strategy/competitive-analysis-expert/SKILL.md)
- [Product Strategy Builder](skills/strategy/product-strategy-builder/SKILL.md)

### Requirements & Acceptance Criteria Skills

These 18 Skills support the path from PRD intake to QA handoff.

- [Acceptance Criteria Generator](skills/requirements/acceptance-criteria-generator/SKILL.md)
- [Business Rules & Decision Table Builder](skills/requirements/business-rule-builder/SKILL.md)
- [Requirements Change Impact Analyzer](skills/requirements/change-impact-analyzer/SKILL.md)
- [Clarification & Decision Builder](skills/requirements/clarification-builder/SKILL.md)
- [Acceptance Criteria Coverage Gap Analyzer](skills/requirements/coverage-gap-analyzer/SKILL.md)
- [Edge Case & Negative Path Generator](skills/requirements/edge-case-generator/SKILL.md)
- [Gherkin Quality Reviewer](skills/requirements/gherkin-quality-reviewer/SKILL.md)
- [Non-Functional Acceptance Criteria Reviewer](skills/requirements/non-functional-reviewer/SKILL.md)
- [PRD Analyzer](skills/requirements/prd-analyzer/SKILL.md)
- [PRD Intake & Normalizer](skills/requirements/prd-intake/SKILL.md)
- [PRD-to-Gherkin Converter](skills/requirements/prd-to-gherkin/SKILL.md)
- [QA Handoff & Automation Readiness Reviewer](skills/requirements/qa-handoff/SKILL.md)
- [Requirement Decomposer](skills/requirements/requirement-decomposer/SKILL.md)
- [Scenario Coverage Planner](skills/requirements/scenario-coverage-planner/SKILL.md)
- [Test Data & Boundary Value Builder](skills/requirements/test-data-builder/SKILL.md)
- [Requirements Traceability Matrix Builder](skills/requirements/traceability-matrix/SKILL.md)
- [User Story Generator](skills/requirements/user-story-generator/SKILL.md)
- [Acceptance Criteria Workflow Orchestrator](skills/requirements/workflow-orchestrator/SKILL.md)

## Suggested Workflows

**PRD to scenarios:** PRD Intake & Normalizer → PRD Analyzer → Requirement Decomposer → Clarification & Decision Builder → User Story Generator / Acceptance Criteria Generator → PRD-to-Gherkin Converter.

**Scenarios to QA handoff:** Scenario Coverage Planner → Edge Case & Negative Path Generator → Gherkin Quality Reviewer → Requirements Traceability Matrix Builder → Coverage Gap Analyzer → QA Handoff.

**Requirement change:** Requirements Change Impact Analyzer → focused requirement review → update impacted criteria and scenarios → refresh traceability → QA handoff.

Workflow files are operating guides. They do not imply that Skills execute or call one another automatically.

## Shared Quality Principles

- Preserve source references and stable identifiers.
- Distinguish facts, interpretations, assumptions, unknowns, conflicts, and proposals.
- Keep acceptance criteria observable and testable.
- Never invent thresholds, permissions, calculations, defaults, retries, error behavior, or performance targets.
- Classify coverage honestly as covered, partial, missing, blocked, duplicate, or not applicable.
- Do not claim testing, linting, integration, or approval unless it actually happened.
- Keep vendor-specific setup separate from reusable instructions as the toolkit expands.

## Repository Layout

| Path | Purpose |
|---|---|
| `skills/<category>/<skill-name>/SKILL.md` | Standalone capabilities |
| `toolkits/` | Curated collections of related Skills |
| `workflows/` | Multi-step process guides |
| `catalog/` | Machine-readable discovery metadata |
| `agents/` | Future specialist agent definitions |
| `commands/` and `prompts/` | Future invocation patterns and reusable prompts |
| `templates/` | Future product artifact templates |
| `integrations/` | Runtime- or vendor-specific adapters |
| `evals/` and `examples/` | Future fixtures, evaluations, and sample outputs |

## Foundation checks

- [Skill authoring standard](docs/skill-standard.md)
- [Current duplication and coverage audit](docs/skill-audit.md)
- [Skill metadata schema](schemas/skill.schema.json)
- [Validation script](scripts/validate_skills.py)

Run `python scripts/validate_skills.py` before submitting changes. The GitHub Actions workflow runs the same checks on pushes and pull requests.

## Adding a Skill

1. Create a unique kebab-case folder under the appropriate category.
2. Add a `SKILL.md` with purpose, inputs, process, expected outputs, quality checks, guardrails, and definition of done.
3. Add its ID, category, and path to `catalog/skills.yaml`.
4. Update this README and any workflows that should reference it.
5. Add examples or evaluation cases for important behaviors.

## Project Guides

- [Contributing](CONTRIBUTING.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)
- [Asset Types](docs/asset-types.md)
- [Skill Standard](docs/skill-standard.md)
- [Skill Audit](docs/skill-audit.md)
- [Requirements & Acceptance Criteria Toolkit](toolkits/acceptance-criteria/TOOLKIT.md)
- [PRD to Acceptance Criteria Workflow](workflows/prd-to-acceptance-criteria/WORKFLOW.md)
- [Requirements Change Review Workflow](workflows/requirements-change-review/WORKFLOW.md)
- [QA Handoff Workflow](workflows/qa-handoff/WORKFLOW.md)

## License

A license has not yet been selected. Add a `LICENSE` file before granting explicit reuse or redistribution rights.
