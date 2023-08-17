from pro_filer.actions.main_actions import show_details
from unittest.mock import patch, Mock


def test_show_details_when_file_exists(capsys):
    context = {"base_path": "/home/teste/python/arquivo_teste.py"}
    mock_exists = Mock(return_value=True)
    mock_getsize = Mock(return_value=100)
    mock_isdir = Mock(return_value=False)
    mock_splitext = Mock(return_value=("arquivo_teste", ".py"))
    mock_getmtime = Mock(return_value=1672521600.0)

    patch_list = [
        patch("os.path.exists", mock_exists),
        patch("os.path.getsize", mock_getsize),
        patch("os.path.isdir", mock_isdir),
        patch("os.path.splitext", mock_splitext),
        patch("os.path.getmtime", mock_getmtime),
    ]

    with patch_list[0], patch_list[1], patch_list[2], patch_list[
        3
    ], patch_list[4]:
        show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        "File name: arquivo_teste.py\n"
        "File size in bytes: 100\n"
        "File type: file\n"
        "File extension: .py\n"
        "Last modified date: 2022-12-31\n"
    )

    assert captured.out == expected_output


def test_show_details_when_file_have_no_extension(capsys):
    context = {"base_path": "/home/teste/python/arquivo_teste"}
    mock_exists = Mock(return_value=True)
    mock_getsize = Mock(return_value=100)
    mock_isdir = Mock(return_value=False)
    mock_splitext = Mock(return_value=("arquivo_teste", ""))
    mock_getmtime = Mock(return_value=1672521600.0)

    patch_list = [
        patch("os.path.exists", mock_exists),
        patch("os.path.getsize", mock_getsize),
        patch("os.path.isdir", mock_isdir),
        patch("os.path.splitext", mock_splitext),
        patch("os.path.getmtime", mock_getmtime),
    ]

    with patch_list[0], patch_list[1], patch_list[2], patch_list[
        3
    ], patch_list[4]:
        show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        "File name: arquivo_teste\n"
        "File size in bytes: 100\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2022-12-31\n"
    )

    assert captured.out == expected_output


def test_show_details_when_file_dont_exists(capsys):
    context = {"base_path": "/home/teste/python/invalid.py"}
    mock_exists = Mock(return_value=False)

    with patch("os.path.exists", mock_exists):
        show_details(context)
    captured = capsys.readouterr()
    expected_output = "File 'invalid.py' does not exist\n"

    assert captured.out == expected_output
