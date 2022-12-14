#!/usr/bin/python3
"""
Unittest for Basemodel class
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test for base model class"""
    def setUp(self):
        self.my_model = BaseModel()

    def test_id(self):
        self.assertNotEqual(self.my_model.id, None)
        self.assertIs(type(self.my_model.id), str)

    def test_created_at(self):
        self.assertNotEqual(self.my_model.created_at, None)
        self.assertIs(type(self.my_model.created_at), datetime.datetime)

    def test_updated_at(self):
        self.assertNotEqual(self.my_model.updated_at, None)
        self.assertIs(type(self.my_model.updated_at), datetime.datetime)

    # start tests for methods
    def test_save(self):
        prev_updated_at = self.my_model.updated_at
        self.my_model.save()

        # test updated_at was updated on save.
        self.assertNotEqual(self.my_model.updated_at, prev_updated_at)

    def test_to_dict(self):
        my_dict = self.my_model.to_dict()
        expected_dct = self.my_model.__dict__
        expected_dct.update(__class__="BaseModel")

        # test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), my_dict.keys())

        # test that to_dict returns type dict
        self.assertIs(type(my_dict), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # test that __str__() returns a string object
        self.assertIs(type(self.my_model.__str__()), str)
