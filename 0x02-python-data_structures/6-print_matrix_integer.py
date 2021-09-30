#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in matrix[x]:
            print("{:d}".format(y), end=" ")
        print()
