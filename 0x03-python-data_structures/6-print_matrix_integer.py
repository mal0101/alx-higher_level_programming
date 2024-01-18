#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colone in row:
            print("{:d}".format(colone), end=" " if colone != row[-1] else "")
        print()
