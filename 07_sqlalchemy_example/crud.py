# CRUD = Create, Read, Update, Delete
from config import DATABASE_URI
from model import Corresp, Type, Department, External, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from random import choice, randint
from datetime import date


def get_session_engine(db_uri):
    engine = create_engine(db_uri)#, echo=True)
    session = scoped_session(sessionmaker(bind=engine))
    return session, engine


def create_database(db_uri):
    session, engine = get_session_engine(db_uri)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return session


def fill_db(session):

    def read_csv(name):
        with open(f'./static_data/{name}.csv', 'r') as f:
            result = [line.strip() for line in f]
        return result

    depts = read_csv('departments')
    externals = [(e.split(';')[0], e.split(';')[1]) for e in read_csv('externals')]
    subjects = read_csv('subjects')
    types = read_csv('types')

    for d in depts:
        dept = Department(name=d)
        session.add(dept)

    for e in externals:
        ext = External(name=e[0], address=e[1])
        session.add(ext)

    for t in types:
        typ = Type(name=t)
        session.add(typ)

    for i in range(50):
        corr = Corresp(number=str(i+1),
            subject=choice(subjects),
            date=date(2021, randint(1, 12), randint(1, 28)),
            direction=bool(i % 2),
            type_id=randint(1, len(types)),
            internal_id=randint(1, len(depts)),
            external_id=randint(1, len(externals)),
            )
        session.add(corr)

    session.commit()


if __name__ == '__main__':
    print('connecting...')

    session = create_database(DATABASE_URI)

    fill_db(session)
    print('db created!')


    session.close()
    print('session closed')
