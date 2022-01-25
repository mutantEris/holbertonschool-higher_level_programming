#!/usr/bin/python3
"""Creates a class"""


class Student:
    """the student class"""
    def __init__(self, first_name, last_name, age):
        """initializes attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary"""
        return self.__dict__
