#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    n = 0
    for i in my_list:
        if i == search:
            new[n] = replace
        n += 1
    return new
