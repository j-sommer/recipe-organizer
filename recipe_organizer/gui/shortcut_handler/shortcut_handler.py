from recipe_organizer.commands.command import CommandType
from recipe_organizer.commands.command_invoker import CommandInvoker


class ShortcutHandler:
    def __init__(self, observed_widget, command_invoker: CommandInvoker):
        self._command_invoker = command_invoker

        self.__bind_to_shortcuts(observed_widget)

    def __bind_to_shortcuts(self, observed_widget):
        observed_widget.bind(
            '<Control-o>',
            lambda e: self._command_invoker.execute(CommandType.OPEN)
        )

        observed_widget.bind(
            '<Control-n>',
            lambda e: self._command_invoker.execute(CommandType.NEW)
        )

        observed_widget.bind(
            '<Control-s>',
            lambda e: self._command_invoker.execute(CommandType.SAVE)
        )
