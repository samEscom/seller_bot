from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class HealthOpenAiResponse(BaseModel):
    status: str
    model_count: int
