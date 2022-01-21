#!/usr/bin/python3
"Reads a file and prints whats in it"

def read_file(filename=""):
    "Behold the file of legibility"
    with open(filename) as f:
        read_data = print(f.read(), end="")
