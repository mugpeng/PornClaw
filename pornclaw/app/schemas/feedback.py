from pydantic import BaseModel


class FeedbackRequest(BaseModel):
    session_id: int
    series_id: int
    feedback_type: str


class FeedbackResponse(BaseModel):
    ok: bool
    updated_profile_summary: dict
