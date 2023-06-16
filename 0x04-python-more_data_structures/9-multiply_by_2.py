#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new  = dict(a_dictionary)
    for i, j in new.items():
        new[i] = j * 2
    return new
