#!/usr/bin/python3
"""Define a load_from_json_file function"""
json = __import__('json')


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""

    with open(filename, encoding="utf-8") as fp:
        return json.load(fp)
