from pydantic import BaseModel

class Asset(BaseModel):
    id: str
    kind: str
    uri: str | None = None
