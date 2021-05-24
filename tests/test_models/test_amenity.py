#!/usr/bin/python3
"""A module for unittests for the base model class"""
import unittest
import models.amenity import Amenity
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """This class test is for unittest"""

    def test_amenity(self):
        usr1 = Amenity()
        self.assertIsInstance(usr1.name, str)
