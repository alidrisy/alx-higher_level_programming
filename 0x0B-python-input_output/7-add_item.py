#!/usr/bin/python3
"""Define  a script that adds all arguments to a Python list
and then save them to a file"""


if __name__ == "__main__":
    argv = __import__('sys').argv
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file

    filename = "add_item.json"
    try:
        new = load_from_json_file(filename)
    except FileNotFoundError:
        new = []
    new.extend(argv[1:])
    save_to_json_file(new, filename)
