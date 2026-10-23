# Product Lifecycle and AI Skill Track Map

This map explains how the expanded Skills fit together and where adjacent capabilities have intentionally different jobs. All new Skills are published as active, portable Skills with `review_status: standardized`. This means the canonical structure and guardrails are present; it does not imply that every Skill has completed editorial review or runtime evaluation.

## Discovery and research boundaries

- **Customer Interview Planner** creates the research plan, participant profile, logistics, and debrief approach. **Interview Question Builder** drafts neutral prompts and probes. **Interview Synthesis** analyzes completed research. **Customer Feedback Analyzer** works across feedback sources, not only interviews.
- **Jobs-to-be-Done Analyzer** frames functional, emotional, and social progress sought by a user. **Persona Builder** summarizes evidence-backed user patterns for communication and design, not invented demographic archetypes.
- **Customer Journey Mapper** maps stages, touchpoints, goals, pain points, and backstage dependencies. **Opportunity Solution Tree Builder** connects an outcome to opportunities, solution ideas, and experiments.
- **Problem Definition Expert** frames the problem; **Problem Validation Planner** plans evidence collection to test whether it is important and real. **Assumption Mapper** inventories beliefs and ranks them by uncertainty and impact.
- **Survey Designer** supports structured quantitative or mixed-method input. It does not replace interviews when the question requires deep context. **Research Insight Prioritizer** ranks already-derived insights by evidence, importance, and actionability.

## Strategy boundaries

- **Competitive Analysis Expert** owns broad evidence-led competitive comparison. **Competitor Feature Matrix** creates a consistent feature-level comparison table. **Competitive Positioning Analyzer** interprets relative value and category framing. These are complementary artifacts, not interchangeable reports.
- **Product Strategy Builder** makes broader product choices. **Product Vision Builder** articulates the desired future and direction. **Strategic Options Analyzer** compares strategic choices. **Strategy Assumption Reviewer** challenges the logic and evidence behind an existing strategy.
- **Market Research Planner** defines the research approach. **TAM/SAM/SOM Estimator** sizes a market with transparent methods and assumptions. **ICP and Segmentation Builder** defines priority customer groups. **Value Proposition Designer** articulates segment-specific value.
- **Business Model Canvas Builder** describes business model components. **Build/Buy/Partner Analyzer** evaluates sourcing alternatives. **Product Portfolio Prioritizer** allocates attention across products or bets rather than ranking individual backlog tickets.

## Execution and analytics boundaries

- **Feature Prioritizer** supports multi-criteria ranking. **RICE Prioritization** applies the specific RICE model and must expose uncertain inputs. **Roadmap Builder** sequences outcome themes; **Roadmap Challenge Reviewer** challenges coherence and commitments.
- **OKRs and KRs Builder** turns outcomes into measurable objectives. **Dependency Mapper** shows relationships and blockers. **Delivery Risk Analyzer** assesses execution risk. **Sprint Planning Assistant** helps shape a bounded sprint based on capacity and readiness.
- **Stakeholder Update Writer**, **Decision Memo Writer**, **Meeting Decision Extractor**, and **Release Notes Writer** have different output contracts: status communication, a decision document, a traceable decision/action log, and user-facing change communication.
- **North Star Metric Builder** selects a primary value indicator. **Metric Tree Builder** decomposes outcomes into drivers. **Event Taxonomy Designer** defines naming and event governance; **Analytics Instrumentation Planner** translates measurement needs into implementable tracking.
- **Funnel Diagnostic**, **Cohort Retention Analyzer**, **Churn Diagnostic**, and **Activation Analysis** diagnose different stages or behaviors. **SQL for Product Analytics** helps draft and validate query logic, but does not claim execution. **Experiment Design Reviewer** reviews a proposed protocol; **A/B Testing Expert** designs an experiment from the ground up; **A/B Test Results Interpreter** interprets supplied results.

## UX and quality boundaries

- **UX Reviewer** provides broad experience review. **Heuristic UX Auditor**, **Accessibility Reviewer**, **Mobile Experience Reviewer**, and **Information Architecture Reviewer** apply narrower lenses.
- **Usability Test Planner** supports general product research. **Prototype Usability Test Planner** specializes in testing early prototypes and validating risky interaction assumptions before implementation. **Usability Findings Synthesizer** analyzes completed sessions.
- **Onboarding Flow Reviewer**, **Empty/Error/Loading State Reviewer**, **Design System Consistency Reviewer**, and **Product Copy Reviewer** focus on specific quality surfaces.
- **Feature Acceptance Reviewer** checks whether feature behavior and acceptance evidence are adequate. **Pre-release Product Auditor** checks cross-functional readiness across experience, analytics, operations, support, risks, and launch gates. **Risk & Edge Case Analyzer** remains the broader risk register capability.

## AI product boundaries

Every AI product Skill should explicitly consider quality, latency, cost, privacy, security, failure handling, and human fallback where relevant. It should distinguish deterministic policy from probabilistic model behavior and should not claim model evaluation or production performance without evidence.

- **AI Opportunity Assessor** asks whether AI is useful for the problem. **AI vs Rules vs Human Decision-Maker** compares implementation approaches. **AI Product Feasibility Reviewer** focuses on AI-specific feasibility; **Technical Feasibility Reviewer** covers general technical feasibility.
- **AI Product Requirements Writer** specifies AI behavior and user-visible requirements. **LLM Use Case Risk Assessor** evaluates use-case risk. **LLM Evaluation Planner**, **Golden Dataset Builder**, and **LLM Evaluation Rubric Builder** respectively define evaluation design, representative examples, and scoring criteria.
- **Prompt Regression Test Planner** detects unintended behavior changes across prompt revisions. **Hallucination Risk Reviewer** focuses on unsupported claims. **RAG Retrieval Quality Reviewer** examines retrieval relevance and grounding; **RAG Product Spec Builder** defines the broader retrieval-augmented product behavior.
- **AI Quality Error Taxonomy Builder** standardizes failure classes. **Model Selection Trade-off Analyzer** compares candidate models. **Agent Workflow Designer** maps multi-step agent behavior; **Tool Calling Requirements Designer** specifies safe tool contracts and permission boundaries.
- **AI Human Handoff Designer** defines escalation and recovery. **AI Latency Cost Optimizer** balances response time and unit economics. **AI Observability Planner** defines signals; **AI Incident Reviewer** analyzes a concrete incident; **Responsible AI Reviewer** focuses on fairness, transparency, user impact, and oversight; **AI Feature Launch Reviewer** assesses readiness before rollout.

## Prototype and technical PM boundaries

- **Idea-to-Prototype Planner** scopes a prototype. **Prototype Requirements Writer** specifies its behavior. **AI App Builder Prompt Generator** turns those requirements into instructions for a chosen builder. Keep vendor-specific syntax in adapters, not in portable Skills.
- **API Integration Planner**, **Database Schema Reviewer**, **Frontend UX Code Reviewer**, **Backend Architecture Reviewer**, and **Code Change Impact Analyzer** examine distinct technical surfaces.
- **Security and Privacy Reviewer** covers application and data protection generally. **Responsible AI Reviewer** focuses on AI-specific impact and oversight.
- **Automated Test Planner** defines test coverage. **Deployment Readiness Reviewer** checks release mechanics. **Prototype-to-Production Gap Analyzer** identifies the work needed to move from demo to a maintained production system.

## Leadership and career boundaries

Leadership Skills support briefs, alignment, decision challenge, trade-off analysis, conflict preparation, dependency review, retrospectives, product reviews, organizational maturity, and coaching. Career Skills support skills assessment, learning plans, interview practice, resume evidence, portfolio planning, achievement quantification, mock interview feedback, and career transitions. Career outputs must never fabricate achievements or credentials.

## Publication and evaluation status

The 122 added Skills are in the main catalog and marked active. Their status is `standardized`, not `content-reviewed`. The structural validator checks required metadata, sections, paths, and catalog consistency. Before promoting a new Skill to `content-reviewed`, add at least two realistic evaluation cases, execute them in the intended runtime, review failures, and record the evaluation evidence.
