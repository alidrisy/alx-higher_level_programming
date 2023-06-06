#!/usr/bin/python3
for str in range(97, 123):
    if str != 113 and str != 101:
        print("{:s}".format(chr(str)), end="")
