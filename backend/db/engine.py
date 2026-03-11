import typing

from fastapi import Depends
from sqlmodel import create_engine, Session


DATABASE_URL = "sqlite:///database.db"
connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=True
)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = typing.Annotated[Session, Depends(get_session)]
