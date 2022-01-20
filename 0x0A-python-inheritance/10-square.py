#!/usr/bin/python3
"""Behold the Square of Power"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is the greatest rectangle"""
    def __init__(self, size):
        """Becometh Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
