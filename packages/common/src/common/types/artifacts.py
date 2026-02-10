from pydantic import BaseModel

class Artifact(BaseModel):
    id: str
    run_id: str
    type: str
    content: str
