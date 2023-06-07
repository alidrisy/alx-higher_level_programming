#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for c in str:
        if(n != i):
            str = str[i]
        i += 1
    return str
