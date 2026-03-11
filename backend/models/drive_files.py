from typing import Optional

from sqlmodel import SQLModel, Field


class DriveFile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    drive_link: str
    file_hash: str = Field(index=True)
    reference_count: int = Field(default=0)
