def preflight(destination: str, artifact_type: str, capabilities: dict) -> bool:
    return artifact_type in capabilities.get(destination, {}).get("types", [])
