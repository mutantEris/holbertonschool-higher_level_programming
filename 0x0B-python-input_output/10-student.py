#!/usr/bin/python3
"""Creates a class"""


class Student:
    """the student class"""
    def __init__(self, first_name, last_name, age):
        """initializes attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """retrieves dictionary"""
            if attrs is None or type(attrs) is not list:
                return self.__dict__
            else:
                my_dict = {}
                for x in self.__dict__:
                    if x in attrs:
                        my_dict[x] = self.__dict__[x]
                return my_dict
