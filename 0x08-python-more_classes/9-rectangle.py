#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initilaize data."""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return thre area of the rectangler"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return thre perimeter of the rectangler"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print the rectangle with the character #"""
        w = self.__width
        h = self.__height
        if h == 0 or w == 0:
            return ""
        my_list = []
        for i in range(h):
            for x in range(w):
                my_list.append(str(self.print_symbol))
            if i != h - 1:
                my_list.append('\n')
        x = ''.join(my_list)
        return x

    def __repr__(self):
        str1 = "Rectangle(" + str(self.__width) + ", " + \
                str(self.__height) + ")"
        return (str1)

    def __del__(self):
        """Print the message Bye rectangle..."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
