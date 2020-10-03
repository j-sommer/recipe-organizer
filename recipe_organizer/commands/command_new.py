from recipe_organizer.commands.command import Command, CommandType
from recipe_organizer.gui.recipe_form.recipe_form import RecipeForm


class CommandNew(Command):

    @property
    def command_type(self) -> CommandType:
        return CommandType.NEW

    def __init__(self, recipe_form: RecipeForm):
        self._recipe_form = recipe_form

    def execute(self) -> None:
        self._recipe_form.clear_form()
