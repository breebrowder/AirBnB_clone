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

        if len(kwargs) > 0:
            conversion = ["created_at", "updated_at"]
            for key, value in kwargs.items():
                if key in conversion:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
                else:
                    models.storage.new(self)

    def save(self):
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
                                        self.id, self.__dict__))
