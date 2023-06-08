#!/usr/bin/env python3
a = 1
b = 2
if __name__ == "__main__":
    from add_0 import add
    print("{:s} + {:s}".format(str(a), str(b)), end="")
    print(" = {:s}".format(str(add(a, b))))
