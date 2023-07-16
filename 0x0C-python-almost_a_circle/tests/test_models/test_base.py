#!/usr/bin/python3
"""Define a class to test the base module"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class BaseTest(unittest.TestCase):
    """Test the id of the Base class"""

    def test_id(self):
        """case1 test without value"""
        b1 = Base()
        self.assertTrue(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b1.id, b2.id - 1)

        """case2 test withe value"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        """case3 test without value after with value"""
        b4 = Base()
        self.assertEqual(b4.id, 3)
        self.assertEqual(b2.id, b4.id - 1)

    def test_Float(self):
        """case4 test with float number"""
        b5 = Base(1.5)
        self.assertEqual(b5.id, 1.5)

        """case5 test with float nan"""
        b6 = Base(float("nan"))
        self.assertNotEqual(b6.id, float("nan"))
        self.assertIsInstance(b6.id, float)

        """case6 test with float inf"""
        b7 = Base(float("inf"))
        self.assertEqual(b7.id, float("inf"))

    def test_id(self):
        """case6 test without value new func"""
        b8 = Base()
        self.assertTrue(b8.id, 1)

    def test_strId(self):
        """test str Id"""
        self.assertEqual(Base("hi").id, "hi")

    def test_listId(self):
        """test list Id"""
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_tupleId(self):
        """test tuple Id"""
        self.assertEqual(Base((1, 2, 3)).id, (1, 2, 3))

    def test_setId(self):
        """test set Id"""
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})

    def test_dictId(self):
        """test dictionry Id"""
        self.assertEqual(Base({"one": 1, "tow": 2}).id, {"one": 1, "tow": 2})

    def test_boolId(self):
        """test bollean Id"""
        self.assertEqual(Base(True).id, True)

    def test_compId(self):
        """test complex Id"""
        self.assertEqual(Base(complex(7)).id, complex(7))

    def test_to_json_string_Rectangle(self):
        """test the static method to_json_string with Rectangle class"""
        r1 = Rectangle(5, 3, 6, 2)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        obj = {'id': r1.id, 'width': 5, 'height': 3, 'x': 6, 'y': 2}
        self.assertDictEqual(dictionary, obj)
        list1 = Base.to_json_string([obj])
        self.assertSequenceEqual(json_dict, list1)
        self.assertIsInstance(json_dict, str)

    def test_to_json_string_Rectangle1(self):
        """test tow dictionry"""
        r1 = Rectangle(5, 3, 6, 2)
        r2 = Rectangle(10, 2, 1, 5, 3)
        dictionary = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        json_dict = Base.to_json_string([dictionary, dictionary2])
        obj = {'id': r1.id, 'width': 5, 'height': 3, 'x': 6, 'y': 2}
        obj2 = {'id': 3, 'width': 10, 'height': 2, 'x': 1, 'y': 5}
        self.assertDictEqual(dictionary, obj)
        self.assertDictEqual(dictionary2, obj2)
        list1 = Base.to_json_string([obj, obj2])
        self.assertSequenceEqual(json_dict, list1)
        self.assertIsInstance(json_dict, str)

    def test_to_json_string(self):
        """test None value"""
        dictionary = None
        json_dict = Base.to_json_string([dictionary])
        self.assertSequenceEqual(json_dict, "[null]")
        self.assertIsInstance(json_dict, str)

    def test_to_json_string1(self):
        """test empty list"""
        json_dict = Base.to_json_string([])
        self.assertSequenceEqual(json_dict, "[]")
        self.assertIsInstance(json_dict, str)

    def test_to_json_string2(self):
        """test None"""
        json_dict = Base.to_json_string(None)
        self.assertSequenceEqual(json_dict, "[]")
        self.assertIsInstance(json_dict, str)

    def test_to_json_string3(self):
        """test integer list"""
        dictionary = 5
        json_dict = Base.to_json_string([dictionary])
        self.assertSequenceEqual(json_dict, "[5]")
        self.assertIsInstance(json_dict, str)

    def test_to_json_string_Square(self):
        """test the static method to_json_string with Square class"""
        r1 = Square(5, 6, 2)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        obj = {'id': r1.id, 'size': 5, 'x': 6, 'y': 2}
        self.assertDictEqual(dictionary, obj)
        list1 = Base.to_json_string([obj])
        self.assertSequenceEqual(json_dict, list1)
        self.assertIsInstance(json_dict, str)

    def test_to_json_string_Square1(self):
        """test tow dictionry"""
        r1 = Square(5, 6, 2)
        r2 = Square(10, 1, 5, 3)
        dictionary = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        json_dict = Base.to_json_string([dictionary, dictionary2])
        obj = {'id': r1.id, 'size': 5, 'x': 6, 'y': 2}
        obj2 = {'id': 3, 'size': 10, 'x': 1, 'y': 5}
        self.assertDictEqual(dictionary, obj)
        self.assertDictEqual(dictionary2, obj2)
        list1 = Base.to_json_string([obj, obj2])
        self.assertSequenceEqual(json_dict, list1)
        self.assertIsInstance(json_dict, str)


if __name__ == "__main__":
    unittest.main()
