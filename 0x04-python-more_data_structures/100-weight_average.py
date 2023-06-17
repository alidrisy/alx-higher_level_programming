#!/usr/bin/python3
def weight_average(my_list=[]):
    s1 = 0
    s2 = 0
    if my_list is None or my_list == []:
        return 0
    for i, j in my_list:
        s1 += i * j
        s2 += j
    return (s1 / s2)
