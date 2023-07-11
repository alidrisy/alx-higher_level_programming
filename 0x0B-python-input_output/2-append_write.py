#!/usr/bin/python3
"""Define append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""

    with open(filename, mode="a", encoding="utf-8") as fp:
        return fp.write(text)
