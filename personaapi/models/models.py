from .base import Base, Model
from sqlalchemy import Column, String


class Entity(Model, Base):
    name = Column(String)
