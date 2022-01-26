#!/usr/bin/python3
"""a square is born"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """super class"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)
