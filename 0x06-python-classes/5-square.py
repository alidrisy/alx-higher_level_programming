#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represint a class square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
        size (int): The size of the new square.
        """
        self.__size = size

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

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #."""
        x = self.__size
        if x == 0:
            print()
        else:
            for i in range(x):
                for c in range(x):
                    print("#", end="")
                print()
