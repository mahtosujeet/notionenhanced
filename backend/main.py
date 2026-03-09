from fastapi import FastAPI
from response_models.checkhealth import CheckHealthResponse

app = FastAPI()


@app.get("/checkhealth", response_model=CheckHealthResponse)
def read_root():
    return {"msg": "Server is running."}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
