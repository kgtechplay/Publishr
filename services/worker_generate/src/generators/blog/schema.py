from pydantic import BaseModel

class BlogAsset(BaseModel):
    type: str = 'blog'
    content: str
