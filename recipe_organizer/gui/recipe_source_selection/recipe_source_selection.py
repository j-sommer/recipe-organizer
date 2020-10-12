from tkinter import Toplevel, Message, Button, filedialog

from recipe_organizer.gui.interfaces.widget_container import WidgetContainer


class RecipeSourceSelection(Toplevel, WidgetContainer):
    _message_info: Message
    _button_dismiss: Button
    _button_select_directory: Button

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.title("Quellverzeichnis auswählen")
        self.attributes('-topmost', 'true')

        self.geometry("400x200")

        self.grab_set()

        self.configure_layout()
        self.define_widgets()
        self.define_layout()

        self.wait_window(self)

    def define_widgets(self) -> None:
        self._message_info = Message(self, text="Einen Ordner als Hauptverzeichnis für die Rezepte auswählen")

        self._button_select_directory = Button(self, text="Auswählen", command=self.__choose_directory)
        self._button_dismiss = Button(self, text="Abbrechen", command=self.destroy)

    def configure_layout(self) -> None:
        self.columnconfigure(0, weight=1)

    def define_layout(self) -> None:
        self._message_info.grid(row=0, column=0, columnspan=2, sticky="ew")
        self._button_select_directory.grid(row=1, column=0)
        self._button_dismiss.grid(row=1, column=1)

    def __choose_directory(self):
        directory = filedialog.askdirectory(title="Hauptverzeichnis auswählen")
