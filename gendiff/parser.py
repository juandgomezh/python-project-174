import json


def load_json(path: str) -> dict:
    with open(path) as f:
        return json.load(f)
    
    