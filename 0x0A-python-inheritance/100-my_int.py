#!/usr/bin/python3
"""Define MyInt calss"""


class MyInt(int):
    """MyInt that inherits from int
    MyInt has == and != operators inverted"""

    def __ne__(self, value):
        return super().__eq__(value)

    def __eq__(self, value):
        return super().__ne__(value)
