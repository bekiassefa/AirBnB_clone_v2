#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class City(BaseModel, Base):
    """Class for the cities table."""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    # Add the primary key
    id = Column(String(60), primary_key=True, nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
