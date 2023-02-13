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
        self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """tests the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), "\n")

    def test_emptyline(self):
        """tests for emptyline to the program"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), "")

    def test_create_BaseModel(self):
        """tests that Base Model is created"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertTrue(type(f.getvalue()) == str)
        self.assertTrue(len(f.getvalue()) == 37)

    def test_show_BaseModel(self):
        """tests that BaseModel can show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        value = f.getvalue()
        self.assertEqual(value, "** instance id missing **\n")

    def test_destroy_BaseModel(self):
        """tests destroy on BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        value = f.getvalue()
        self.assertEqual(value, "** instance id missing **\n")

    def test_all_BaseModel(self):
        """tests all BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        value = f.getvalue()
        self.assertEqual(type(value), str)
        self.assertEqual(value, f.getvalue())

    def test_update_BaseModel(self):
        """tests update BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        value = f.getvalue()
        self.assertEqual(value, "** instance id missing **\n")
        self.assertEqual(type(value), str)

    def test_BaseModel_all(self):
        """tests BaseModel.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        value = f.getvalue()
        self.assertEqual(type(value), str)
        self.assertTrue(value.startswith('['))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        value = f.getvalue()
        self.assertEqual(type(value), str)
        self.assertTrue(value.startswith('['))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        value = f.getvalue()
        self.assertTrue(value.startswith('['))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            HBNBCommand().onecmd("City.all()")
            HBNBCommand().onecmd("Amenity.all()")
            HBNBCommand().onecmd("Place.all()")
        value = f.getvalue()
        self.assertEqual(value, "[]\n[]\n[]\n[]\n")

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
        value = f.getvalue() 
        self.assertEqual(value, "0\n0\n0\n0\n0\n0\n0\n")

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
        value = f.getvalue()
        self.assertEqual(value, "** no instance found **\n" * 7)

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
        value = f.getvalue()
        self.assertEqual(value, "** no instance found **\n" * 7)

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
        value = f.getvalue()
        self.assertEqual(value, "** no instance found **\n" * 7)

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
        value = f.getvalue()
        self.assertEqual(value, "** no instance found **\n" * 7)

    def test_help(self):
        """tests the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            HBNBCommand().onecmd("help create")
            HBNBCommand().onecmd("help show")
            HBNBCommand().onecmd("help destroy")
        value = f.getvalue()
        self.assertTrue(len(value) == 929)

    def test_all(self):
        """tests the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            HBNBCommand().onecmd("all User")
            HBNBCommand().onecmd("User.all()")
            HBNBCommand().onecmd("BaseModel.all()")
            HBNBCommand().onecmd("State.all()")
        value = f.getvalue()
        self.assertEqual(type(value), str)
        self.assertEqual(value, f.getvalue())
        self.assertTrue(len(value))
