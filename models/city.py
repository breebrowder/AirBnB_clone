#!/usr/bin/python3
""" City Class that inherits from BaseModel """

import json
from models import BaseModel


class City(BaseModel):
    """ Inherited class """
    state_id = ""
    name = ""
