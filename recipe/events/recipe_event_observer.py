from abc import abstractmethod, ABC

from recipe.events.recipe_event import RecipeEvent


class RecipeEventObserver(ABC):
    @abstractmethod
    def notify(self, event: RecipeEvent) -> None:
        pass
