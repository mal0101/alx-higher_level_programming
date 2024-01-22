#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        new.append(result)
    return new
