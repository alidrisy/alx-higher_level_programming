#!/usr/bin/python3
"""Define a class TestRectungle inherts from unittest
test the modle Rectungle"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import io
import sys


class TestRectungle(unittest.TestCase):
    """class test the modle Rectungle"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_idInt(self):
        """case1 test without value"""
        R1 = Rectangle(10, 1)
        self.assertIsInstance(R1, Base)

        """case2 test with value"""
        R2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(R2.id, 12)

        """case3 test without value raise id"""
        R3 = Rectangle(10, 2)
        self.assertEqual(R3.id - 1, R1.id)

    def test_noArg(self):
        """test without argument"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_oneArg(self):
        """test with one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width_priv(self):
        """test access private attr"""
        r1 = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            print(r1.__width)

    def test_width(self):
        """case1 test assign integer to width"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r1.width = 12
        self.assertEqual(r1.width, 12)

    def test_width2(self):
        """case2 test assign string to width"""
        with self.assertRaises(TypeError):
            Rectangle("4", 2)

        with self.assertRaises(TypeError):
            Rectangle("school", 2)

    def test_width3(self):
        """case3 test assign zero or negative number to width"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(-5, 2)

    def test_width4(self):
        """case4 test assign float number to width"""
        with self.assertRaises(TypeError):
            Rectangle(1.4, 2)
        with self.assertRaises(TypeError):
            Rectangle(float("nan"), 2)

    def test_height_priv(self):
        """test access private attr"""
        r1 = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            print(r1.__height)

    def test_height(self):
        """case1 test assign integer to height"""
        h1 = Rectangle(10, 2)
        self.assertEqual(h1.height, 2)
        h1.height = 3
        self.assertEqual(h1.height, 3)

    def test_height2(self):
        """case2 test assign string to height"""
        with self.assertRaises(TypeError):
            Rectangle(4, "2")
        with self.assertRaises(TypeError):
            Rectangle(2, "school")

    def test_height3(self):
        """case3 test assign zero or negative number to height"""
        with self.assertRaises(ValueError):
            Rectangle(3, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, -2)

    def test_height4(self):
        """case4 test assign float number to height"""
        with self.assertRaises(TypeError):
            Rectangle(4, 2.5)
        with self.assertRaises(TypeError):
            Rectangle(2, float("inf"))

    def test_x_priv(self):
        """test access private attr"""
        r1 = Rectangle(10, 2, 3, 4)
        with self.assertRaises(AttributeError):
            print(r1.__x)

    def test_x(self):
        """case1 test assign integer to x"""
        r1 = Rectangle(10, 2, 5)
        self.assertEqual(r1.x, 5)
        r1.x = 2
        self.assertEqual(r1.x, 2)

        r2 = Rectangle(10, 2, 0)
        self.assertEqual(r2.x, 0)

    def test_x2(self):
        """case2 test assign string to x"""
        with self.assertRaises(TypeError):
            Rectangle(4, 3, "2")
        with self.assertRaises(TypeError):
            Rectangle(2, 5, "school")

    def test_x3(self):
        """case3 test assgin negative number to x"""
        with self.assertRaises(ValueError):
            Rectangle(3, 6, -15)
        with self.assertRaises(ValueError):
            Rectangle(5, 3, -2)

    def test_x4(self):
        """case4 test assign float number to x"""
        with self.assertRaises(TypeError):
            Rectangle(4, 7, 2.5)
        with self.assertRaises(TypeError):
            Rectangle(2, 5, float("inf"))

    def test_y_priv(self):
        """test access private attr"""
        r1 = Rectangle(10, 2, 3, 4)
        with self.assertRaises(AttributeError):
            print(r1.__y)

    def test_y(self):
        """case1 test assign integer to y"""
        r1 = Rectangle(10, 2, 5, 6)
        self.assertEqual(r1.y, 6)
        r1.y = 3
        self.assertEqual(r1.y, 3)

        r2 = Rectangle(10, 2, 5, 0)
        self.assertEqual(r2.y, 0)

    def test_y2(self):
        """case2 test assign string to y"""
        with self.assertRaises(TypeError):
            Rectangle(4, 3, 6, "2")

        with self.assertRaises(TypeError):
            Rectangle(2, 5, 3, "school")

    def test_y3(self):
        """case3 test assgin negative number to y"""
        with self.assertRaises(ValueError):
            Rectangle(3, 6, 6, -15)
        with self.assertRaises(ValueError):
            Rectangle(5, 3, 7, -2)

    def test_y4(self):
        """case4 test assign float number to y"""
        with self.assertRaises(TypeError):
            Rectangle(4, 7, 6, 2.5)
        with self.assertRaises(TypeError):
            Rectangle(2, 5, 8, float("inf"))

    def test_area(self):
        """test area function with only width and height values"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1 = Rectangle(3, 10)
        self.assertEqual(r1.area(), 30)
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_display(self):
        """test display function with only width and height values"""
        r1 = Rectangle(3, 2)
        displayOutput = io.StringIO()
        sys.stdout = displayOutput
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("###\n###\n", displayOutput.getvalue())

    def test_display2(self):
        """test the output of the function with values"""
        r1 = Rectangle(3, 2, 2, 3)
        displayOutput = io.StringIO()
        sys.stdout = displayOutput
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("\n\n\n  ###\n  ###\n", displayOutput.getvalue())

    def test_display3(self):
        """test the output of the function witheout y value"""
        r1 = Rectangle(3, 2, 2)
        displayOutput = io.StringIO()
        sys.stdout = displayOutput
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("  ###\n  ###\n", displayOutput.getvalue())

    def test_str(self):
        """test str return value"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertMultiLineEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_str2(self):
        """test with zero y x value"""
        r1 = Rectangle(4, 6, 0, 0, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 0/0 - 4/6")

    def test_str3(self):
        """test with string id value"""
        r1 = Rectangle(4, 6, 0, 0, "hi")
        self.assertEqual(str(r1), "[Rectangle] (hi) 0/0 - 4/6")

    def test_update(self):
        """test no values with *argv"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """empty update"""
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")

    def test_update1(self):
        """test regular valuse 'one value with *argv'"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update id"""
        r1.update(2)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/2 - 4/6")
        self.assertEqual(r1.id, 2)

    def test_update2(self):
        """test regular valuse 'tow value with *argv'"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update id and width"""
        r1.update(2, 3)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/2 - 3/6")
        self.assertTrue(r1.id == 2 and r1.width == 3)

    def test_update3(self):
        """test regular valuse with *argv"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update all"""
        r1.update(2, 3, 4, 5, 6)
        self.assertEqual(str(r1), "[Rectangle] (2) 5/6 - 3/4")

    def test_update4(self):
        """test string one value with *argv"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update string id value"""
        r1.update("hi")
        self.assertEqual(str(r1), "[Rectangle] (hi) 1/2 - 4/6")

    def test_updateRasise(self):
        """test wrong value with *argv"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), f"[Rectangle] (12) 1/2 - 4/6")
        """update string width value"""
        with self.assertRaises(TypeError):
            r1.update(6, "5")
        """update zero width value"""
        with self.assertRaises(ValueError):
            r1.update(6, 0)
        """update float width value"""
        with self.assertRaises(TypeError):
            r1.update(6, 1.5)
        """update negative value"""
        with self.assertRaises(ValueError):
            r1.update(6, 1, -1, 4)
        """update tuple value"""
        with self.assertRaises(TypeError):
            r1.update(6, 1, 1, (4, 5))

    def test_updatekw(self):
        """test regular valuse 'one value with **kwargv'"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update id"""
        r1.update(id=2)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/2 - 4/6")
        self.assertEqual(r1.id, 2)

    def test_updateargs(self):
        """test regular valuse 'one value with *args and  **kwargv'"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update id"""
        r1.update(3, 2, 4, x=10)
        self.assertEqual(str(r1), "[Rectangle] (3) 1/2 - 2/4")
        self.assertNotEqual(r1.x, 10)

    def test_updatekw2(self):
        """test regular valuse one value with **kwargv'"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update width"""
        r1.update(width=2)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 2/6")
        self.assertTrue(r1.width == 2)

    def test_updatekw2y(self):
        """test regular valuse one value with **kwargv'"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update x"""
        r1.update(x=3)
        self.assertEqual(str(r1), "[Rectangle] (12) 3/2 - 4/6")
        self.assertTrue(r1.x == 3)

    def test_updatekw3(self):
        """test regular valuse with **kwargv"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update all"""
        r1.update(x=5, width=3, height=4, id=1, y=6)
        self.assertEqual(str(r1), "[Rectangle] (1) 5/6 - 3/4")

    def test_updatekw4(self):
        """test string one value with **kwargv"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 1/2 - 4/6")
        """update string id value"""
        r1.update(id="hi")
        self.assertEqual(str(r1), "[Rectangle] (hi) 1/2 - 4/6")

    def test_updateKwRasise(self):
        """test wrong value with *argv"""
        r1 = Rectangle(4, 6, 1, 2, 12)
        self.assertEqual(str(r1), f"[Rectangle] (12) 1/2 - 4/6")
        """update string width value"""
        with self.assertRaises(TypeError):
            r1.update(x=6, width="5")
        """update zero width value"""
        with self.assertRaises(ValueError):
            r1.update(id=6, height=0)
        """update float width value"""
        with self.assertRaises(TypeError):
            r1.update(x=6, y=1.5)
        """update negative value"""
        with self.assertRaises(ValueError):
            r1.update(x=6, y=1, width=-1, height=4)
        """update tuple value"""
        with self.assertRaises(TypeError):
            r1.update(id=6, y=1, height=1, x=(4, 5))

    def test_to_dictionary(self):
        """test the return value of the function with tow values"""
        r1 = Rectangle(10, 2)
        r1_dict = r1.to_dictionary()
        dict1 = {'id': r1.id, 'width': 10, 'height': 2, 'x': 0, 'y': 0}
        self.assertEqual(dict1, r1_dict)

    def test_to_dictionary1(self):
        """test the return value of the function with three values"""
        r1 = Rectangle(10, 2, 1)
        r1_dict = r1.to_dictionary()
        dict1 = {'id': r1.id, 'width': 10, 'height': 2, 'x': 1, 'y': 0}
        self.assertEqual(dict1, r1_dict)

    def test_to_dictionary2(self):
        """test the return value of the function with four values"""
        r1 = Rectangle(10, 2, 1, 5)
        r1_dict = r1.to_dictionary()
        dict1 = {'id': r1.id, 'width': 10, 'height': 2, 'x': 1, 'y': 5}
        self.assertEqual(dict1, r1_dict)

    def test_to_dictionary3(self):
        """test the return value of the function with all values"""
        r1 = Rectangle(10, 2, 1, 5, 3)
        r1_dict = r1.to_dictionary()
        dict1 = {'id': 3, 'width': 10, 'height': 2, 'x': 1, 'y': 5}
        self.assertEqual(dict1, r1_dict)


if __name__ == "__main__":
    unittest.main()
