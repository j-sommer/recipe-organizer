from app import main


def test_app_initialization(mocker):
    # Given
    mocker.patch("builtins.print")

    # When
    main()

    # Then
    print.assert_called_once()
