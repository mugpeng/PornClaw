from pydantic import BaseModel


class RecommendRequest(BaseModel):
    session_id: int


class RecommendationItem(BaseModel):
    series_id: int
    series_name: str
    score_breakdown: dict
    reason_text: str


class RecommendResponse(BaseModel):
    top_5: list[RecommendationItem]
    score_breakdowns: list[dict]
    reasons: list[str]
