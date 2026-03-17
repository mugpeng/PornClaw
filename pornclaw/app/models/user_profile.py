from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("source_sessions.id"), nullable=False)
    liked_tags_json: Mapped[str] = mapped_column(Text, default="[]", nullable=False)
    disliked_tags_json: Mapped[str] = mapped_column(Text, default="[]", nullable=False)
    free_text_intent: Mapped[str | None] = mapped_column(Text)
    derived_preferences_json: Mapped[str] = mapped_column(Text, default="{}", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
