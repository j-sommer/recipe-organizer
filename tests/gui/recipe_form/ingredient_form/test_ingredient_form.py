from unittest.mock import patch

from gui.recipe_form.ingredient_form.ingredient_form import IngredientForm
from recipe.ingredient.ingredient import Ingredient

module_path = "gui.recipe_form.ingredient_form.ingredient_form"


def test_ingredient_form_initialization():
    # Given
    ingredient = Ingredient("name", "type", 42)
    parent = None

    expected_entries_count = 3

    with patch(f"{module_path}.Frame"), \
         patch(f"{module_path}.Entry") as mock_entry:
        # When
        ingredient_form = IngredientForm(parent, ingredient)

        # Then
        assert ingredient_form
        assert mock_entry.call_count == expected_entries_count
