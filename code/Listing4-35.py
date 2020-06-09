from sqlalchemy import Column, String

from sqlalchemy.ext.declarative import declarative_base

import sqlalchemy.types as types

import numpy as np

Base = declarative_base()


class Int32(types.TypeDecorator):

    impl = types.Integer

    def process_bind_param(self, value, dialect):

        return value

    def process_result_value(self, value, dialect):

        return np.int32(value)


class User(Base):

    __tablename__ = "user"

    id = Column(Int32, primary_key=True)

    name = Column(String(50))
