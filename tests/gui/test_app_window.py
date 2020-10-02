from tkinter import Tk
from unittest.mock import patch, MagicMock

from gui.app_window import AppWindow
from gui.recipe_form.recipe_form import RecipeForm
from gui.recipe_selection.recipe_selection import RecipeSelection

module_path = "gui.app_window"


def test_app_window_initialization():
    # Given
    with patch(f"{module_path}.Tk", autospec=True) as mock_tkinter, \
            patch(f"{module_path}.FontManager", autospec=True), \
            patch(f"{module_path}.RecipeForm", autospec=True) as mock_recipe_form, \
            patch(f"{module_path}.RecipeSelection", autospec=True) as mock_recipe_selection:
        tk_instance = MagicMock(Tk)
        mock_tkinter.return_value = tk_instance

        recipe_form_instance = MagicMock(RecipeForm)
        mock_recipe_form.return_value = recipe_form_instance

        recipe_selection_instance = MagicMock(RecipeSelection)
        mock_recipe_selection.return_value = recipe_selection_instance

        # When
        AppWindow()

        # Then
        tk_instance.title.assert_called_once_with("Ingredient Extractor")
        tk_instance.state.assert_called_once_with("zoomed")
        tk_instance.minsize.assert_called_once_with(300, 200)

        mock_recipe_form.assert_called_once()
        mock_recipe_selection.assert_called_once()
