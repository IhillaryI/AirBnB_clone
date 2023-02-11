#!/usr/bin/python3
"""
Module contains Tests for file_storage.py,
located in models/engine/file_storage.py
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path


class FileStorageTestCase(unittest.TestCase):
    """TestCase for FileStorage class"""
    def setUp(self):
        """sets up the test"""
        self.fs = FileStorage()

    def test_for_class_attributes(self):
        """tests_for_private_class_attributes"""
        pass

    def test_for_public_instance_methods(self):
        """tests the public instance methods"""
        base = BaseModel()
        obj = base.to_dict()

        self.assertEqual(type(self.fs.all()), dict)

        # self.assertEqual(self.fs.new(obj), None)

        self.assertEqual(self.fs.save(), None)

        self.assertEqual(self.fs.reload(), None)
        self.assertTrue(path.isfile("file.json"))
