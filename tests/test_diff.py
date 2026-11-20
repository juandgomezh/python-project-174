import json
from pathlib import Path

import pytest

from gendiff import generate_diff
from gendiff.formatters.plain import format_value

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

@pytest.mark.parametrize("ext", ["json", "yml"])
def test_verificar_diferencias_anidadas(ext):
    archivo1 = FIXTURES / f"nested_1.{ext}"
    archivo2 = FIXTURES / f"nested_2.{ext}"
    esperado = (FIXTURES / "expected_nested.txt").read_text().rstrip("\n")

    assert generate_diff(str(archivo1), str(archivo2)) == esperado
    
def test_verificar_formato_de_salida_no_soportado():
    a = FIXTURES / "file1.json"
    with pytest.raises(ValueError, match="Formato de salida no soportado"):
        generate_diff(str(a), str(a), "xml")

def test_verificar_archivos_identicos():
    a = FIXTURES / "file1.json"
    resultado = generate_diff(str(a), str(a))
    assert "+ " not in resultado and "- " not in resultado
    assert "host: hexlet.io" in resultado
    
@pytest.mark.parametrize("ext", ["json", "yml"])
def test_verificar_formato_plain(ext):
    archivo1 = FIXTURES / f"nested_1.{ext}"
    archivo2 = FIXTURES / f"nested_2.{ext}"
    esperado = (FIXTURES / "expected_plain.txt").read_text().rstrip("\n")

    assert generate_diff(str(archivo1), str(archivo2), "plain") == esperado


def test_format_value_numero():
    assert format_value(42) == "42"


def test_formato_json_es_json_valido_y_conserva_la_estructura():
    archivo1 = FIXTURES / "nested_1.json"
    archivo2 = FIXTURES / "nested_2.json"

    resultado = json.loads(generate_diff(str(archivo1), str(archivo2), "json"))

    claves = [nodo["key"] for nodo in resultado]
    assert claves == sorted(claves)
    por_clave = {nodo["key"]: nodo for nodo in resultado}
    assert por_clave["common"]["type"] == "nested"
    assert por_clave["group2"]["type"] == "deleted"
    assert por_clave["group3"]["type"] == "added"
    assert por_clave["group1"]["type"] == "nested"
    assert "children" in por_clave["common"]


def test_formato_json_con_yaml_igual_que_con_json():
    json_out = generate_diff(
        str(FIXTURES / "nested_1.json"), str(FIXTURES / "nested_2.json"), "json"
    )
    yaml_out = generate_diff(
        str(FIXTURES / "nested_1.yml"), str(FIXTURES / "nested_2.yml"), "json"
    )
    assert json_out == yaml_out


def test_verificar_diferencias_extension_yaml():
    archivo1 = FIXTURES / "file1.yaml"
    archivo2 = FIXTURES / "file2.yaml"
    esperado = (FIXTURES / "expected_flat.txt").read_text().rstrip("\n")

    assert generate_diff(str(archivo1), str(archivo2)) == esperado
