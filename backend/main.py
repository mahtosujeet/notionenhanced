import logging
from fastapi import FastAPI
from config.logging_config import setup_logging
from response_models.checkhealth import CheckHealthResponse

setup_logging()
logger = logging.getLogger(__name__)
logger.info("Logger Config loaded.")

logger.info("Initializing FastAPI...")
app = FastAPI()

@app.get("/checkhealth", response_model=CheckHealthResponse)
def read_root():
    return {"msg": "Server is running."}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


logger.info("FastAPI running...")
