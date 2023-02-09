#!/usr/bin/python3

"""
Console contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Place": Place,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
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
        if command is None:
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
        if command is None or command == "":
            print("** class name missing **")
        elif command not in classes.keys():
            print("** class doesn't exist **")
        elif args is None or args == "":
            print("** instance id missing **")
        else:
            instances = storage.all()
            instance = None
            for key, val in instances.items():
                if val.id == args:
                    instance = instances[key]
            if instance and instance.to_dict()["__class__"] == command:
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance base on the class name and id

        Args:
            line (str): the input to destroy
        """
        command, args, line = self.parseline(line)
        instance_key = None

        if command is None or command == "":
            print("** class name missing **")
        elif command not in classes.keys():
            print("** class doesn't exist **")
        elif args is None or args == "":
            print("** instance id missing **")
        else:
            instances = storage.all()
            for key, val in instances.items():
                if val.id == args:
                    instance_key = key
            if instance_key is not None:
                del instances[instance_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of all
        instances based on or not on the class name

        Args:
            line (str): line input to all
        """
        command, args, line = self.parseline(line)
        allobjs = storage.all()
        all_str_repr = []

        if command is None or command == "":
            all_str_repr = [val.__str__() for val in allobjs.values()]
            print(all_str_repr)
        else:
            if command not in classes.keys():
                print("** class doesn't exist **")
            else:
                all_str_repr = [val.__str__() for val in allobjs.values()
                                if val.__class__.__name__ == command.strip()]
                print(all_str_repr)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute

        Args:
            line (str): line input to update
        Usage: update <class name> <id> <attribute name> "<attribute value>
        """
        command, args, line = self.parseline(line)
        allobjs = storage.all()
        instance_key = None

        if command is None or command == "":
            print("** class name missing **")
            return
        if command not in classes.keys():
            print("** class name doesn't exist **")
            return

        if args == "" or args is None:
            print("** instance id missing **")
        else:
            for key, val in allobjs.items():
                if val.id == args.split()[0]:
                    instance_key = key
            if instance_key is None:
                print("** no instance found **")
            else:
                if len(args.split()) < 2:
                    print("** attribute name missing **")
                elif len(args.split()) < 3:
                    print("** value missing **")
                else:
                    obj = allobjs[instance_key]
                    ID, attr, val = args.split()[:3]
                    if hasattr(obj, attr):
                        attr_type = type(getattr(obj, attr))
                        setattr(obj, attr, attr_type(val.strip('"')))
                    else:
                        setattr(obj, attr, val.strip('"'))
                    storage.save()

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
