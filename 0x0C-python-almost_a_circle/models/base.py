#!/usr/bin/python3
"""Base class for base class"""


import json


class Base:
    """the class that is base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """lists dictionaries in json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
