#!/usr/bin/env python3
"""
Declare a SQLAlchemy model named 'User' corresponding to a
database table named "users"
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

Base = declarative_base()


class User(Base):
    """
    Definition of class User
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)


if __name__ == "__main__":
    print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
