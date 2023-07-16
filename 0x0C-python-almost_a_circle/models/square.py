#!/usr/bin/python3
"""Define A Square class inhirts from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a Square is a special Rectangle return values
    and print square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        i = 0
        if args and args != ():
            for j in args:
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
                i += 1
        else:
            super().update(**kwargs)

    def to_dictionary(self):
        new = []
        ne = ["id", "size", "x", "y"]
        for key in ne:
            if hasattr(self, key):
                new += [(key, getattr(self, key))]
        return dict(new)
