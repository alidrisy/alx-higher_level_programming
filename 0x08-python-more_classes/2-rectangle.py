#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initilaize data."""

        self.width = width
        self.height = height

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
