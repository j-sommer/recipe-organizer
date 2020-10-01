from tkinter import Menu

from events.event import Event, EventType
from events.event_publisher import EventPublisher


class MenuBar(Menu):
    _file_menu: Menu

    def __init__(self):
        super().__init__()

        self.define_menu_entries()

    def define_menu_entries(self):
        self._file_menu = Menu(self, tearoff=0)
        self._file_menu.add_command(label="Neu")
        self._file_menu.add_command(label="Öffnen", command=self.open_recipe)
        self._file_menu.add_command(label="Speichern")
        self.add_cascade(label="Datei", menu=self._file_menu)

    def open_recipe(self):
        EventPublisher.broadcast(Event(event_type=EventType.OPEN, payload=None))
