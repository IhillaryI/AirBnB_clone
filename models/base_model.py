#!/usr/bin/python3

"""
Module contains a class BaseModel which will serve as the
Base for future classes to be created in the project
"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """class BaseModel defines all common attributes
    for other classes

    Attributes:
        id (str): unique id created with uuid4
        created_at (datetime): time the instance was created
        updated_at (datetime): time the instance was updated
    """
    def __init__(self):
        """initializes the instance"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns the dictionary containing all key/value pairs
        of __dict__ of the instance"""
        return self.__dict__

    def __str__(self):
        """method to print the class in string form"""
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"
