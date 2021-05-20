#!/usr/bin/python3
""" This is the entry point of our command interpreter """

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ This is our console """

    prompt = '(hbnb)'

    def emptyline(self):
        """ Do nothing """
        pass

    def do_quit(self, line):
        """ Command to exit program """
        return True

    def do_EOF(self, line):
        """ exits at EOF """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
