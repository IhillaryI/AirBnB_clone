#!/usr/bin/python3
"""
Module contains test case
for Review class
"""

import unittest
from datetime import datetime
from models.review import Review


class ReviewTestCase(unittest.TestCase):
    """Tests the State class"""
    def test_class_attributes(self):
        """test the public class attributes"""
        review = Review()
        self.assertEqual(type(review.id), str)
        self.assertEqual(type(review.created_at), datetime)
        self.assertEqual(type(review.updated_at), datetime)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
