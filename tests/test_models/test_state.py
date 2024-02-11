#!/usr/bin/python3
"""
Module for State unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """
    instanatiom 
    """

    def testnoargsinstantiates(self):
        self.assertEqual(State, type(State()))

    def testnewinstancestoredinobjects(self):
        self.assertIn(State(), models.storage.all().values())

    def testidispublicstr(self):
        self.assertEqual(str, type(State().id))

    def testcreatedatispublicdatetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def testnameispublicclassattribute(self):
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_two_states_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def testtwostatesdifferentcreatedat(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def testtwostatesdifferentupdatedat(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def teststrrepresentation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        state = State()
        state.id = "777777"
        state.created_at = state.updated_at = my_date
        state_str = state.__str__()
        self.assertIn("[State] (777777)", state_str)
        self.assertIn("'id': '777777'", state_str)
        self.assertIn("'created_at': " + my_date_repr, state_str)
        self.assertIn("'updated_at': " + my_date_repr, state_str)

    def testargsunused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def testinstantiationwithkwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        state = State(id="345", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, my_date)
        self.assertEqual(state.updated_at, my_date)

    def testinstantiationwithNonekwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
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
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def testtwosaves(self):
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        second_updated_at = state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        state.save()
        self.assertLess(second_updated_at, state.updated_at)

    def testsavewitharg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def testsaveupdatesfile(self):
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())


class TestState_to_dict(unittest.TestCase):
    """
    to dict 
    """

    def testtodicttype(self):
        self.assertTrue(dict, type(State().to_dict()))

    def testtodictcontainscorrectkeys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def testtodictcontainsaddedattributes(self):
        state = State()
        state.middle_name = "Johnson"
        state.my_number = 777
        self.assertEqual("Johnson", state.middle_name)
        self.assertIn("my_number", state.to_dict())

    def testtodictdatetimeattributesarestrs(self):
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def testtodictoutput(self):
        my_date = datetime.today()
        state = State()
        state.id = "777777"
        state.created_at = state.updated_at = my_date
        tdict = {
            'id': '777777',
            '__class__': 'State',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), tdict)

    def testcontrasttodictdunderdict(self):
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def testtodictwitharg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == "__main__":
    unittest.main()
