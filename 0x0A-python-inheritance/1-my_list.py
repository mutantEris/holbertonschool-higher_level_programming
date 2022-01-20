#!/usr/bin/python3
"""Writes an inheriting class"""


class MyList(list):
    """class MyList inherits list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
