#!/usr/bin/python3
""" HBnB console Module """

import cmd
import sys
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBnB command interpreter.
    Attributes:
        prompt: The command prompt.
    """
    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "Amenity",
                 "State", "City", "Place", "Review"}

    def emptyline(self):
        """ empty line shouldn't have an output """
        pass

    def do_quit(self, arg):
        """ execute quit command """
        return True

    def do_EOF(self, arg):
        """ Exit """
        return True

    def do_create(self, arg):
        """
        creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        """create an instance of class"""
        cl = globals()[arg]
        obj = cl()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id.
        """
        l = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(l) == 1:
            print("** instance id is missing **")
            return
        objects_dict = storage.all()
        my_key = l[0] + "." + l[1]
        if my_key in objects_dict:
            print(objects_dict[my_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file)
        """
        l = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(l) == 1:
            print("** instance id is missing **")
            return
        my_key = l[0] + "." + l[1]
        objects_dict = storage.all()
        if my_key in objects_dict:
            del objects_dict[my_key]
            storage.save()
            print(storage.all())

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        arg = arg.split()
        dict_obj = storage.all()
        l = []
        if len(arg):
            class_name = arg[0]
            if class_name not in HBNBCommand.__classes:
                print("* class doesn't exist *")
                return
            for k, v in dict_obj.items():
                if class_name in k:
                    l.append((dict_obj[k].__str__()))
        else:
            for k, v in dict_obj.items():
                l.append((dict_obj[k].__str__()))
        print(l)

    def do_update(self, cmd_line):
        """ Updates an instancebased on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = cmd_line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        try:
            args[1]
        except Exception:
            print("** instance id missing **")
            return
        objects_dict = storage.all()
        my_key = args[0] + "." + args[1]
        if my_key not in objects_dict:
            print("** no instance found **")
            return
        try:
            args[2]
        except Exception:
            print("** attribute name missing **")
            return
        try:
            args[3]
        except Exception:
            print("** value missing **")
            return
        if args[3]:
            setattr(objects_dict[my_key], args[2], args[3])
            my_obj = objects_dict[my_key]
            my_obj.updated_at = datetime.now()
            storage.save()

    @classmethod
    def all(self, class_name, objects_dict):
        """ print all objects of class_name """
        l2 = []
        for key, val in objects_dict.items():
            if class_name in key:
                l2.append((objects_dict[key].__str__()))
        print(l2)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
