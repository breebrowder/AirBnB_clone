#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """This class test Basemodel with unittest"""

    def test_basemodel(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.__str__(), str)
        self.assertTrue(len(bm.to_dict()) > 0)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def testbasemodel_save(self):
        bm = BaseModel()
        bm1 = bm.updated_at
        bm.save()
        self.assertNotEqual(bm1, bm.updated_at)

    def test_basemodel_newsave(self):
        bm = BaseModel()
        if os.path.exists("file.json"):
            os.remove("file.json")
        bm.save()
        self.assertTrue(os.path.exists("file.json"))

if __name__ == '__main__':
    unittest.main()
