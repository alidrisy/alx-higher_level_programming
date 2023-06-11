#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    x = range(3)
    for i in x:
        for n in x:
            print("{}".format(matrix[i][n]), end='')
        print('')
