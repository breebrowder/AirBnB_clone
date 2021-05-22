#!/usr/bin/python3
""" This is the entry point of our command interpreter """

import cmd
import models
from models import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This is our console """

    prompt = '(hbnb)'
    classes = {"BaseModel": BaseModel,
               "City": City,
               "User": User,
               "State": State,
               "Place": Place,
               "Amenity": Amenity,
               "Review": Review}

    def emptyline(self):
        """ Do nothing """
        pass

    def do_quit(self, line):
        """ Command to exit program """
        return True

    def do_EOF(self, line):
        """ exits at EOF """
        return True

    def do_create(self, line):
        """ create new inst of BaseModel, save to the JSON file, prints ID """
        if line:
            if line in HBNBCommand.classes:
                newStance = HBNBCommand.classes.get(line)
                newStance.save()
                print(newStance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Prints the string repr of an inst based on class name & id """
        space_arg = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif space_arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(space_arg) < 2:
            print("** instance id missing **")
        elif space_arg[0] + '.' + space_arg[1] not in \
             models.storage.all().keys():
            print("** no instance found **")
        else:
            obj = models.storage.all().get(space_arg[0] + '.' + space_arg[1])
            print(obj)

    def do_destroy(self, line):
        """  Deletes an instance based on the class name and id """
        space_arg = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif space_arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(space_arg) < 2:
            print("** instance id missing **")
        elif space_arg[0] + '.' + space_arg[1] not in \
             models.storage.all().keys():
            print("** no instance found **")
        else:
            models.storage.all().pop(space_arg[0] + '.' + space_arg[1], None)
            models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
