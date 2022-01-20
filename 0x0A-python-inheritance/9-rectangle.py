#!/usr/bin/python3
"""Behold the Rectangle of Power"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is the greatest rectangle"""
    def __init__(self, width, height):
        """Becometh Rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        """returns area"""
        return self._width * self._height

    def __str__(self):
        """prints some words"""
        return "[Rectangle] {}/{}".format(self._width, self._height)
