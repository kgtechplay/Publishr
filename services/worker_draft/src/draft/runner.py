def create_draft(topic: str, research: dict, user_feedback: str = "") -> dict:
    return {"topic": topic, "research": research, "feedback": user_feedback, "draft": "Initial draft body"}
