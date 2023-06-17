#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for i in a_dictionary.keys():
        if a_dictionary[i] == value:
            new.append(i)
    for x in new:
        del a_dictionary[x]
    return a_dictionary
