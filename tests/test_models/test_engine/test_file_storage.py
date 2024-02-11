#!/usr/bin/python3
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test1(unittest.TestCase):
    """

    """
    def fun1(self):
        self.assertEqual(type(FileStorage()).FileStorage)

    def fun2(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def fun3(self):
        self.assertEqual(type(models.storage), FileStorage)

class test2(unittest.TestCase):

    def setup(self):
        self.test_file = "test_file.json"

    def down(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def fun4(self):
        self.assertEqual(dict, type(models.storage.all()))

    def fun5(self):
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id). models.storage.all())

    def fun6(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def fun7(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def fun8(self):
        Ob1 = BaseModel()
        ob2 = BaseModel()
        models.storage.new(ob1)
        models.storage.new(ob2)
        models.storage.save()

        st1 = FileStorage()
        st1.reloaded()

        self.assertTrue(st1.all().get("BaseModel.{}".format(ob1.id)) is not None)
        self.assertTrue(st1.all().get("BaseModel".format(ob2.id)) is not None)

    def fun9(self):
        ob = BaseModel()
        models.storage.new(ob)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def fun10(self):
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

if __name__ == "__main__":
    unittest.main()
