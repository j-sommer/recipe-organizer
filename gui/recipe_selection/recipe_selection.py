from tkinter import Label, filedialog, Button

from recipe.recipe import Recipe


class RecipeSelection:
    FILE_TYPES = [
        ('json files', '*.json')
    ]

    def __init__(self, parent):
        self._label_recipe_selection = None
        self._button_recipe_selection = None
        self._selected_recipe_file = None

        self.define_widgets(parent)
        self.define_layout()

    def define_widgets(self, parent):
        self._label_recipe_selection = Label(parent, text="Rezeptauswahl")
        self._button_recipe_selection = Button(parent, text="auswählen", command=self.open_selection_dialog)

    def define_layout(self):
        self._label_recipe_selection.grid(column=0)
        self._button_recipe_selection.grid(column=0)

    def open_selection_dialog(self):
        self._selected_recipe_file = filedialog.askopenfilename(initialdir="/", title="Rezept auswählen",
                                                                filetypes=self.FILE_TYPES)
        self.read_json_file(self._selected_recipe_file)

    def read_json_file(self, file_path):
        with open(file_path, "r") as file:
            json_data = file.read()
            selected_recipe = Recipe.from_json(json_data)
            for ingredient in selected_recipe.ingredients:
                print(ingredient.name)
