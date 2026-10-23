from github_work_tracker.client import GitHubAPIError, GitHubClient
from github_work_tracker.report import build_weekly_summary

class Response:
    headers = {}
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def read(self): return b"not-json"

def test_malformed_json_fails_closed():
    client = GitHubClient(token="test-token", opener=lambda *a, **k: Response())
    try: client._request("https://api.github.com/repos/acme/app/issues")
    except GitHubAPIError as exc: assert "invalid JSON" in str(exc)
    else: raise AssertionError("Expected invalid JSON to fail")

def test_report_has_no_credential_parameter_or_echo():
    report = build_weekly_summary("acme/app", "2026-10-15T00:00:00Z", [])
    assert "Bearer " not in report
