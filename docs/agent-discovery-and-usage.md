# Universal Agent, Skill, and Workflow Discovery & Usage Guide

This guide explains how to discover, select, invoke, combine, evaluate, and maintain Product Manager Toolkit assets across different AI assistants, agent runtimes, and manual workflows.

It is deliberately platform-neutral. A repository asset does not automatically become an executable tool in every product. The host application must support the relevant format or you must provide the instructions manually. Treat every integration capability as unverified until checked in the target environment.

## 1. Purpose and scope

Use this guide when you need to answer any of these questions:

- Which Skill or workflow is appropriate for a product task?
- How do I find the canonical file and understand its inputs and output contract?
- How do I use an asset in an AI assistant that supports files, instructions, or custom agents?
- How do I combine multiple Skills without losing context or duplicating work?
- When do I need a specialist agent, a critic, a workflow guide, or a human decision?
- How do I check quality, handle failures, and keep assets current?

The repository publishes portable Skills, documented workflows, and twelve draft specialist-agent contracts. These are reference definitions, not deployed runtimes; tools are not configured and behavioral security has not been certified.

## 2. Understand the asset types

Choose the smallest asset that can reliably do the job. These types are related but not interchangeable.

| Asset | What it is | Use it when | What it does not imply |
|---|---|---|---|
| Skill | Focused task capability with instructions and an output contract | You need one distinct deliverable or review | Automatic execution, tool access, or persistent memory |
| Agent | Specialist role or runtime configuration that may use tools or coordinate capabilities | A task benefits from a defined role, controlled tools, repeated decisions, or orchestration | That a matching agent is currently published or that the runtime supports it |
| Workflow | Ordered steps, inputs, decisions, and handoffs | A task requires multiple outputs or checks in a deliberate sequence | Automatic execution; a Markdown workflow may be a manual playbook |
| Toolkit | Curated capabilities for a broader job to be done | You need a coherent collection for a product activity | A single executable agent |
| Prompt or command | Reusable instruction or named entry point | You need a repeatable way to start work in a compatible environment | Portability to every host |
| Template | Reusable artifact structure | You need consistency in PRDs, plans, decision records, or similar deliverables | That the fields are already supported by evidence |
| Integration | Platform-specific adapter or tool connection | You need vendor-specific setup or capabilities | Support until the guide and environment are verified |
| Evaluation | Test cases, expected behaviors, prohibited patterns, and scoring rules | You need to check behavior and prevent regressions | That a model has passed unless execution and scoring are recorded |

### Keep these distinctions clear

- A Skill describes how to perform a focused task.
- An agent describes a role and, where supported, its operating environment, permissions, and orchestration behavior.
- A workflow describes how work moves between steps. It may be followed by a human or orchestrated by a compatible runtime.
- An integration provides platform-specific details. Keep those details out of portable core Skills where possible.
- An evaluation fixture is a test input and rubric, not evidence of a passing test by itself.

## 3. Find the right asset

### 3.1 Start from the user outcome

Describe the desired result as a verb plus a deliverable, rather than starting with a tool name.

Examples:

- “Synthesize these customer interviews into evidence-backed themes.”
- “Compare three roadmap options and explain trade-offs.”
- “Review whether this AI feature is ready for launch.”
- “Turn approved requirements into testable acceptance criteria.”
- “Diagnose where users abandon onboarding.”

Clarify the output you need, the source material available, the audience, and the decision the output should support.

### 3.2 Search in this order

1. **Start with the [README and Skill catalog](../README.md).** Use the README’s capability tracks to narrow the area.
2. **Search the machine-readable catalog** at [catalog/skills.yaml](../catalog/skills.yaml) for an asset ID, category, tags, and path.
3. **Open the canonical Skill file** at the path listed in the catalog. Read the full file, not just the title.
4. **Check the overlap map** in [docs/skill-track-map.md](skill-track-map.md) when two Skills look similar.
5. **Check workflow guides** in [workflows/](../workflows/) when the task spans multiple deliverables.
6. **Check toolkits** in [toolkits/](../toolkits/) for curated sequences.
7. **Check the agent catalog** at [catalog/agents.yaml](../catalog/agents.yaml) if you are looking for an agent. Read the full operating guide and machine-readable contract. Draft definitions do not imply runtime deployment or configured tools.
8. **Check integrations** in [integrations/](../integrations/) only when platform-specific instructions actually exist. Verify current tool support in the target product before relying on it.

For local repository search, common options include searching file names or text in your editor, using GitHub's repository search, or running commands such as:

```bash
# List canonical Skill files
find skills -name SKILL.md -print

# Search Skills by topic or phrase
grep -RniE "interview synthesis|customer feedback|opportunity tree" skills

# List documented workflows
find workflows -name WORKFLOW.md -print
```

These are optional local-development commands. The repository can also be explored through the GitHub web interface without installing anything.

### 3.3 Read before invoking

Before selecting a Skill, inspect:

- **Purpose:** the job it is designed to perform.
- **When to use:** appropriate and inappropriate situations.
- **Inputs:** required source material, context, constraints, and optional inputs.
- **Process:** the method and expected order of operations.
- **Expected outputs:** the artifact or decision support it should produce.
- **Quality checklist:** criteria for a usable result.
- **Guardrails:** prohibited assumptions, safety constraints, privacy considerations, and evidence rules.
- **Definition of done:** how completion is established.
- **Metadata:** current status, version, portability, review status, and tags.

Do not select solely by title similarity. Compare expected input and output contracts. If two assets appear to overlap, identify their different jobs or choose one and state the boundary.

## 4. Select Skill, agent, workflow, or human review

Use this decision process:

1. **One well-bounded task and one output?** Start with a Skill.
2. **Several dependent tasks with explicit handoffs?** Use a workflow and select the Skills for each step.
3. **A compatible runtime must repeatedly choose steps, call approved tools, maintain task state, or coordinate subtasks?** Consider an agent only if a documented definition and runtime support exist.
4. **A second opinion or adversarial review would materially reduce risk?** Use a critic Skill or reviewer asset if one exists, with a separate review rubric. Do not claim an unavailable critic agent exists.
5. **The task requires authorization, high-impact judgment, sensitive-data access, or irreversible actions?** Keep a human decision or approval gate.
6. **No suitable asset exists?** Use the closest relevant method only if it is safe and fit for purpose; declare the gap and assumptions, and propose a new Skill only after checking for overlap.

Prefer the minimum number of assets that achieves the result. More Skills or agents can add latency, cost, conflicting advice, and coordination overhead without improving the decision.

## 5. Invoke a Skill in any compatible AI assistant

There is no single invocation syntax supported by every AI product. Use the approach that the host product supports.

### Option A: The host supports Skills or reusable instruction files

1. Follow the host product's current instructions for importing or enabling a Skill.
2. Point it to the canonical `SKILL.md` file or install it using the host's supported mechanism.
3. Confirm the Skill is enabled in the current workspace/session and that the host can read its full instructions.
4. Provide the task, source files, relevant constraints, audience, and output format.
5. Ask the assistant to follow the Skill's process and report unresolved gaps rather than silently filling them.
6. Review the result against the Skill's quality checklist and definition of done.

Do not assume a host will discover or load repository files automatically. Verify this in the target environment.

### Option B: The host supports file attachments but not Skills

1. Open the relevant `SKILL.md`.
2. Attach or paste the full contents into the session, where permitted.
3. State explicitly that it is the task procedure to follow.
4. Provide source material separately and identify which source is authoritative.
5. Request the output contract stated in the Skill.
6. Manually check the result against the file's quality checklist and guardrails.

If the Skill is too long for the host's context limit, do not truncate critical guardrails without saying so. Use a supported file or context mechanism, or split the work into smaller tasks while preserving the necessary rules.

### Option C: The host supports neither reusable Skills nor attachments

Copy only the relevant, permitted instruction text into the prompt, along with the essential source material. Include the task purpose, required inputs, process, output format, and critical guardrails. Label this as a manual adaptation, not a native installation, and acknowledge any omitted context.

### Universal task brief

Adapt this template for any host:

```text
Task:
[What must be accomplished and why]

Selected asset:
[Exact Skill ID and canonical path, or workflow name]

Source material:
[Attached files, URLs, data, and system of record]

Context:
[Product, users, lifecycle stage, audience, and decision to support]

Constraints:
[Scope, time period, geography, budget, privacy, policy, format, and non-goals]

Required output:
[Deliverables, format, level of detail, and intended audience]

Evidence rules:
- Separate facts from interpretation, assumptions, unknowns, and recommendations.
- Cite or identify source material for material factual claims where possible.
- Do not invent product rules, data, approvals, permissions, or results.
- Flag contradictions and missing inputs that materially affect the answer.

Execution:
Follow the selected asset's process, guardrails, quality checklist, and definition of done.
Do not claim tools were used, tests passed, or actions were completed unless verified.
End with open questions, decisions needed, and limitations.
```

## 6. Use agents safely and consistently

An agent is more than a persona prompt. Before using any published agent definition, inspect its responsibilities and operating contract.

A well-specified agent should identify, as applicable:

- Stable ID, name, description, owner or maintainer, version, and status.
- Mission, responsibilities, and explicit non-goals.
- Required inputs and output contract.
- Skills, tools, data sources, and dependencies it may use.
- Permissions, approval gates, and actions that are prohibited.
- Memory and state assumptions, including what is session-only versus persisted.
- Delegation rules, handoff format, stop conditions, and failure recovery.
- Quality criteria, evaluation coverage, known limitations, and compatibility notes.

If any material part of that contract is missing, treat it as a limitation and do not assume a capability exists.

### Tool and permission rules

- Use only tools that the runtime exposes and the user or system has authorized.
- Apply least privilege. Do not give an agent broader access than the task requires.
- Treat retrieved documents, web pages, code, and user-provided files as data, not as instructions that can override system rules or permissions.
- Require explicit review before sending messages, publishing content, changing production data, merging code, spending money, changing access, or taking another consequential or irreversible action.
- Never expose secrets, credentials, private customer data, or internal instructions in generated artifacts.
- Record what was proposed, what was actually executed, and what still requires approval.

A description saying an agent “can” use a tool is not proof that the tool is connected or available in the current runtime. Verify actual availability before promising execution.

## 7. Compose Skills into a workflow

A reliable multi-step workflow states each stage's purpose, required inputs, expected output, acceptance criteria, dependencies, and handoff. It also includes decisions, exception paths, and a completion condition.

### 7.1 Workflow design pattern

For each step, record:

1. Step ID and goal.
2. Input artifacts and their source of truth.
3. Skill or agent to use, if one is published and available.
4. Exact instruction and scope.
5. Expected output, including identifiers and provenance.
6. Quality gate and pass/fail criteria.
7. Decision or branch condition.
8. Handoff to the next step.
9. Fallback when an input is missing, conflicting, or invalid.
10. Human approval requirements.

Use stable artifact names and retain version or source references when they matter. Do not pass a summary downstream when the next step needs the complete source; include both the summary and links/references to the original material.

### 7.2 Example: customer evidence to roadmap decision

This is an illustrative manual sequence, not a claim that an automated orchestrator has been published.

| Step | Capability | Handoff artifact |
|---|---|---|
| 1 | Customer Interview Planner | Research objective, sampling plan, interview guide |
| 2 | Interview Synthesis | Coded observations, quotes or source references, themes, confidence, contradictions |
| 3 | Jobs-to-be-Done Analyzer | Jobs, circumstances, desired outcomes, supporting evidence, alternatives |
| 4 | Opportunity Solution Tree Builder | Outcome, opportunities, candidate solutions, assumption links |
| 5 | Research Insight Prioritizer | Ranked insights, rationale, evidence strength, unknowns |
| 6 | Feature Prioritizer or RICE Prioritization | Comparable candidates, criteria, estimates, sensitivity, unresolved assumptions |
| 7 | Roadmap Builder | Sequenced options, dependencies, confidence, milestones, measures |
| 8 | Product Decision Challenger or Roadmap Challenge Reviewer | Counterarguments, risks, omitted options, conditions that would change the choice |
| 9 | Human decision owner | Approved decision, rationale, rejected alternatives, accountable owner |

At each handoff, preserve the distinction between what customers actually said, how the team interpreted it, and what the team proposes to do. Customer quotes are not proof that a solution will work. Prioritization scores are decision aids, not objective truth. Roadmap recommendations should expose uncertainty and dependencies.

### 7.3 Example: AI feature readiness review

A possible review sequence is:

1. Define user problem and success criteria.
2. Assess whether AI is appropriate compared with deterministic rules or a human process.
3. Write AI-specific requirements and risk assumptions.
4. Plan the evaluation dataset, rubric, and regression tests.
5. Review retrieval, tool-calling, privacy, security, latency, cost, observability, and human fallback as applicable.
6. Define launch monitoring, incident response, rollback or disablement, and user communication.
7. Run a challenge review and obtain accountable human approval.

Select the actual Skills from the catalog for each stage. Do not infer that the sequence runs automatically, or that the model has passed an evaluation, just because the plan exists.

### 7.4 Avoid over-orchestration

- Combine two Skills only when their outputs or perspectives are materially different.
- Do not ask multiple agents to produce the same deliverable unless you are intentionally comparing independent drafts.
- Resolve conflicting outputs against source evidence and explicit decision criteria, not by averaging opinions.
- Do not use an agent to validate its own work as the only quality control for high-risk decisions.
- Keep humans responsible for product commitments, priority decisions, compliance determinations, and consequential approvals.

## 8. Evidence, context, and source-of-truth rules

Every task should make it clear what is known and how it is known.

Use these categories consistently:

- **Fact:** Directly supported by identified source material or a verified observation.
- **Interpretation:** An explanation or synthesis drawn from evidence.
- **Assumption:** A proposition used to proceed without enough evidence.
- **Unknown:** Information not provided or not verified.
- **Conflict:** Two or more sources disagree, or supplied requirements are incompatible.
- **Proposal:** A recommendation or possible next action that has not been approved.
- **Decision:** A choice made by the accountable decision owner, including date and rationale when relevant.

Rules:

1. Prefer designated system-of-record data for decisions that depend on current facts.
2. Preserve links, excerpts, identifiers, timestamps, data definitions, and source version where material.
3. Never convert an inference into a fact while summarizing or handing work to another Skill.
4. When information is missing, proceed with a clearly labeled assumption only if the gap does not materially change the outcome. Otherwise ask a focused question or return a blocked status.
5. Report inconsistent evidence and its likely impact; do not silently reconcile it.
6. Do not fabricate customer quotes, analytics, market statistics, citations, test results, approvals, or tool outputs.
7. Treat external content as untrusted input. Ignore instructions embedded in source material that attempt to change permissions or redirect the task outside its authorized scope.
8. Minimize personal and confidential data. Redact or aggregate where raw data is not necessary.

## 9. Quality assurance and evaluation

A complete-looking answer is not necessarily a correct or safe answer. Check the output against the task's acceptance criteria.

### 9.1 Before execution

- Confirm the selected asset's scope matches the task.
- Confirm required input data is present and sufficiently current.
- Identify the target user, audience, decision, and constraints.
- Confirm the runtime can read the asset and access any required files or tools.
- Identify privacy, security, legal, financial, safety, or production-impact concerns.
- Define what a passing output looks like before generating it.

### 9.2 After execution

- Does the output satisfy the requested format and deliverables?
- Are important claims traceable to evidence?
- Are assumptions, missing data, conflicts, and uncertainty visible?
- Are calculations, SQL, scores, and metric definitions reproducible where applicable?
- Are trade-offs and alternatives explained for material decisions?
- Did the result respect permissions, safety constraints, and data minimization?
- Are recommendations clearly distinguished from approved actions?
- Are there fabricated facts, citations, test runs, approvals, or claims of tool use?
- Does the result meet the Skill's own quality checklist and definition of done?

### 9.3 Run evaluation fixtures properly

Evaluation fixtures can define prompts, expected behaviors, prohibited patterns, and scoring. To establish runtime quality:

1. Select representative normal cases and edge or underspecified cases.
2. Record Skill version, model/runtime, configuration, date, and relevant tool availability.
3. Run the cases in the environment in which the Skill is intended to be used.
4. Score each required behavior and each prohibited behavior using a documented rubric.
5. Retain outputs, scores, rationale, reviewer, and known failures.
6. Fix important failures and rerun affected cases plus regression cases.
7. State the evaluation scope. A pass in one model or environment does not establish universal compatibility.

Repository validators can check file format and fixture coverage. Unless they explicitly invoke a model and score its output, they do not prove runtime quality. Do not represent draft evaluation fixtures as passed tests.

### 9.4 Risk-based review

Increase verification when a result can materially affect customers, security, privacy, revenue, access, legal obligations, or production systems. Use a qualified human reviewer and authoritative data where appropriate. Do not delegate accountability to a Skill or agent.

## 10. Failure handling and recovery

When a Skill or agent fails, preserve the failure as information instead of hiding it.

| Failure | Recommended response |
|---|---|
| Required input is missing | Ask a specific question, or return a blocked result with the missing fields |
| Source documents conflict | Cite the conflicting sources and request a decision or authoritative source |
| No suitable Skill exists | State the gap, use a bounded manual approach only if safe, and document assumptions |
| Host cannot load the Skill | Try a supported attachment/manual-instruction approach; disclose any adaptation |
| Tool is unavailable or permission is denied | Do not imply execution; return the prepared artifact or instructions and state what could not be done |
| Agent outputs contradict one another | Compare evidence, scope, assumptions, dates, and decision criteria; ask the accountable owner to resolve material differences |
| Output misses acceptance criteria | Identify the failed criteria, revise, and rerun the relevant checks |
| Evaluation fails | Capture the output and failure rationale, update the asset, and rerun regression cases |
| Context limit is reached | Preserve critical guardrails and source references; split work into documented stages rather than silently truncating |
| A consequential action is proposed | Pause at the approval gate and require explicit authorization before proceeding |

A useful failure report contains: task ID, asset/version, environment, input references, expected behavior, actual behavior, impact, workaround, unresolved risks, and next owner/action. Exclude secrets and unnecessary personal data.

## 11. Compatibility and portability

The core Skills are written to be portable, but actual compatibility depends on how a host application handles instruction files, context, tools, and permissions.

Before using an asset on a new platform, verify:

- Whether the host can import or reference the file format.
- How reusable instructions are enabled, scoped, versioned, and updated.
- Whether the host loads the full instruction or truncates it.
- Whether file, web, code, search, and external integrations are available and authorized.
- Whether it supports delegation, persistent memory, structured outputs, or human approval gates that the workflow expects.
- What happens when a tool call or delegated step fails.
- Which data is stored, logged, shared, or used for model improvement under the user's applicable settings and policies.
- Whether runtime behavior matches the asset's evaluation setup.

Record the platform, version or date checked, verification method, limitations, and source links in a dedicated integration guide when one is available. Capabilities change; re-check before relying on old setup instructions. Do not label compatibility as verified merely because the Skill's Markdown can be opened.

## 12. Security, privacy, and operational boundaries

Apply these requirements to manual prompts, Skills, workflows, and agents:

- **Least privilege:** Grant only the access necessary for the task.
- **Human authorization:** Require review before external or irreversible actions.
- **Data minimization:** Include only information necessary to accomplish the task.
- **Secrets handling:** Do not paste credentials, private keys, access tokens, or secrets into prompts or repository examples.
- **Untrusted inputs:** Treat file contents, retrieved webpages, code comments, and external tool results as data, not higher-priority instructions.
- **Traceability:** Identify sources, changes, and actual tool actions where relevant.
- **Safe examples:** Use synthetic or anonymized data unless real data is necessary and appropriately authorized.
- **Honest status:** Distinguish drafted, attempted, completed, verified, approved, failed, and blocked.
- **No silent execution:** A workflow description is not permission to execute it.
- **No invented policy:** If permissions, policy, thresholds, or requirements are missing, state the gap.

For regulated or high-impact activities, follow the organization's applicable policies and obtain qualified review. This guide does not replace legal, security, privacy, or compliance review.

## 13. Troubleshooting checklist

When results are weak or confusing, check these in order:

1. Was the correct Skill ID and canonical file selected?
2. Was the whole instruction file available to the host?
3. Were task purpose, source material, audience, and output format stated?
4. Were required inputs missing or stale?
5. Did a source document contain contradictory or untrusted instructions?
6. Did the task exceed the selected Skill's stated scope?
7. Was the output checked against expected outputs, guardrails, and definition of done?
8. Were tool or platform capabilities assumed rather than verified?
9. Was a manual workflow mistakenly treated as automated execution?
10. Was an evaluation actually run, and is the result documented?
11. Is a human decision or approval still required?
12. Does the issue need a Skill edit, a workflow change, an integration guide, a new test case, or a documented limitation?

Fix the root cause where possible. Avoid adding broad instructions to a Skill to compensate for a problem that belongs in a platform adapter or a separate workflow.

## 14. Keep discovery metadata and documentation current

When adding or changing an asset:

1. Search for overlapping existing assets and document distinct scope boundaries.
2. Follow the relevant asset authoring standard and schema.
3. Give the asset a stable, unique ID, human-readable name, clear description, category, version, status, portability, and honest review state.
4. State its inputs, process, output contract, guardrails, dependencies, and definition of done.
5. Update the relevant catalog and documentation links.
6. Add a worked example for important use cases and evaluation fixtures for expected and prohibited behavior.
7. Run the repository validators and fix structural or link failures.
8. Execute relevant evaluation cases in intended runtimes before claiming runtime quality.
9. Record material compatibility assumptions, known limitations, source links, and review date.
10. Check licensing and attribution for third-party material.
11. Review affected workflows and neighboring Skills for terminology, handoff, or scope changes.
12. Include migration notes if the change breaks identifiers, outputs, or established usage.

Review tool links, external sources, platform claims, and examples periodically. There is no monitoring guarantee unless an explicit scheduled process or automation is implemented and verified.

## 15. Quick-reference operating procedure

For day-to-day use, follow this sequence:

1. **Define:** Write the outcome and decision to support.
2. **Discover:** Search README/catalog; open the canonical Skill or workflow.
3. **Select:** Match purpose, inputs, outputs, and risk to the task.
4. **Prepare:** Gather source material, context, constraints, permissions, and success criteria.
5. **Invoke:** Use the host's documented mechanism, an attachment, or a clearly labeled manual adaptation.
6. **Execute:** Follow the asset's process without skipping critical guardrails.
7. **Handoff:** Preserve evidence, source identifiers, assumptions, conflicts, and open questions.
8. **Review:** Check output quality and request an independent challenge when justified.
9. **Approve:** Obtain human decisions and authorization for consequential actions.
10. **Verify:** Run relevant tests or evaluation cases and record actual results.
11. **Report:** State what was completed, what was verified, limitations, and remaining actions.
12. **Improve:** Feed repeatable failures into Skills, workflows, tests, or integration documentation.

## 16. Related repository references

- [README and catalog overview](../README.md)
- [Skill catalog](../catalog/skills.yaml)
- [Agent catalog](../catalog/agents.yaml)
- [Workflow catalog](../catalog/workflows.yaml)
- [Skill authoring standard](skill-standard.md)
- [Skill coverage and duplication audit](skill-audit.md)
- [Skill track map and overlap boundaries](skill-track-map.md)
- [Asset type definitions](asset-types.md)
- [Asset definition schemas and validation](../schemas/README.md)
- [Contribution guide](../CONTRIBUTING.md)
- [Evaluation fixtures and instructions](../evals/README.md)
- [Workflow guides](../workflows/)

## 17. Definition of done

A discovery and usage process is complete only when:

- The asset was found in a canonical catalog or path and its current file was inspected.
- The asset type and scope match the requested job.
- Inputs, constraints, source of truth, and output requirements were established.
- Runtime loading and any required tools were verified or limitations were disclosed.
- Execution followed the defined process and guardrails.
- Outputs were checked against the acceptance criteria and quality checklist.
- Important evidence, assumptions, unknowns, conflicts, and recommendations remain distinguishable.
- Required human decisions and approvals were obtained, or clearly remain open.
- Claims about tools, execution, testing, compatibility, and approval are supported by what actually happened.
- Follow-up fixes, evaluation results, or content gaps are recorded when needed.

**Completion does not mean that every task is fully automated.** It means the user can discover the right asset, understand how to apply it in the actual environment, evaluate the result, and see the boundaries of what has and has not been done.


## Specialist agents and security boundary

The [agent catalog](../catalog/agents.yaml) lists twelve draft specialist-agent definitions. Each has a machine-readable contract and operating guide under [agents/](../agents/). See the [agent overview](../agents/README.md) for the roster and shared guardrails.

All definitions default to read-only, session-only, no configured tools, and recommend-and-draft-only behavior. Never infer that an agent can execute a Skill or action because it references that Skill. Before runtime deployment, verify allowlisted tools, permission scopes, secrets handling, logging, data retention, and approval enforcement. Run normal, missing-evidence, conflicting-evidence, boundary, and prompt-injection evaluations. Schema validation is not a security certification.
