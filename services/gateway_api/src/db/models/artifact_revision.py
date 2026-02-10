from dataclasses import dataclass

@dataclass
class ArtifactRevisionModel:
    id: str
    artifact_id: str
    revision: int
