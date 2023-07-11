#!/usr/bin/python3
"""Define save_to_json_file function"""
json = __import__('json')


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename,mode="w", encoding="utf-8") as fp:
        json.dump(my_obj, fp)
