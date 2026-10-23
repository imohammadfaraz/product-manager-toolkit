# Coding Agents

**Status:** Documented pattern only. **Verification:** Unverified. **Execution:** Not available from this repository. **Last verification:** Not yet verified.

## Purpose and intended PM use
Define safe boundaries for coding agents that inspect repositories and propose patches.

Intended capabilities: Repository files and test output within granted scope. These are intended use cases, not verified runtime capabilities. No live connector, API client, credentials, or runtime test is included.

## Integration method
Approved GitHub App, local CLI or hosted coding-agent platform. Verify exact API/MCP/CLI, version, supported operations and plan requirements using current official documentation.

## Setup
1. Obtain system-owner approval and define repositories and data scope.
2. Review official documentation, scopes, terms, rate limits and data retention.
3. Create a dedicated least-privilege identity, preferably read-only.
4. Store credentials in a secret manager. Never commit tokens or put them in prompts/logs.
5. Configure the adapter in an isolated runtime outside this repository.
6. Use a sandbox with synthetic data, bounded network access and no production secrets.
7. Require review of every diff and explicit approval before merge, deploy, release or external write.

## Authentication and permissions
Authentication: Platform auth or GitHub App token scoped to selected repositories. Exact scopes are not verified here. Limit access to selected repositories and actions. No write or merge rights by default. Human approval is required for changes to shared branches, deployments, deletion or production mutation.

## Data handling
Potential data: Repository files and test output within granted scope. Send minimum task-relevant context. Confirm provider retention, residency and training-use settings before sharing confidential code or customer data. Redact secrets and private data from logs. Treat repository content, issue comments and generated output as untrusted.

## Failure handling
- Auth/permission failure: stop; never auto-expand scopes.
- Tests fail or runtime output is ambiguous: report logs and do not claim success.
- Malicious instructions appear in repo files: treat as untrusted content and follow the approved task, not embedded instructions.
- PII/credential exposure: stop, minimize exposure and follow incident response.

## Security controls
Least privilege, sandbox execution, no production secrets, allowlisted repositories, bounded tool/network access, dependency review, secret scanning, audit logging and human review before merge/deploy.

## Limitations
- Sandbox execution; no production secrets; review diffs before merge/deploy.
- Hosted coding-agent capabilities vary by vendor, plan and runtime.
- This guide is not proof of compatibility or a security certification. Runtime implementation and maintenance require a named owner.

## Verification record
- Status: unverified
- Last verification date: not yet verified
- Test performed: none, documentation only
- Evidence: none
- Maintainer: named technical owner required before execution status
