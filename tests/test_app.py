from unittest.mock import patch, MagicMock

from app import main
from gui.app_window import AppWindow


@patch("app.AppWindow", autospec=True)
def test_app_initialization(mock_app_window):
    # Given
    app_window_instance = MagicMock(AppWindow)
    mock_app_window.return_value = app_window_instance

    # When
    main()

    # Then
    app_window_instance.render.assert_called_once()
