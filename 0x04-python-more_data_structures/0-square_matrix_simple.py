#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new = []
	list = []
	list1 = []
	list2 = []
	n = 0
	for i in matrix:
		if n == 0:
			list += map(lambda x: x*x, i)
		elif n == 1:
			list1 += map(lambda x: x*x, i)
		else:
			list2 += map(lambda x: x*x, i)
		n += 1
	new = [list, list1, list2]
	return new
