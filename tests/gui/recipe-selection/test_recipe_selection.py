import tkinter

from gui.recipe_selection.recipe_selection import RecipeSelection


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
