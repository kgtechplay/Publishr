def publish(payload: dict) -> dict:
    return {'destination': 'substack', 'status': 'posted', 'payload': payload}
