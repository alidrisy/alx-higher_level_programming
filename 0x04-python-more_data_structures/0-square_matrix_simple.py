#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new.append(list(map(lambda x: x*x, i)))
    return new
