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

def render(nodes: list, depth: int = 0) -> str:
    pad = " " * (depth * INDENT)
    lines = []
    for node in nodes:
        key = node["key"]
        kind = node["type"]
        if kind == "nested":
            body = render(node["children"], depth + 1)
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