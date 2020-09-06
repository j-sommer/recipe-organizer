import tkinter

from gui.app_window import AppWindow
from gui.recipe_selection.recipe_selection import RecipeSelection


def test_app_window_initialization(mocker):
    # Given
    mocker.patch.object(tkinter.Tk, "__init__", return_value=None)
    mock_title = mocker.patch.object(tkinter.Tk, "title", return_value=None)
    mock_state = mocker.patch.object(tkinter.Tk, "state", return_value=None)
    mock_min_size = mocker.patch.object(tkinter.Tk, "minsize", return_value=None)
    mock_main_loop = mocker.patch.object(tkinter.Tk, "mainloop", return_value=None)

    mock_recipe_selection = mocker.patch.object(RecipeSelection, "__init__", return_value=None)

    # When
    AppWindow()

    # Then
    mock_title.assert_called_once_with("Ingredient Extractor")
    mock_state.assert_called_once_with("zoomed")
    mock_min_size.assert_called_once_with(300, 200)
    mock_recipe_selection.assert_called_once()
    mock_main_loop.assert_called_once()
