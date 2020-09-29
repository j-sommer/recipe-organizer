from unittest import mock
from unittest.mock import patch, mock_open

from pytest import fixture

from gui.recipe_selection.recipe_selection import RecipeSelection
from recipe.events.recipe_event import RecipeEvent, RecipeEventType
from recipe.recipe import Recipe

module_path = "gui.recipe_selection.recipe_selection"


@fixture(autouse=True)
def mocks():
    with patch(f"{module_path}.Label", autospec=True) as mock_label, \
            patch(f"{module_path}.Button", autospec=True) as mock_button, \
            patch(f"{module_path}.RecipeEventPublisher", autospec=True) as mock_event_publisher, \
            patch(f"{module_path}.filedialog", autospec=True) as mock_filedialog, \
            patch(f"{module_path}.Recipe", autospec=True) as mock_recipe, \
            patch(f"{module_path}.Frame", autospec=True) as mock_frame:
        yield {"mock_label": mock_label, "mock_button": mock_button, "mock_event_publisher": mock_event_publisher,
               "mock_frame": mock_frame, "mock_filedialog": mock_filedialog, "mock_recipe": mock_recipe}


def test_recipe_selection_initialization(mocks):
    # Given
    label_instance = mocks["mock_label"].return_value
    button_instance = mocks["mock_button"].return_value

    # When
    recipe_selection = RecipeSelection()

    # Then - label and button should have been placed
    assert recipe_selection
    button_instance.grid.assert_called_once()
    label_instance.grid.assert_called_once()
    mocks["mock_event_publisher"].add.assert_called_once_with(recipe_selection)


def test_save_event_handling(mocks):
    # Given
    recipe_selection = RecipeSelection()
    recipe_selection._selected_recipe_file = "path/to/file"

    recipe = Recipe("title", [], [], "preparation")
    recipe_event = RecipeEvent(event_type=RecipeEventType.SAVE, payload=recipe)

    with patch("builtins.open", mock_open(read_data="content")) as mock_file_open:
        file_instance = mock_file_open()
        # When
        recipe_selection.notify(recipe_event)

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
        recipe_selection.open_selection_dialog()

        # Then
        mock_file_open.assert_called_once_with(mock_path, mock.ANY)
        mocks["mock_event_publisher"].broadcast.assert_called_once()
