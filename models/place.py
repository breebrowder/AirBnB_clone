#!/usr/bin/python3
""" Place Class that inherits from BaseModel """

import json
from models import BaseModel


class Place(BaseModel):
    """ Inherited class """
    city_id = ""
    user_id = ""
    name = ""
    decription = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
