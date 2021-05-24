#!/usr/bin/python3
"""A module for unittests for the base model class"""
import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """This class test is for unittest"""

    def test_place(self):
        usr1 = Place()
        self.assertIsInstance(usr1.city_id, str)
        self.assertIsInstance(usr1.user_id, str)
        self.assertIsInstance(usr1.name, str)
        self.assertIsInstance(usr1.description, str)
        self.assertIsInstance(usr1.number_rooms, int)
        self.assertIsInstance(usr1.number_bathrooms, int)
        self.assertIsInstance(usr1.max_guest, int)
        self.assertIsInstance(usr1.price_by_night, int)
        self.assertIsInstance(usr1.latitude, float)
        self.assertIsInstance(usr1.longitude, float)
        self.assertIsInstance(usr1.amenity_ids, list)
