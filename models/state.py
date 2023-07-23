#!/usr/bin/python3
"""
    Implementation of the State class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """Class for the states table."""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # Add the primary key
    id = Column(String(60), primary_key=True, nullable=False)

    # Define the relationship as a string argument
    if storage_type != 'db':
        @property
        def cities(self):
            """Return the list of City objects from storage linked to the current State."""
            all_cities = models.storage.all("City")  # Use "City" as a string argument
            state_cities = [city for city in all_cities.values() if city.state_id == self.id]
            return state_cities

# Do NOT include the cities relationship here


