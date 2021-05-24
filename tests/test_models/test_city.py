#!/usr/bin/python3
"""A module for unittests for the base model class"""
import unittest
import models.City import City
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """This class is to test with unittest"""

    def test_city(self):
        usr1 = City()
        self.assertIsInstance(usr1.state_id, str)
        self.assertIsInstance(usr1.name, str)
