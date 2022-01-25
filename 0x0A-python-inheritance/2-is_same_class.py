#!/usr/bin/python3
"""checks if object is exactly the object class"""


def is_same_class(obj, a_class):
    """Writes a function that returns True if the object is an instance
    of the specified class"""

    return type(obj) is a_class
