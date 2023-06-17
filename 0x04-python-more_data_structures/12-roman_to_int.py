#!/usr/bin/python3
def roman_to_int(roman_string):
	x = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    if not isinstance(roman_string, str):
		return 0
	s = 0
	r = len(roman_string)
	for i, j in x.items():
		for c in range(r):
			n = roman_string[c]
			if roman_string[c] == 'I' and c != r - 1:
				if roman_string[c+1] != 'I':
					j -= 1
			if i == n:
				s += j 
			elif n not in x.keys():
				return 0
    return s
