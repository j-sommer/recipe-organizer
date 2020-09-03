from app import main
from gui.app_window import AppWindow


def test_app_initialization(mocker):
    # Given
    mock_app_window = mocker.patch.object(AppWindow, "__init__", return_value=None)
    # When
    main()

    # Then
    mock_app_window.assert_called_once()
