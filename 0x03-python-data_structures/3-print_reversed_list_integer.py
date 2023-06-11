#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    n = range(x)
    c = x - 1
    for i in n:
        print("{:d}".format(my_list[i + c]))
        c -= 2
