#!/usr/bin/python3
"""
Module for testing Review
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """
    revidw
    """

    def testnoargsinstantiates(self):
        self.assertEqual(Review, type(Review()))

    def testnewinstancestoredinobjects(self):
        self.assertIn(Review(), models.storage.all().values())

    def testidispublicstr(self):
        self.assertEqual(str, type(Review().id))

    def testcreatedatispublicdatetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def testupdatedatispublicdatetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def testplaceidispublicclassattribute(self):
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def testuseridispublicclassattribute(self):
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def testtextispublicclassattribute(self):
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def testtworeviewsuniqueids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def testtworeviewsdifferentcreatedat(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def testtworeviewsdifferentupdatedat(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def teststrrepresentation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        review = Review()
        review.id = "777777"
        review.created_at = review.updated_at = my_date
        review_str = review.__str__()
        self.assertIn("[Review] (777777)", review_str)
        self.assertIn("'id': '777777'", review_str)
        self.assertIn("'created_at': " + my_date_repr, review_str)
        self.assertIn("'updated_at': " + my_date_repr, review_str)

    def testargsunused(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def testinstantiationwithkwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        review = Review(id="777", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(review.id, "777")
        self.assertEqual(review.created_at, my_date)
        self.assertEqual(review.updated_at, my_date)

    def testinstantiationwithNonekwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """
    save
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
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def testtwosaves(self):
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        second_updated_at = review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        review.save()
        self.assertLess(second_updated_at, review.updated_at)

    def testsavewitharg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def testsaveupdatesfile(self):
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())


class TestReview_to_dict(unittest.TestCase):
    """
    to dict
    """

    def testtodicttype(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def testtodictcontainscorrectkeys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def testtodictcontainsaddedattributes(self):
        review = Review()
        review.middle_name = "Johnson"
        review.my_number = 777
        self.assertEqual("Johnson", review.middle_name)
        self.assertIn("my_number", review.to_dict())

    def testtodictdatetimeattributesarestrs(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def testtodictoutput(self):
        my_date = datetime.today()
        review = Review()
        review.id = "777777"
        review.created_at = review.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Review',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), to_dict)

    def testcontrastodictdunderdict(self):
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def testtodictwitharg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
