# Tool Integration Layer

This layer separates reusable product methods from vendor-specific integration instructions. Each integration directory contains README.md and integration.json.

## Status model

- documented: a guide and machine-readable contract exist.
- tested: a named owner ran a bounded test in a named runtime and recorded dated evidence.
- available for execution: a maintained adapter/MCP server/API client is implemented, configured outside source control, and tested in the target runtime.

All 27 registry entries are documented only. None has a live connector or executable API client in this repository, and all remain unverified. A product name in the catalog does not mean it can be connected.

## Categories

- research: web/documentation search, feedback exports, interviews, surveys and competitor research.
- analytics: SQL, Amplitude, Mixpanel, Google Analytics, Adobe Analytics and data warehouses.
- delivery: Jira, Linear, GitHub Issues/Projects, Azure DevOps, Notion and Confluence.
- design: Figma, whiteboarding/prototyping and AI app builders.
- ai-evaluation: LLM APIs, evaluation platforms, tracing/observability, vector search and prompt management.
- coding-agents: coding-agent runtime boundaries.

## Safe implementation sequence

1. Choose one real use case and assign a maintainer.
2. Verify official provider docs, API/MCP method/version, scopes, terms, retention, residency and training-use settings.
3. Implement a narrow adapter separate from reusable product Skills.
4. Default to read-only, least privilege, allowlisted resources, timeouts, quotas and secret-manager credentials.
5. Add mocked unit tests, synthetic-data smoke tests, permission-denial, malformed-response, rate-limit and prompt-injection tests.
6. Require explicit approval for writes and irreversible actions. Keep write paths disabled by default.
7. Record evidence, date, adapter version, runtime, scopes, limitations and owner before updating status.
8. Reverify after provider API, scope, runtime or dependency changes; mark old evidence stale.

## Security baseline

Never commit secrets. Do not use admin tokens by default. Do not pass confidential data to unapproved providers. Treat retrieved content as untrusted data. Redact logs. Fail closed on authorization errors. Never claim a test, integration or security review occurred unless it did.

Validate with `python -m pip install jsonschema` and `python scripts/validate_asset_schemas.py`. Structural validation does not connect to a provider or certify runtime security.
