from tkinter import Tk

from gui.recipe_form.recipe_form import RecipeForm
from gui.recipe_selection.recipe_selection import RecipeSelection


class AppWindow:
    def __init__(self):
        self._window = Tk()
        self._window.title("Ingredient Extractor")
        self._window.state("zoomed")
        self._window.minsize(300, 200)

        self._recipe_selection = RecipeSelection()
        self._recipe_form = RecipeForm()

        self._recipe_selection.set_recipe_callback(self._recipe_form.set_values)

        self._recipe_selection.grid(row=0)
        self._recipe_form.grid(row=1)

    def render(self):
        self._window.mainloop()
