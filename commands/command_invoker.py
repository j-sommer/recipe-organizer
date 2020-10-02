from time import time

from commands.command import Command, CommandType


class CommandInvoker:
    _commands = {}
    _history: [(float, CommandType)] = []

    def register(self, command: Command) -> None:
        self._commands[command.command_type] = command

    def execute(self, command_type: CommandType):
        if command_type in self._commands:
            self._history.append((time(), command_type))
            self._commands[command_type].execute()
