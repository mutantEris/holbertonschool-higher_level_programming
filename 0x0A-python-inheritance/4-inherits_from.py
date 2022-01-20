#!usr/bin/python3
"""Checks if object is a child class"""


def inherits_from(obj, a_class):
    """returns True if the object is a child class """

    return isinstance(obj, a_class) and type(obj) is not a_class
