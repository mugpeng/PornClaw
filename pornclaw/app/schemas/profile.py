from pydantic import BaseModel


class ProfileCreateRequest(BaseModel):
    session_id: int
    liked_tags: list[str]
    disliked_tags: list[str]
    free_text_intent: str = ""


class ProfileCreateResponse(BaseModel):
    profile_id: int
    derived_preferences: dict
