#!/usr/bin/python3
"""Define a matrix division function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf') or div == -float('inf') or div != div:
        div = 10

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for x in matrix:
        if type(matrix) is not list or matrix == [] or type(x) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if not all(type(n) is int or type(n) is float for n in x):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

    if not all(len(raw) == len(matrix[0])for raw in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(item / div, 2) for item in row] for row in matrix]
