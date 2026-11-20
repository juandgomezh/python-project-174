import json


def render(nodes: list) -> str:
    return json.dumps(nodes, indent=2, ensure_ascii=False)
