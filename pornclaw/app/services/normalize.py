from app.config import settings
from app.utils.text import slugify_title, split_tags


def normalize_item(raw_item: dict) -> dict:
    tags_raw = split_tags(raw_item.get("tags_raw"))
    normalized_tags = normalize_tags(tags_raw + [raw_item.get("title", ""), raw_item.get("description_raw", "")])
    series_name = raw_item.get("series_name_raw") or derive_series_name(raw_item.get("title", ""))
    return {
        **raw_item,
        "tags_raw_list": tags_raw,
        "normalized_tags": normalized_tags,
        "series_name": series_name,
        "title_clean": slugify_title(raw_item.get("title", "")),
    }


def normalize_tags(values: list[str]) -> list[str]:
    lowered = " ".join(value.lower() for value in values if value)
    tags: list[str] = []
    for standard_tag, aliases in settings.tag_aliases.items():
        if any(alias.lower() in lowered for alias in aliases):
            tags.append(standard_tag)
    return sorted(set(tags))


def derive_series_name(title: str) -> str:
    cleaned = slugify_title(title)
    return cleaned.title() if cleaned else "Untitled Series"
