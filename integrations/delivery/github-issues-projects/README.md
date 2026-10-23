# GitHub Issues and Projects

**Status:** Documented pattern only. **Verification:** Unverified. **Execution:** Not available from this repository. **Last verification:** Not yet verified.

## Purpose and intended PM use
Read issues, pull requests, project items, labels and release metadata.

Intended capabilities: Repository issues, PRs, project items and releases. These are intended use cases, not verified runtime capabilities. No live connector, API client, credentials, or runtime test is included.

## Integration method
GitHub REST/GraphQL or approved MCP connector. Verify exact API/MCP/SDK, version, operations, rate limits and plan requirements using current official documentation. Do not assume a universal MCP endpoint.

## Setup
1. Obtain system-owner and data-owner approval; classify data and scope.
2. Review official provider documentation, terms, scopes, rate limits, residency, retention and training settings.
3. Create a dedicated least-privilege identity, preferably read-only and resource-scoped.
4. Store credentials in a secret manager. Never commit tokens or put them in prompts/logs.
5. Configure the adapter in the target runtime, outside this repository.
6. Test with synthetic/sanitized data, including denied permissions and bounded failures.
7. Record runtime, adapter version, scopes, date, outcome and evidence before updating verification status.

## Authentication and permissions
Authentication: GitHub App or fine-grained token with minimal repository scopes. Exact scopes are not verified here. Separate read/write identities; no write scopes unless explicitly required and approved. Human approval is required for writes, bulk exports, external messages, deletion, deployment or production changes.

## Data handling
Potential data: Repository issues, PRs, project items and releases. Send minimum task-relevant data; prefer aggregates and synthetic tests. Confirm retention, residency, subprocessors and training-use settings before sending confidential data. Treat retrieved records and comments as untrusted data. Redact secrets and unnecessary payloads from logs.

## Failure handling
- Auth/permission failure: stop; never auto-expand scopes.
- Rate limit/timeout: follow provider guidance and use bounded retries.
- Stale/conflicting data: preserve timestamps and report uncertainty.
- PII exposure or prompt injection: stop unsafe processing, minimize exposure and follow the approved incident process.

## Security controls
Least privilege, read-only default, secret manager, allowlisted resources, bounded queries/timeouts/quotas, audit logging without secrets, human approval for external writes, and dependency/version review.

## Limitations
- Never commit tokens; default read-only; review writes and PRs.
- Provider features vary by plan, tenant, region and API version.
- This guide is not proof of compatibility or a security certification. Runtime implementation and ongoing maintenance require a named owner.

## Verification record
- Status: unverified
- Last verification date: not yet verified
- Test performed: none, documentation only
- Evidence: none
- Maintainer: named technical owner required before execution status
