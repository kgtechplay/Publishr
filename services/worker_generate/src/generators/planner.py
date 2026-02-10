def plan_generation(requested: list[str] | None = None) -> list[str]:
    return requested or ["linkedin", "x", "blog", "video", "animation"]
