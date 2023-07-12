#!/usr/bin/python3
"""Define student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and attrs != []:
            new = []
            for key in attrs:
                if type(key) is str and key in self.__dict__.keys():
                    new += [(key, getattr(self, key))]
            return dict(new)
        return self.__dict__
