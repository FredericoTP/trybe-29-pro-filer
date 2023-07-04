from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path

# tmp_path --> https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html


def test_show_disk_usage_without_files(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_usage_files(tmp_path, capsys):
    content_one = "Sorvete para sobremesa"
    content_two = "Olá"
    output_path_one = tmp_path / "one.txt"
    output_path_two = tmp_path / "two.txt"
    output_path_one.touch()
    output_path_one.write_text(content_one)
    output_path_two.touch()
    output_path_two.write_text(content_two)

    context = {"all_files": [str(output_path_one), str(output_path_two)]}

    output_one = f"'{_get_printable_file_path(str(output_path_one))}':".ljust(
        70
    )
    output_two = f"'{_get_printable_file_path(str(output_path_two))}':".ljust(
        70
    )
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f"{output_one} 22 (84%)\n\
{output_two} 4 (15%)\nTotal size: 26\n"
    )
