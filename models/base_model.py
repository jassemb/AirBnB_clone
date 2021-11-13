#!urs/bin/python3
"""
This module creates the Base class
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Base model that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwagrs):
        """
        Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwagrs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

        elif len(kwagrs) > 0:
            for key, value in kwagrs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time_format)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns the informal representation
        """
        return ("[{}]) ({}) {}".format(self.__class__.__name__, self.id,
                                       self.__dict__))

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        d = dict(**self.__dict__)
        d['__class__'] = str(type(self).__name__)
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return (d)
