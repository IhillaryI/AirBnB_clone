#!/usr/bin/python3
"""
Module contains class State
which inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class Inherits from BaseModel

    Attributes:
        name (str): name
    """
    name = ""
