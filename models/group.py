from .database import Base
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    group_name = Column(String)