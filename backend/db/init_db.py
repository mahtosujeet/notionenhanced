import logging

from sqlmodel import SQLModel
from .engine import engine

import models.user
import models.drive_files
import models.sync_mapping
import models.notion


logger = logging.getLogger(__name__)

def init_db():
    logger.info("Creating db tables")
    SQLModel.metadata.create_all(engine)
    logger.info("DB Tables created")

