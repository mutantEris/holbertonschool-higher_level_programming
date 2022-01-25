#!/usr/bin/python3
"""Pascals triangle"""


def pascal_triangle(n):
    """makes a pascals triangle"""
    x = []
    if n <= 0:
        return x
    for line in range(n):
        y = []
        for tallst in range(line + 1):
            if tallst == line:
                y.append(1)
                x.append(y)
            elif tallst == 0:
                y.append(1)
            else:
                y.append(x[line - 1][tallst - 1] + x[line - 1][tallst])
    return x
