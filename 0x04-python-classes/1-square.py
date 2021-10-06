#!/usr/bin/python3
"""defines shape with four equal sides"""


class Square:
    """defines object by size"""

    def __init__(self, size):
        self.__size = size

        if type size is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
