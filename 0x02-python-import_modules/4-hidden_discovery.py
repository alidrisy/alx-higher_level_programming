#!/usr/bin/python3
import hidden_4


def discovr():
    n = dir(hidden_4)
    for x in n:
        if x[:2] != '__':
            print("{:s}".format(x))


if __name__ == "__main__":
    discovr()
