import json

from sqlalchemy.orm import Session

from app.adapters.demo_source import DemoSourceAdapter
from app.models import RawItem, SeriesItem, SourceSession
from app.services.aggregate import aggregate_series
from app.services.normalize import normalize_item


class AppError(Exception):
    pass


def ingest_source(db: Session, source_url: str) -> SourceSession:
    adapter = DemoSourceAdapter()
    if not adapter.validate_source_url(source_url):
        raise AppError("数据源 URL 非法。")
    session = SourceSession(
        source_url=source_url,
        source_name=adapter.detect_source_name(source_url),
        status="running",
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    try:
        raw_items = [normalize_item(item) for item in adapter.fetch_recent_items(source_url)]
        if not raw_items:
            raise AppError("抓取为空。")
        for item in raw_items:
            db.add(
                RawItem(
                    session_id=session.id,
                    title=item["title"],
                    detail_url=item["detail_url"],
                    cover_url=item.get("cover_url"),
                    publish_time=item.get("publish_time"),
                    author_or_group=item.get("author_or_group"),
                    tags_raw_json=json.dumps(item.get("tags_raw_list", [])),
                    description_raw=item.get("description_raw"),
                    series_name_raw=item.get("series_name"),
                    chapter_raw=item.get("chapter_or_episode_raw"),
                    extra_json=json.dumps({"normalized_tags": item.get("normalized_tags", [])}),
                )
            )
        aggregated = aggregate_series(raw_items)
        for row in aggregated:
            db.add(
                SeriesItem(
                    session_id=session.id,
                    series_name=row["series_name"],
                    representative_cover=row.get("representative_cover"),
                    latest_update_time=row.get("latest_update_time"),
                    update_count_7d=row.get("update_count_7d", 0),
                    tags_json=json.dumps(row.get("tags", [])),
                    source_urls_json=json.dumps(row.get("source_urls", [])),
                    authors_json=json.dumps(row.get("authors", [])),
                    meta_json=json.dumps(row.get("meta", {})),
                )
            )
        session.status = "completed"
        session.raw_items_count = len(raw_items)
        session.series_count = len(aggregated)
        db.commit()
        db.refresh(session)
        return session
    except Exception as exc:
        session.status = "failed"
        session.error_message = str(exc)
        db.commit()
        raise AppError(str(exc)) from exc
