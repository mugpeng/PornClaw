# PornClaw Phase 1 Design

**Goal**

Build a local-first prototype web application that ingests a single content source URL, normalizes recent items, aggregates them into series, collects lightweight user preferences and feedback, and returns explainable Top 5 series recommendations.

**Architecture**

The application is a FastAPI monolith with server-rendered Jinja2 pages and a small JSON API layer for the same workflows. SQLite stores ingest sessions, raw items, aggregated series, user profiles, feedback, and recommendation records. Source crawling is isolated behind an adapter interface so the phase can succeed with a demo/static source while still supporting real URLs when page structure is compatible.

**Core Flow**

1. User submits a source URL plus explicit likes, dislikes, and a free-text preference sentence.
2. Backend creates a `source_session`, selects the demo adapter, fetches recent items, normalizes them, stores raw items, aggregates them into series, and stores an initial `user_profile`.
3. User sees 8-12 candidate series and marks them as like/dislike/skip.
4. Recommendation service scores all series with transparent scoring components and stores Top 5 recommendations.
5. Recommendation page shows reasons, accepts additional feedback, and allows regeneration so the next round reflects the new signals.

**Key Design Decisions**

- Use one default adapter implementation that supports:
  - A bundled local demo page under the app itself.
  - Generic static HTML parsing for simple list/card based pages.
- Keep normalization rule-based with configuration-driven tag mappings.
- Aggregate by `series_name_raw` first, then fallback to a cleaned title heuristic.
- Parse free-text preferences using deterministic keyword mappings only.
- Use weighted scoring rather than ML or embeddings; every scoring term is persisted.

**Error Handling**

- Invalid URL, inaccessible source, parse mismatch, empty ingest, aggregation failure, and empty recommendations all update session status and surface a readable message in the UI.
- Service layer raises typed `AppError` exceptions with user-facing and internal context.
- Routes stay thin and convert service failures into `error.html` or API error payloads.

**Testing Scope**

- Adapter output schema contract.
- Series aggregation from multiple raw items.
- Recommendation ordering predictability for a controlled dataset.
- Optional parser and explanation tests if time allows.

**Constraints**

- No auth, no background jobs, no embeddings, no complex ML, no multi-source merge.
- Favor stable local demo behavior over brittle external crawling.
