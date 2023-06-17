#!/usr/bin/python3
def roman_to_int(roman_string):
	x = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
	if not isinstance(roman_string, str):
		return 0
	j = 0
	s = 0
	for n int reversed(roman_string):
		j = x[n]
		s += j if s < j * 5 else -j
	return s
