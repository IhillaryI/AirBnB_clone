#!/usr/bin/python3

"""
Console contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage

classes = {
        "BaseModel": BaseModel
        }


class HBNBCommand(cmd.Cmd):
    """Creates the command interpreter class
    Attribute:
        prompt (str): the console prompt
    """

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of a given BaseModel

        Args:
            line (str): the line input to create
        """
        command, args, line = self.parseline(line)
        if command == None:
            print("** class name missing **")
        elif command not in classes.keys():
            print("** class doesn't exist **")
        else:
            obj = classes[command]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id

        Args:
            line (str): the line input to show
        """
        command, args, line = self.parseline(line)
        if command == None or command == "":
            print("** class name missing **")
        elif command not in classes.keys():
            print("** class doesn't exist **")
        elif args == None or args == "":
            print("** instance id missing **")
        else:
            instances = storage.all()
            instance = None
            for key,val in instances.items():
                if val.id == args:
                    instance = instances[key]
            if instance:
                print(instance)
            else:
                print("** no instance found **")
                print("args => ", args)

    def do_destroy(self, line):
        """Deletes an instance base on the class name and id

        Args:
            line (str): the input to destroy
        """
        command, args, line = self.parseline(line)
        if command == None or command == "":
            print("** class name missing **")
        elif command not in classes.keys():
            print("** class doesn't exist **")
        elif args == None or args == "":
            print("** instance id missing **")
        else:
            instances = storage.all()
            intance_key = None
            for key, val in instances.items():
                if val.id == args:
                    instance_key = key
            if instance_key:
                del instances[instance_key]
                storage.save()
            else:
                print("** no instance found **")


    def do_quit(self, line):
        """Quit command to exit the program
        
        Args:
            line (str): None
        """
        return True

    def help_quit(self):
        """Help text to print for quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        print()
        return True

    def emptyline(self):
        """overides the method in Cmd"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
