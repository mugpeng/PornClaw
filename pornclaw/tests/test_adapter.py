from app.adapters.demo_source import DemoSourceAdapter


def test_demo_adapter_returns_normalized_fields() -> None:
    adapter = DemoSourceAdapter()

    items = adapter.fetch_recent_items("demo://seed")

    assert items
    required = {
        "source_id",
        "title",
        "detail_url",
        "cover_url",
        "publish_time",
        "author_or_group",
        "tags_raw",
        "description_raw",
        "series_name_raw",
        "chapter_or_episode_raw",
    }
    assert required.issubset(items[0].keys())
