#!/usr/bin/python3
"""Define print_square functiont."""


def print_square(size):
    """Prints a square with the character #."""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
