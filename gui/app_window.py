from tkinter import Tk

from commands.command_invoker import CommandInvoker
from commands.command_open import CommandOpen
from commands.command_save import CommandSave
from gui.event_display.event_display import EventDisplay
from gui.font_manager.font_manager import FontManager
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

        font_manager = FontManager(self._window)
        font_manager.set_default_font()

        self._recipe_selection = RecipeSelection()

        self.define_widgets()
        self.define_layout()
        self.define_command_handling()

    def define_widgets(self) -> None:
        self._recipe_form = RecipeForm()
        self._event_display = EventDisplay()

    def define_layout(self) -> None:
        self._recipe_form.grid(row=1)
        self._event_display.grid(row=2)

    def define_command_handling(self):
        command_invoker = CommandInvoker()
        command_open = CommandOpen(self._recipe_selection)
        command_save = CommandSave(self._recipe_form, self._recipe_selection)

        command_invoker.register(command_open)
        command_invoker.register(command_save)

        self._menu_bar = MenuBar(command_invoker)
        self._window.config(menu=self._menu_bar)

    def render(self):
        self._window.mainloop()
