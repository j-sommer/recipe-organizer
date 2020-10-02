from commands.command import Command, CommandType
from gui.recipe_selection.recipe_selection import RecipeSelection


class CommandOpen(Command):

    @property
    def command_type(self) -> CommandType:
        return CommandType.OPEN

    def __init__(self, recipe_selection: RecipeSelection):
        self._recipe_selection = recipe_selection

    def execute(self) -> None:
        self._recipe_selection.open_recipe()
