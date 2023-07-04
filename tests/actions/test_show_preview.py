from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, first_result, second_result, third_result",
    [
        (
            {
                "all_files": ["a", "b"],
                "all_dirs": [],
            },
            "Found 2 files and 0 directories",
            "First 5 files: ['a', 'b']",
            "First 5 directories: []",
        ),
        (
            {
                "all_files": [],
                "all_dirs": ["a", "b"],
            },
            "Found 0 files and 2 directories",
            "First 5 files: []",
            "First 5 directories: ['a', 'b']",
        ),
        (
            {
                "all_files": ["a", "b", "c", "d", "e", "f"],
                "all_dirs": ["a", "b", "c", "d", "e", "f"],
            },
            "Found 6 files and 6 directories",
            "First 5 files: ['a', 'b', 'c', 'd', 'e']",
            "First 5 directories: ['a', 'b', 'c', 'd', 'e']",
        ),
    ],
)
def test_show_preview_possibilities(
    capsys, context, first_result, second_result, third_result
):
    show_preview(context)
    captured = capsys.readouterr()
    assert first_result in captured.out
    assert second_result in captured.out
    assert third_result in captured.out


def test_show_preview_arguments_empty(capsys):
    show_preview({"all_files": [], "all_dirs": []})
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"


def test_show_preview_error():
    with pytest.raises(TypeError):
        show_preview()

    with pytest.raises(KeyError):
        show_preview({})
