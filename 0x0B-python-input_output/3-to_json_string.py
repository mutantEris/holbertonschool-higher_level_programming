#!/usr/bin/python3
"""Writes a function that returns the JSON representation of an object """


import json


def to_json_string(my_obj):
    """writes function"""
    return json.dumps(my_obj)
