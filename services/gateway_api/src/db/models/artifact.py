from dataclasses import dataclass

@dataclass
class ArtifactModel:
    id: str
    run_id: str
    kind: str
    uri: str
