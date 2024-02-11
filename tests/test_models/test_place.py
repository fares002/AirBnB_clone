#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    place 
    """

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

    def testnoargsinstantiates(self):
        self.assertEqual(Place, type(Place()))

    def testnewinstancestoredinobjects(self):
        self.assertIn(Place(), models.storage.all().values())

    def testidispublicstr(self):
        self.assertEqual(str, type(Place().id))

    def testcreatedatispublicdatetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def testupdatedatispublicdatetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def testcityidispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(my_place))
        self.assertNotIn("city_id", my_place.__dict__)

    def testuseridispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(my_place))
        self.assertNotIn("user_id", my_place.__dict__)

    def testnameispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(my_place))
        self.assertNotIn("name", my_place.__dict__)

    def testdescriptionispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(my_place))
        self.assertNotIn("desctiption", my_place.__dict__)

    def testnumberroomsispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(my_place))
        self.assertNotIn("number_rooms", my_place.__dict__)

    def testnumberbathroomsispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(my_place))
        self.assertNotIn("number_bathrooms", my_place.__dict__)

    def testmaxguestispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(my_place))
        self.assertNotIn("max_guest", my_place.__dict__)

    def testpricebynightispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(my_place))
        self.assertNotIn("price_by_night", my_place.__dict__)

    def testlatitudeispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(my_place))
        self.assertNotIn("latitude", my_place.__dict__)

    def testlongitudeispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(my_place))
        self.assertNotIn("longitude", my_place.__dict__)

    def testamenityidsispublicclassattribute(self):
        my_place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(my_place))
        self.assertNotIn("amenity_ids", my_place.__dict__)

    def testtwoplacesuniqueids(self):
        my_place1 = Place()
        my_place2 = Place()
        self.assertNotEqual(my_place1.id, my_place2.id)

    def testtwoplacesdifferentcreatedat(self):
        my_place1 = Place()
        sleep(0.05)
        my_place2 = Place()
        self.assertLess(my_place1.created_at, my_place2.created_at)

    def testtwoplacesdifferentupdatedat(self):
        my_place1 = Place()
        sleep(0.05)
        my_place2 = Place()
        self.assertLess(my_place1.updated_at, my_place2.updated_at)

    def teststrrepresentation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        my_place = Place()
        my_place.id = "777777"
        my_place.created_at = my_place.updated_at = my_date
        my_place_str = my_place.__str__()
        self.assertIn("[Place] (777777)", my_place_str)
        self.assertIn("'id': '777777'", my_place_str)
        self.assertIn("'created_at': " + my_date_repr, my_place_str)
        self.assertIn("'updated_at': " + my_date_repr, my_place_str)

    def testargsunused(self):
        my_place = Place(None)
        self.assertNotIn(None, my_place.__dict__.values())

    def testinstantiationwithkwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        my_place = Place(id="777", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(my_place.id, "777")
        self.assertEqual(my_place.created_at, my_date)
        self.assertEqual(my_place.updated_at, my_date)

    def testinstantiationwithNonekwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """
    save1 
    """

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
        my_place = Place()
        sleep(0.05)
        first_updated_at = my_place.updated_at
        my_place.save()
        self.assertLess(first_updated_at, my_place.updated_at)

    def testtwosaves(self):
        my_place = Place()
        sleep(0.05)
        first_updated_at = my_place.updated_at
        my_place.save()
        second_updated_at = my_place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_place.save()
        self.assertLess(second_updated_at, my_place.updated_at)

    def testsavewitharg(self):
        my_place = Place()
        with self.assertRaises(TypeError):
            my_place.save(None)

    def testsaveupdatesfile(self):
        my_place = Place()
        my_place.save()
        my_place_id = "Place." + my_place.id
        with open("file.json", "r") as f:
            self.assertIn(my_place_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    place
    """

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

    def testtodicttype(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def testtodictcontainscorrectkeys(self):
        my_place = Place()
        self.assertIn("id", my_place.to_dict())
        self.assertIn("created_at", my_place.to_dict())
        self.assertIn("updated_at", my_place.to_dict())
        self.assertIn("__class__", my_place.to_dict())

    def testtodictcontainsaddedattributes(self):
        my_place = Place()
        my_place.middle_name = "Johnson"
        my_place.my_number = 777
        self.assertEqual("Johnson", my_place.middle_name)
        self.assertIn("my_number", my_place.to_dict())

    def testtodictdatetimeattributesarestrs(self):
        my_place = Place()
        my_place_dict = my_place.to_dict()
        self.assertEqual(str, type(my_place_dict["id"]))
        self.assertEqual(str, type(my_place_dict["created_at"]))
        self.assertEqual(str, type(my_place_dict["updated_at"]))

    def testtodictoutput(self):
        my_date = datetime.today()
        my_place = Place()
        my_place.id = "777777"
        my_place.created_at = my_place.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Place',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(my_place.to_dict(), to_dict)

    def testcontrasttodictdunderdict(self):
        my_place = Place()
        self.assertNotEqual(my_place.to_dict(), my_place.__dict__)

    def testtodictwitharg(self):
        my_place = Place()
        with self.assertRaises(TypeError):
            my_place.to_dict(None)


if __name__ == "__main__":
    unittest.main()
