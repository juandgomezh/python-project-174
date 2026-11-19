from gendiff.parser import load_file

INDENT = 4


def format_value(value, depth):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        pad = " " * (depth * INDENT + INDENT)
        lines = [
            f"{pad}{key}: {format_value(val, depth + 1)}"
            for key, val in value.items()
        ]
        closing = " " * (depth * INDENT)
        return "{\n" + "\n".join(lines) + "\n" + closing + "}"
    return str(value)


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


def render_stylish(nodes: list, depth: int = 0) -> str:
    pad = " " * (depth * INDENT)
    lines = []
    for node in nodes:
        key = node["key"]
        kind = node["type"]
        if kind == "nested":
            body = render_stylish(node["children"], depth + 1)
            lines.append(f"{pad}    {key}: {body}")
        elif kind == "changed":
            old = format_value(node["old"], depth + 1)
            new = format_value(node["new"], depth + 1)
            lines.append(f"{pad}  - {key}: {old}")
            lines.append(f"{pad}  + {key}: {new}")
        else:
            marker = {"added": "+", "deleted": "-", "unchanged": " "}[kind]
            value = format_value(node["value"], depth + 1)
            lines.append(f"{pad}  {marker} {key}: {value}")
    return "{\n" + "\n".join(lines) + "\n" + pad + "}"


def generate_diff(file_path1: str, file_path2: str) -> str:
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    return render_stylish(build_diff(data1, data2))
