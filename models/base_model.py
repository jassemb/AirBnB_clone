#!/usr/bin/python3
"""This module creates the BaseModel class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A class named BaseModel
    Attributes:
    attr1(id): object id
    attr2(created_at): datetime instance is created
    attr3(updated_at): datetime instance is created and updated when changed
    """
    def __init__(self, *args, **kwargs):
        """Initiliazes an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    dt_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_obj)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates public instance attr updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        newdict = self.__dict__.copy()
        newdict['created_at'] = datetime.isoformat(newdict['created_at'])
        newdict['updated_at'] = datetime.isoformat(newdict['updated_at'])
        newdict['__class__'] = self.__class__.__name__
        return newdict

