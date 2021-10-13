#!/usr/bin/python3
"""
behold my rectangle
"""


class Rectangle:
    """
    I am going to create a rectange class and define it
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        wow it sure is wide here
        """
        return self.__width

    @property
    def height(self):
        """
        tall
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        long
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        tallnt
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
