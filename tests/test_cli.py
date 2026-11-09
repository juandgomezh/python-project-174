import sys
from pathlib import Path

from gendiff.scripts.gendiff import main

FIXTURES = Path(__file__).parent / "fixtures"

def test_cli_muestra_diferencias(monkeypatch, capsys):
    archivo1 = FIXTURES / "file1.json"
    archivo2 = FIXTURES / "file2.json"
    esperado = (FIXTURES / "expected_flat.txt").read_text().rstrip("\n")

    monkeypatch.setattr(sys, "argv", ["gendiff", str(archivo1), str(archivo2)])
    main()
    captura= capsys.readouterr()
    assert captura.out.rstrip("\n") == esperado