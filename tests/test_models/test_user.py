#!/usr/bin/python3
"""A module for unittests for the base model class"""
import unittest
import models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """This class test is for unittest"""

    def test_user(self):
        usr1 = User()
        self.assertIsInstance(usr1.email, str)
        self.assertIsInstance(usr1.password, str)
        self.assertIsInstance(usr1.first_name, str)
        self.assertIsInstance(usr1.last_name, str)
