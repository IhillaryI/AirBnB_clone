#!/usr/bin/python3

"""
Test case for module: base_model
from package: models
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):
    """TestCase for BaseModel class"""
    def test_public_instances_attributes(self):
        """tests the class public instance attributes"""
        base = BaseModel()
        self.assertTrue(type(base.id) == str)
        self.assertTrue(type(base.created_at) == datetime)
        self.assertTrue(type(base.updated_at) == datetime)

    def test_instance_with_args(self):
        """test the creation of an instance with *args"""
        pass

    def test_instance_with_kwargs(self):
        """test the creation of an instance with **kwargs"""
        pass

    def test_public_instance_methods(self):
        """tests the instance public methods"""
        base = BaseModel()
        prev_updated_at = base.updated_at

        base.save()
        self.assertTrue(prev_updated_at != base.updated_at)
        self.assertTrue(type(base.to_dict()) == dict)

    def test__str__output(self):
        """test the __str__ method of the class"""
        base = BaseModel()
        self.assertEqual(type(base.__str__()), str)
