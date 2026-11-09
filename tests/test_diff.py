from pathlib import Path

import pytest

from gendiff import generate_diff

# raiz
FIXTURES = Path(__file__).parent / "fixtures"


def test_verificar_diferencias_json():
    file1 = FIXTURES / "file1.json"
    file2 = FIXTURES / "file2.json"
    expected = (FIXTURES / "expected_flat.txt").read_text().rstrip("\n")

    assert generate_diff(str(file1), str(file2)) == expected
    
def test_verificar_archivo_inexistente():
    inexistente = FIXTURES / "no_existe.json"
    file2 = FIXTURES / "file2.json"

    with pytest.raises(FileNotFoundError):
        generate_diff(str(inexistente), str(file2))