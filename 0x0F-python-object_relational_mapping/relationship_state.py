#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, merge, save-update',
                          backref='state')
