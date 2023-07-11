#!/usr/bin/python3
"""Define class_to_json function"""
json = __import__('json')


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return json.dumps(obj.__dict__)
