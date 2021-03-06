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
