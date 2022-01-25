#!/usr/bin/python3
"""Returns an object"""


import json


def save_to_json_file(my_obj, filename):
    """writes object to text file"""
    with open(filename, "w") as f:
        write_data = f.write(json.dumps(my_obj))
