from abc import abstractmethod, ABC

from events.event import Event


class EventObserver(ABC):
    @abstractmethod
    def notify(self, event: Event) -> None:
        pass
