def send_to_dead_letter(message: dict) -> dict:
    return {"dead_lettered": True, "message": message}
