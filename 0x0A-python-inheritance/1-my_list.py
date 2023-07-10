#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """Class that inherits from list"""

    def __init__(self):
        """Initialize data"""
        super().__init__()

    def print_sorted(self):
        """prints the list"""
        list1 = super().__str__()
        new = []
        for i in list1:
            if i.isdigit():
                new.append(int(i))
        print(sorted(new))
