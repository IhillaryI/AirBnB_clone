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

    def test_quit(self):
        """tests the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")

    def test_EOF(self):
        """tests the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")

    def test_emptyline(self):
        """tests for emptyline to the program"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")

    def test_create_BaseModel(self):
        """tests that Base Model is created"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

    def test_show_BaseModel(self):
        """tests that BaseModel can show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")

    def test_destroy_BaseModel(self):
        """tests destroy on BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")

    def test_all_BaseModel(self):
        """tests all BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")

    def test_update_BaseModel(self):
        """tests update BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")

    def test_BaseModel_all(self):
        """tests BaseModel.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            HBNBCommand().onecmd("Review.all()")
            HBNBCommand().onecmd("User.all()")
            HBNBCommand().onecmd("State.all()")
            HBNBCommand().onecmd("City.all()")
            HBNBCommand().onecmd("Amenity.all()")
            HBNBCommand().onecmd("Place.all()")

    def test_count_on_all_class(self):
        """tests the count() on all clasess"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            HBNBCommand().onecmd("Review.count()")
            HBNBCommand().onecmd("User.count()")
            HBNBCommand().onecmd("State.count()")
            HBNBCommand().onecmd("Place.count()")
            HBNBCommand().onecmd("Amenity.count()")
            HBNBCommand().onecmd("City.count()")

    def test_show_on_all_classes(self):
        """tests the show() on all classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("1234")')
            HBNBCommand().onecmd('User.show("1234")')
            HBNBCommand().onecmd('State.show("1234")')
            HBNBCommand().onecmd('City.show("1234")')
            HBNBCommand().onecmd('Amenity.show("1234")')
            HBNBCommand().onecmd('Place.show("1234")')
            HBNBCommand().onecmd('Review.show("1234")')

    def tests_destroy_on_all_classes(self):
        """tests destroy() on all classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy("1234")')
            HBNBCommand().onecmd('User.destroy("1234")')
            HBNBCommand().onecmd('City.destroy("1234")')
            HBNBCommand().onecmd('State.destroy("1234")')
            HBNBCommand().onecmd('Place.destroy("1234")')
            HBNBCommand().onecmd('Amenity.destroy("1234")')
            HBNBCommand().onecmd('Review.destroy("1234")')

    def tests_update_on_all_classes_without_dict(self):
        """tests update() on all classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("1234", "name", "John")')
            HBNBCommand().onecmd('User.update("1234", "name", "John")')
            HBNBCommand().onecmd('City.update("1234", "name", "John")')
            HBNBCommand().onecmd('State.update("1234", "name", "John")')
            HBNBCommand().onecmd('Place.update("1234", "name", "John")')
            HBNBCommand().onecmd('Amenity.update("1234", "name", "John")')
            HBNBCommand().onecmd('Review.update("1234", "name", "John")')

    def tests_update_on_all_classes_with_dict(self):
        """tests update() on all classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("1234", {"name": "John"})')
            HBNBCommand().onecmd('User.update("1234", {"name": "John"})')
            HBNBCommand().onecmd('City.update("1234", {"name": "John"})')
            HBNBCommand().onecmd('State.update("1234", {"name": "John"})')
            HBNBCommand().onecmd('Place.update("1234", {"name": "John"})')
            HBNBCommand().onecmd('Amenity.update("1234", {"name": "John"})')
            HBNBCommand().onecmd('Review.update("1234", {"name": "John"})')

    def test_help(self):
        """tests the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            HBNBCommand().onecmd("help create")
            HBNBCommand().onecmd("help show")
            HBNBCommand().onecmd("help destro")

    def test_all(self):
        """tests the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            HBNBCommand().onecmd("all User")
            HBNBCommand().onecmd("User.all()")
            HBNBCommand().onecmd("BaseModel.all()")
            HBNBCommand().onecmd("State.all()")
