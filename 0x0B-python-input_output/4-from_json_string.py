#!/usr/bin/python3
"""Define from_json_string function"""
json = __import__('json')


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string"""

    return json.loads(my_str)
