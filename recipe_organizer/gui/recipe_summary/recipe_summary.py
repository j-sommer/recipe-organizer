from tkinter import Frame, Label, RAISED

from recipe_organizer.gui.interfaces.widget_container import WidgetContainer
from recipe_organizer.recipe.recipe import Recipe


class RecipeSummary(Frame, WidgetContainer):
    _recipe: Recipe
    _label_title: Label
    _label_title_value: Label
    _recipe_labels: [Label] = []

    def __init__(self, parent, recipe: Recipe):
        Frame.__init__(self, parent, bd=1, relief=RAISED)
        self._recipe = recipe

        self.bind("<Enter>", self.__on_enter)
        self.bind("<Leave>", self.__on_leave)
        self.bind("<Button-1>", self.__on_click)

        self.define_widgets()
        self.define_layout()

        self.__define_labels()

    def define_widgets(self) -> None:
        self._label_title = Label(self, text="Rezept:")
        self._label_title_value = Label(self, text=self._recipe.title)

    def define_layout(self) -> None:
        self._label_title.grid(row=0, column=0, padx=6, pady=6)
        self._label_title_value.grid(row=0, column=1, padx=6, pady=6)

    def __define_labels(self):
        for index, label in enumerate(self._recipe.labels):
            element = Label(self, text=label, bd=1, relief=RAISED)
            element.grid(row=1, column=index, padx=7, pady=7)

            self._recipe_labels.append(element)

    def __on_enter(self, event) -> None:
        self.configure(bd=2)

    def __on_leave(self, event) -> None:
        self.configure(bd=1)

    def __on_click(self, event) -> None:
        print("clicked")
