# AGENTS.md
## Project
Stack: Python 3.11 + FastAPI
Install: pip install -e .[dev]
Run: uvicorn app.main:app --reload
Test: pytest -q

## Conventions
- Run `ruff check --fix .` and `black .` before proposing changes
- Pydantic v2; strict typing; no secrets in code (.env + settings)

## Tasks
- Always run `pytest -q` before proposing a commit/PR
- Update OpenAPI docs when endpoints change
