from tkinter import Menu

from commands.command import CommandType
from commands.command_invoker import CommandInvoker


class MenuBar(Menu):
    _file_menu: Menu

    def __init__(self, command_invoker: CommandInvoker):
        super().__init__()

        self._command_invoker = command_invoker

        self.define_menu_entries()

    def define_menu_entries(self):
        self._file_menu = Menu(self, tearoff=0)
        self._file_menu.add_command(label="Neu")
        self._file_menu.add_command(label="Öffnen", command=self.__open_recipe)
        self._file_menu.add_command(label="Speichern", command=self.__save_recipe)
        self.add_cascade(label="Datei", menu=self._file_menu)

    def __open_recipe(self):
        self._command_invoker.execute(CommandType.OPEN)

    def __save_recipe(self):
        self._command_invoker.execute(CommandType.SAVE)