#!/usr/bin/python3
""" This module is to create first class of base"""
from uuid import uuid4
from datetime import datetime
import models
import json

class BaseModel:
    """This class is for the BaseModel"""

    def __init__(self, *args, **kwargs):

        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.id = str(uuid.uuid4())

        if kwargs is not ():
            pass

    def save(self):
<<<<<<< HEAD
        return self.updated_at

    def to_dict(self):
        self.created_at = datetime.now().isoformat()
        return self.__dict__

    def __str__(self):
           return("[{}] ({}) {}".format(self.__class__.__name__,
=======
        """updates updated_at with the current datetime"""

        return self.updated_at

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.__dict__.update({'__class__' : self.__class__.__name__})
        return self.__dict__

    def __str__(self):
        """Prints information in specified format"""

        return("[{}] ({}) {}".format(self.__class__.__name__,
>>>>>>> d217d459116522972795221ae88eee6fc82b2f1c
                                        self.id, self.__dict__))
