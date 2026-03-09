from pydantic import BaseModel

class CheckHealthResponse(BaseModel):
    msg: str
