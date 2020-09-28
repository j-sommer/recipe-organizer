from unittest.mock import patch

from gui.recipe_form.recipe_form import RecipeForm
from recipe.ingredient.ingredient import Ingredient
from recipe.recipe import Recipe

module_path = "gui.recipe_form.recipe_form"


def test_recipe_form_initialization():
    # Given
    with patch(f"{module_path}.Label"), \
         patch(f"{module_path}.Entry"), \
         patch(f"{module_path}.Frame"):
        # When
        recipe_form = RecipeForm()

        # Then
        assert recipe_form


def test_recipe_handling():
    # Given
    with patch(f"{module_path}.IngredientForm") as mock_ingredient_form, \
            patch(f"{module_path}.Entry") as mock_entry:
        ingredients = [Ingredient("ingredientA", "g", 50), Ingredient("ingredientB", "g", 50)]
        recipe = Recipe("title", [], ingredients, "preparation")

        expected_ingredient_form_count = len(ingredients)
        expected_preparation_entries_count = 1

        patch.object(RecipeForm, "__init__", return_value=None)
        recipe_form = RecipeForm()

        # When
        recipe_form.set_values(recipe)

        # Then
        assert mock_entry.call_count == expected_preparation_entries_count
        assert mock_ingredient_form.call_count == expected_ingredient_form_count
