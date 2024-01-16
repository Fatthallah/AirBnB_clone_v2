#!/usr/bin/python3
"""The Comment I have to write"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Review(BaseModel, Base):
    """The Comment I have to write
    The Comment:
        The Comment I have to write
        The Comment I have to write
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)