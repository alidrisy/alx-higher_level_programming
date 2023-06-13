#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
	new_list = my_list
	x = 0
	for i in my_list:
        if idx == x:
            new_list.remove(i)
        x += 1
    return new_list
