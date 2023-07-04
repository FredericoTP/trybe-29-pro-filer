from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files_exception():
    context_exception = {"all_files": ["a.py", "b.py"]}
    with pytest.raises(ValueError):
        find_duplicate_files(context_exception)


def test_find_duplicate_files_no_duplicates():
    context_no_duplicates = {"all_files": []}
    result = find_duplicate_files(context_no_duplicates)
    assert result == []


def test_find_duplicate_files_duplicated(tmp_path):
    output_path_one = tmp_path / "a"
    output_path_two = tmp_path / "b"
    output_path_three = tmp_path / "air.txt"
    output_path_one.mkdir()
    output_path_two.mkdir()
    output_path_three.touch()
    output_path_three.write_text("a")
    text_one = output_path_one / "water.txt"
    text_two = output_path_two / "water.txt"
    text_one.touch()
    text_two.touch()

    context_duplicates = {
        "all_files": [
            str(text_one),
            str(text_two),
            str(output_path_three),
        ]
    }

    result = find_duplicate_files(context_duplicates)
    assert len(result) == 1
    assert "water.txt" in result[0][0]
    assert "water.txt" in result[0][1]
