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
                cls_to_ins = HBNBCommand.classes.get(line)
                newStance = cls_to_ins()
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

    def do_all(self, line):
        """ Prints all str repr of instances based or not on the cls name """
        space_arg = line.split(' ')
        arg = ""
        str_list = []
        if line == "":
            for key, value in models.storage.all().items():
                arg = str(value)
                str_list.append(arg)
            print(str_list)
        elif space_arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == space_arg[0]:
                    arg = str(value)
                    str_list.append(arg)
            print(str_list)

    def do_update(self, line):
        """ Updates an inst based on cls name & id by adding/updating attr """
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
        elif len(space_arg) < 3:
            print("** attribute name missing **")
        elif len(space_arg) < 4:
            print("** attribute name missing **")
        else:
            obj = models.storage.all().get(space_arg[0] + '.' + space_arg[1])
            setattr(obj, space_arg[2], space_arg[3][1:-1])
            obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
