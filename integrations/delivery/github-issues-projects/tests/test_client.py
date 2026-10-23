import json
from email.message import Message
from github_work_tracker.client import GitHubAPIError, GitHubClient

class FakeResponse:
    def __init__(self, body, headers=None):
        self.body = json.dumps(body).encode()
        self.headers = Message()
        for key, value in (headers or {}).items(): self.headers[key] = value
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def read(self): return self.body

def test_client_requires_token():
    try: GitHubClient(token="")
    except ValueError as exc: assert "GITHUB_TOKEN" in str(exc)
    else: raise AssertionError("Expected missing token to fail closed")

def test_issues_pagination_and_pull_requests_excluded():
    calls = []
    def opener(request, timeout=20):
        calls.append(request.full_url)
        if len(calls) == 1:
            return FakeResponse([{"number": 1, "title": "Issue"}, {"number": 2, "title": "PR", "pull_request": {"url": "x"}}], {"Link": '<https://api.github.com/repos/acme/app/issues?page=2>; rel="next"'})
        return FakeResponse([{"number": 3, "title": "Next page"}])
    issues = GitHubClient(token="test-token", opener=opener).list_issues_updated_since("acme/app", "2026-10-15T00:00:00Z")
    assert [item["number"] for item in issues] == [1, 3]
    assert len(calls) == 2

def test_graphql_errors_are_not_silently_ignored():
    client = GitHubClient(token="test-token", opener=lambda *a, **k: FakeResponse({"errors": [{"message": "Resource not accessible by personal access token"}]}))
    try: client._request("https://api.github.com/graphql", {"query": "query { viewer { login } }"})
    except GitHubAPIError as exc: assert "Resource not accessible" in str(exc)
    else: raise AssertionError("Expected GraphQL permission error")
