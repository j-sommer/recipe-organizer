from tkinter import filedialog
from unittest import mock
from unittest.mock import patch, mock_open, Mock

from gui.recipe_selection.recipe_selection import RecipeSelection
from recipe.recipe import Recipe

module_path = "gui.recipe_selection.recipe_selection"


def test_recipe_selection_initialization():
    # Given
    with patch(f"{module_path}.Label", autospec=True) as mock_label, \
            patch(f"{module_path}.Button", autospec=True) as mock_button, \
            patch(f"{module_path}.Frame", autospec=True):
        label_instance = mock_label.return_value
        button_instance = mock_button.return_value

        # When
        recipe_selection = RecipeSelection()

        # Then - label and button should have been placed
        assert recipe_selection
        button_instance.grid.assert_called_once()
        label_instance.grid.assert_called_once()


def test_set_recipe_callback():
    # Given
    patch.object(RecipeSelection, "__init__", return_value=None)

    recipe_selection = RecipeSelection()
    callback = Mock()

    # When
    recipe_selection.set_recipe_callback(callback)
    recipe_selection._on_selected_recipe()

    # Then
    callback.assert_called_once()


def test_recipe_selection_file_deserialization():
    # Given
    with patch(f"{module_path}.Label", autospec=True), \
         patch(f"{module_path}.Button", autospec=True), \
         patch(f"{module_path}.filedialog", autospec=True) as mock_filedialog, \
            patch(f"{module_path}.Recipe", autospec=True) as mock_recipe, \
            patch(f"{module_path}.Frame", autospec=True):
        mock_path = "/path/to/json"

        recipe = Recipe("title", [], [], "preparation")
        mock_recipe.from_json.return_value = recipe

        mock_filedialog.askopenfilename.return_value = mock_path

        with patch("builtins.open", mock_open(read_data="content")) as mock_file_open:
            recipe_selection = RecipeSelection()

            # When
            recipe_selection.open_selection_dialog()

            # Then
            mock_file_open.assert_called_once_with(mock_path, mock.ANY)
