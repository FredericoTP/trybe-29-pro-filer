from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import Mock, patch
import pytest


def test_show_details_file_not_found(capsys):
    mock_os_path_exists = Mock(return_value=False)
    fake_file_context = {"base_path": "/home/trybe/????"}

    with patch("os.path.exists", mock_os_path_exists):
        show_details(fake_file_context)
        captured = capsys.readouterr()
        assert captured.out == "File '????' does not exist\n"


@pytest.mark.parametrize(
    "context, name, size, type, extension, date",
    [
        (
            {"base_path": "/home/trybe/Downloads/Trybe_logo.png"},
            "File name: Trybe_logo.png\n",
            "File size in bytes: 100\n",
            "File type: file\n",
            "File extension: .png\n",
            "Last modified date: 2019-05-21\n",
        ),
    ],
)
def test_show_details_file_found(
    capsys, context, name, size, type, extension, date
):
    mock_os_path_exists = Mock(return_value=True)
    mock_os_path_getsize = Mock(return_value=100)
    mock_os_path_isdir = Mock(return_value=False)
    mock_os_path_splitext = Mock(return_value=("Trybe_logo", ".png"))
    mock_os_path_getmtime = Mock(return_value=1558447897.0442736)

    with (
        patch("os.path.exists", mock_os_path_exists),
        patch("os.path.getsize", mock_os_path_getsize),
        patch("os.path.isdir", mock_os_path_isdir),
        patch("os.path.splitext", mock_os_path_splitext),
        patch("os.path.getmtime", mock_os_path_getmtime),
    ):
        show_details(context)
        captured = capsys.readouterr()
        assert name in captured.out
        assert size in captured.out
        assert type in captured.out
        assert extension in captured.out
        assert date in captured.out


@pytest.mark.parametrize(
    "context, name, size, type, extension, date",
    [
        (
            {"base_path": "/home/trybe/Downloads"},
            "File name: Downloads\n",
            "File size in bytes: 500\n",
            "File type: directory\n",
            "File extension: [no extension]\n",
            "Last modified date: 2019-05-21\n",
        ),
    ],
)
def test_show_details_directory_found(
    capsys, context, name, size, type, extension, date
):
    mock_os_path_exists = Mock(return_value=True)
    mock_os_path_getsize = Mock(return_value=500)
    mock_os_path_isdir = Mock(return_value=True)
    mock_os_path_splitext = Mock(return_value=("Downloads", ""))
    mock_os_path_getmtime = Mock(return_value=1558447897.0442736)

    with (
        patch("os.path.exists", mock_os_path_exists),
        patch("os.path.getsize", mock_os_path_getsize),
        patch("os.path.isdir", mock_os_path_isdir),
        patch("os.path.splitext", mock_os_path_splitext),
        patch("os.path.getmtime", mock_os_path_getmtime),
    ):
        show_details(context)
        captured = capsys.readouterr()
        assert name in captured.out
        assert size in captured.out
        assert type in captured.out
        assert extension in captured.out
        assert date in captured.out
