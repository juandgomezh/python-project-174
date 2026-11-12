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
    
def test_verificar_diferencias_yaml():
    file1 = FIXTURES / "file1.yml"
    file2 = FIXTURES / "file2.yml"
    expected = (FIXTURES / "expected_flat.txt").read_text().rstrip("\n")

    assert generate_diff(str(file1), str(file2)) == expected
    

def test_verificar_archivo_inexistente():
    inexistente = FIXTURES / "no_existe.json"
    file2 = FIXTURES / "file2.json"

    with pytest.raises(FileNotFoundError):
        generate_diff(str(inexistente), str(file2))
        

def test_verificar_valor_null():
    archivo1 = FIXTURES / "null_1.json"
    archivo2 = FIXTURES / "null_2.json"
    esperado = (FIXTURES / "expected_null.txt").read_text().rstrip("\n")

    assert generate_diff(str(archivo1), str(archivo2)) == esperado
    
def test_verificar_formato_no_soportado():
    archivo1 = FIXTURES / "file1.txt"
    archivo2 = FIXTURES / "file2.json"

    with pytest.raises(ValueError, match="Formato no soportado"):
        generate_diff(str(archivo1), str(archivo2))