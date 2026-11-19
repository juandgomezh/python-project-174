def format_value(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def render(nodes, path=""):
    lines = []
    for node in nodes:
        name = f"{path}.{node['key']}" if path else node["key"]
        kind = node["type"]
        if kind == "nested":
            lines.append(render(node["children"], name))
        elif kind == "added":
            lines.append(
                f"Property '{name}' was added with value: "
                f"{format_value(node['value'])}"
            )
        elif kind == "deleted":
            lines.append(f"Property '{name}' was removed")
        elif kind == "changed":
            lines.append(
                f"Property '{name}' was updated. "
                f"From {format_value(node['old'])} to {format_value(node['new'])}"
            )
    return "\n".join(line for line in lines if line)
