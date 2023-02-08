#!/usr/bin/python3

"""
Modules creates class FileStorage
that serializes instances to a JSON file and deserializes
JSON file to instances
"""

import json
import os
import models

def customEncoder(obj):
    return obj.to_dict()

class FileStorage():
    """serializes object instances to JSON
    and deserializes them

    Attributes:
        __file_path (str): private class attribute.
        the json file path
        __objects (dict): stores all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file path __file_path"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f, default=customEncoder, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file(__file_path) exists"""
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            self.__objects = {}
            self.__objects = {k: BaseModel(**v) for k,v in loaded.items()}
