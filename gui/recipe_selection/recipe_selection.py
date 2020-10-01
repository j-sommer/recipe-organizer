from tkinter import filedialog
from typing import Callable

from events.event import Event, EventType
from events.event_observer import EventObserver
from events.event_publisher import EventPublisher
from recipe.recipe import Recipe


class RecipeSelection(EventObserver):
    FILE_TYPES = [
        ('json files', '*.json')
    ]
    _selected_recipe_file: str

    _event_handler = {
        EventType.OPEN: Callable,
        EventType.SAVE: Callable
    }

    def __init__(self):
        super().__init__()

        EventPublisher.add(self)

        self._event_handler[EventType.OPEN] = self.open_recipe
        self._event_handler[EventType.SAVE] = self.write_recipe_to_file

    def notify(self, event: Event) -> None:
        if event.event_type in self._event_handler:
            self._event_handler.get(event.event_type)(event)

    def open_recipe(self, event: Event):
        self._selected_recipe_file = filedialog.askopenfilename(initialdir="/", title="Rezept auswählen",
                                                                filetypes=self.FILE_TYPES)
        self.read_recipe_from_file(self._selected_recipe_file)

    def save_recipe(self, event: Event):
        self.write_recipe_to_file(event.payload, self._selected_recipe_file)

    @staticmethod
    def read_recipe_from_file(file_path: str) -> None:
        with open(file_path, "r") as file:
            json_data = file.read()
            recipe = Recipe.from_json(json_data)

            EventPublisher.broadcast(Event(EventType.READ, payload=recipe))

    @staticmethod
    def write_recipe_to_file(recipe: Recipe, file_path: str) -> None:
        with open(file_path, "w") as file:
            json_data = recipe.to_json()
            file.write(json_data)
