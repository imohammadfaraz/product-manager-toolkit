"""Read-only GitHub REST and GraphQL client using the Python standard library."""
from __future__ import annotations
import json, os, urllib.error, urllib.parse, urllib.request
from typing import Any, Callable

class GitHubAPIError(RuntimeError):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status

class GitHubClient:
    """Read-only API client. No mutation methods are exposed."""
    def __init__(self, token: str | None = None, api_url: str = "https://api.github.com", opener: Callable = urllib.request.urlopen):
        self.token = token if token is not None else os.getenv("GITHUB_TOKEN", "")
        if not self.token:
            raise ValueError("Set GITHUB_TOKEN to a read-only GitHub credential.")
        self.api_url, self.opener = api_url.rstrip("/"), opener

    def _request(self, url: str, payload: dict[str, Any] | None = None) -> tuple[Any, dict[str, str]]:
        headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {self.token}", "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "product-manager-toolkit-github-work-tracker"}
        data = None
        if payload is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(payload).encode()
        request = urllib.request.Request(url, data=data, headers=headers, method="POST" if payload is not None else "GET")
        try:
            with self.opener(request, timeout=20) as response:
                raw = response.read().decode("utf-8")
                result = json.loads(raw) if raw else {}
                response_headers = {k.lower(): v for k, v in response.headers.items()}
        except urllib.error.HTTPError as exc:
            try: detail = exc.read().decode("utf-8")[:500]
            except Exception: detail = "No response body."
            raise GitHubAPIError(f"GitHub API returned HTTP {exc.code}: {detail}", exc.code) from None
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise GitHubAPIError(f"GitHub API request failed: {type(exc).__name__}") from None
        except json.JSONDecodeError:
            raise GitHubAPIError("GitHub API returned invalid JSON.") from None
        if isinstance(result, dict) and result.get("errors"):
            messages = "; ".join(str(e.get("message", "GraphQL error")) for e in result["errors"])
            raise GitHubAPIError(f"GitHub GraphQL error: {messages}")
        return result, response_headers

    @staticmethod
    def _next_link(header: str) -> str | None:
        for part in header.split(","):
            pieces = part.strip().split(";")
            if len(pieces) > 1 and 'rel="next"' in pieces[1]:
                return pieces[0].strip().strip("<>")
        return None

    def list_issues_updated_since(self, repository: str, since: str) -> list[dict[str, Any]]:
        owner, name = repository.split("/", 1)
        query = urllib.parse.urlencode({"state": "all", "since": since, "per_page": 100, "sort": "updated", "direction": "desc"})
        url = f"{self.api_url}/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(name)}/issues?{query}"
        items = []
        while url:
            page, headers = self._request(url)
            if not isinstance(page, list): raise GitHubAPIError("Unexpected response while listing issues.")
            items.extend(item for item in page if "pull_request" not in item)
            url = self._next_link(headers.get("link", ""))
        return items

    def get_user_project(self, owner_login: str, project_number: int) -> dict[str, Any]:
        project_query = """query UserProject($login: String!) { user(login: $login) { projectsV2(first: 100) { nodes { id number title url shortDescription } } } }"""
        data, _ = self._request(f"{self.api_url}/graphql", {"query": project_query, "variables": {"login": owner_login}})
        user = (data.get("data") or {}).get("user")
        if user is None: raise GitHubAPIError(f"GitHub user '{owner_login}' was not found or is not accessible.")
        projects = (user.get("projectsV2") or {}).get("nodes") or []
        project = next((p for p in projects if p.get("number") == project_number), None)
        if project is None: raise GitHubAPIError(f"Project #{project_number} was not found among the first 100 boards visible to {owner_login}.")
        item_query = """query ProjectItems($id: ID!, $after: String) { node(id: $id) { ... on ProjectV2 { items(first: 100, after: $after) { pageInfo { hasNextPage endCursor } nodes { id content { __typename ... on Issue { number title state url updatedAt repository { nameWithOwner } } ... on PullRequest { number title state url updatedAt repository { nameWithOwner } } } fieldValues(first: 50) { nodes { ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name } } } ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon { name } } } ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } } ... on ProjectV2ItemFieldNumberValue { number field { ... on ProjectV2FieldCommon { name } } } } } } } } } }"""
        items, after = [], None
        while True:
            result, _ = self._request(f"{self.api_url}/graphql", {"query": item_query, "variables": {"id": project["id"], "after": after}})
            node = (result.get("data") or {}).get("node")
            if node is None: raise GitHubAPIError("Project could not be read. Confirm Projects v2 permissions for this user-owned board.")
            connection = node.get("items") or {}
            items.extend(connection.get("nodes") or [])
            info = connection.get("pageInfo") or {}
            if not info.get("hasNextPage"): break
            after = info.get("endCursor")
            if not after: raise GitHubAPIError("Paginated project response did not include a cursor.")
        return {**project, "items": items}
