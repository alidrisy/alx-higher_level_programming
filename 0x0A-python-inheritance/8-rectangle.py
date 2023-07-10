#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Define Rectangle class"""


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize data"""
        self.__width = width
        self.__height = height
        super().integer_validator("height", height)
		super().integer_validator("width", width)
