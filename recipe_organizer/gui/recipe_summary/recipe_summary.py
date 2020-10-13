from tkinter import Frame, Label, RAISED

from recipe_organizer.gui.interfaces.widget_container import WidgetContainer
from recipe_organizer.recipe.recipe import Recipe


class RecipeSummary(Frame, WidgetContainer):
    _recipe: Recipe
    _label_title: Label
    _label_title_value: Label

    def __init__(self, parent, recipe: Recipe):
        Frame.__init__(self, parent, bd=1, relief=RAISED)
        self._recipe = recipe

        self.define_widgets()
        self.define_layout()

    def define_widgets(self) -> None:
        self._label_title = Label(self, text="Rezept:")
        self._label_title_value = Label(self, text=self._recipe.title)

    def define_layout(self) -> None:
        self._label_title.grid(row=0, column=0)
        self._label_title_value.grid(row=0, column=1)
