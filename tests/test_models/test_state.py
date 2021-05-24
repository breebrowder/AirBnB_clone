#!/usr/bin/python3
"""A module for unittests for the base model class"""
import unittest
from models.state import State
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """This class test is for unittest"""

    def test_state(self):
        usr1 = State()
        self.assertIsInstance(usr1.name, str)
        
