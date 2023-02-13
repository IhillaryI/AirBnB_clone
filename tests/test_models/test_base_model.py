#!/usr/bin/python3
"""
Test case for module: base_model
from package: models
"""
import unittest
from os import path
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class BaseModelTestCase(unittest.TestCase):
    """TestCase for BaseModel class"""
    def test_public_instances_attributes(self):
        """tests the class public instance attributes"""
        base = BaseModel()
        self.assertTrue(type(base.id) == str)
        self.assertTrue(type(base.created_at) == datetime)
        self.assertTrue(type(base.updated_at) == datetime)

    def test_instance_with_kwargs(self):
        """test the creation of an instance with **kwargs"""
        base = BaseModel()
        base_dict = base.to_dict()
        new_base = BaseModel(base_dict)
        self.assertFalse(base is new_base)

    def test_public_instance_methods(self):
        """tests the instance public methods"""
        base = BaseModel()
        prev_updated_at = base.updated_at

        base.save()
        self.assertTrue(prev_updated_at != base.updated_at)
        self.assertTrue(type(base.to_dict()) == dict)

    def test_str_method(self):
        """Test string method for instance."""
        test_me = BaseModel()
        class_name = test_me.__class__.__name__
        obj_id = test_me.id
        obj_dict = test_me.__dict__
        obj_str = "[{}] ({}) {}".format(class_name, obj_id, obj_dict)
        self.assertEqual(str(test_me), obj_str)

    def test_intance_dictionary_obj(self):
        """test the instance to_dict() object"""
        base = BaseModel()
        base.name = "Oscar"
        base.number = 88
        obj = base.to_dict()
        self.assertEqual(obj["__class__"], "BaseModel")
        self.assertTrue(type(obj) == dict)
        self.assertTrue(type(obj["__class__"]) == str)
        self.assertTrue(type(obj["created_at"]) == str)
        self.assertTrue(type(obj["updated_at"]) == str)
        self.assertTrue(obj["name"] == "Oscar")
        self.assertTrue(obj["number"] == 88)

    def test_save_method(self):
        """tests the save method on BaseModel"""
        base = BaseModel()
        base.name = "My_Base"
        updated_at = base.updated_at
        base.save()
        key = f"{base.__class__.__name__}.{base.id}"
        storage.reload()
        self.assertTrue(key in storage.all().keys())
        self.assertFalse(base.updated_at == updated_at)
