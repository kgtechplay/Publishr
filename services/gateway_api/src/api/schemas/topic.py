from pydantic import BaseModel

class Topic(BaseModel):
    id: str
    title: str
    body: str
