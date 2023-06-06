#!/usr/bin/python3
def print_last_digit(number):
    x = abs(number) % 10
    print("{:d}".format(x), end="")
    return x
