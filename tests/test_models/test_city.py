#!/usr/bin/python3
"""
Module for City unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """
    city
    """

    def testnoargsinstantiates(self):
        self.assertEqual(City, type(City()))

    def testnewinstancestoredinobjects(self):
        self.assertIn(City(), models.storage.all().values())

    def testidispublicstr(self):
        self.assertEqual(str, type(City().id))

    def testcreatedatispublicdatetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def teststateidispublicclassattribute(self):
        my_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(my_city))
        self.assertNotIn("state_id", my_city.__dict__)

    def testnameispublicclassattribute(self):
        my_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(my_city))
        self.assertNotIn("name", my_city.__dict__)

    def testtwocitiesuniqueids(self):
        my_city1 = City()
        my_city2 = City()
        self.assertNotEqual(my_city1.id, my_city2.id)

    def testtwocitiesdifferentcreatedat(self):
        my_city1 = City()
        sleep(0.05)
        my_city2 = City()
        self.assertLess(my_city1.created_at, my_city2.created_at)

    def testtwocitiesdifferentupdatedat(self):
        my_city1 = City()
        sleep(0.05)
        my_city2 = City()
        self.assertLess(my_city1.updated_at, my_city2.updated_at)

    def teststrrepresentation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        my_city = City()
        my_city.id = "777777"
        my_city.created_at = my_city.updated_at = my_date
        my_city_str = my_city.__str__()
        self.assertIn("[City] (777777)", my_city_str)
        self.assertIn("'id': '777777'", my_city_str)
        self.assertIn("'created_at': " + my_date_repr, my_city_str)
        self.assertIn("'updated_at': " + my_date_repr, my_city_str)

    def testargsunused(self):
        my_city = City(None)
        self.assertNotIn(None, my_city.__dict__.values())

    def testinstantiationwithkwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        my_city = City(id="345", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(my_city.id, "345")
        self.assertEqual(my_city.created_at, my_date)
        self.assertEqual(my_city.updated_at, my_date)

    def testinstantiationwithNonekwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """
    city
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def testonesave(self):
        my_city = City()
        sleep(0.05)
        first_updated_at = my_city.updated_at
        my_city.save()
        self.assertLess(first_updated_at, my_city.updated_at)

    def testtwosaves(self):
        my_city = City()
        sleep(0.05)
        first_updated_at = my_city.updated_at
        my_city.save()
        second_updated_at = my_city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_city.save()
        self.assertLess(second_updated_at, my_city.updated_at)

    def testsavewitharg(self):
        my_city = City()
        with self.assertRaises(TypeError):
            my_city.save(None)

    def testsaveupdatesfile(self):
        my_city = City()
        my_city.save()
        my_city_id = "City." + my_city.id
        with open("file.json", "r") as f:
            self.assertIn(my_city_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """
    ciry
    """

    def testtodicttype(self):
        self.assertTrue(dict, type(City().to_dict()))

    def testtodictcontainscorrectkeys(self):
        my_city = City()
        self.assertIn("id", my_city.to_dict())
        self.assertIn("created_at", my_city.to_dict())
        self.assertIn("updated_at", my_city.to_dict())
        self.assertIn("__class__", my_city.to_dict())

    def testtodictcontainsaddedattributes(self):
        my_city = City()
        my_city.middle_name = "Johnson"
        my_city.my_number = 777
        self.assertEqual("Johnson", my_city.middle_name)
        self.assertIn("my_number", my_city.to_dict())

    def testtodictdatetimeattributesarestrs(self):
        my_city = City()
        my_city_dict = my_city.to_dict()
        self.assertEqual(str, type(my_city_dict["id"]))
        self.assertEqual(str, type(my_city_dict["created_at"]))
        self.assertEqual(str, type(my_city_dict["updated_at"]))

    def testtodictoutput(self):
        my_date = datetime.today()
        my_city = City()
        my_city.id = "123456"
        my_city.created_at = my_city.updated_at = my_date
        to_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(my_city.to_dict(), to_dict)

    def testcontrasttodictdunderdict(self):
        my_city = City()
        self.assertNotEqual(my_city.to_dict(), my_city.__dict__)

    def testtodictwitharg(self):
        my_city = City()
        with self.assertRaises(TypeError):
            my_city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
