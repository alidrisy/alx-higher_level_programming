#!/usr/bin/python3
"""Define add_attribute function"""


def add_attribute(cls, name, new):
    """adds a new attribute to an object if it’s possible to class"""
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, name, new)
