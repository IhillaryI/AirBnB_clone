#!/usr/bin/python3

"""
Module contains a class BaseModel which will serve as the
Base for future classes to be created in the project
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """class BaseModel defines all common attributes
    for other classes

    Attributes:
        id (str): unique id created with uuid4
        created_at (datetime): time the instance was created
        updated_at (datetime): time the instance was updated
    """
    def __init__(self, *arg, **kwargs):
        """initializes the instance"""
        if len(kwargs.items()) > 0:
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                    continue
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """returns the dictionary containing all key/value pairs
        of __dict__ of the instance"""
        obj = self.__dict__.copy()
        obj['created_at'] = obj['created_at'].isoformat()
        obj['updated_at'] = obj['updated_at'].isoformat()
        obj['__class__'] = f"{self.__class__.__name__}"
        return obj

    def __str__(self):
        """method to print the class in string form"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
