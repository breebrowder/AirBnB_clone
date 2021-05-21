#!/usr/bin/python3

""" In this module we will create a class to manage File Storage """

from models import BaseModel
import json
from os import path


class FileStorage:
    """ This class will manage storage for multiple classes """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dict __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects["{}.{}".format
                              (obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        new_Dict = {}
        for key, value in FileStorage.__objects.items():
            new_Dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(new_Dict))

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if path.isfile(self.__file_path):
            with open(FileStorage.__file_path, mode="r") as f:
                myFile = json.load(f)
                for key, value in myFile.items():
                    new_Items = myFile[key]["__class__"]
                    new_Class = self.classes[new_Items]
                    self.__objects[key] = new_Class(**value)
        if path.isfile(self.__file_path) is False:
            return
