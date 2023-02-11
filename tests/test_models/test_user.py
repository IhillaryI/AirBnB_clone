#!/usr/bin/python3
"""
Module contains unittest for
User class
"""

import unittest
from models.user import User


class UserTestCase(unittest.TestCase):
    """User class Unit tests"""
    def test_public_attributes(self):
        """tests the public attributes of User"""
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.last_name, "")
