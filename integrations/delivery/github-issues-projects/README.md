# GitHub Issues and Projects: Weekly Delivery Summary

**Implementation status:** Adapter code and mocked tests added; live verification is pending. **Maintainer:** [@imohammadfaraz](https://github.com/imohammadfaraz). **Access mode:** Read-only. **Last live verification:** Not yet performed.

## First outcome

Generate a Markdown weekly delivery summary using repository issues updated in a seven-day window and a current snapshot of a personal GitHub Projects v2 board. The report includes issue links, state, updated timestamp, labels, assignees, linked board items and a count of the board's Status field.

Issue activity is based on updated_at, not a historical event log. Project status is a current snapshot, not proof of when a status changed. The report does not infer delivery progress from comments or issue text.

## Implemented scope

- Python 3.10+ adapter using the standard library, with REST for repository issues and GraphQL for user-owned Projects v2.
- REST pagination for issue listing and GraphQL pagination for project items.
- Pull requests excluded from repository issue activity; linked pull requests in the board remain visible.
- Source URLs in report output, bounded HTTP timeout, fail-closed API errors, and no mutation methods.
- Mocked unit tests for report output, source links, pagination, pull-request filtering, missing credentials and API failures.

## Authentication for a personal Projects v2 board

A public repository does not make a personal Projects v2 board public or grant access to it. GitHub Projects permissions differ from repository issue permissions, and personal Projects v2 access may require a classic personal access token with the project scope. Confirm current GitHub documentation and account policy before creating a token. If a private repository is added later, the credential also needs minimum repository read access for that repository.

1. Create a dedicated credential with read-only access to the target repository's Issues and the personal Projects v2 board. Do not use an admin token.
2. Provide it through the GITHUB_TOKEN environment variable or an approved secret manager that injects that variable at runtime.
3. Never commit the token, put it in an issue, or include it in logs or report output.
4. Start with a public, non-sensitive test repository and board. Review provider retention and organizational policies before sending private content to any AI model.

## Install and run

    python -m venv .venv
    python -m pip install -e ./integrations/delivery/github-issues-projects
    export GITHUB_TOKEN="<read-only-token>"
    github-weekly-summary --repo OWNER/REPO --output weekly-delivery-summary.md

To include the personal Projects v2 board, pass the GitHub login that owns the board and the project number from its URL:

    github-weekly-summary --repo OWNER/REPO --project-owner YOUR_LOGIN --project-number 1 --output weekly-delivery-summary.md

The number above is an example only. Use the actual number from your board URL. On Windows PowerShell, set the environment variable with $env:GITHUB_TOKEN = "<read-only-token>".

Optional: set the exact start of the window with --since 2026-10-15T00:00:00Z. Default window is seven days before runtime, UTC. The report writes locally to the path passed with --output.

## Tests

    python -m pip install pytest
    PYTHONPATH=integrations/delivery/github-issues-projects/src pytest integrations/delivery/github-issues-projects/tests -q

Tests use mocked API responses. They do not authenticate with GitHub and do not count as a live smoke test. The mocked suite passed in GitHub Actions on Python 3.12: https://github.com/imohammadfaraz/product-manager-toolkit/actions/runs/40032483810. The repository asset schema validation also passed after the contract enum fix: https://github.com/imohammadfaraz/product-manager-toolkit/actions/runs/40032483822.

## Live smoke-test checklist

- [ ] Use a dedicated read-only credential and an explicitly approved public test repository.
- [ ] Retrieve issues from the chosen repository and compare the report with GitHub UI/API results.
- [ ] Retrieve a personal Projects v2 board and compare item counts and Status values with the board UI.
- [ ] Confirm missing project access fails closed without automatic scope expansion.
- [ ] Confirm report source URLs are present and no token or unnecessary private payload is emitted.
- [ ] Record date, runtime, Python version, adapter commit, credential type and scopes, test target, result and evidence URL. Never record the token.

## Verification evidence

- **Status:** Implemented, not live-verified
- **Mocked tests:** Passed in GitHub Actions on Python 3.12 on 2026-10-23 UTC
- **Live smoke test date:** None
- **Runtime and Python version:** Not recorded
- **Target repository / board:** Not recorded
- **Evidence URL:** None
- **Maintainer:** @imohammadfaraz

Do not change registry status to tested or execution_available=true until a real live smoke test has passed and evidence is recorded.

## Limitations

- User-owned board discovery currently checks the first 100 Projects v2 boards visible to the user; item pagination is handled.
- The report uses current board fields. It does not reconstruct status changes over time or include comments, issue bodies or release metadata.
- Up to 50 field values per project item are requested; projects with more field values may need field-value pagination.
- Authorization failures stop the run. The client has no write endpoints and does not broaden permissions automatically.
- Structural and mocked tests do not prove provider compatibility, live access or security certification.
