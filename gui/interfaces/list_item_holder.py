from abc import ABC, abstractmethod
from typing import Any


class ListItemHolder(ABC):
    @abstractmethod
    def remove_item(self, to_remove: Any) -> None:
        pass
