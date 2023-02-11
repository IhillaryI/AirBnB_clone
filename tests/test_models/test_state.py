#!/usr/bin/python3
"""
Module contains test case
for State class
"""

import unittest
from datetime import datetime
from models.state import State


class StateTestCase(unittest.TestCase):
    """Tests the State class"""
    def test_class_attributes(self):
        """test the public class attributes"""
        state = State()
        self.assertEqual(type(state.id), str)
        self.assertEqual(type(state.name), str)
        self.assertEqual(type(state.created_at), datetime)
        self.assertEqual(type(state.updated_at), datetime)

        state.name = "Anambra"

        self.assertEqual(state.name, "Anambra")
