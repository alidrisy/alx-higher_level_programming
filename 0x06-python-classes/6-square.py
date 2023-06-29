#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represint a class square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
        size (int): the size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        x = self.__size
        v = self.__position[0]
        for b in range(self.__position[1]):
            print()
        if x == 0:
            for n in range(v):
                print(" ", end="")
            print()

        for i in range(x):
            for n in range(v):
                print(" ", end="")
            for c in range(x):
                print("#", end="")
            print()
