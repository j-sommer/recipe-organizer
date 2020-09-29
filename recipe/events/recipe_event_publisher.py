from typing import List

from recipe.events.recipe_event_observer import RecipeEventObserver

_observers: List[RecipeEventObserver] = []


class RecipeEventPublisher:

    @staticmethod
    def add(observer):
        _observers.append(observer)

    @staticmethod
    def remove(observer):
        _observers.remove(observer)

    @staticmethod
    def broadcast(event):
        for observer in _observers:
            observer.notify(event)
