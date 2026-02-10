def validate_content(text: str) -> list[str]:
    violations = []
    if "forbidden" in text.lower():
        violations.append("Contains forbidden term")
    return violations
