#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """amenities class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
