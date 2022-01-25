#!/usr/bin/python3
"""Behold the Square of Power"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is the greatest rectangle"""

    def __init__(self, size):
        """Becometh Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self._size = size

    def area(self):
        """returns area of square"""
        return super().area()

    def __str__(self):
        return "[Square] {}/{}".format(self._size, self._size)
