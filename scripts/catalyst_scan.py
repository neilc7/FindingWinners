#!/usr/bin/env python3
"""Create a dated catalyst-scan brief from the watchlist and research skill."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
WATCHLIST_PATH = ROOT / "data" / "watchlist.json"
SKILL_PATH = ROOT / "skill.md"
REPORT_DIR = ROOT / "reports" / "catalyst-scans"


def load_watchlist() -> list[dict[str, object]]:
    with WATCHLIST_PATH.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload["companies"]


def select_companies(companies: list[dict[str, object]], tickers: list[str]) -> list[dict[str, object]]:
    if not tickers:
        return companies

    wanted = {ticker.upper() for ticker in tickers}
    selected = [company for company in companies if str(company["ticker"]).upper() in wanted]
    missing = sorted(wanted - {str(company["ticker"]).upper() for company in selected})
    if missing:
        raise SystemExit(f"Unknown ticker(s): {', '.join(missing)}")
    return selected


def company_block(company: dict[str, object]) -> str:
    notes = company.get("notes") or []
    note_lines = "\n".join(f"  - {note}" for note in notes) if notes else "  - None yet"

    return dedent(
        f"""
        ## {company["ticker"]} - {company["company"]}

        - Theme: {company["theme"]}
        - Group: {company["group"]}
        - Status: {company["status"]}
        - Conviction: {company["conviction"]}
        - Existing notes:
        {note_lines}

        ### Recent Information Scan

        - Earnings / guidance:
        - Investor presentations / conference commentary:
        - Analyst changes:
        - Industry, customer, partnership, or product news:
        - Social / Reddit sentiment:

        ### Change Detection

        - Material change:
        - Score: TBD
        - Evidence:

        ### Variant Perception

        - Consensus belief:
        - Management belief:
        - Contradicting evidence:
        - Underappreciated positive/negative:

        ### Catalysts

        - 1 month:
        - 3 months:
        - 6 months:
        - 12 months:

        ### Scoring

        - Information Change: TBD / 5
        - Business Quality: TBD / 5
        - Valuation Support: TBD / 5
        - Catalyst Strength: TBD / 5
        - Sentiment Opportunity: TBD / 5
        - Total: TBD / 25

        ### Decision

        - Ranking:
        - Next action:
        - Follow-up date:
        """
    ).strip()


def render_report(companies: list[dict[str, object]], lookback_days: int, report_date: dt.date) -> str:
    skill = SKILL_PATH.read_text(encoding="utf-8").strip()
    company_sections = "\n\n".join(company_block(company) for company in companies)

    return "\n\n".join(
        [
            f"# Catalyst Scan - {report_date.isoformat()}",
            "Purpose: find early business catalysts before a stock has already moved a lot.",
            "\n".join(
                [
                    "Lookback windows:",
                    f"- Last {lookback_days} days",
                    "- Last 90 days",
                    "- Since the last earnings report",
                ]
            ),
            "## Research Skill",
            skill,
            "## Watchlist Scan",
            company_sections,
        ]
    ) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a catalyst scan brief from the watchlist.")
    parser.add_argument("tickers", nargs="*", help="Optional tickers to scan. Defaults to the full watchlist.")
    parser.add_argument("--lookback-days", type=int, default=30, help="Primary recent-information lookback window.")
    parser.add_argument("--date", default=dt.date.today().isoformat(), help="Report date in YYYY-MM-DD format.")
    parser.add_argument("--stdout", action="store_true", help="Print the report instead of writing it to reports/.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report_date = dt.date.fromisoformat(args.date)
    companies = select_companies(load_watchlist(), args.tickers)
    report = render_report(companies, args.lookback_days, report_date)

    if args.stdout:
        print(report, end="")
        return

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ticker_slug = "all" if not args.tickers else "-".join(ticker.upper() for ticker in args.tickers)
    output_path = REPORT_DIR / f"{report_date.isoformat()}-{ticker_slug}.md"
    output_path.write_text(report, encoding="utf-8")
    print(output_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
