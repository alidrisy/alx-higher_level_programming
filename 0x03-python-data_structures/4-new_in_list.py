#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    x = len(my_list)
    if 0 <= idx < x:
        new_list[idx] = element
        return new_list
    return my_list
