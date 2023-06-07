#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for c in str:
        if(n != i):
            return str[i]
        i += 1
