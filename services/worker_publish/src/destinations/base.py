from abc import ABC, abstractmethod

class DestinationPlugin(ABC):
    @abstractmethod
    def publish(self, artifact: dict) -> dict: ...
