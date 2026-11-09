from pathlib import Path

from gendiff import generate_diff

# raiz
FIXTURES = Path(__file__).parent / "fixtures"


def test_generate_diff_flat_json():
    file1 = FIXTURES / "file1.json"
    file2 = FIXTURES / "file2.json"
    expected = (FIXTURES / "expected_flat.txt").read_text().rstrip("\n")

    assert generate_diff(str(file1), str(file2)) == expected