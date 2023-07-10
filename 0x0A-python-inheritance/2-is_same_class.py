#!/usr/bin/python3
"""Define an type check function"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instanc
    of the specified class ; otherwise False."""
    if type(obj) is a_class:
        return True
    else:
        return False
