#!/usr/bin/python3
""" This module is to create first class of base"""
import uuid
from datetime import datetime


class BaseModel:
    """This class is for the BaseModel"""

    def __init__(self, *args, **kwargs):

        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.id = str(uuid.uuid4())

        if kwargs is not ():
            pass

    def save(self):
        return self.updated_at

    def to_dict(self):
        self.created_at = datetime.now().isoformat()
        return self.__dict__

    def __str__(self):
           return("[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__))
