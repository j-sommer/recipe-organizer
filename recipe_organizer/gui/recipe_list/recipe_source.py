from pathlib import Path
from tkinter import Frame, Label

from recipe_organizer.events.event import Event, EventType
from recipe_organizer.events.event_observer import EventObserver
from recipe_organizer.events.event_publisher import EventPublisher
from recipe_organizer.gui.interfaces.widget_container import WidgetContainer
from recipe_organizer.gui.recipe_summary.recipe_summary import RecipeSummary
from recipe_organizer.recipe.recipe import Recipe


class RecipeSource(Frame, WidgetContainer, EventObserver):
    _MAX_COLUMN_COUNT = 6

    _label_source_directory: Label
    _recipe_summaries: [RecipeSummary] = []

    _row_index = 0

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.define_widgets()
        self.define_layout()

        EventPublisher.add(self)

    def define_widgets(self) -> None:
        self._label_source_directory = Label(self, text="-")

    def define_layout(self) -> None:
        self._label_source_directory.grid(row=self.__get_row_index())

    def notify(self, event: Event) -> None:
        if event.event_type == EventType.SOURCE_SET:
            self._label_source_directory.configure(text=event.payload.name)
            self.__load_recipes(event.payload)

    def __get_row_index(self) -> int:
        current_index = self._row_index
        self._row_index += 1
        return current_index

    def __load_recipes(self, directory: Path):
        recipes: [Recipe] = []
        file_paths = directory.glob("**/*.json")
        for file_path in file_paths:
            with open(file_path, "r", encoding="utf-8") as file:
                json_data = file.read()
                try:
                    recipe = Recipe.from_json(json_data)
                except KeyError:
                    pass
                else:
                    recipes.append(recipe)

        self.__create_list(recipes)

    def __create_list(self, recipes: [Recipe]):
        current_row_index = self.__get_row_index()

        for index, recipe in enumerate(recipes):
            if index % self._MAX_COLUMN_COUNT == 0:
                current_row_index = self.__get_row_index()

            recipe_summary = RecipeSummary(self, recipe)
            recipe_summary.grid(row=current_row_index, column=index % self._MAX_COLUMN_COUNT, padx=16, pady=10)
            self.columnconfigure(index, minsize=200)

            self._recipe_summaries.append(recipe_summary)
