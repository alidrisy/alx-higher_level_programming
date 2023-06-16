#!/usr/bin/python3
def roman_to_int(roman_string):
    x = 0
    for i in roman_string:
        if i == 'I':
            x += 1
        elif i == 'V':
            x += 5
        elif i == 'X':
            x += 10
        elif i == 'L':
            x += 50
        elif i == 'C':
            x += 100
        elif i == 'D':
            x += 500
        elif i == 'M':
            x += 1000
    if x > 3999:
        x = 0
    return (x)
