from tkinter import Label, Entry, END, Frame, Text


class RecipeForm(Frame):
    def __init__(self):
        super().__init__()

        self._label_title = None
        self._entry_title = None
        self._frame_ingredients = None
        self._label_ingredients = None

        self.define_widgets()
        self.define_layout()

    def define_widgets(self):
        self._label_title = Label(self, text="Titel")
        self._entry_title = Entry(self)
        self._frame_ingredients = Frame(self)

    def configure_layout(self):
        self.columnconfigure(0, pad=12)
        self.columnconfigure(1, pad=12)

    def define_layout(self):
        self._label_title.grid(row=0, column=0)
        self._entry_title.grid(row=0, column=1)
        self._frame_ingredients.grid(row=1)

    def set_values(self, recipe):
        if recipe:
            self._entry_title.delete(0, END)
            self._entry_title.insert(0, recipe.title)

            self._label_ingredients = Label(self._frame_ingredients, text="Zutaten")
            self._label_ingredients.grid(row=0, column=0)

            for index, ingredient in enumerate(recipe.ingredients):
                self.define_ingredient_widget(index, ingredient)

            self.define_preparation_widget(recipe)

    def define_ingredient_widget(self, index, ingredient):
        position = index + 1
        entry_ingredient = Entry(self._frame_ingredients)
        entry_ingredient.grid(row=position, column=0, pady=10, padx=5)
        entry_ingredient.insert(0, ingredient.name)

        entry_quantity = Entry(self._frame_ingredients)
        entry_quantity.grid(row=position, column=1, padx=5)
        entry_quantity.insert(0, ingredient.quantity)

        entry_quantity_type = Entry(self._frame_ingredients)
        entry_quantity_type.grid(row=position, column=2)
        entry_quantity_type.insert(0, ingredient.quantity_type)

    def define_preparation_widget(self, recipe):
        label_preparation = Label(self, text="Zubereitung")
        label_preparation.grid(row=2, column=0)

        text_preparation = Text(self)
        text_preparation.insert(END, recipe.preparation)
        text_preparation.grid(row=3)
