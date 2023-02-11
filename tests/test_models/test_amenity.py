#!/usr/bin/python3

"""
Module contains test case
for Amenity class
"""

import unittest
from datetime import datetime
from models.amenity import Amenity


class AmenityTestCase(unittest.TestCase):
    """Tests the State class"""
    def test_class_attributes(self):
        """test the public class attributes"""
        amenity = Amenity()
        self.assertEqual(type(amenity.id), str)
        self.assertEqual(type(amenity.name), str)
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertEqual(type(amenity.updated_at), datetime)

        amenity.name = "Running Water"

        self.assertEqual(amenity.name, "Running Water")
