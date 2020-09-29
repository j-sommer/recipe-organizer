from tkinter import Label, filedialog, Button, Frame

from recipe.events.recipe_event import RecipeEvent, RecipeEventType
from recipe.events.recipe_event_observer import RecipeEventObserver
from recipe.events.recipe_event_publisher import RecipeEventPublisher
from recipe.recipe import Recipe


class RecipeSelection(Frame, RecipeEventObserver):
    FILE_TYPES = [
        ('json files', '*.json')
    ]

    _label_recipe_selection: Label = None
    _button_recipe_selection: Button = None

    _selected_recipe_file: str = None

    def __init__(self):
        super().__init__()

        self.define_widgets()
        self.configure_layout()
        self.define_layout()

        RecipeEventPublisher.add(self)

    def notify(self, event: RecipeEvent) -> None:
        if event.event_type == RecipeEventType.SAVE:
            self.write_recipe_to_file(event.payload, self._selected_recipe_file)

    def define_widgets(self):
        self._label_recipe_selection = Label(self, text="Rezeptauswahl")
        self._button_recipe_selection = Button(self, text="auswählen", command=self.open_selection_dialog)

    def configure_layout(self):
        self.rowconfigure(0, pad=30)
        self.columnconfigure(0, pad=8)
        self.rowconfigure(1, pad=20)
        self.columnconfigure(1, pad=8)

    def define_layout(self):
        self._label_recipe_selection.grid(row=0, column=0)
        self._button_recipe_selection.grid(row=1, column=1)

    def open_selection_dialog(self):
        self._selected_recipe_file = filedialog.askopenfilename(initialdir="/", title="Rezept auswählen",
                                                                filetypes=self.FILE_TYPES)
        self.read_recipe_from_file(self._selected_recipe_file)

    @staticmethod
    def read_recipe_from_file(file_path: str) -> None:
        with open(file_path, "r") as file:
            json_data = file.read()
            recipe = Recipe.from_json(json_data)

            RecipeEventPublisher.broadcast(RecipeEvent(RecipeEventType.READ, payload=recipe))

    @staticmethod
    def write_recipe_to_file(recipe: Recipe, file_path: str) -> None:
        with open(file_path, "w") as file:
            json_data = recipe.to_json()
            file.write(json_data)
