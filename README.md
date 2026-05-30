# Finding Winners

A lightweight research framework for finding companies where fundamentals may be improving faster than investor expectations.

The process is built around a few small, composable files:

- `watchlist.md`: human-readable watchlist organized by theme.
- `data/watchlist.json`: machine-readable watchlist used by scripts and automations.
- `skill.md`: the repeatable research rubric for catalyst detection.
- `scripts/catalyst_scan.py`: creates a dated scan brief from the watchlist and skill.

## Quick Start

Create a full-watchlist catalyst scan:

```bash
python3 scripts/catalyst_scan.py
```

Create a scan for specific tickers:

```bash
python3 scripts/catalyst_scan.py NVDA CRWD
```

Print the scan to stdout instead of writing a report:

```bash
python3 scripts/catalyst_scan.py --stdout
```

Generated reports are written to `reports/catalyst-scans/`.

## Research Cadence

Suggested rhythm:

- Weekly full-watchlist scan for early catalysts and narrative changes.
- Mid-week targeted scan for high-priority names around earnings, conferences, product launches, or regulatory events.
- Monthly watchlist cleanup to promote, archive, or reprioritize names.
