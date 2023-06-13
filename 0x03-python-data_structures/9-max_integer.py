#!/usr/bin/python3
def max_integer(my_list=[]):
	i = len(my_list) - 1
	if my_list is None:
		return
	while i > 1:
		j = 0
		while j < i:
			if my_list[j] > my_list[j + 1]:
				tmp = my_list[j]
				my_list[j] = my_list[j + 1]
				my_list[j + 1] = tmp
			j += 1
		i -= 1
	n = len(my_list) - 1
	return my_list[n]
