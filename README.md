# Product Manager Toolkit

**A modular, AI-powered toolkit for Product Managers.**

Reusable Skills, specialist agents, workflows, prompts, templates, integrations, and evaluation resources for work from product discovery and strategy through requirements, execution, growth, and learning.

> **Design principle:** Keep product artifacts grounded in source evidence, traceable, testable where applicable, and explicit about unresolved decisions. Never invent product rules to make an output look complete.

## Browse Skills

This repository currently contains **150 standalone Skills**, each in its own `SKILL.md` file.

### Existing Product Management Skills

Ten migrated Skills have now been editorially reviewed for portability, conflicting instructions, evidence handling, and scope boundaries. The remaining toolkit-authored Skills use the shared canonical structure; a `standardized` status indicates structural consistency, not a claim that every Skill has passed runtime evaluation.

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
| `agents/<agent-id>/AGENT.md` and `agent.json` | Specialist agent operating guides and portable contracts |
| `commands/` and `prompts/` | Future invocation patterns and reusable prompts |
| `templates/` | Future product artifact templates |
| `integrations/` | Vendor-specific integration guides and machine-readable contracts; currently documented only |
| `evals/` and `examples/` | Evaluation fixtures and sample outputs |

## Specialist agents

Twelve draft specialist agents cover discovery, strategy, execution, analytics, AI product management, AI product building, growth, UX review, independent product critique, PM operations, Skill authoring, and workflow orchestration. Start with the [agent roster and security boundaries](agents/README.md) or [machine-readable agent catalog](catalog/agents.yaml). These are portable reference definitions, not deployed agents; tools are not configured and runtime safety has not been certified.

## Universal discovery and usage

- [Universal Agent, Skill, and Workflow Discovery & Usage Guide](docs/agent-discovery-and-usage.md)

Use this guide to discover the right asset, invoke it in a compatible host, combine Skills into workflows, evaluate outputs, and understand platform, permissions, and human-review boundaries.

## Asset definition schemas

- [Schema overview and validation instructions](schemas/README.md)
- [Skill metadata schema](schemas/skill.schema.json)
- [Agent definition schema](schemas/agent.schema.json)
- [Workflow definition schema](schemas/workflow.schema.json)
- [Integration definition schema](schemas/integration.schema.json)
- [Integration discovery catalog](catalog/integrations.yaml)

CI validates all four schemas and their canonical example fixtures. Schema validation is structural and does not establish runtime quality or platform compatibility.

## Tool integration layer

The [integration registry](catalog/integrations.yaml) indexes 27 documented integration patterns across research, analytics, delivery, design, AI evaluation, and coding agents. Each has a README setup guide and machine-readable integration contract. See the [integration layer overview](integrations/README.md) and [reusable integration template](integrations/INTEGRATION_TEMPLATE.md).

**Important:** all entries are documented-only and unverified. This repository does not yet include live MCP servers, API clients, configured credentials, or executable integrations. The registry explicitly distinguishes documentation from tested and executable status. CI validates the shape of each integration contract, not live connectivity or security.

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
- [Universal Agent, Skill, and Workflow Discovery & Usage Guide](docs/agent-discovery-and-usage.md)
- [Requirements & Acceptance Criteria Toolkit](toolkits/acceptance-criteria/TOOLKIT.md)
- [PRD to Acceptance Criteria Workflow](workflows/prd-to-acceptance-criteria/WORKFLOW.md)
- [Requirements Change Review Workflow](workflows/requirements-change-review/WORKFLOW.md)
- [QA Handoff Workflow](workflows/qa-handoff/WORKFLOW.md)

## License

A license has not yet been selected. Add a `LICENSE` file before granting explicit reuse or redistribution rights.


## Product Lifecycle and AI-Native Skills

The following 122 Skills expand coverage across discovery, strategy, execution, analytics, design quality, AI product management, prototyping, leadership, and PM career development. Core instructions are portable. Vendor-specific setup and changing tool capabilities belong in separate integration guides.

### Product Discovery & Customer Research

- [Customer Interview Planner](skills/discovery/customer-interview-planner/SKILL.md)
- [Interview Question Builder](skills/discovery/interview-question-builder/SKILL.md)
- [Interview Synthesis](skills/discovery/interview-synthesis/SKILL.md)
- [Customer Feedback Analyzer](skills/discovery/customer-feedback-analyzer/SKILL.md)
- [Jobs-to-be-Done Analyzer](skills/discovery/jobs-to-be-done-analyzer/SKILL.md)
- [Persona Builder](skills/discovery/persona-builder/SKILL.md)
- [Customer Journey Mapper](skills/discovery/customer-journey-mapper/SKILL.md)
- [Opportunity Solution Tree Builder](skills/discovery/opportunity-solution-tree-builder/SKILL.md)
- [Problem Validation Planner](skills/discovery/problem-validation-planner/SKILL.md)
- [Assumption Mapper](skills/discovery/assumption-mapper/SKILL.md)
- [Survey Designer](skills/discovery/survey-designer/SKILL.md)
- [Research Insight Prioritizer](skills/discovery/research-insight-prioritizer/SKILL.md)

### Product Strategy & Market Intelligence

- [Market Research Planner](skills/strategy/market-research-planner/SKILL.md)
- [TAM/SAM/SOM Estimator](skills/strategy/tam-sam-som-estimator/SKILL.md)
- [Competitor Feature Matrix](skills/strategy/competitor-feature-matrix/SKILL.md)
- [Competitive Positioning Analyzer](skills/strategy/competitive-positioning-analyzer/SKILL.md)
- [ICP And Segmentation Builder](skills/strategy/icp-and-segmentation-builder/SKILL.md)
- [Value Proposition Designer](skills/strategy/value-proposition-designer/SKILL.md)
- [Business Model Canvas Builder](skills/strategy/business-model-canvas-builder/SKILL.md)
- [Product Vision Builder](skills/strategy/product-vision-builder/SKILL.md)
- [Strategic Options Analyzer](skills/strategy/strategic-options-analyzer/SKILL.md)
- [Strategy Assumption Reviewer](skills/strategy/strategy-assumption-reviewer/SKILL.md)
- [Product Portfolio Prioritizer](skills/strategy/product-portfolio-prioritizer/SKILL.md)
- [Build Buy Partner Analyzer](skills/strategy/build-buy-partner-analyzer/SKILL.md)

### Prioritization, Roadmaps & Execution

- [Feature Prioritizer](skills/execution/feature-prioritizer/SKILL.md)
- [RICE Prioritization](skills/execution/rice-prioritization/SKILL.md)
- [Roadmap Builder](skills/execution/roadmap-builder/SKILL.md)
- [Roadmap Challenge Reviewer](skills/execution/roadmap-challenge-reviewer/SKILL.md)
- [OKRs and KRs Builder](skills/execution/okrs-and-krs-builder/SKILL.md)
- [Dependency Mapper](skills/execution/dependency-mapper/SKILL.md)
- [Delivery Risk Analyzer](skills/execution/delivery-risk-analyzer/SKILL.md)
- [Sprint Planning Assistant](skills/execution/sprint-planning-assistant/SKILL.md)
- [Backlog Health Reviewer](skills/execution/backlog-health-reviewer/SKILL.md)
- [Stakeholder Update Writer](skills/execution/stakeholder-update-writer/SKILL.md)
- [Decision Memo Writer](skills/execution/decision-memo-writer/SKILL.md)
- [Meeting Decision Extractor](skills/execution/meeting-decision-extractor/SKILL.md)
- [Release Notes Writer](skills/execution/release-notes-writer/SKILL.md)
- [Post Launch Reviewer](skills/execution/post-launch-reviewer/SKILL.md)

### Product Analytics, Experimentation & Growth

- [North Star Metric Builder](skills/analytics/north-star-metric-builder/SKILL.md)
- [Metric Tree Builder](skills/analytics/metric-tree-builder/SKILL.md)
- [Event Taxonomy Designer](skills/analytics/event-taxonomy-designer/SKILL.md)
- [Analytics Instrumentation Planner](skills/analytics/analytics-instrumentation-planner/SKILL.md)
- [Funnel Diagnostic](skills/analytics/funnel-diagnostic/SKILL.md)
- [Cohort Retention Analyzer](skills/analytics/cohort-retention-analyzer/SKILL.md)
- [Churn Diagnostic](skills/analytics/churn-diagnostic/SKILL.md)
- [Activation Analysis](skills/analytics/activation-analysis/SKILL.md)
- [SQL For Product Analytics](skills/analytics/sql-for-product-analytics/SKILL.md)
- [Dashboard Requirements Writer](skills/analytics/dashboard-requirements-writer/SKILL.md)
- [Experiment Design Reviewer](skills/analytics/experiment-design-reviewer/SKILL.md)
- [A/B Test Results Interpreter](skills/analytics/ab-test-results-interpreter/SKILL.md)
- [Growth Opportunity Diagnostic](skills/analytics/growth-opportunity-diagnostic/SKILL.md)
- [Product Metric Anomaly Investigator](skills/analytics/product-metric-anomaly-investigator/SKILL.md)

### UX, Design & Product Quality

- [Usability Test Planner](skills/design/usability-test-planner/SKILL.md)
- [Usability Findings Synthesizer](skills/design/usability-findings-synthesizer/SKILL.md)
- [Heuristic UX Auditor](skills/design/heuristic-ux-auditor/SKILL.md)
- [Accessibility Reviewer](skills/design/accessibility-reviewer/SKILL.md)
- [Onboarding Flow Reviewer](skills/design/onboarding-flow-reviewer/SKILL.md)
- [Information Architecture Reviewer](skills/design/information-architecture-reviewer/SKILL.md)
- [Empty Error Loading State Reviewer](skills/design/empty-error-loading-state-reviewer/SKILL.md)
- [Mobile Experience Reviewer](skills/design/mobile-experience-reviewer/SKILL.md)
- [Design System Consistency Reviewer](skills/design/design-system-consistency-reviewer/SKILL.md)
- [Product Copy Reviewer](skills/design/product-copy-reviewer/SKILL.md)
- [Feature Acceptance Reviewer](skills/design/feature-acceptance-reviewer/SKILL.md)
- [Pre Release Product Auditor](skills/design/pre-release-product-auditor/SKILL.md)

### AI Product Management

- [AI Opportunity Assessor](skills/ai-product/ai-opportunity-assessor/SKILL.md)
- [AI Vs Rules Vs Human Decision Maker](skills/ai-product/ai-vs-rules-vs-human-decision-maker/SKILL.md)
- [AI Product Requirements Writer](skills/ai-product/ai-product-requirements-writer/SKILL.md)
- [LLM Use Case Risk Assessor](skills/ai-product/llm-use-case-risk-assessor/SKILL.md)
- [AI Product Feasibility Reviewer](skills/ai-product/ai-product-feasibility-reviewer/SKILL.md)
- [LLM Evaluation Planner](skills/ai-product/llm-evaluation-planner/SKILL.md)
- [Golden Dataset Builder](skills/ai-product/golden-dataset-builder/SKILL.md)
- [LLM Evaluation Rubric Builder](skills/ai-product/llm-evaluation-rubric-builder/SKILL.md)
- [Prompt Regression Test Planner](skills/ai-product/prompt-regression-test-planner/SKILL.md)
- [Hallucination Risk Reviewer](skills/ai-product/hallucination-risk-reviewer/SKILL.md)
- [RAG Retrieval Quality Reviewer](skills/ai-product/rag-retrieval-quality-reviewer/SKILL.md)
- [AI Quality Error Taxonomy Builder](skills/ai-product/ai-quality-error-taxonomy-builder/SKILL.md)
- [Model Selection Tradeoff Analyzer](skills/ai-product/model-selection-tradeoff-analyzer/SKILL.md)
- [RAG Product Spec Builder](skills/ai-product/rag-product-spec-builder/SKILL.md)
- [Agent Workflow Designer](skills/ai-product/agent-workflow-designer/SKILL.md)
- [Tool Calling Requirements Designer](skills/ai-product/tool-calling-requirements-designer/SKILL.md)
- [AI Human Handoff Designer](skills/ai-product/ai-human-handoff-designer/SKILL.md)
- [AI Latency Cost Optimizer](skills/ai-product/ai-latency-cost-optimizer/SKILL.md)
- [AI Observability Planner](skills/ai-product/ai-observability-planner/SKILL.md)
- [AI Incident Reviewer](skills/ai-product/ai-incident-reviewer/SKILL.md)
- [Responsible AI Reviewer](skills/ai-product/responsible-ai-reviewer/SKILL.md)
- [AI Feature Launch Reviewer](skills/ai-product/ai-feature-launch-reviewer/SKILL.md)

### AI Product Builder & Technical PM

- [Idea To Prototype Planner](skills/product-builder/idea-to-prototype-planner/SKILL.md)
- [Prototype Requirements Writer](skills/product-builder/prototype-requirements-writer/SKILL.md)
- [AI App Builder Prompt Generator](skills/product-builder/ai-app-builder-prompt-generator/SKILL.md)
- [Technical Feasibility Reviewer](skills/product-builder/technical-feasibility-reviewer/SKILL.md)
- [API Integration Planner](skills/product-builder/api-integration-planner/SKILL.md)
- [Database Schema Reviewer](skills/product-builder/database-schema-reviewer/SKILL.md)
- [Frontend UX Code Reviewer](skills/product-builder/frontend-ux-code-reviewer/SKILL.md)
- [Backend Architecture Reviewer](skills/product-builder/backend-architecture-reviewer/SKILL.md)
- [Security And Privacy Reviewer](skills/product-builder/security-and-privacy-reviewer/SKILL.md)
- [Code Change Impact Analyzer](skills/product-builder/code-change-impact-analyzer/SKILL.md)
- [Automated Test Planner](skills/product-builder/automated-test-planner/SKILL.md)
- [Deployment Readiness Reviewer](skills/product-builder/deployment-readiness-reviewer/SKILL.md)
- [Prototype Usability Test Planner](skills/product-builder/prototype-usability-test-planner/SKILL.md)
- [Prototype To Production Gap Analyzer](skills/product-builder/prototype-to-production-gap-analyzer/SKILL.md)

### Product Leadership & Communication

- [Executive Product Brief Writer](skills/leadership/executive-product-brief-writer/SKILL.md)
- [Stakeholder Alignment Planner](skills/leadership/stakeholder-alignment-planner/SKILL.md)
- [Product Decision Challenger](skills/leadership/product-decision-challenger/SKILL.md)
- [Tradeoff Analysis Builder](skills/leadership/tradeoff-analysis-builder/SKILL.md)
- [Conflict Resolution Preparation](skills/leadership/conflict-resolution-preparation/SKILL.md)
- [Cross Functional Dependency Reviewer](skills/leadership/cross-functional-dependency-reviewer/SKILL.md)
- [Product Team Retrospective](skills/leadership/product-team-retrospective/SKILL.md)
- [Product Review Facilitator](skills/leadership/product-review-facilitator/SKILL.md)
- [Product Org Maturity Assessor](skills/leadership/product-org-maturity-assessor/SKILL.md)
- [Product Leadership Coaching Guide](skills/leadership/product-leadership-coaching-guide/SKILL.md)

### PM Career & Learning

- [PM Skill Gap Assessor](skills/career/pm-skill-gap-assessor/SKILL.md)
- [PM Learning Roadmap Builder](skills/career/pm-learning-roadmap-builder/SKILL.md)
- [Product Case Interview Coach](skills/career/product-case-interview-coach/SKILL.md)
- [Product Sense Interview Practice](skills/career/product-sense-interview-practice/SKILL.md)
- [Metrics Interview Coach](skills/career/metrics-interview-coach/SKILL.md)
- [Product Strategy Interview Coach](skills/career/product-strategy-interview-coach/SKILL.md)
- [Resume Impact Bullet Reviewer](skills/career/resume-impact-bullet-reviewer/SKILL.md)
- [PM Portfolio Project Planner](skills/career/pm-portfolio-project-planner/SKILL.md)
- [Portfolio Case Study Reviewer](skills/career/portfolio-case-study-reviewer/SKILL.md)
- [PM Achievement Quantifier](skills/career/pm-achievement-quantifier/SKILL.md)
- [Mock Interview Evaluator](skills/career/mock-interview-evaluator/SKILL.md)
- [PM Career Transition Planner](skills/career/pm-career-transition-planner/SKILL.md)
