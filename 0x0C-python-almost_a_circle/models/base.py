#!/usr/bin/python3

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

        def to_json_string(list_dictionaries):
            if list_dictionaries is None:
                return "[]"
            
