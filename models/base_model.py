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
        """updates updated_at with the current datetime"""

        self.updated_at = datetime.now().isoformat
        return self.updated_at

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        self.created_at = datetime.now().isoformat()
        self.__dict__.update({'__class__' : self.__class__.__name__})
        return self.__dict__

    def __str__(self):
        """Prints information in specified format"""

        return("[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__))
