from pydantic import BaseModel

class LinkedinAsset(BaseModel):
    type: str = 'linkedin'
    content: str
