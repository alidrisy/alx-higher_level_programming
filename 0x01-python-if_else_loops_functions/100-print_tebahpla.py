#!/usr/bin/python3
c = 122
while c > 96:
    if c % 2 == 0:
        x = c
    else:
        x = c - 32
    print("{}".format(chr(x)), end="")
    c -= 1
