#!/usr/bin/python3
"""Define a to_json_string function"""
json = __import__('json')


def to_json_string(my_obj):
    return json.dumps(my_obj)
