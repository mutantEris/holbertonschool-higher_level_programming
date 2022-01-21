#!/usr/bin/python3

def read_file(filename=""):
    with open(filename) as f:
        read_data = print(f.read(), end="")
