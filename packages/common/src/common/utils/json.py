import json

def dumps(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False)
