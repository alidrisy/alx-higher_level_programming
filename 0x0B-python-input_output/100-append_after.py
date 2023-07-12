#!/usr/bin/python3
"""Define an append_after class"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""

    with open(filename) as fp:
        new = []
        new = fp.readlines()

    with open(filename, "w") as fp:
        for i in range(len(new)):
            if search_string in new[i]:
                new[i] += new_string
        fp.writelines(new)
