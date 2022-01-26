#!/usr/bin/python3
"""a square is born"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """super class"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """The bigs"""
        return self.width

    @size.setter
    def size(self, value):
        """the big"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
