from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

def get_session_engine(db_uri):
    engine = create_engine(db_uri)  # , echo=True)
    session = sessionmaker(engine)
    return session, engine


def create_database(db_uri):
    session, engine = get_session_engine(db_uri)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return session
