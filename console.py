#!/usr/bin/python3
"""
console module
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "Amenity",
               "State", "City", "Place", "Review"]

    @classmethod
    def count(self, class_name, objects_dict):
        """ count the number of instance"""
        counter = 0
        for key in objects_dict.keys():
            if class_name in key:
                counter += 1
        print(counter)

    def do_quit(self, args):
        """
        exit program
        """
        return True

    def do_EOF(self, args):
        """
        Quit Command to exit the program
        """
        return True

    def emptyline(self):
        """
        empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_help(self, args):
        """
        help command
        """
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """
        creates a new instances of BaseModel
        saves it and print the id
        """
        args = args.split(" ")
        if args == "":
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new = eval("{}()".format(args[0]))
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        Print the string representation of an
        instance based on the class name and id
        """
        args = args.split()
        if args == "":
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        dict_obj = storage.all()
        my_key = args[0] + "." + args[1]
        if my_key in dict_obj:
            print(dict_obj[my_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Delete an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        objects = storage.all()

        if tokens[0] in self.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj = objects[name]
                if obj:
                    objs = storage.all()
                    del objs["{}.{}".format(type(obj).__name__, obj.id)]
                    storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Print all string representation of all instances
        based or not on the class name
        """
        args = args.split()
        dict_obj = storage.all()
        list = []
        if len(args):
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            for k, v in dict_obj.items():
                if class_name in k:
                    list.append((dict_obj[k].__str__()))
        else:
            for k, v in dict_obj.items():
                list.append((dict_obj[k].__str__()))
        print(list)

    def do_update(self, args):
        """
        Update an instance based on the class
        name and id by adding or updating attribute
        """
        args = args.split()
        objects = storage.all()
        if args == "":
            print("** class name missing **")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(args[0], args[1])
            if k in objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                if len(args) < 4:
                    print("** value missing **")
                else:
                    obj = objects[k]
                    setattr(obj, args[2], args[3])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
