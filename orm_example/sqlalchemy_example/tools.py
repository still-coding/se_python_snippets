from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from models import Base


def get_session_engine(db_uri: str) -> tuple[sessionmaker[Session], Engine]:
    engine = create_engine(db_uri)  # echo=True prints all SQL
    return sessionmaker(engine), engine


def create_database(db_uri: str) -> sessionmaker[Session]:
    session_factory, engine = get_session_engine(db_uri)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return session_factory
