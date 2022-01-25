#!/usr/bin/python3
"""Writes a function that creates an object from a json file"""


import json


def load_from_json_file(filename):
    """makes json object"""
    with open(filename) as f:
        return json.loads(f.read())
