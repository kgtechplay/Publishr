def next_delay(attempt: int) -> int:
    return min(60, 2 ** attempt)
