from tkinter import filedialog

from events.event import Event, EventType
from events.event_publisher import EventPublisher
from recipe.recipe import Recipe


class RecipeSelection:
    FILE_TYPES = [
        ('json files', '*.json')
    ]
    _selected_recipe_file: str

    def __init__(self):
        super().__init__()

    def open_recipe(self):
        self._selected_recipe_file = filedialog.askopenfilename(initialdir="/", title="Rezept auswählen",
                                                                filetypes=self.FILE_TYPES)
        self.read_recipe_from_file(self._selected_recipe_file)

    # TODO introduce recipe json file class
    @staticmethod
    def read_recipe_from_file(file_path: str) -> None:
        with open(file_path, "r") as file:
            json_data = file.read()
            recipe = Recipe.from_json(json_data)

            EventPublisher.broadcast(Event(EventType.FILE_READ, payload=recipe))

    def write_recipe_to_file(self, recipe: Recipe) -> None:
        with open(self._selected_recipe_file, "w") as file:
            json_data = recipe.to_json()
            file.write(json_data)

            EventPublisher.broadcast(Event(EventType.SAVED, payload=None))
