#!/usr/bin/python3
"""Define a Base class"""
import json


class Base:
    """the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initilaize data"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return ([])
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        new = []
        fn = list_objs[0].__class__.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                new.append(obj.to_dictionary())
        ne = cls.to_json_string(new)
        with open(fn, mode="w", encoding="utf-8") as fp:
            fp.write(ne)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if "width" in dictionary.keys():
            rc = cls(dictionary["width"], dictionary["height"])
        elif "size" in dictionary.keys():
            rc = cls(dictionary["size"])
        rc.update(**dictionary)
        return rc

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        fn = cls.__name__+".json"
        with open(fn) as fp:
            new = fp.read()
        ne = cls.from_json_string(new)
        if ne == []:
            return []
        cls1 = []
        for obj in ne:
            cls1.append(cls.create(**obj))
        return cls1
