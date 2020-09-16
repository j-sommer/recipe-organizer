from tkinter import Label, filedialog, Button, Frame

from recipe.recipe import Recipe


class RecipeSelection(Frame):
    FILE_TYPES = [
        ('json files', '*.json')
    ]

    def __init__(self):
        super().__init__()

        self._label_recipe_selection = None
        self._button_recipe_selection = None

        self._on_selected_recipe = None

        self.define_widgets()
        self.configure_layout()
        self.define_layout()

    def set_recipe_callback(self, on_selected_recipe):
        self._on_selected_recipe = on_selected_recipe

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
        selected_recipe_file = filedialog.askopenfilename(initialdir="/", title="Rezept auswählen",
                                                          filetypes=self.FILE_TYPES)
        self.read_json_file(selected_recipe_file)

    def read_json_file(self, file_path):
        with open(file_path, "r") as file:
            json_data = file.read()
            recipe = Recipe.from_json(json_data)
            if self._on_selected_recipe:
                self._on_selected_recipe(recipe)
