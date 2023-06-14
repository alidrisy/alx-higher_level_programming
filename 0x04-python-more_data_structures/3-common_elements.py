#!/usr/bin/python3
def common_elements(set_1, set_2):
    for i in set_1:
        for j in set_2:
            if i is j:
                x = i
    return (x)
