#!/usr/bin/python3
"""

"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()

        modl = my_model.to_dict()

        self.assertIsInstance(modl, dict)

        self.assertEqual(modl["__class__"], 'BaseModel')
        self.assertEqual(modl['id'], my_model.id)
        self.assertEqual(modl['created_at'], my_model.created_at.isoformat())
        self.assertEqual(modl["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
