from tkinter import Tk

from gui.event_display.event_display import EventDisplay
from gui.interfaces.widget_container import WidgetContainer
from gui.menu_bar.menu_bar import MenuBar
from gui.recipe_form.recipe_form import RecipeForm
from gui.recipe_selection.recipe_selection import RecipeSelection


class AppWindow(WidgetContainer):
    _menu_bar: MenuBar
    _recipe_selection: RecipeSelection
    _recipe_form: RecipeForm

    _event_display: EventDisplay

    def __init__(self):
        self._window = Tk()
        self._window.title("Ingredient Extractor")
        self._window.state("zoomed")
        self._window.minsize(300, 200)

        self._recipe_selection = RecipeSelection()

        self.define_widgets()
        self.define_layout()

        self._menu_bar = MenuBar()
        self._window.config(menu=self._menu_bar)

    def define_widgets(self) -> None:
        self._recipe_form = RecipeForm()
        self._event_display = EventDisplay()

    def define_layout(self) -> None:
        self._recipe_form.grid(row=1)
        self._event_display.grid(row=2)

    def render(self):
        self._window.mainloop()
