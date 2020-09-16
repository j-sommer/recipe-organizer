from unittest.mock import patch

from gui.recipe_form.recipe_form import RecipeForm
from recipe.ingredient.ingredient import Ingredient
from recipe.recipe import Recipe

module_path = "gui.recipe_form.recipe_form"


def test_recipe_form_initialization():
    # Given
    with patch(f"{module_path}.Label") as mock_label, \
            patch(f"{module_path}.Entry") as mock_entry, \
            patch(f"{module_path}.Frame") as mock_frame:
        label_instance = mock_label.return_value
        entry_instance = mock_entry.return_value
        frame_instance = mock_frame.return_value

        # When
        recipe_form = RecipeForm()

        # Then
        assert recipe_form
        label_instance.grid.assert_called_once()
        entry_instance.grid.assert_called_once()
        frame_instance.grid.assert_called_once()


def test_recipe_handling():
    # Given
    with patch(f"{module_path}.Entry") as mock_entry:
        ingredients = [Ingredient("ingredientA", "g", 50), Ingredient("ingredientB", "g", 50)]
        recipe = Recipe("title", [], ingredients, "preparation")

        expected_ingredient_entries_count = len(ingredients) * 3
        expected_preparation_entries_count = 1

        patch.object(RecipeForm, "__init__", return_value=None)
        recipe_form = RecipeForm()

        # When
        recipe_form.set_values(recipe)

        # Then
        assert mock_entry.call_count == expected_ingredient_entries_count + expected_preparation_entries_count
