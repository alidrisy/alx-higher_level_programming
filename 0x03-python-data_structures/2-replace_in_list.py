#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if 0 <= idx < x:
        my_list[idx] = element
    return my_list
