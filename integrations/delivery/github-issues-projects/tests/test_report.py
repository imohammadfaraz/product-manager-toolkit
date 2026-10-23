from github_work_tracker.report import build_weekly_summary

def test_summary_includes_source_link_and_counts():
    issues = [{"number": 12, "title": "Fix login", "html_url": "https://github.com/acme/app/issues/12", "state": "closed", "updated_at": "2026-10-22T10:00:00Z", "assignees": [{"login": "dev"}], "labels": [{"name": "bug"}]}]
    report = build_weekly_summary("acme/app", "2026-10-15T00:00:00Z", issues)
    assert "Issues updated in window: **1**" in report
    assert "[#12 Fix login](https://github.com/acme/app/issues/12)" in report
    assert "| closed |" in report

def test_project_status_is_current_snapshot_and_groups_fields():
    project = {"title": "Delivery", "url": "https://github.com/users/acme/projects/1", "items": [{"content": {"title": "Ship feature", "url": "https://github.com/acme/app/issues/3", "state": "open", "repository": {"nameWithOwner": "acme/app"}}, "fieldValues": {"nodes": [{"name": "In progress", "field": {"name": "Status"}}]}}]}
    report = build_weekly_summary("acme/app", "2026-10-15T00:00:00Z", [], project)
    assert "Current status distribution" in report
    assert "| In progress | 1 |" in report
    assert "current snapshot, not a historical status-change log" in report
    assert "https://github.com/acme/app/issues/3" in report

def test_empty_issue_window_is_explicit():
    assert "No repository issues were updated during this window." in build_weekly_summary("acme/app", "2026-10-15T00:00:00Z", [])
