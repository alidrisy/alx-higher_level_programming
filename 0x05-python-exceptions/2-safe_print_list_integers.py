#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    if my_list:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                num += 1
            except (IndentationError, TypeError, ValueError):
                continue
    print()
    return num
