#!/usr/bin/python3
"""Appends words to a file"""

def append_write(filename="", text=""):
    """appends WORDS to file"""
    with open(filename, "a") as f:
        append_data = f.write(text)
        return len(text)
