# 🔍 Calculadora de diferencias

[![hexlet-check](https://github.com/juandgomezh/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/juandgomezh/python-project-174/actions)

## 📌 Descripción del proyecto

La calculadora de diferencias (`gendiff`) es una herramienta de línea de comandos y una librería de Python que compara dos archivos de configuración y muestra qué claves se agregaron, se eliminaron o cambiaron.

Por ahora trabaja con archivos JSON planos. Las claves se muestran ordenadas alfabéticamente y cada línea lleva una marca que indica qué ocurrió con ella.

Acerca del diseño…

El proyecto separa la lectura de archivos (`gendiff/parser.py`), la lógica de comparación (`gendiff/diff.py`) y la interfaz de terminal (`gendiff/scripts/gendiff.py`), de modo que cada parte se pueda probar y ampliar por separado.

La finalidad...

El objetivo es practicar estructuras de datos (diccionarios, conjuntos y listas), lectura de archivos, empaquetado con Poetry, pruebas con pytest y automatización con GitHub Actions.

---

## 📦 Requisitos mínimos

- Python >= 3.10
- Poetry (gestor de dependencias y empaquetado)

---

## 🚀 Instalación

```bash
git clone https://github.com/juandgomezh/python-project-174.git
cd python-project-174
make install
```

Otros comandos disponibles:

```bash
make lint    # revisa el estilo con ruff
make build   # genera el paquete en dist/
```

---

## 🧪 Uso

```bash
poetry run gendiff file1.json file2.json
```

Con estos archivos:

`file1.json`

```json
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}
```

`file2.json`

```json
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
```

la salida es:

```text
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

| Marca | Significado |
|---|---|
| `-` | la clave estaba solo en el primer archivo, o su valor cambió |
| `+` | la clave está solo en el segundo archivo, o es el valor nuevo |
| (sin marca) | la clave y su valor son iguales en ambos archivos |

También se puede usar desde Python:

```python
from gendiff import generate_diff

print(generate_diff("file1.json", "file2.json"))
```

---

## 🎬 Demostraciones

### Ayuda del comando

[![Ayuda de gendiff](https://asciinema.org/a/5LyACZVIctsuq3ie.svg)](https://asciinema.org/a/5LyACZVIctsuq3ie)

### Comparación de archivos JSON planos

[![Comparación de JSON planos](https://asciinema.org/a/AsrysAXwv4AkGuTQ.svg)](https://asciinema.org/a/AsrysAXwv4AkGuTQ)

---

## ✅ Pruebas

```bash
poetry run pytest --cov=gendiff --cov-report=term-missing
```

---

<details>
<summary>Pruebas automáticas de Códica</summary>

Las pruebas...

</details>
