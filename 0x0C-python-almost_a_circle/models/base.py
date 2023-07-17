#!/usr/bin/python3
"""Define a Base class"""
import json
import csv
import turtle


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
        fn = cls.__name__ + ".json"
        with open(fn, mode="w") as fp:
            if list_objs is None or list_objs == []:
                fp.write("[]")
            else:
                new = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])
                fp.write(new)

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
        try:
            with open(fn) as fp:
                new = fp.read()
                ne = cls.from_json_string(new)
                cls1 = []
                for obj in ne:
                    cls1.append(cls.create(**obj))
                return cls1
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and save object in CSV file"""
        fn = cls.__name__ + ".csv"
        with open(fn, mode="w", newline="") as fp:
            if list_objs is None or list_objs == []:
                fp.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]
                writer = csv.DictWriter(fp, fieldnames=header)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file."""
        fn = cls.__name__ + ".csv"
        try:
            with open(fn, mode="r", newline="") as fp:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(fp, fieldnames=header)
                list_dict = [dict([k, int(v)] for k, v in d.items())
                             for d in list_dict]
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        turt = turtle.Turtle()
        for x in range(2):
            i = 0
            if x == 0:
                dic = list_rectangles
                x = "width"
                y = "height"
                n = "Rectangle"
            else:
                dic = list_squares
                x = "size"
                y = "size"
                n = "Square"
            for obj in dic:
                dc = obj.to_dictionary()
                turt.colormode(255)
                turt.pensize(5)
                turt.color("black", "Gray")
                turt.write(f"{i+1}{n}", False, align="left", font=("Arial", 4, "normal"))
                turt.bgcolor("white")
                turt.begin_fill()
                turt.shape("circle")
                turt.speed(1)
                turt.setx(dc[x] + 50)
                turt.sety(dc[y] + 50)
                turt.setx(0)
                turt.sety(0)
                turt.end_fill()
                turt.clearscreen()
                i += 1
        turtle.done()
