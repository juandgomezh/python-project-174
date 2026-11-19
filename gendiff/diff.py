from gendiff.parser import load_file
from gendiff.formatters.stylish import render_stylish

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


def generate_diff(file_path1: str, file_path2: str) -> str:
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    return render_stylish(build_diff(data1, data2))
