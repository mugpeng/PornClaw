# PornClaw Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a minimal end-to-end PornClaw prototype that ingests one source URL, aggregates items into series, captures user preferences and feedback, and produces explainable Top 5 recommendations.

**Architecture:** Implement a FastAPI monolith with SQLAlchemy models, service-layer orchestration, and Jinja2 pages. Keep crawling behind a demo-friendly adapter, make normalization/configuration explicit, and store score breakdowns so recommendation behavior is testable and explainable.

**Tech Stack:** Python 3.11, FastAPI, Jinja2, SQLAlchemy, SQLite, requests, BeautifulSoup4, pytest, Docker Compose

---

## Chunk 1: Skeleton and Failing Tests

### Task 1: Create project structure and dependency files

**Files:**
- Create: `pornclaw/app/...`
- Create: `pornclaw/tests/...`
- Create: `pornclaw/requirements.txt`
- Create: `pornclaw/Dockerfile`
- Create: `pornclaw/docker-compose.yml`
- Create: `pornclaw/README.md`

- [ ] Step 1: Create the required directory tree.
- [ ] Step 2: Add minimal dependency definitions and boot files.
- [ ] Step 3: Add test configuration.

### Task 2: Write failing core tests

**Files:**
- Create: `pornclaw/tests/test_adapter.py`
- Create: `pornclaw/tests/test_aggregate.py`
- Create: `pornclaw/tests/test_recommend.py`

- [ ] Step 1: Write adapter contract test.
- [ ] Step 2: Run adapter test and confirm failure.
- [ ] Step 3: Write aggregation behavior test.
- [ ] Step 4: Run aggregation test and confirm failure.
- [ ] Step 5: Write recommendation ranking test.
- [ ] Step 6: Run recommendation test and confirm failure.

## Chunk 2: Domain and Services

### Task 3: Implement configuration, database, and models

**Files:**
- Create: `pornclaw/app/config.py`
- Create: `pornclaw/app/db.py`
- Create: `pornclaw/app/models/*.py`

- [ ] Step 1: Add settings and tag mapping configuration.
- [ ] Step 2: Add SQLAlchemy engine, session, and base.
- [ ] Step 3: Add the six required models with timestamps and JSON text fields.

### Task 4: Implement adapter, normalization, aggregation, and preference parsing

**Files:**
- Create: `pornclaw/app/adapters/base.py`
- Create: `pornclaw/app/adapters/demo_source.py`
- Create: `pornclaw/app/services/normalize.py`
- Create: `pornclaw/app/services/aggregate.py`
- Create: `pornclaw/app/services/preference_parser.py`

- [ ] Step 1: Implement the adapter contract and demo parsing path.
- [ ] Step 2: Implement normalization helpers and config-driven tag mapping.
- [ ] Step 3: Implement aggregation rules.
- [ ] Step 4: Implement free-text preference parsing.
- [ ] Step 5: Re-run the first two tests until green.

### Task 5: Implement profile, recommend, explain, and ingest orchestration

**Files:**
- Create: `pornclaw/app/services/ingest.py`
- Create: `pornclaw/app/services/profile.py`
- Create: `pornclaw/app/services/recommend.py`
- Create: `pornclaw/app/services/explain.py`

- [ ] Step 1: Build ingest orchestration from source session through series creation.
- [ ] Step 2: Build profile merge/update logic from explicit tags, free text, and feedback.
- [ ] Step 3: Build weighted recommendation scoring and persistence.
- [ ] Step 4: Build explanation text generation.
- [ ] Step 5: Re-run recommendation test until green.

## Chunk 3: Web App, Demo Source, and Verification

### Task 6: Implement API and page routes with templates

**Files:**
- Create: `pornclaw/app/main.py`
- Create: `pornclaw/app/routes/*.py`
- Create: `pornclaw/app/schemas/*.py`
- Create: `pornclaw/app/templates/*.html`
- Create: `pornclaw/app/static/styles.css`

- [ ] Step 1: Implement home page and form submission.
- [ ] Step 2: Implement candidate feedback flow.
- [ ] Step 3: Implement recommendations page and feedback refresh.
- [ ] Step 4: Implement the required JSON APIs.
- [ ] Step 5: Add bundled demo source page endpoint.

### Task 7: Add scripts, Docker, README, and final verification

**Files:**
- Create: `pornclaw/scripts/init_db.py`
- Create: `pornclaw/.env.example`
- Modify: `pornclaw/README.md`
- Modify: `pornclaw/Dockerfile`
- Modify: `pornclaw/docker-compose.yml`

- [ ] Step 1: Add DB init script and environment example.
- [ ] Step 2: Add Docker build/run flow.
- [ ] Step 3: Write README with architecture, flow, run steps, and roadmap.
- [ ] Step 4: Run `pytest`.
- [ ] Step 5: Run a basic import/startup verification for the app.
