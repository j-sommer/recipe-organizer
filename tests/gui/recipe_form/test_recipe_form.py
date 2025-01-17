from tkinter import Frame
from unittest.mock import patch, MagicMock

import pytest
from pytest import fixture

from recipe_organizer.gui.recipe_form.recipe_form import RecipeForm
from recipe_organizer.recipe.ingredient.ingredient import Ingredient
from recipe_organizer.recipe.recipe import Recipe

module_path = "recipe_organizer.gui.recipe_form.recipe_form"


@fixture(autouse=True)
def mocks():
    with patch(f"{module_path}.Label") as mock_label, \
            patch(f"{module_path}.Entry") as mock_entry, \
            patch(f"{module_path}.Button") as mock_button, \
            patch(f"{module_path}.IngredientForm") as mock_ingredient_form, \
            patch(f"{module_path}.Frame") as mock_frame:
        yield {"mock_label": mock_label, "mock_entry": mock_entry, "mock_button": mock_button, "mock_frame": mock_frame,
               "mock_ingredient_form": mock_ingredient_form}


@pytest.mark.skip(reason="restructuring initialization")
def test_recipe_form_initialization(mocks):
    # Given
    parent = None

    # When
    recipe_form = RecipeForm(parent)

    # Then
    assert recipe_form


@pytest.mark.skip(reason="restructuring initialization")
def test_recipe_handling(mocks):
    # Given
    parent = None

    ingredients = [Ingredient("ingredientA", "g", 50), Ingredient("ingredientB", "g", 50)]
    recipe = Recipe("title", [], ingredients, "preparation")

    expected_ingredient_form_count = len(ingredients)
    expected_preparation_entries_count = 1

    patch.object(RecipeForm, "__init__", return_value=None)
    recipe_form = RecipeForm(parent)

    # When
    recipe_form.set_form_values(recipe)

    # Then
    assert mocks["mock_entry"].call_count == expected_preparation_entries_count
    assert mocks["mock_ingredient_form"].call_count == expected_ingredient_form_count


@pytest.mark.skip(reason="restructuring initialization")
def test_add_ingredient(mocks):
    # Given
    recipe_form = RecipeForm()
    recipe_form._frame_ingredients = MagicMock(Frame)
    recipe_form._ingredient_forms = []

    # When
    recipe_form._RecipeForm__add_ingredient()

    # Then
    assert len(recipe_form._ingredient_forms) == 1
