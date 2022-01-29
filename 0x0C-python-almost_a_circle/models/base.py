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

    @staticmethod
    def to_json_string(list_dictionaries):
        """lists dictionaries in json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to file"""
        thelist = []
        saves = cls.__name__ + '.json'
        if list_objs is not None:
            for x in list_objs:
                thelist.append(cls.to_dictionary(x))
        with open(saves, 'w') as f:
            f.write(cls.to_json_string(thelist))

    @staticmethod
    def from_json_string(json_string):
        aDict = json.loads(json_string)
        """to_json_string but instead no"""
        if json_string is None or json_string == []:
            return "[]"
        else:
            return aDict
