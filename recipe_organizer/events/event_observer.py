from abc import abstractmethod, ABC

from recipe_organizer.events.event import Event


class EventObserver(ABC):
    @abstractmethod
    def notify(self, event: Event) -> None:
        pass
