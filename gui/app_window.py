from tkinter import Tk

from gui.recipe_selection.recipe_selection import RecipeSelection


class AppWindow:
    def __init__(self):
        self._window = Tk()
        self._window.title("Ingredient Extractor")
        self._window.state("zoomed")
        self._window.minsize(300, 200)

        self._recipe_selection = RecipeSelection(self._window)

        self._window.mainloop()
