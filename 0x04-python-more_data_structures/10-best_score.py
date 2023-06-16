#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return (None)
  n = 0
    x = None
    for i, j in sorted(a_dictionary.items()):
        if j > n:
            n = j
            x = i
    return x
