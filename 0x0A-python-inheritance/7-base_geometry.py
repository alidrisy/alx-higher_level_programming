#!/usr/bin/python3
"""Define BaseGeometry class"""


class BaseGeometry:
    """A check value class"""

    def area(self):
        """Raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
