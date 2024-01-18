#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colonne in row:
            print("{:d}".format(colonne), end=" " if colonne != row[-1] else "")
        print()
