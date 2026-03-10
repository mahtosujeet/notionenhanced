import logging

from sqlmodel import SQLModel
from .engine import engine

import models.user


logger = logging.getLogger(__name__)

def init_db():
    logger.info("Creating db tables")
    SQLModel.metadata.create_all(engine)
    logger.info("DB Tables created")

