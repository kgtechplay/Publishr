from pydantic import BaseModel

class ResearchCompleted(BaseModel):
    run_id: str

class DraftCompleted(BaseModel):
    run_id: str

class AssetGenerated(BaseModel):
    run_id: str
    asset_type: str

class PublishCompleted(BaseModel):
    run_id: str
    destination: str
