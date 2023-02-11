#!/usr/bin/python3
"""
Module contains class City
which inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel

    Attributes:
        state_id (str): state_id
        name (str): name
    """
    state_id = ""
    name = ""
