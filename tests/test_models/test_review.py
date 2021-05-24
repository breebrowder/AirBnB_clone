#!/usr/bin/python3
"""A module for unittests for the base model class"""
import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """This class test is for unittest"""

    def test_review(self):
        usr1 = Review()
        self.assertIsInstance(usr1.place_id, str)
        self.assertIsInstance(usr1.user_id, str)
        self.assertIsInstance(usr1.text, str)

if __name__ == '__main__':
    unittest.main()
