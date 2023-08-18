from pro_filer.actions.main_actions import find_duplicate_files
import pytest


def test_find_duplicate_files_with_valid_files(tmp_path):
    file_paths = []
    for i in range(1, 5):
        file_paths.append(tmp_path / f"arquivo{i}.txt")
    context = {"all_files": [str(file) for file in file_paths]}
    for j in range(0, 3):
        file_paths[j].write_text("Texto igual!")
    file_paths[3].write_text("Texto diferente!")

    [file_path1, file_path2, file_path3, _file_path4] = context["all_files"]
    duplicate_files = find_duplicate_files(context)
    expected_output = [
        (file_path1, file_path2),
        (file_path1, file_path3),
        (file_path2, file_path3),
    ]

    assert duplicate_files == expected_output


def test_find_duplicate_files_with_not_found_file(tmp_path):
    file_paths = []
    for i in range(1, 5):
        file_paths.append(tmp_path / f"arquivo{i}.txt")
    context = {
        "all_files": [str(file) for file in file_paths]
    }
    context["all_files"].append(str(tmp_path / "arquivo_inexistente.txt"))
    for j in range(0, 4):
        file_paths[j].write_text("Texto igual!")

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
