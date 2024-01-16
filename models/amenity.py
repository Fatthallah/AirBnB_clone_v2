#!/usr/bin/python3
"""The Comment I have to write"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity

class Amenity(BaseModel, Base):
    """The Comment I have to write
    The Comment:
        The Comment I have to write
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)