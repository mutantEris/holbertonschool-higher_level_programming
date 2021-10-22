#!/usr/bin/python3
"""squares home base"""
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """stringle"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """bigness"""
        return self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
            """kwarg"""
            numbarg=0
            if args:
                for arg in args:
                    numbarg+=1
                    if numbarg == 1:
                        self.id = arg
                    if numbarg == 2:
                        self.size = arg
                    if numbarg == 3:
                        self.x = arg
                    if numbarg == 4:
                        self.y = arg
            elif kwargs:
                for arg in kwargs.keys():
                    if arg == "id":
                        self.id = kwargs.get(arg)
                    if arg == "size":
                        self.size = kwargs.get(arg)
                    if arg == "x":
                        self.x = kwargs.get(arg)
                    if arg == "y":
                        self.y = kwargs.get(arg)

    def to_dictionary(self):
        mobydict = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            }
        return mobydict
