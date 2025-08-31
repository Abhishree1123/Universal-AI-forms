# Contributing to FormDL

Thanks for your interest!

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install || true
```

## Guidelines
- Keep the **spec minimal** and **extensible**.
- Prefer **pure JSON** for profile portability; use CBOR for compact offline encoding.
- For new features, add tests and update README.

## Commit style
Use conventional commits if possible (feat:, fix:, docs:, chore:).

## Pull Requests
- Reference an issue.
- Explain design tradeoffs.
- Include tests where practical.
