#!/usr/bin/python3
"""module used to create class square"""


class Square:
    """defines object by size"""
    def __init__(self, size=0):
        """defines self"""

        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
