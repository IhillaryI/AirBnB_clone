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
        base = BaseModel()
        base.save()
        storage = FileStorage()
        storage.reload()
        allobjs = storage.all()
        self.assertEqual(type(storage.all()), dict)
        for key, val in allobjs.items():
            if isinstance(val, BaseModel):
                self.assertTrue(isinstance(val, BaseModel))

    def test_new_method(self):
        """tests the class new method"""
        base = BaseModel()
        base_obj = base.to_dict()
        storage = FileStorage()
        storage.reload()
        base.save()
        self.assertEqual(storage.new(base), None)
        allobjs = storage.all()
        for val in allobjs.values():
            if val.id == base_obj["id"]:
                self.assertEqual(val.id, base_obj["id"])

    def test_the_save_method(self):
        """tests the save method"""
        base = BaseModel()
        storage = FileStorage()
        storage.save()
        allobjs = storage.all()
        for val in allobjs.values():
            if val == base:
                self.assertEqual(val, base)

    def test_reload_method(self):
        """tests the reload method"""
        storage = FileStorage()
        self.assertEqual(storage.reload(), None)
        allobjs = storage.all()
        for val in allobjs.values():
            self.assertTrue(val)

