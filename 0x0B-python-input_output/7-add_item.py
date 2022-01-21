#!/usr/bin/python3
"""Adds more arguments to a python list"""


import json
from sys import argv
save_to_json_file = import('5-save_to_json_file.py').save_to_json_file
load_from_json_file = import('6-load_from_json_file').load_from_json_file


def load_add_save():
    """adds arguments to a python list"""
    try:
        my_list = load_from_json_file('add_item.json')
    except Exception:
        my_list = []
    my_list += argv[1:]
    save_to_json_file(mylist, 'add_item.json')


if __name__ == "__main__":
    load_add_save()
