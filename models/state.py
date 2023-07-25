#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
<<<<<<< HEAD
            """
            get list of City instances with state_id
            equals to the current State.id
            """
            list_cities = []
            all_cities = models.storage.all(City)
            for key, city_obj in all_cities.items():
                if city_obj.state_id == self.id:
                    list_cities.append(city_obj)
            return list_cities
from models.city import City
=======
            """Getter attribute cities that returns the list of City"""
            from models import storage
            from models.city import City
            my_list = []
            all_city = storage.all(City)
            for city in all_city.values():
                if city.state_id == self.id:
                    my_list.append(city)
            return my_list
>>>>>>> 182001e3fbf25ba85c47c580c15d5154f0e57099
