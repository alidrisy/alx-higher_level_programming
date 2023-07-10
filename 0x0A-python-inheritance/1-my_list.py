#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """prints the list"""
        print(sorted(self))
