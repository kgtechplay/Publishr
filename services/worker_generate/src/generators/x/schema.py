from pydantic import BaseModel

class XAsset(BaseModel):
    type: str = 'x'
    content: str
