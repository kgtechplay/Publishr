from abc import ABC, abstractmethod

class GeneratorPlugin(ABC):
    @abstractmethod
    def generate(self, draft: dict) -> dict: ...
