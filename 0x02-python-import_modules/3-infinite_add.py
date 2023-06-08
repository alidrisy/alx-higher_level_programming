#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    x = len(argv)
    d = 0
    if x == 1:
        print("{:d}".format(0))
    else:
        n = range(x)
        for i in n:
            if i > 0:
                d += int(argv[i])
    if d:
        print("{:d}".format(d))
