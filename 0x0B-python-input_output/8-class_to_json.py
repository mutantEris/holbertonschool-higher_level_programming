#!/usr/bin/python3
"""returns the dictionary description"""


def class_to_json(obj):
    """returns a dictionary description with data"""
    return obj.__dict__
