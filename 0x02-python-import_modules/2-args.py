#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    x = len(argv)
    if x == 1:
        print("0 arguments.")
    else:
        print("{:d} ".format(x - 1), end="")
        if x == 2:
            print("argument:")
        else:
            print("arguments:")
        n = range(x)
        for i in n:
            if i > 0:
                print("{:d}: {}".format(i, argv[i]))
