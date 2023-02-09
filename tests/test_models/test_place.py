#!/usr/bin/python3

"""
Module contains test case
for Place class
"""

import unittest
from datetime import datetime
from models.place import Place


class PlaceTestCase(unittest.TestCase):
    """Tests the State class"""
    def test_class_attributes(self):
        """test the public class attributes"""
        place = Place()
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.updated_at), datetime)

        place.name = "Anambra"

        self.assertEqual(place.name, "Anambra")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
