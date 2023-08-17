from pro_filer.actions.main_actions import show_preview  # NOQA

# import pytest


def test_empty_files_dirs_lists(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()  # Captura a saída
    output = captured.out
    assert output.replace("\n", "") == "Found 0 files and 0 directories"


def test_max_number_files(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/utils/calc.py",
            "src/utils/counter.py",
            "src/utils/parser.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    show_preview(context)
    captured = capsys.readouterr()  # Captura a saída
    output = captured.out
    files = (
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py', "
        "'src/utils/calc.py', "
        "'src/utils/counter.py']\n"
    )
    assert output == (
        "Found 6 files and 2 directories\n"
        + files
        + "First 5 directories: ['src', 'src/utils']\n"
    )
