#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    x = len(my_list)
    if idx > x:
        return my_list
    else:
        my_list[idx] = element
        return my_list
