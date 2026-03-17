from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class RawItem(Base):
    __tablename__ = "raw_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("source_sessions.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    detail_url: Mapped[str] = mapped_column(String(500), nullable=False)
    cover_url: Mapped[str | None] = mapped_column(String(500))
    publish_time: Mapped[datetime | None] = mapped_column(DateTime)
    author_or_group: Mapped[str | None] = mapped_column(String(255))
    tags_raw_json: Mapped[str] = mapped_column(Text, default="[]", nullable=False)
    description_raw: Mapped[str | None] = mapped_column(Text)
    series_name_raw: Mapped[str | None] = mapped_column(String(255))
    chapter_raw: Mapped[str | None] = mapped_column(String(255))
    extra_json: Mapped[str] = mapped_column(Text, default="{}", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
