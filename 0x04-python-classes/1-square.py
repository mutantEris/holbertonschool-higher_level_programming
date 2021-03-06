#!/usr/bin/python3
"""module used to create class square"""


class Square:
    """defines object by size"""
    def __init__(self, size=0):
        """defines self"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
