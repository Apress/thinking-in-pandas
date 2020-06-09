from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


SQLITE_URL = "sqlite://"

POSTGRES_URL = "postgresql://postgres@localhost:5432"


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    name = Column(String(50))


engine = create_engine(SQLITE_URL)

Session = sessionmaker(bind=engine)


def create_tables():

    Base.metadata.create_all(engine)


def add_user():

    session = Session()

    user = User(id=0, name="Eric")

    session.add(user)

    session.commit()

    session.close()


create_tables()
add_user()
