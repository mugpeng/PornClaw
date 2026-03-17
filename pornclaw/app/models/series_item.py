from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class SeriesItem(Base):
    __tablename__ = "series_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("source_sessions.id"), nullable=False)
    series_name: Mapped[str] = mapped_column(String(255), nullable=False)
    representative_cover: Mapped[str | None] = mapped_column(String(500))
    latest_update_time: Mapped[datetime | None] = mapped_column(DateTime)
    update_count_7d: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    tags_json: Mapped[str] = mapped_column(Text, default="[]", nullable=False)
    source_urls_json: Mapped[str] = mapped_column(Text, default="[]", nullable=False)
    authors_json: Mapped[str] = mapped_column(Text, default="[]", nullable=False)
    meta_json: Mapped[str] = mapped_column(Text, default="{}", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
