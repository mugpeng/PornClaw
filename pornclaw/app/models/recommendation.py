from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("source_sessions.id"), nullable=False)
    series_id: Mapped[int] = mapped_column(ForeignKey("series_items.id"), nullable=False)
    rank: Mapped[int] = mapped_column(Integer, nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)
    score_breakdown_json: Mapped[str] = mapped_column(Text, default="{}", nullable=False)
    reason_text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
