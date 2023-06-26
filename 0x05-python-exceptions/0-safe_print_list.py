#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    if my_list:
        for i in range(x):
            try:
                print(my_list[i], end='')
            except IndexError:
                print()
                return(n)
            else:
                n += 1
    print()
    return (n)
