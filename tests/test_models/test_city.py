#!/usr/bin/python3

"""
Module contains test case
for City class
"""

import unittest
from datetime import datetime
from models.city import City


class CityTestCase(unittest.TestCase):
    """Tests the State class"""
    def test_class_attributes(self):
        """test the public class attributes"""
        city = City()
        self.assertEqual(type(city.id), str)
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.created_at), datetime)
        self.assertEqual(type(city.updated_at), datetime)

        city.name = "Awka"

        self.assertEqual(city.name, "Awka")
        self.assertEqual(city.state_id, "")
