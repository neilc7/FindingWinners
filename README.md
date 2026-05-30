# Finding Winners

A research framework for finding companies where fundamentals are improving faster than investor expectations — especially those benefiting from the AI narrative before the market catches on.

## How It Works

This repo is designed to be used with an AI agent (Cursor, Claude, etc.) that has web search capability. There are no scripts to run. You point the AI at this repo and tell it to do the research.

### Key Files

| File | Purpose |
|---|---|
| `goal.md` | Investment thesis, what we're looking for, case studies |
| `skill.md` | The research process — step-by-step instructions for the AI agent |
| `watchlist.md` | Companies to scan, grouped by theme |
| `reports/catalyst-scans/` | Output — dated research reports |

## Running a Scan

Open this repo in Cursor (or any AI tool with web search) and say:

**Full watchlist scan:**
> Follow `skill.md` to run a catalyst scan on the full watchlist.

**Specific tickers:**
> Follow `skill.md` to run a catalyst scan on DELL, ALAB, and DOCN.

**Quick check on one name:**
> Follow `skill.md` to do a deep dive on ALAB. Focus on the last 7 days.

The agent will read the instructions, search the web for each company, and write a report to `reports/catalyst-scans/`.

## Research Cadence

| Frequency | What |
|---|---|
| Weekly | Full watchlist scan for early catalysts and narrative shifts |
| Mid-week | Targeted scan for high-priority names around earnings or events |
| Monthly | Watchlist cleanup — promote, archive, or add names |

## Adding Companies

Edit `watchlist.md` directly. Add the ticker under the appropriate theme group with company name, theme, status, and any notes.
