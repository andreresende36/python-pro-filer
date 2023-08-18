from pro_filer.actions.main_actions import show_disk_usage
from os.path import getsize
import math


def test_show_usage_with_existent_files(tmp_path, capsys):
    file_contents = [
        "File content 1",
        "File big content 2",
    ]
    file_paths = []
    for i, content in enumerate(file_contents, start=1):
        file_path = tmp_path / f"test_file{i}.txt"
        file_path.write_text(content)
        file_paths.append(str(file_path))
    context = {"all_files": file_paths}
    # files_sizes = [2500, 5000]
    # side_effect_list = files_sizes * 2 + list(reversed(files_sizes))
    # mock_getsize = Mock(side_effect=side_effect_list)
    # with patch("os.path.getsize", mock_getsize):
    show_disk_usage(context)

    captured = capsys.readouterr()
    size1 = getsize(file_paths[1])
    size2 = getsize(file_paths[0])
    total_size = getsize(file_paths[1]) + getsize(file_paths[0])
    expected_output = (
        "'/tmp/pytest-of-andreresende..."
        "with_existent_0/test_file2.txt':".ljust(71)
        + f"{size1} ({math.floor(size1 * 100/total_size)}%)\n"
        "'/tmp/pytest-of-andreresende..."
        "with_existent_0/test_file1.txt':".ljust(80)
        + f"{size2} ({math.floor(size2 * 100/total_size)}%)\n"
        f"Total size: {total_size}\n"
    )

    assert captured.out == expected_output


def test_show_usage_with_no_files(capsys):
    context = {"all_files": []}

    show_disk_usage(context)

    captured = capsys.readouterr()
    expected_output = "Total size: 0\n"

    assert captured.out == expected_output
