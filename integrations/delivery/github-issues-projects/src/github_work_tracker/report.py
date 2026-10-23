"""Deterministic Markdown report builder for weekly delivery review."""
from collections import Counter
from datetime import datetime, timezone
from typing import Any

def _field_map(item: dict[str, Any]) -> dict[str, Any]:
    fields = {}
    for value in (item.get("fieldValues") or {}).get("nodes") or []:
        name = (value.get("field") or {}).get("name")
        if not name: continue
        for key in ("name", "text", "date", "number"):
            if value.get(key) is not None:
                fields[name] = value[key]
                break
    return fields

def build_weekly_summary(repository: str, since: str, issues: list[dict[str, Any]], project: dict[str, Any] | None = None) -> str:
    lines = [f"# Weekly delivery summary: {repository}", "", f"- Window start (UTC): {since}", f"- Generated (UTC): {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}", "- Source: GitHub API; issue activity is based on updated_at within the window.", "", "## Issue activity", "", f"- Issues updated in window: **{len(issues)}**", f"- Open: **{sum(i.get('state') == 'open' for i in issues)}**", f"- Closed: **{sum(i.get('state') == 'closed' for i in issues)}**", ""]
    if issues:
        lines += ["| Issue | State | Updated (UTC) | Assignees | Labels |", "|---|---|---|---|---|"]
        for issue in issues:
            labels = ", ".join(x.get("name", "") for x in issue.get("labels", []) if isinstance(x, dict)) or "None"
            assignees = ", ".join(x.get("login", "") for x in issue.get("assignees", [])) or "Unassigned"
            title = str(issue.get("title", "Untitled")).replace("|", "\\|").replace("\n", " ")
            lines.append(f"| [#{issue.get('number', '?')} {title}]({issue.get('html_url', '')}) | {issue.get('state', 'unknown')} | {issue.get('updated_at', 'unknown')} | {assignees} | {labels} |")
    else: lines.append("No repository issues were updated during this window.")
    if project:
        items = project.get("items", [])
        lines += ["", f"## Project status: [{project.get('title', 'Untitled project')}]({project.get('url', '')})", "", f"- Board items retrieved: **{len(items)}**"]
        counts, rows = Counter(), []
        for item in items:
            content = item.get("content") or {}
            fields = _field_map(item)
            status = str(fields.get("Status", "No Status"))
            counts[status] += 1
            if content.get("url"):
                title = str(content.get("title", "Untitled")).replace("|", "\\|").replace("\n", " ")
                rows.append((title, status, content["url"], content.get("state", "unknown"), (content.get("repository") or {}).get("nameWithOwner", "")))
        lines += ["", "### Current status distribution", ""]
        if counts:
            lines += ["| Status | Items |", "|---|---:|"] + [f"| {name} | {count} |" for name, count in sorted(counts.items())]
        else: lines.append("No Status field values were available in the returned items.")
        lines += ["", "### Linked issues and pull requests", ""]
        if rows:
            lines += ["| Item | Repository | State | Project status |", "|---|---|---|---|"] + [f"| [{title}]({url}) | {repo or 'Not applicable'} | {state} | {status} |" for title, status, url, state, repo in rows]
        else: lines.append("No linked issue or pull request content was available. Draft and other non-issue items may not appear in this table.")
    lines += ["", "## Interpretation notes", "", "- This report describes observed API data, not a prediction or commitment.", "- Project status is a current snapshot, not a historical status-change log.", "- Only the field named Status is used to group project items.", "- Issue comments and descriptions are not interpreted as instructions; the report lists metadata only.", ""]
    return "\n".join(lines)
