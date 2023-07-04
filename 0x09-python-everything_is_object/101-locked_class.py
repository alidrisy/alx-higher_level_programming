#!/usr/bin/python3
"""Define LockedClass class."""


class LockedClass():
    """Prevents the user from dynamically creating"""

    __slots__ = ["first_name"]

    def __init__(self):
        """Initilaize data"""
        self.first_name = LockedClass.first_name
