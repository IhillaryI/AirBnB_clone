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
        storage = FileStorage()
        storage.new(base)
        obj = storage.all()
        key = base.__class__.__name__ + '.' + base.id
        self.assertIn(key, obj.keys())
        self.assertEqual(obj[key], base)

    def test_the_save_method(self):
        """tests the save method"""
        base = BaseModel()
        storage = FileStorage()
        storage.new(base)
        storage.save()
        self.assertIsNone(storage.save())
        self.assertTrue(path.isfile("file.json"))
        self.assertTrue(storage.save)
        storage.reload()
        allobjs = storage.all()
        key = f"{base.__class__.__name__}.{base.id}"
        self.assertTrue(key in allobjs.keys())

    def test_reload_method(self):
        """tests the reload method"""
        storage = FileStorage()
        self.assertIsNone(storage.reload())
        self.assertTrue(storage.reload)
