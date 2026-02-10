from dataclasses import dataclass

@dataclass
class PublishJobModel:
    id: str
    run_id: str
    destination: str
    status: str
