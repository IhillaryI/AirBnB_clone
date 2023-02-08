#!/usr/bin/python3

"""
Console contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Creates the command interpreter class
    Attribute:
        prompt (str): the console prompt
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        print()
        return True

    def emptyline(self):
        """overides the method in Cmd"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
