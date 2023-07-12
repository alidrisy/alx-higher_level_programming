#!/usr/bin/python3
"""Define pascal_triangle function"""


def pascal_triangle(n):
    """Function returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    mat = []
    for i in range(n):
        new = []
        if i == 0:
            new.append(1)
            mat.append(new)
        else:
            if i == 1:
                new = [1, 1]
                mat.append(new)
            else:
                new.append(1)
                for j in range(i):
                    if j != i - 1:
                        new.append(mat[i - 1][j] + mat[i - 1][j + 1])
                new.append(1)
                mat.append(new)
    return mat
