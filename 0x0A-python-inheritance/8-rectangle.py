#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize data"""
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
