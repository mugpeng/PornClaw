from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    @abstractmethod
    def validate_source_url(self, url: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def fetch_recent_items(self, url: str) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def detect_source_name(self, url: str) -> str:
        raise NotImplementedError
