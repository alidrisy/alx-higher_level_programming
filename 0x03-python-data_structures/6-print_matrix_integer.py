#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = range(3)
    for i in matrix:
        for n in i:
            print("{:d}".format(i), end=' ')
            print('')
