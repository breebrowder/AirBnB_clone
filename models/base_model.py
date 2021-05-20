#!/usr/bin/python3
""" This module is to create the first class of Base """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ This class is for the BaseModel """

    def __init__(self, *args, **kwargs):

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ """
        theDict = self.__dict__
        strinDict = {}
        for key, value in theDict.items():
            if isinstance(value, datetime):
                strinDict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                strinDict[key] = value
        strinDict["__class__"] = self.__class__.__name__
        return strinDict

    def __str__(self):
        """ Will return string form of Class """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ update an attribute with current datetime """
        self.updated_at = datetime.now()
