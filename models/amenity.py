#!/usr/bin/python3

"""
Module contains class Amenity
which inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel

    Attributes:
        name (str): name
    """
    name = ""
