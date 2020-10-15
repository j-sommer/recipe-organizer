from pathlib import Path
from tkinter import Toplevel, Button, filedialog, E, W, S, Label, CENTER

from recipe_organizer.events.event import Event, EventType
from recipe_organizer.events.event_publisher import EventPublisher
from recipe_organizer.gui.interfaces.widget_container import WidgetContainer


class RecipeSourceSelection(Toplevel, WidgetContainer):
    _label_info: Label
    _button_dismiss: Button
    _button_select_directory: Button

    _source_directory: Path

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.title("Quellverzeichnis auswählen")

        self.grab_set()

        self.configure_layout()
        self.define_widgets()
        self.define_layout()

        self.geometry("500x300")
        self.wait_window(self)

    def define_widgets(self) -> None:
        self._label_info = Label(self, text="Einen Ordner als Hauptverzeichnis für die Rezepte auswählen",
                                 justify=CENTER)

        self._button_select_directory = Button(self, text="Auswählen", command=self.__choose_directory)
        self._button_dismiss = Button(self, text="Abbrechen", command=self.destroy)

    def configure_layout(self) -> None:
        self.columnconfigure(0, minsize=250)
        self.columnconfigure(1, minsize=250)
        self.rowconfigure(0, minsize=150)
        self.rowconfigure(1, minsize=150)

    def define_layout(self) -> None:
        self._label_info.grid(row=0, column=0, columnspan=2, sticky=E + W, padx=15)
        self._button_select_directory.grid(row=1, column=0, sticky=S + W, padx=10, pady=12)
        self._button_dismiss.grid(row=1, column=1, sticky=S + E, padx=10, pady=12)

    def get_selected_directory(self):
        return self._source_directory

    def __choose_directory(self):
        directory = filedialog.askdirectory(title="Hauptverzeichnis auswählen")

        if directory:
            self._source_directory = Path(directory)

            EventPublisher.broadcast(Event(EventType.SOURCE_SET, payload=self._source_directory))
            self.destroy()
