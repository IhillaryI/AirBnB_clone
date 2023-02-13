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
    def test_all_method(self):
        """test the public instance method all"""
        storage = FileStorage()
        allobjs = storage.all()
        self.assertIsInstance(storage.all(), dict)
        self.assertIsNotNone(storage.all())
        self.assertEqual(allobjs, storage.all())
        self.assertTrue(storage.all)

    def test_new_method(self):
        """tests the class new method"""
        base = BaseModel()
        base_dict = base.to_dict()
        new_base = BaseModel(base_dict)
        storage = FileStorage()
        self.assertTrue(storage.new)
        self.assertIsNone(storage.new(new_base))
        allobjs = storage.all()
        for val in allobjs.values():
            if val == new_base:
                self.assertEqual(val, new_base)

    def test_the_save_method(self):
        """tests the save method"""
        storage = FileStorage()
        self.assertIsNone(storage.save())
        self.assertTrue(path.isfile("file.json"))
        self.assertTrue(storage.save)

    def test_reload_method(self):
        """tests the reload method"""
        storage = FileStorage()
        self.assertIsNone(storage.reload())
        self.assertTrue(storage.reload)
