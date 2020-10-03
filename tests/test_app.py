from unittest.mock import patch, MagicMock

from recipe_organizer.app import main
from recipe_organizer.gui.app_window import AppWindow


@patch("recipe_organizer.app.AppWindow", autospec=True)
def test_app_initialization(mock_app_window):
    # Given
    app_window_instance = MagicMock(AppWindow)
    mock_app_window.return_value = app_window_instance

    # When
    main()

    # Then
    app_window_instance.render.assert_called_once()
