from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import json
from pro_filer.cli_helpers import _get_printable_file_path


def generate_output(content, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(content))


def test_show_disk_usage_without_files(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_usage_files(tmp_path, capsys):
    content_one = {"esporte": "futebol"}
    constent_two = {
        "esporte": "futebol",
        "comida": "sorvete",
        "filme": "interestelar",
    }
    output_path_one = tmp_path / "one.json"
    output_path_two = tmp_path / "two.json"

    generate_output(content_one, output_path_one)
    generate_output(constent_two, output_path_two)

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
        == f"{output_two} 68 (75%)\n\
{output_one} 22 (24%)\nTotal size: 90\n"
    )
