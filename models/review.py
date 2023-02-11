#!/usr/bin/python3
"""
Module constains class
which inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel

    Attributes:
        place_id (str): place_id
        user_id (str): user_id
        text (str): text
    """
    place_id = ""
    user_id = ""
    text = ""
