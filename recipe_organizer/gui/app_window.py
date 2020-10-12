from tkinter import Tk, N, S, E, W

from recipe_organizer.commands.command_invoker import CommandInvoker
from recipe_organizer.commands.command_new import CommandNew
from recipe_organizer.commands.command_open import CommandOpen
from recipe_organizer.commands.command_save import CommandSave
from recipe_organizer.gui.event_display.event_display import EventDisplay
from recipe_organizer.gui.font_manager.font_manager import FontManager
from recipe_organizer.gui.interfaces.widget_container import WidgetContainer
from recipe_organizer.gui.menu_bar.menu_bar import MenuBar
from recipe_organizer.gui.recipe_form.recipe_form import RecipeForm
from recipe_organizer.gui.recipe_selection.recipe_selection import RecipeSelection
from recipe_organizer.gui.recipe_source_selection.recipe_source_selection import RecipeSourceSelection
from recipe_organizer.gui.scrollable_frame.scrollable_frame import ScrollableFrame
from recipe_organizer.gui.shortcut_handler.shortcut_handler import ShortcutHandler


class AppWindow(WidgetContainer):
    _menu_bar: MenuBar
    _scrollable_frame: ScrollableFrame
    _recipe_form: RecipeForm
    _event_display: EventDisplay
    _recipe_source_selection: RecipeSourceSelection

    _recipe_selection: RecipeSelection

    def __init__(self):
        self._window = Tk()
        self._window.title("Ingredient Extractor")
        self._window.state("zoomed")
        self._window.minsize(300, 200)

        self._scrollable_frame = ScrollableFrame(self._window)

        font_manager = FontManager(self._window)
        font_manager.set_default_font()

        self._recipe_selection = RecipeSelection()

        self.define_widgets()
        self.configure_layout()
        self.define_layout()
        self.define_command_handling()

    def define_widgets(self) -> None:
        self._recipe_form = RecipeForm(self._scrollable_frame.content)
        self._event_display = EventDisplay(self._scrollable_frame.content)
        self._recipe_source_selection = RecipeSourceSelection(self._window)

    def configure_layout(self):
        self._window.columnconfigure(0, weight=1)
        self._window.rowconfigure(0, weight=1)

    def define_layout(self) -> None:
        self._scrollable_frame.grid(row=0, column=0, sticky=N + S + E + W)
        self._recipe_form.grid(row=0, sticky=N + S + E + W)
        self._event_display.grid(row=1, column=0, sticky=S)

    def define_command_handling(self):
        command_invoker = CommandInvoker()
        shortcut_handler = ShortcutHandler(self._window, command_invoker)
        command_open = CommandOpen(self._recipe_selection)
        command_save = CommandSave(self._recipe_form, self._recipe_selection)
        command_new = CommandNew(self._recipe_form)

        command_invoker.register(command_open)
        command_invoker.register(command_save)
        command_invoker.register(command_new)

        self._menu_bar = MenuBar(command_invoker)
        self._window.config(menu=self._menu_bar)

    def render(self):
        self._window.mainloop()
