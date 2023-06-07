#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for c in str:
        if(n != i):
            print(str[i], end="")
        i += 1
