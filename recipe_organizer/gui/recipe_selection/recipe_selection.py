from tkinter import filedialog

from recipe_organizer.events.event import Event, EventType
from recipe_organizer.events.event_publisher import EventPublisher
from recipe_organizer.recipe.recipe import Recipe


class RecipeSelection:
    FILE_TYPES = [
        ('json files', '*.json')
    ]
    _selected_recipe_file: str = None

    def open_recipe_file(self) -> None:
        file_name = filedialog.askopenfilename(initialdir="/", title="Rezept auswählen",
                                               filetypes=self.FILE_TYPES)

        if file_name:
            self.__read_recipe_from_file(file_name)
            self._selected_recipe_file = file_name

    def save_recipe_to_file(self, recipe: Recipe) -> None:
        if self._selected_recipe_file is not None:
            self.__write_to_selected_file_and_publish(recipe, self._selected_recipe_file)
        else:
            file_name = filedialog.asksaveasfilename(defaultextension=".json", filetypes=self.FILE_TYPES)

            if file_name:
                self._selected_recipe_file = file_name
                self.__write_to_selected_file_and_publish(recipe, self._selected_recipe_file)

    @staticmethod
    def __read_recipe_from_file(file_path: str) -> None:
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = file.read()
            recipe = Recipe.from_json(json_data)

            EventPublisher.broadcast(Event(EventType.FILE_READ, payload=recipe))

    @staticmethod
    def __write_to_selected_file_and_publish(recipe: Recipe, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json_data = recipe.to_json()
            file.write(json_data)

            EventPublisher.broadcast(Event(EventType.SAVED, payload=None))
