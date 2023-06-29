#!/usr/bin/python3
"""Define a class MagicClass."""


class MagicClass:
    """Represint a class magic."""

    def __init__(self, radius=0):
        """initialize radius"""
        self.__radius = 0
        if (type(radius) is not int) and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
		
    def area(self):
        """return self.redius"""
        return self.__radius**2 * math.pi
				
    def circumference(self):
        """return self.redius"""
        return 2*math.pi * self.__radius
