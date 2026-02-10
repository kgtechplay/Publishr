from pydantic import BaseModel

class VideoAsset(BaseModel):
    type: str = 'video'
    content: str
