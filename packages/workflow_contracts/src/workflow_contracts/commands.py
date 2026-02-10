from pydantic import BaseModel

class StartRun(BaseModel):
    run_id: str
    topic_id: str

class PublishRun(BaseModel):
    run_id: str
