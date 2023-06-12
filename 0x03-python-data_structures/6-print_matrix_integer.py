#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = range(3)
    for i in x:
        for n in x:
            print("{:d}".format(matrix[i][n]), end='')
       print('')
