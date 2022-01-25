#!/usr/bin/python3
"""Writes a file and prints how much is in it"""


def write_file(filename="", text=""):
    """Writes filey words"""
    with open(filename, "w") as f:
        write_data = f.write(text)
        return len(text)
