"""Command-line entry point for a read-only weekly delivery summary."""
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from .client import GitHubClient
from .report import build_weekly_summary

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a read-only weekly GitHub Issues and Projects summary.")
    parser.add_argument("--repo", required=True, help="Repository in owner/name form.")
    parser.add_argument("--project-owner", help="Personal GitHub login that owns the Projects v2 board.")
    parser.add_argument("--project-number", type=int, help="Number shown in the personal Projects v2 board URL.")
    parser.add_argument("--since", help="Window start in ISO-8601 format; defaults to seven days ago (UTC).")
    parser.add_argument("--output", default="weekly-delivery-summary.md", help="Markdown output path.")
    args = parser.parse_args()
    if bool(args.project_owner) != bool(args.project_number): parser.error("--project-owner and --project-number must be supplied together.")
    since = args.since or (datetime.now(timezone.utc) - timedelta(days=7)).replace(microsecond=0).isoformat()
    client = GitHubClient()
    issues = client.list_issues_updated_since(args.repo, since)
    project = client.get_user_project(args.project_owner, args.project_number) if args.project_owner else None
    Path(args.output).write_text(build_weekly_summary(args.repo, since, issues, project), encoding="utf-8")
    print(f"Wrote {args.output}. Issues: {len(issues)}. Project board: {'included' if project else 'not requested'}.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
