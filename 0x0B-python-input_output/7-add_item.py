#!/usr/bin/python3
"""Define  a script that adds all arguments to a Python list
and then save them to a file"""
argv = __import__('sys').argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []
filename = "add_item.json"
new = []

with open(filename, encoding="utf-8") as fp:
    x = fp.read()
    if x is not None:
        new = load_from_json_file(filename)

my_list += new
my_list += argv[1:]
save_to_json_file(my_list, filename)
