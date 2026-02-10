class LLMClient:
    def complete(self, prompt: str) -> str:
        return f"Mock completion for: {prompt[:50]}"
