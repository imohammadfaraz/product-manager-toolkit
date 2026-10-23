from github_work_tracker.client import GitHubAPIError

def test_permission_denial_is_an_error_not_an_empty_success():
    error = GitHubAPIError("GitHub API returned HTTP 403: Resource not accessible by integration", 403)
    assert error.status == 403
    assert "Resource not accessible" in str(error)
