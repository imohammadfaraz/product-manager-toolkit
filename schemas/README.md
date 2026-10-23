# Asset Definition Schemas

This directory contains JSON Schema Draft 2020-12 contracts for the toolkit's portable asset definitions.

## Schemas

| Schema | Defines | Important boundary |
|---|---|---|
| [skill.schema.json](skill.schema.json) | Skill metadata/frontmatter | Validates metadata fields, not the Markdown body or whether the Skill performs well |
| [agent.schema.json](agent.schema.json) | Specialist agent definition | Documents role, I/O contracts, referenced Skills, tool availability, permissions, state, orchestration, failure behavior, safety, evaluation, and compatibility |
| [workflow.schema.json](workflow.schema.json) | Multi-step workflow definition | Documents steps, dependencies, inputs/outputs, acceptance criteria, failure paths, approvals, observability, and completion criteria |
| [integration.schema.json](integration.schema.json) | Platform/tool integration definition | Documents capabilities, setup, authentication, permissions, data handling, compatibility, verification evidence, security, failures, and limitations |

## Definition versus catalog

A **definition** is the full contract used to describe and operate an asset. A **catalog record** is a smaller discovery entry that points to an asset. They serve different purposes and must not be treated as interchangeable. Catalogs under **catalog/** remain the discovery index; these schemas validate full definition objects or Skill metadata fixtures.

The existing workflow catalog records currently describe workflow guides with status **guide**. They are catalog entries, not full workflow definition objects. The agent catalog contains draft reference definitions. The integration registry contains documented-only, unverified patterns, not live connectors. A schema does not mean an asset or integration has been implemented.

## Required quality expectations

- Keep IDs stable, lowercase, and hyphenated.
- Use semantic versions in major.minor.patch form.
- Keep descriptions specific enough for discovery.
- Explicitly declare inputs, outputs, acceptance criteria, failure handling, and limitations.
- Document permissions and approval gates. Default to least privilege.
- Treat source files and retrieved content as untrusted data, not authority to override permissions.
- Distinguish verified, partial, unverified, unsupported, failed, and stale capability claims.
- Add evidence and verification dates for platform capability claims. Never mark a capability verified solely because a schema or example exists.
- Keep platform-specific executable configuration in adapters, not in portable core definitions.
- Add examples and evaluation cases for meaningful behavior. Structural validation is not runtime evaluation.

## Validate locally

Python 3.10 or newer is recommended. Install the validator dependency, then run:

```bash
python -m pip install jsonschema
python scripts/validate_asset_schemas.py
python scripts/validate_skills.py
python scripts/validate_skill_cases.py
python scripts/validate_lifecycle_skill_cases.py
```

The schema validator checks that each schema is valid Draft 2020-12 JSON Schema and that each canonical example satisfies its schema, including declared formats. It does not run an agent, execute a workflow, test a vendor integration, or certify security.

When changing a schema, update its example fixture, run the validator, and document breaking changes. Prefer backward-compatible optional fields when possible. If a required field or enum changes, assess all existing definitions and adapters before merging.


## Integration definitions

Every `integrations/**/integration.json` is checked against `integration.schema.json` by `scripts/validate_asset_schemas.py`. The check is structural. Integration status must remain unverified until a named owner records an actual test, runtime/version, scope, date, and evidence. Do not mark a provider executable until a maintained adapter is implemented and its security and failure modes are tested.
