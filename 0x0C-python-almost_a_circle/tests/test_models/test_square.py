#!/usr/bin/python3
"""Define a class TestRectungle inherts from unittest
test the modle Rectungle"""
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import unittest
import io
import sys


class TestSquare(unittest.TestCase):
    """class test the modle Rectungle"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_idInt(self):
        """case1 test without value"""
        R1 = Square(10, 1)
        self.assertIsInstance(R1, Base)
        self.assertIsInstance(R1, Rectangle)

        """case2 test with value"""
        R2 = Square(10, 0, 0, 12)
        self.assertEqual(R2.id, 12)

        """case3 test without value raise id"""
        R3 = Square(10, 2)
        self.assertEqual(R3.id - 1, R1.id)

    def test_noArg(self):
        """test without argument"""
        with self.assertRaises(TypeError):
            Square()

    def test_size(self):
        """case1 test assign integer to size"""
        r1 = Square(10)
        self.assertEqual(r1.size, 10)
        r1.size = 12
        self.assertEqual(r1.size, 12)

    def test_size2(self):
        """case2 test assign string to size"""
        with self.assertRaises(TypeError):
            Square("4")

        with self.assertRaises(TypeError):
            Square("school")

    def test_size3(self):
        """case3 test assign zero or negative number to size"""
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)

    def test_size4(self):
        """case4 test assign float number to size"""
        with self.assertRaises(TypeError):
            Square(1.4)
        with self.assertRaises(TypeError):
            Square(float("nan"), 2)

    def test_x(self):
        """case1 test assign integer to x"""
        r1 = Square(10, 5)
        self.assertEqual(r1.x, 5)
        r1.x = 2
        self.assertEqual(r1.x, 2)

        r2 = Square(10, 0)
        self.assertEqual(r2.x, 0)

    def test_x2(self):
        """case2 test assign string to x"""
        with self.assertRaises(TypeError):
            Square(4, "2")
        with self.assertRaises(TypeError):
            Square(2, "school")

    def test_x3(self):
        """case3 test assgin negative number to x"""
        with self.assertRaises(ValueError):
            Square(3, -15)
        with self.assertRaises(ValueError):
            Square(5, -2)

    def test_x4(self):
        """case4 test assign float number to x"""
        with self.assertRaises(TypeError):
            Square(4, 2.5)
        with self.assertRaises(TypeError):
            Square(2, float("inf"))

    def test_y(self):
        """case1 test assign integer to y"""
        r1 = Square(10, 5, 6)
        self.assertEqual(r1.y, 6)
        r1.y = 3
        self.assertEqual(r1.y, 3)

        r2 = Square(10, 5, 0)
        self.assertEqual(r2.y, 0)

    def test_y2(self):
        """case2 test assign string to y"""
        with self.assertRaises(TypeError):
            Square(4, 6, "2")

        with self.assertRaises(TypeError):
            Square(2, 3, "school")

    def test_y3(self):
        """case3 test assgin negative number to y"""
        with self.assertRaises(ValueError):
            Square(6, 6, -15)
        with self.assertRaises(ValueError):
            Square(5, 7, -2)

    def test_y4(self):
        """case4 test assign float number to y"""
        with self.assertRaises(TypeError):
            Square(4, 6, 2.5)
        with self.assertRaises(TypeError):
            Square(2, 8, float("inf"))

    def test_area(self):
        """test area function with only size values"""
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)
        r1 = Square(6)
        self.assertEqual(r1.area(), 36)
        with self.assertRaises(ValueError):
            Square(0)

    def test_display(self):
        """test display function with only size values"""
        r1 = Square(3)
        displayOutput = io.StringIO()
        sys.stdout = displayOutput
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("###\n###\n###\n", displayOutput.getvalue())

    def test_display2(self):
        """test the output of the function with values"""
        r1 = Square(3, 2, 3)
        displayOutput = io.StringIO()
        sys.stdout = displayOutput
        r1.display()
        sys.stdout = sys.__stdout__
        str1 = "\n\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(str1, displayOutput.getvalue())

    def test_display3(self):
        """test the output of the function witheout y value"""
        r1 = Square(3, 2)
        displayOutput = io.StringIO()
        sys.stdout = displayOutput
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("  ###\n  ###\n  ###\n", displayOutput.getvalue())

    def test_str(self):
        """test str return value"""
        r1 = Square(6, 2, 1, 12)
        self.assertMultiLineEqual(str(r1), "[Square] (12) 2/1 - 6")
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 6")

    def test_str2(self):
        """test with zero y x value"""
        r1 = Square(6, 0, 0, 12)
        self.assertEqual(str(r1), "[Square] (12) 0/0 - 6")

    def test_str3(self):
        """test with string id value"""
        r1 = Square(4, 0, 0, "hi")
        self.assertEqual(str(r1), "[Square] (hi) 0/0 - 4")

    def test_update(self):
        """test no values with *argv"""
        r1 = Square(4, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 4")
        """empty update"""
        r1.update()
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 4")

    def test_update1(self):
        """test regular valuse 'one value with *argv'"""
        r1 = Square(6, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 6")
        """update id"""
        r1.update(2)
        self.assertEqual(str(r1), "[Square] (2) 1/2 - 6")
        self.assertEqual(r1.id, 2)

    def test_update2(self):
        """test regular valuse 'tow value with *argv'"""
        r1 = Square(6, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 6")
        """update id and size"""
        r1.update(2, 3)
        self.assertEqual(str(r1), "[Square] (2) 1/2 - 3")
        self.assertTrue(r1.id == 2 and r1.size == 3)

    def test_update3(self):
        """test regular valuse with *argv"""
        r1 = Square(4, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 4")
        """update all"""
        r1.update(2, 3, 5, 6)
        self.assertEqual(str(r1), "[Square] (2) 5/6 - 3")

    def test_update4(self):
        """test string one value with *argv"""
        r1 = Square(6, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 6")
        """update string id value"""
        r1.update("hi")
        self.assertEqual(str(r1), "[Square] (hi) 1/2 - 6")

    def test_updateRasise(self):
        """test wrong value with *argv"""
        r1 = Square(6, 1, 2, 12)
        self.assertEqual(str(r1), f"[Square] (12) 1/2 - 6")
        """update string size value"""
        with self.assertRaises(TypeError):
            r1.update(6, "5")
        """update zero size value"""
        with self.assertRaises(ValueError):
            r1.update(6, 0)
        """update float size value"""
        with self.assertRaises(TypeError):
            r1.update(6, 1.5)
        """update negative value"""
        with self.assertRaises(ValueError):
            r1.update(6, -1, 4)
        """update tuple value"""
        with self.assertRaises(TypeError):
            r1.update(6, 1, 1, (4, 5))

    def test_updatekw(self):
        """test regular valuse 'one value with **kwargv'"""
        r1 = Square(3, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 3")
        """update id"""
        r1.update(id=2)
        self.assertEqual(str(r1), "[Square] (2) 1/2 - 3")
        self.assertEqual(r1.id, 2)

    def test_updateargs(self):
        """test regular valuse 'one value with *args and  **kwargv'"""
        r1 = Square(4, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 4")
        """update id"""
        r1.update(3, 2, x=10)
        self.assertEqual(str(r1), "[Square] (3) 1/2 - 2")
        self.assertNotEqual(r1.x, 10)

    def test_updatekw2(self):
        """test regular valuse one value with **kwargv'"""
        r1 = Square(6, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 6")
        """update size"""
        r1.update(size=2)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 2")
        self.assertTrue(r1.size == 2)

    def test_updatekw2y(self):
        """test regular valuse one value with **kwargv'"""
        r1 = Square(4, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 4")
        """update x"""
        r1.update(x=3)
        self.assertEqual(str(r1), "[Square] (12) 3/2 - 4")
        self.assertTrue(r1.x == 3)

    def test_updatekw3(self):
        """test regular valuse with **kwargv"""
        r1 = Square(6, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 6")
        """update all"""
        r1.update(x=5, size=3, id=1, y=6)
        self.assertEqual(str(r1), "[Square] (1) 5/6 - 3")

    def test_updatekw4(self):
        """test string one value with **kwargv"""
        r1 = Square(4, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 4")
        """update string id value"""
        r1.update(id="hi")
        self.assertEqual(str(r1), "[Square] (hi) 1/2 - 4")

    def test_updateKwRasise(self):
        """test wrong value with *argv"""
        r1 = Square(6, 1, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 1/2 - 6")
        """update string size value"""
        with self.assertRaises(TypeError):
            r1.update(x=6, size="5")
        """update zero size value"""
        with self.assertRaises(ValueError):
            r1.update(id=6, size=0)
        """update float y value"""
        with self.assertRaises(TypeError):
            r1.update(x=6, y=1.5)
        """update negative value"""
        with self.assertRaises(ValueError):
            r1.update(x=6, y=1, size=-1)
        """update tuple value"""
        with self.assertRaises(TypeError):
            r1.update(id=6, y=1, x=(4, 5))

    def test_to_dictionary(self):
        """test the return value of the function with one values"""
        r1 = Square(10)
        r1_dict = r1.to_dictionary()
        dict1 = {'id': r1.id, 'size': 10, 'x': 0, 'y': 0}
        self.assertEqual(dict1, r1_dict)

    def test_to_dictionary1(self):
        """test the return value of the function with tow values"""
        r1 = Square(10, 1)
        r1_dict = r1.to_dictionary()
        dict1 = {'id': r1.id, 'size': 10, 'x': 1, 'y': 0}
        self.assertEqual(dict1, r1_dict)

    def test_to_dictionary2(self):
        """test the return value of the function with three values"""
        r1 = Square(10, 1, 5)
        r1_dict = r1.to_dictionary()
        dict1 = {'id': r1.id, 'size': 10, 'x': 1, 'y': 5}
        self.assertEqual(dict1, r1_dict)

    def test_to_dictionary3(self):
        """test the return value of the function with four values"""
        r1 = Square(10, 1, 5, 3)
        r1_dict = r1.to_dictionary()
        dict1 = {'id': 3, 'size': 10, 'x': 1, 'y': 5}
        self.assertEqual(dict1, r1_dict)


if __name__ == "__main__":
    unittest.main()
