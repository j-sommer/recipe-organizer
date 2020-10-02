from unittest import mock
from unittest.mock import patch, mock_open

from pytest import fixture

from gui.recipe_selection.recipe_selection import RecipeSelection
from recipe.recipe import Recipe

module_path = "gui.recipe_selection.recipe_selection"


@fixture(autouse=True)
def mocks():
    with patch(f"{module_path}.EventPublisher", autospec=True) as mock_event_publisher, \
            patch(f"{module_path}.filedialog", autospec=True) as mock_filedialog, \
            patch(f"{module_path}.Recipe", autospec=True) as mock_recipe:
        yield {"mock_event_publisher": mock_event_publisher, "mock_filedialog": mock_filedialog,
               "mock_recipe": mock_recipe}


def test_save_event_handling(mocks):
    # Given
    recipe_selection = RecipeSelection()
    recipe_selection._selected_recipe_file = "path/to/file"

    recipe = Recipe("title", [], [], "preparation")

    with patch("builtins.open", mock_open(read_data="content")) as mock_file_open:
        file_instance = mock_file_open()
        # When
        recipe_selection.write_recipe_to_file(recipe)

        # Then
        file_instance.write.assert_called_once()


def test_recipe_selection_file_deserialization(mocks):
    # Given
    mock_path = "/path/to/json"

    recipe = Recipe("title", [], [], "preparation")
    mocks["mock_recipe"].from_json.return_value = recipe

    mocks["mock_filedialog"].askopenfilename.return_value = mock_path

    with patch("builtins.open", mock_open(read_data="content")) as mock_file_open:
        recipe_selection = RecipeSelection()

        # When
        recipe_selection.open_recipe()

        # Then
        mock_file_open.assert_called_once_with(mock_path, mock.ANY)
        mocks["mock_event_publisher"].broadcast.assert_called_once()
