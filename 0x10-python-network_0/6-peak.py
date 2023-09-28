#!/usr/bin/python3
""" function find_peak """

def find_peak(list_of_integers):
    """ This function finds peak in a list of integer """
	if list_of_integers:
		return sorted(list_of_integers)[len(list_of_integers) - 1]
