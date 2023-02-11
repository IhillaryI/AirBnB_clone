#!/usr/bin/python3

"""
Module contains Unit tests for
Module console.py
"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class ConsoleTestCase(unittest.TestCase):

    def test_help(self):
        """tests the help command"""
        with patch('sys.stdout', new = StringIO()) as f:
            HBNBCommand().onecmd("help")
            HBNBCommand().onecmd("help create")
            HBNBCommand().onecmd("help show")
            HBNBCommand().onecmd("help destro")

    def test_all(self):
        """tests the show command"""
        with patch('sys.stdout', new = StringIO()) as f:
            HBNBCommand().onecmd("all")
            HBNBCommand().onecmd("all User")
            HBNBCommand().onecmd("User.all()")
            HBNBCommand().onecmd("BaseModel.all()")
            HBNBCommand().onecmd("State.all()")
