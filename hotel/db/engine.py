from hotel.db.models import Base
from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

engine: Engine = None
DBSession = sessionmaker()


def init_db(file: str):
    engine = create_engine(file)
    Base.metadata.bind = engine
    DBSession.bind = engine
