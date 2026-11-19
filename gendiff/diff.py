from gendiff.formatters.stylish import render
from gendiff.parser import load_file

FORMATTERS = {"stylish": render}

def build_diff(data1: dict, data2: dict) -> list:
    nodes = []
    for key in sorted(data1.keys() | data2.keys()):
        if key not in data2:
            nodes.append({"key": key, "type": "deleted", "value": data1[key]})
        elif key not in data1:
            nodes.append({"key": key, "type": "added", "value": data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            nodes.append({
                "key": key,
                "type": "nested",
                "children": build_diff(data1[key], data2[key]),
            })
        elif data1[key] == data2[key]:
            nodes.append({"key": key, "type": "unchanged", "value": data1[key]})
        else:
            nodes.append({
                "key": key,
                "type": "changed",
                "old": data1[key],
                "new": data2[key],
            })
    return nodes


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    if format_name not in FORMATTERS:
        raise ValueError(f"Formato de salida no soportado: {format_name}")
    return FORMATTERS[format_name](build_diff(data1, data2))
