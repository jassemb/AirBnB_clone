#!/usr/bin/python3
"""
    serializes instances to a JSON file and
    deserializes JSON file to instances
"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """
    that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key id
        """
        obj_dict = obj.to_dict()
        key = "{}.{}".format(obj_dict["__class__"], obj_dict["id"])
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        my_dict ={}
        for key, value in self.__objects.items():
            dict_value = value.to_dict()
            my_dict.update({key: dict_value})
        with open(self.__file_path, 'w') as file:
            json.dump(my_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists('{}'.format(self.__file_path)) is True:
            with open(filename, encoding='utf-8') as file:
                my_dict = json.loads(file.read())
