from commands.command import Command, CommandType
from gui.recipe_form.recipe_form import RecipeForm
from gui.recipe_selection.recipe_selection import RecipeSelection
from recipe.recipe import Recipe


class CommandSave(Command):

    @property
    def command_type(self) -> CommandType:
        return CommandType.SAVE

    def __init__(self, recipe_form: RecipeForm, recipe_selection: RecipeSelection):
        self._recipe_form = recipe_form
        self._recipe_selection = recipe_selection

    def execute(self) -> None:
        recipe: Recipe = self._recipe_form.get_recipe_from_form()
        self._recipe_selection.save_recipe_to_file(recipe)
