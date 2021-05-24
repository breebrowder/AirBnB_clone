#!/usr/bin/python3
""" Review Class that inherits from BaseModel """

import json
from models import BaseModel


class Review(BaseModel):
    """ Inherited class """
    place_id = ""
    user_id = ""
    text = ""
