#!/usr/bin/python3
"""Define an append_after class"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""

    with open(filename, mode="r", encoding="utf-8") as fp:
        new = []
        new = fp.readlines()

    with open(filename, mode="w", encoding="utf-8") as fp:
        for i in range(len(new)):
            if search_string in new[i]:
                new.insert(i+1, new_string)
        fp.writelines(new)
