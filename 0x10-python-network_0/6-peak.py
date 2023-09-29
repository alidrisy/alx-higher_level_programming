#!/usr/bin/python3
""" Function find peaks inside a list """


def find_peak(list_of_integers):
    """ This function finds peak in a list of integer """
    if list_of_integers:
        x = len(list_of_integers)
        if x = 1:
            return list_of_integers[0]
        p = list_of_integers[0]
        for i in range(1, x - 1):
            if list_of_integers[i] > list_of_integers[i - 1] and\
                    list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
            if list_of_integers[i] > p:
                p = list_of_integers[i]
            if list_of_integers[i] == list_of_integers[i - 1] and\
                    list_of_integers[i] == list_of_integers[i + 1]:
                return p
        return p
