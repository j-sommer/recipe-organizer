from tkinter import Label, filedialog, Button


class RecipeSelection:
    FILE_TYPES = [
        ('text files', '*.txt'),
        ('all files', '*'),
    ]

    def __init__(self, parent):
        self._label_recipe_selection = None
        self._button_recipe_selection = None
        self._dialog_recipe_selection = None

        self.define_widgets(parent)
        self.define_layout()

    def define_widgets(self, parent):
        self._label_recipe_selection = Label(parent, text="Rezeptauswahl")
        self._button_recipe_selection = Button(parent, text="auswählen", command=self.open_selection_dialog)

    def define_layout(self):
        self._label_recipe_selection.grid(column=0)
        self._button_recipe_selection.grid(column=0)

    def open_selection_dialog(self):
        self._dialog_recipe_selection = filedialog.askopenfile(initialdir="/", title="Rezept auswählen",
                                                               filetypes=self.FILE_TYPES)
