from tkinter import Label, Entry, END, Frame, Text

from gui.recipe_form.ingredient_form.ingredient_form import IngredientForm


class RecipeForm(Frame):
    def __init__(self):
        super().__init__()

        self._label_title = None
        self._entry_title = None
        self._frame_ingredients = None
        self._label_ingredients = None
        self._label_preparation = None
        self._text_preparation = None

    def define_widgets(self):
        self._label_title = Label(self, text="Titel")
        self._entry_title = Entry(self)
        self._label_ingredients = Label(self, text="Zutaten")
        self._frame_ingredients = Frame(self)
        self._label_preparation = Label(self, text="Zubereitung")
        self._text_preparation = Text(self)

    def configure_layout(self):
        pass

    def define_layout(self):
        self._label_title.grid(row=0, column=0)
        self._entry_title.grid(row=0, column=1)
        self._label_ingredients.grid(row=1, column=0)
        self._frame_ingredients.grid(row=2)
        self._label_preparation.grid(row=3, column=0)
        self._text_preparation.grid(row=4)

    def set_values(self, recipe):
        if recipe:
            self.define_widgets()
            self.define_layout()

            self._entry_title.insert(0, recipe.title)

            for index, ingredient in enumerate(recipe.ingredients):
                self.define_ingredient_form(index, ingredient)

            self._text_preparation.insert(END, recipe.preparation)

    def define_ingredient_form(self, position, ingredient):
        ingredient_form = IngredientForm(self._frame_ingredients, ingredient)
        ingredient_form.grid(row=position)
