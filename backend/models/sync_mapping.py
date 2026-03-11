from sqlmodel import SQLModel, Field


class SyncMapping(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    drive_link_ref: int = Field(foreign_key="drivefile.id")
    notion_block_link: str
    workspace_id: str = Field(primary_key=True)
    status: str
