from datetime import datetime,timezone
from typing import Optional

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    google_user_id: str = Field(index=True)
    email: str

    drive_refresh_token: str
    drive_access_token: str

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
