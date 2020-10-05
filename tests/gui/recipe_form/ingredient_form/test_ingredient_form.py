from unittest.mock import patch

from recipe_organizer.gui.interfaces.list_item_holder import ListItemHolder
from recipe_organizer.gui.recipe_form.ingredient_form.ingredient_form import IngredientForm
from recipe_organizer.recipe.ingredient.ingredient import Ingredient

module_path = "recipe_organizer.gui.recipe_form.ingredient_form.ingredient_form"


def test_ingredient_form_initialization():
    # Given
    ingredient = Ingredient("name", "type", 42)
    parent = None
    list_holder: ListItemHolder = None

    expected_entries_count = 2

    with patch(f"{module_path}.Frame"), \
        patch(f"{module_path}.QuantityType") as mock_quantity_type, \
         patch(f"{module_path}.Entry") as mock_entry:
        # When
        ingredient_form = IngredientForm(parent, ingredient, list_holder)

        # Then
        assert ingredient_form
        assert mock_entry.call_count == expected_entries_count
        assert mock_quantity_type.call_count == 1
