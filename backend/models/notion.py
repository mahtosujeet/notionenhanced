from sqlmodel import SQLModel, Field


class Notion(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    workspace_id: str
    notion_refresh_token: str
    notion_access_token: str
