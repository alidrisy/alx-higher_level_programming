#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8).
    returns: the number of characters written"""

    with open(filename,mode="r+", encoding="utf-8") as fp:
        return fp.write(text)
