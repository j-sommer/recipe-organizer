import tkinter
from tkinter import filedialog
from unittest import mock
from unittest.mock import patch, mock_open

from gui.recipe_selection.recipe_selection import RecipeSelection
from recipe.recipe import Recipe


def test_recipe_selection_initialization(mocker):
    # Given
    mock_parent = None
    mocker.patch.object(tkinter.Label, "__init__", return_value=None)
    mocker.patch.object(tkinter.Button, "__init__", return_value=None)

    mock_label_grid = mocker.patch.object(tkinter.Label, "grid", return_value=None)
    mock_button_grid = mocker.patch.object(tkinter.Button, "grid", return_value=None)

    # When
    recipe_selection = RecipeSelection(mock_parent)

    # Then - label and button should have been placed
    assert recipe_selection
    mock_label_grid.assert_called_once()
    mock_button_grid.assert_called_once()


def test_recipe_selection_file_deserialization(mocker):
    # Given
    mock_path = "/path/to/json"
    mock_recipe = Recipe("title", [], [], "preparation")

    mock_parent = None
    mocker.patch.object(tkinter.Label, "__init__", return_value=None)
    mocker.patch.object(tkinter.Button, "__init__", return_value=None)

    mocker.patch.object(tkinter.Label, "grid", return_value=None)
    mocker.patch.object(tkinter.Button, "grid", return_value=None)

    mocker.patch.object(filedialog, "askopenfilename", return_value=mock_path)

    mocker.patch.object(Recipe, "from_json", return_value=mock_recipe)

    with patch("builtins.open", mock_open(read_data="content")) as mock_file_open:
        recipe_selection = RecipeSelection(mock_parent)

        # When
        recipe_selection.open_selection_dialog()

        # Then
        mock_file_open.assert_called_once_with(mock_path, mock.ANY)
