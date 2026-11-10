import json

import yaml


def load_json(path: str) -> dict:
    with open(path) as f:
        return json.load(f)
    
def load_yaml(path: str) -> dict:
    with open(path) as f:
        return yaml.load(f, Loader=yaml.SafeLoader)
    
def load_file(path: str) -> dict:
    if path.endswith(".json"):
        return load_json(path)
    if path.endswith(".yml"):
        return load_yaml(path)
    if path.endswith(".yaml"):
        return load_yaml(path)
    raise ValueError(f"Formato no soportado: {path}")