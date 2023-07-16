#!/usr/bin/python3
"""Define Rectangle class inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """A class to get an area of rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end='')
            for x in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__x}/\
{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        i = 0
        if args and args != ():
            for j in args:
                if i == 0:
                    self.id = j
                if i == 1:
                    self.width = j
                if i == 2:
                    self.height = j
                if i == 3:
                    self.x = j
                if i == 4:
                    self.y = j
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        new = []
        ne = ["id", "width", "height", "x", "y"]
        for key in ne:
            if hasattr(self, key):
                new += [(key, getattr(self, key))]
        return dict(new)
