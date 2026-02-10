from pydantic import BaseModel

class AnimationAsset(BaseModel):
    type: str = 'animation'
    content: str
